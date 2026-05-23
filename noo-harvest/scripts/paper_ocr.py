from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable

try:
    import torch
    from PIL import Image
    from transformers import AutoTokenizer
except ModuleNotFoundError as exc:  # pragma: no cover - import guard for mis-invocation
    raise SystemExit(
        "paper_ocr.py requires the DeepSeek OCR runtime environment. "
        "Use noo-harvest/scripts/paper_prepare.py or run with the project OCR python."
    ) from exc

VENDOR_ROOT = Path(__file__).resolve().parent.parent / "vendor"
if str(VENDOR_ROOT) not in sys.path:
    sys.path.insert(0, str(VENDOR_ROOT))

from deepseek_ocr2_nooharvest import DeepseekOCR2Config, DeepseekOCR2ForCausalLM
from deepseek_ocr2_nooharvest.modeling_deepseekocr2 import process_image_with_refs, re_match

GROUNDING_PROMPT = "<image>\n<|grounding|>Convert the document to markdown. "
FREE_OCR_PROMPT = "<image>\nFree OCR. "
BASE_SIZE = 1024
IMAGE_SIZE = 768
RASTER_DPI = 144
FORMULA_MARGIN_PX = 18
FORMULA_LABELS = frozenset({"equation"})
TOKENIZER_MODEL_NAME = "deepseek-ai/DeepSeek-OCR-2"

REF_PATTERN = re.compile(r"<\|ref\|>(.*?)<\|/ref\|><\|det\|>(.*?)<\|/det\|>", re.DOTALL)
MATH_SIGNAL_PATTERN = re.compile(r"(\\[A-Za-z]+|[_^{}]|[=<>≤≥]|∈|∑|∏|β|κ|λ|μ|α|γ)")
WORD_PATTERN = re.compile(r"[A-Za-z]{3,}")
ALL_CAPS_HEADER_PATTERN = re.compile(r"^[A-Z0-9 .,'&-]{8,}$")


@dataclass(slots=True)
class Box:
    x1: int
    y1: int
    x2: int
    y2: int


@dataclass(slots=True)
class BlockRecord:
    block_id: str
    page_index: int
    label: str
    boxes_norm: list[Box]
    boxes_px: list[Box]
    text: str
    grounding_text: str
    text_source: str
    formula_crop_path: str | None = None
    formula_raw_path: str | None = None
    flags: list[str] = field(default_factory=list)


@dataclass(slots=True)
class PageRecord:
    page_index: int
    image_path: str
    grounding_raw_path: str
    grounding_overlay_path: str
    blocks_path: str
    blocks: list[BlockRecord]


@dataclass(slots=True)
class DocumentRecord:
    source_pdf: str
    model_path: str
    pages: list[PageRecord]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdf")
    parser.add_argument("output_dir")
    parser.add_argument("--model-path")
    parser.add_argument("--pages", help="Comma-separated 1-based pages and ranges, e.g. 1,3-5")
    return parser.parse_args()


def parse_page_spec(spec: str | None, total_pages: int) -> list[int]:
    if not spec:
        return list(range(1, total_pages + 1))
    chosen: set[int] = set()
    for fragment in spec.split(","):
        fragment = fragment.strip()
        if not fragment:
            continue
        if "-" in fragment:
            start_text, end_text = fragment.split("-", 1)
            start = int(start_text)
            end = int(end_text)
            chosen.update(range(start, end + 1))
        else:
            chosen.add(int(fragment))
    pages = sorted(page for page in chosen if 1 <= page <= total_pages)
    if not pages:
        raise ValueError("page selection resolved to an empty set")
    return pages


def discover_model_path(explicit: str | None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    env_path = os.environ.get("NOO_HARVEST_DEEPSEEK_OCR2_MODEL_PATH")
    if env_path:
        candidates.append(Path(env_path).expanduser())

    repo_root = Path(__file__).resolve().parents[2]
    candidates.append(
        repo_root
        / ".tmp/deepseek-ocr2/hf-cache/models--deepseek-ai--DeepSeek-OCR-2/snapshots/aaa02f3811945a91062062994c5c4a3f4c0af2b0"
    )

    cache_roots = [
        Path.home() / ".cache/huggingface/hub/models--deepseek-ai--DeepSeek-OCR-2/snapshots",
        Path.home() / ".cache/huggingface/models--deepseek-ai--DeepSeek-OCR-2/snapshots",
    ]
    for root in cache_roots:
        if root.is_dir():
            candidates.extend(sorted(root.iterdir(), reverse=True))

    for candidate in candidates:
        if not candidate.exists():
            continue
        if (candidate / "config.json").is_file() and (candidate / "model-00001-of-000001.safetensors").is_file():
            return candidate

    raise FileNotFoundError("could not locate a local DeepSeek-OCR-2 snapshot; pass --model-path")


def pdf_page_count(pdf_path: Path) -> int:
    result = subprocess.run(
        ["pdfinfo", str(pdf_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError("pdfinfo did not report a page count")


def render_page(pdf_path: Path, page_index: int, page_dir: Path) -> Path:
    page_dir.mkdir(parents=True, exist_ok=True)
    for stale in page_dir.glob("page-*.png"):
        stale.unlink()
    prefix = page_dir / "page"
    subprocess.run(
        [
            "pdftoppm",
            "-r",
            str(RASTER_DPI),
            "-png",
            "-f",
            str(page_index),
            "-l",
            str(page_index),
            str(pdf_path),
            str(prefix),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    rendered_pages = sorted(page_dir.glob("page-*.png"))
    if len(rendered_pages) != 1:
        raise FileNotFoundError(f"expected exactly one rendered page, found {len(rendered_pages)} in {page_dir}")
    rendered = rendered_pages[0]
    target = page_dir / "page.png"
    rendered.replace(target)
    return target


def scaled_box(box: Box, width: int, height: int) -> Box:
    return Box(
        x1=round(box.x1 / 999 * width),
        y1=round(box.y1 / 999 * height),
        x2=round(box.x2 / 999 * width),
        y2=round(box.y2 / 999 * height),
    )


def parse_boxes(raw: str) -> list[Box]:
    parsed = ast.literal_eval(raw)
    boxes: list[Box] = []
    for entry in parsed:
        if len(entry) != 4:
            continue
        boxes.append(Box(*(int(value) for value in entry)))
    if not boxes:
        raise ValueError(f"failed to parse OCR coordinates: {raw!r}")
    return boxes


def parse_grounded_blocks(raw_text: str, page_index: int, image: Image.Image) -> list[BlockRecord]:
    matches = list(REF_PATTERN.finditer(raw_text))
    blocks: list[BlockRecord] = []
    width, height = image.size
    for idx, match in enumerate(matches, start=1):
        start = match.end()
        end = matches[idx].start() if idx < len(matches) else len(raw_text)
        content = raw_text[start:end].strip()
        boxes_norm = parse_boxes(match.group(2))
        boxes_px = [scaled_box(box, width, height) for box in boxes_norm]
        blocks.append(
            BlockRecord(
                block_id=f"p{page_index:04d}-b{idx:04d}",
                page_index=page_index,
                label=match.group(1).strip().lower(),
                boxes_norm=boxes_norm,
                boxes_px=boxes_px,
                text=content,
                grounding_text=content,
                text_source="grounding",
            )
        )
    return blocks


def fuse_adjacent_formula_blocks(blocks: list[BlockRecord]) -> list[BlockRecord]:
    fused: list[BlockRecord] = []
    idx = 0
    while idx < len(blocks):
        block = blocks[idx]
        if block.label not in FORMULA_LABELS:
            fused.append(block)
            idx += 1
            continue

        run = [block]
        idx += 1
        while idx < len(blocks) and blocks[idx].label in FORMULA_LABELS:
            run.append(blocks[idx])
            idx += 1

        if len(run) == 1:
            fused.append(block)
            continue

        merged = BlockRecord(
            block_id=run[0].block_id,
            page_index=run[0].page_index,
            label=run[0].label,
            boxes_norm=[box for item in run for box in item.boxes_norm],
            boxes_px=[box for item in run for box in item.boxes_px],
            text="\n\n".join(item.text for item in run if item.text.strip()),
            grounding_text="\n\n".join(item.grounding_text for item in run if item.grounding_text.strip()),
            text_source="grounding",
            flags=[f"merged_formula_cluster:{len(run)}"],
        )
        fused.append(merged)
    return fused


def union_boxes(boxes: Iterable[Box]) -> Box:
    boxes = list(boxes)
    return Box(
        x1=min(box.x1 for box in boxes),
        y1=min(box.y1 for box in boxes),
        x2=max(box.x2 for box in boxes),
        y2=max(box.y2 for box in boxes),
    )


def crop_with_margin(image: Image.Image, box: Box, margin: int) -> Image.Image:
    width, height = image.size
    x1 = max(0, box.x1 - margin)
    y1 = max(0, box.y1 - margin)
    x2 = min(width, box.x2 + margin)
    y2 = min(height, box.y2 + margin)
    return image.crop((x1, y1, x2, y2))


def math_score(text: str) -> int:
    math_hits = len(MATH_SIGNAL_PATTERN.findall(text))
    word_hits = len(WORD_PATTERN.findall(text))
    return (4 * math_hits) - word_hits


def scrub_formula_text(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    lines = [line.rstrip() for line in text.splitlines()]
    while lines and ALL_CAPS_HEADER_PATTERN.match(lines[0]) and not MATH_SIGNAL_PATTERN.search(lines[0]):
        lines.pop(0)
    cleaned = "\n".join(line for line in lines if line.strip())
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = re.sub(r"^max\s+\\\[\s*", r"\\[\\max ", cleaned)
    return cleaned.strip()


def select_formula_surface(grounding_text: str, free_ocr_text: str, *, force_free_ocr: bool = False) -> tuple[str, str, list[str]]:
    free_ocr_text = scrub_formula_text(free_ocr_text)
    if not free_ocr_text:
        return grounding_text, "grounding", ["formula_ocr_empty"]
    if force_free_ocr:
        return free_ocr_text, "formula_ocr", ["formula_ocr_forced_cluster"]
    if math_score(free_ocr_text) + 2 < math_score(grounding_text):
        return grounding_text, "grounding", ["formula_ocr_regressed"]
    return free_ocr_text, "formula_ocr", []


class PaperOcrEngine:
    def __init__(self, model_path: Path) -> None:
        self.model_path = model_path
        self.tokenizer = AutoTokenizer.from_pretrained(
            str(model_path),
            local_files_only=True,
            trust_remote_code=False,
        )
        config = DeepseekOCR2Config.from_pretrained(str(model_path), local_files_only=True)
        config._attn_implementation = "eager"
        self.model = DeepseekOCR2ForCausalLM.from_pretrained(
            str(model_path),
            config=config,
            torch_dtype=torch.bfloat16,
            local_files_only=True,
            use_safetensors=True,
        ).eval().cuda()

    def scorch(self, image_path: Path, prompt: str) -> str:
        return self.model.infer(
            self.tokenizer,
            prompt=prompt,
            image_file=str(image_path),
            output_path="",
            base_size=BASE_SIZE,
            image_size=IMAGE_SIZE,
            crop_mode=True,
            eval_mode=True,
        )


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def render_document_markdown(pages: list[PageRecord]) -> str:
    fragments: list[str] = []
    for page in pages:
        fragments.append(f"<!-- page {page.page_index} -->")
        for block in page.blocks:
            text = block.text.strip()
            if text:
                fragments.append(text)
        fragments.append("")
    return "\n\n".join(fragment for fragment in fragments if fragment)


def process_page(engine: PaperOcrEngine, page_image_path: Path, page_index: int, page_dir: Path) -> PageRecord:
    page_dir.mkdir(parents=True, exist_ok=True)
    (page_dir / "images").mkdir(exist_ok=True)
    image = Image.open(page_image_path).convert("RGB")

    grounding_raw = engine.scorch(page_image_path, GROUNDING_PROMPT)
    grounding_raw_path = page_dir / "grounding.raw.txt"
    grounding_raw_path.write_text(grounding_raw, encoding="utf-8")

    matches_ref, _, _ = re_match(grounding_raw)
    overlay = process_image_with_refs(image.copy(), matches_ref, str(page_dir))
    overlay_path = page_dir / "grounding.overlay.jpg"
    overlay.save(overlay_path)

    blocks = fuse_adjacent_formula_blocks(parse_grounded_blocks(grounding_raw, page_index, image))
    formulas_dir = page_dir / "formulas"
    formulas_dir.mkdir(exist_ok=True)

    for block in blocks:
        if block.label not in FORMULA_LABELS:
            continue
        crop_box = union_boxes(block.boxes_px)
        crop = crop_with_margin(image, crop_box, FORMULA_MARGIN_PX)
        crop_path = formulas_dir / f"{block.block_id}.png"
        crop.save(crop_path)

        raw_formula = engine.scorch(crop_path, FREE_OCR_PROMPT)
        raw_formula_path = formulas_dir / f"{block.block_id}.freeocr.raw.txt"
        raw_formula_path.write_text(raw_formula, encoding="utf-8")

        chosen_text, source, flags = select_formula_surface(
            block.grounding_text,
            raw_formula,
            force_free_ocr=any(flag.startswith("merged_formula_cluster:") for flag in block.flags),
        )
        block.text = chosen_text
        block.text_source = source
        block.formula_crop_path = str(crop_path)
        block.formula_raw_path = str(raw_formula_path)
        block.flags.extend(flags)
        torch.cuda.empty_cache()

    blocks_path = page_dir / "blocks.json"
    write_json(blocks_path, [asdict(block) for block in blocks])
    return PageRecord(
        page_index=page_index,
        image_path=str(page_image_path),
        grounding_raw_path=str(grounding_raw_path),
        grounding_overlay_path=str(overlay_path),
        blocks_path=str(blocks_path),
        blocks=blocks,
    )


def main() -> None:
    args = parse_args()
    input_pdf = Path(args.input_pdf).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    model_path = discover_model_path(args.model_path)
    page_total = pdf_page_count(input_pdf)
    pages = parse_page_spec(args.pages, page_total)

    engine = PaperOcrEngine(model_path)
    page_records: list[PageRecord] = []
    pages_root = output_dir / "pages"

    for page_index in pages:
        page_dir = pages_root / f"{page_index:04d}"
        page_image_path = render_page(input_pdf, page_index, page_dir)
        page_record = process_page(engine, page_image_path, page_index, page_dir)
        page_records.append(page_record)
        torch.cuda.empty_cache()

    document = DocumentRecord(
        source_pdf=str(input_pdf),
        model_path=str(model_path),
        pages=page_records,
    )
    write_json(output_dir / "document.blocks.json", asdict(document))
    (output_dir / "document.md").write_text(render_document_markdown(page_records), encoding="utf-8")


if __name__ == "__main__":
    main()
