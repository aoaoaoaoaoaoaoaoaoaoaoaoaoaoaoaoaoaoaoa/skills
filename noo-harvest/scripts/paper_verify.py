#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.13.*"
# dependencies = []
# ///

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

MAX_PAGE_ATTEMPTS = 2


BOOT_SCHEMA = {
    "type": "object",
    "properties": {
        "ready": {"type": "boolean"},
        "contract": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
            "maxItems": 5,
        },
    },
    "required": ["ready", "contract"],
    "additionalProperties": False,
}

PAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "page_index": {"type": "integer", "minimum": 1},
        "emissions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "block_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "minItems": 1,
                    },
                    "kind": {
                        "type": "string",
                        "enum": [
                            "heading",
                            "paragraph",
                            "equation",
                            "list",
                            "caption",
                            "footnote",
                            "reference",
                            "theorem",
                            "proof",
                            "other",
                        ],
                    },
                    "markdown": {"type": "string"},
                    "notes": {"type": "string"},
                },
                "required": ["block_ids", "kind", "markdown", "notes"],
                "additionalProperties": False,
            },
        },
        "drops": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "block_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "minItems": 1,
                    },
                    "reason": {
                        "type": "string",
                        "enum": [
                            "header_footer",
                            "page_number",
                            "empty",
                            "artifact",
                            "redundant",
                            "table_omitted",
                            "other",
                        ],
                    },
                    "notes": {"type": "string"},
                },
                "required": ["block_ids", "reason", "notes"],
                "additionalProperties": False,
            },
        },
        "tip": {
            "type": "object",
            "properties": {
                "status": {"type": "string", "enum": ["clear", "carry"]},
                "kind": {
                    "type": "string",
                    "enum": ["none", "paragraph", "list", "equation", "reference", "other"],
                },
                "block_ids": {"type": "array", "items": {"type": "string"}},
                "markdown": {"type": "string"},
                "notes": {"type": "string"},
            },
            "required": ["status", "kind", "block_ids", "markdown", "notes"],
            "additionalProperties": False,
        },
        "flags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "block_ids": {"type": "array", "items": {"type": "string"}},
                    "severity": {"type": "string", "enum": ["low", "medium", "high"]},
                    "kind": {
                        "type": "string",
                        "enum": [
                            "ocr_uncertain",
                            "symbol_uncertain",
                            "structure_uncertain",
                            "cross_page_continuation",
                            "table_omitted",
                            "other",
                        ],
                    },
                    "note": {"type": "string"},
                },
                "required": ["block_ids", "severity", "kind", "note"],
                "additionalProperties": False,
            },
        },
        "batch_notes": {"type": "string"},
    },
    "required": ["page_index", "emissions", "drops", "tip", "flags", "batch_notes"],
    "additionalProperties": False,
}

BOOT_PROMPT = """You are phase-2 paper verifier for a scholarly OCR pipeline.

Your job is to turn an OCR block ledger into faithful markdown. You are not summarizing. You are not compressing. You are reconstructing the paper as accurately as possible from the supplied block stream.

Non-negotiable rules:
- Equations and symbols are sacred.
- Preserve technical wording and notation unless the supplied OCR is obviously broken.
- Drop only obvious boilerplate: repeated running headers, repeated footers, page numbers, empty garbage, and clearly unusable table sludge.
- Consolidate adjacent blocks when they are one logical unit.
- Use markdown that is faithful, sparse, and literal.
- Never use shell commands or tools. Operate only on the provided payload and attached page image.
- The authoritative contract is the JSON schema in each turn.

Reply under the schema with ready=true and 3-5 terse contract bullets."""

FENCED_JSON_PATTERN = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the phase-2 Codex verification pass over a paper_ocr block ledger."
    )
    parser.add_argument("input", help="Path to document.blocks.json or the OCR output directory containing it")
    parser.add_argument("output_dir", help="Directory for persistent phase-2 verification state")
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


def resolve_document_path(raw: str) -> Path:
    candidate = Path(raw).expanduser().resolve()
    if candidate.is_dir():
        candidate = candidate / "document.blocks.json"
    if not candidate.is_file():
        raise FileNotFoundError(f"could not find OCR ledger at {candidate}")
    return candidate


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


@dataclass(slots=True)
class TipState:
    status: str = "clear"
    kind: str = "none"
    block_ids: list[str] = field(default_factory=list)
    markdown: str = ""
    notes: str = ""


@dataclass(slots=True)
class EmissionRecord:
    sequence: int
    page_index: int
    block_ids: list[str]
    kind: str
    markdown: str
    notes: str
    forced_tip_flush: bool = False


@dataclass(slots=True)
class DropRecord:
    page_index: int
    block_ids: list[str]
    reason: str
    notes: str


@dataclass(slots=True)
class FlagRecord:
    page_index: int
    block_ids: list[str]
    severity: str
    kind: str
    note: str


@dataclass(slots=True)
class PageRunRecord:
    page_index: int
    attempt: int
    prompt_path: str
    response_path: str
    image_path: str


@dataclass(slots=True)
class FailureState:
    status: str = "clear"
    page_index: int | None = None
    attempt: int | None = None
    error: str = ""
    prompt_path: str | None = None
    response_path: str | None = None
    error_path: str | None = None


@dataclass(slots=True)
class VerificationState:
    source_document_path: str
    source_pdf: str
    codex_thread_id: str | None
    codex_boot_response: dict[str, Any] | None
    selected_pages: list[int]
    completed_pages: list[int] = field(default_factory=list)
    tip: TipState = field(default_factory=TipState)
    failure: FailureState = field(default_factory=FailureState)
    emissions: list[EmissionRecord] = field(default_factory=list)
    drops: list[DropRecord] = field(default_factory=list)
    flags: list[FlagRecord] = field(default_factory=list)
    runs: list[PageRunRecord] = field(default_factory=list)

    @classmethod
    def new(cls, *, source_document_path: Path, source_pdf: str, selected_pages: list[int]) -> "VerificationState":
        return cls(
            source_document_path=str(source_document_path),
            source_pdf=source_pdf,
            codex_thread_id=None,
            codex_boot_response=None,
            selected_pages=selected_pages,
        )


def load_state(state_path: Path) -> VerificationState | None:
    if not state_path.is_file():
        return None
    raw = json.loads(state_path.read_text(encoding="utf-8"))
    failure = raw.get("failure") or {}
    return VerificationState(
        source_document_path=raw["source_document_path"],
        source_pdf=raw["source_pdf"],
        codex_thread_id=raw["codex_thread_id"],
        codex_boot_response=raw["codex_boot_response"],
        selected_pages=list(raw["selected_pages"]),
        completed_pages=list(raw["completed_pages"]),
        tip=TipState(**raw["tip"]),
        failure=FailureState(
            status=failure.get("status", "clear"),
            page_index=failure.get("page_index"),
            attempt=failure.get("attempt"),
            error=failure.get("error", ""),
            prompt_path=failure.get("prompt_path"),
            response_path=failure.get("response_path"),
            error_path=failure.get("error_path"),
        ),
        emissions=[EmissionRecord(**item) for item in raw["emissions"]],
        drops=[DropRecord(**item) for item in raw["drops"]],
        flags=[FlagRecord(**item) for item in raw["flags"]],
        runs=[
            PageRunRecord(
                page_index=item["page_index"],
                attempt=item.get("attempt", 1),
                prompt_path=item["prompt_path"],
                response_path=item["response_path"],
                image_path=item["image_path"],
            )
            for item in raw["runs"]
        ],
    )


def save_state(state_path: Path, state: VerificationState) -> None:
    write_json(state_path, asdict(state))


def page_payload(page: dict[str, Any]) -> dict[str, Any]:
    blocks = []
    for block in page["blocks"]:
        blocks.append(
            {
                "block_id": block["block_id"],
                "label": block["label"],
                "text": block["text"],
                "grounding_text": block["grounding_text"],
                "text_source": block["text_source"],
                "flags": block["flags"],
            }
        )
    return {
        "page_index": page["page_index"],
        "image_path": page["image_path"],
        "blocks": blocks,
    }


def recent_emissions(state: VerificationState, limit: int = 3) -> list[dict[str, Any]]:
    tail = state.emissions[-limit:]
    return [
        {
            "sequence": item.sequence,
            "page_index": item.page_index,
            "kind": item.kind,
            "markdown_preview": item.markdown[:240],
        }
        for item in tail
    ]


def page_image_attachments(page: dict[str, Any]) -> list[Path]:
    blocks = list(page["blocks"])
    needs_visual_grounding = any(
        block["label"] == "equation"
        or block["text_source"] == "formula_ocr"
        or bool(block["flags"])
        for block in blocks
    )
    if not needs_visual_grounding:
        return []
    return [Path(page["image_path"])]


def build_page_prompt(
    state: VerificationState,
    page: dict[str, Any],
    *,
    allowed_block_ids: list[str],
    validation_feedback: str | None = None,
    previous_invalid_response: dict[str, Any] | None = None,
) -> str:
    image_policy = (
        "An image of the current page is attached because this page contains formulas or OCR-risky blocks."
        if page_image_attachments(page)
        else "No image is attached for this page; rely on the block payload."
    )
    payload = {
        "mode": "verify_page",
        "document": {
            "source_pdf": state.source_pdf,
            "selected_pages": state.selected_pages,
        },
        "page": page_payload(page),
        "current_tip": asdict(state.tip),
        "allowed_block_ids": allowed_block_ids,
        "recent_emissions": recent_emissions(state),
        "instructions": {
            "goal": "Emit faithful markdown for this page while preserving OCR-derived equations and technical wording.",
            "drop_only": [
                "repeated running headers",
                "repeated footers",
                "page numbers",
                "empty garbage",
                "unusable table sludge",
            ],
            "equation_policy": "Prefer symbolic fidelity over prose smoothness. Do not normalize notation into a different style.",
            "table_policy": "If a table is badly corrupted, drop it and emit a high-severity table_omitted flag instead of fabricating structure.",
            "tip_policy": (
                "Carry forward only truly unfinished structures that need the next page. "
                "A carry tip may either hold wholly un-emitted trailing blocks or overlap the final emitted chunk when that chunk remains open."
            ),
            "block_id_policy": (
                "Every block id used in emissions, drops, and carry tips must come exactly from allowed_block_ids. "
                "Never invent, rename, or mutate a block id."
            ),
        },
    }
    if validation_feedback is not None:
        payload["retry_context"] = {
            "validation_error": validation_feedback,
            "previous_invalid_response": previous_invalid_response,
        }
        lead = (
            "Your previous response for this page failed validation. "
            "Re-emit the entire page response from scratch under the schema, correcting the failure exactly.\n\n"
        )
    else:
        lead = ""
    return (
        f"{lead}Continue the phase-2 verification contract. "
        f"{image_policy} "
        "Return only a JSON object matching this schema, with no prose before or after it.\n\n"
        "Schema:\n"
        f"{json.dumps(PAGE_SCHEMA, ensure_ascii=False, indent=2)}\n\n"
        "Payload:\n"
        f"{json.dumps(payload, ensure_ascii=False, indent=2)}"
    )


def parse_jsonl_events(stdout: str) -> tuple[str | None, str]:
    thread_id: str | None = None
    last_message: str | None = None
    for raw_line in stdout.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        event = json.loads(line)
        event_type = event.get("type")
        if event_type == "thread.started":
            thread_id = event.get("thread_id")
        elif event_type == "item.completed":
            item = event.get("item", {})
            if item.get("type") == "agent_message":
                last_message = item.get("text")
    if last_message is None:
        raise RuntimeError(f"Codex did not produce a final agent message.\nSTDOUT:\n{stdout}")
    return thread_id, last_message


def decode_json_message(raw: str) -> dict[str, Any]:
    text = raw.strip()
    if not text:
        raise ValueError("Codex returned an empty final message")
    fenced = FENCED_JSON_PATTERN.fullmatch(text)
    if fenced:
        text = fenced.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise
        return json.loads(text[start : end + 1])


def run_codex_turn(
    *,
    prompt: str,
    schema: dict[str, Any],
    session_id: str | None,
    image_paths: list[Path],
    working_root: Path,
) -> tuple[str | None, dict[str, Any]]:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, dir="/tmp") as handle:
        json.dump(schema, handle)
        schema_path = Path(handle.name)
    try:
        if session_id is None:
            cmd = [
                "codex",
                "exec",
                "--json",
                "--output-schema",
                str(schema_path),
                "--disable",
                "fast_mode",
                "--skip-git-repo-check",
                "-C",
                str(working_root),
                "-c",
                'approval_policy="never"',
                "-c",
                'sandbox_mode="read-only"',
            ]
        else:
            cmd = [
                "codex",
                "exec",
                "resume",
                "--json",
                "--disable",
                "fast_mode",
                "--skip-git-repo-check",
                "-c",
                'approval_policy="never"',
                "-c",
                'sandbox_mode="read-only"',
                session_id,
            ]
        for image_path in image_paths:
            cmd.extend(["-i", str(image_path)])
        cmd.append("-")
        result = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            capture_output=True,
            check=False,
            cwd=working_root,
        )
    finally:
        schema_path.unlink(missing_ok=True)
    if result.returncode != 0:
        raise RuntimeError(
            "Codex turn failed.\n"
            f"Command: {' '.join(cmd)}\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )
    thread_id, message = parse_jsonl_events(result.stdout)
    return thread_id, decode_json_message(message)


def account_blocks(
    page: dict[str, Any],
    response: dict[str, Any],
    carry_block_ids: set[str] | None = None,
) -> None:
    page_ids = {block["block_id"] for block in page["blocks"]}
    carry_ids = set(carry_block_ids or [])
    known_ids = page_ids | carry_ids
    dropped: set[str] = set()
    referenced: set[str] = set()

    def ingest(block_ids: list[str], label: str) -> None:
        block_set = set(block_ids)
        unknown = block_set - known_ids
        if unknown:
            raise ValueError(f"{label} references unknown block ids: {sorted(unknown)}")
        if label == "emission":
            if dropped & block_set:
                raise ValueError(f"{label} overlaps dropped block ids: {sorted(dropped & block_set)}")
            referenced.update(block_set)
            return
        if label == "drop":
            if carry_ids & block_set:
                raise ValueError(f"{label} references carry-over block ids: {sorted(carry_ids & block_set)}")
            overlap = dropped & block_set
            if overlap:
                raise ValueError(f"{label} overlaps already-dropped block ids: {sorted(overlap)}")
            if referenced & block_set:
                raise ValueError(f"{label} overlaps emitted or tipped block ids: {sorted(referenced & block_set)}")
            dropped.update(block_set)
            return
        if label == "tip":
            if dropped & block_set:
                raise ValueError(f"{label} overlaps dropped block ids: {sorted(dropped & block_set)}")
            referenced.update(block_set)

    for emission in response["emissions"]:
        ingest(list(emission["block_ids"]), "emission")
    for dropped_item in response["drops"]:
        ingest(list(dropped_item["block_ids"]), "drop")
    if response["tip"]["status"] == "carry":
        ingest(list(response["tip"]["block_ids"]), "tip")
    elif response["tip"]["block_ids"]:
        raise ValueError("clear tip must not carry block ids")

    missing = page_ids - (referenced | dropped)
    if missing:
        raise ValueError(f"page {page['page_index']} left unaccounted block ids: {sorted(missing)}")


def append_page_response(state: VerificationState, response: dict[str, Any]) -> None:
    next_sequence = len(state.emissions) + 1
    page_index = response["page_index"]
    for emission in response["emissions"]:
        state.emissions.append(
            EmissionRecord(
                sequence=next_sequence,
                page_index=page_index,
                block_ids=list(emission["block_ids"]),
                kind=emission["kind"],
                markdown=emission["markdown"].strip(),
                notes=emission["notes"],
            )
        )
        next_sequence += 1
    for dropped in response["drops"]:
        state.drops.append(
            DropRecord(
                page_index=page_index,
                block_ids=list(dropped["block_ids"]),
                reason=dropped["reason"],
                notes=dropped["notes"],
            )
        )
    for flag in response["flags"]:
        state.flags.append(
            FlagRecord(
                page_index=page_index,
                block_ids=list(flag["block_ids"]),
                severity=flag["severity"],
                kind=flag["kind"],
                note=flag["note"],
            )
        )
    state.tip = TipState(**response["tip"])
    if page_index not in state.completed_pages:
        state.completed_pages.append(page_index)


def flush_tip(state: VerificationState) -> None:
    if state.tip.status != "carry" or not state.tip.markdown.strip():
        return
    if state.emissions:
        tail = state.emissions[-1]
        if tail.markdown.strip() == state.tip.markdown.strip() and set(tail.block_ids) == set(state.tip.block_ids):
            return
    state.emissions.append(
        EmissionRecord(
            sequence=len(state.emissions) + 1,
            page_index=state.completed_pages[-1] if state.completed_pages else 0,
            block_ids=list(state.tip.block_ids),
            kind=state.tip.kind if state.tip.kind != "none" else "other",
            markdown=state.tip.markdown.strip(),
            notes=f"forced terminal tip flush: {state.tip.notes}".strip(),
            forced_tip_flush=True,
        )
    )
    state.tip = TipState()


def render_verified_markdown(state: VerificationState) -> str:
    chunks = [item.markdown.strip() for item in state.emissions if item.markdown.strip()]
    return "\n\n".join(chunks) + ("\n" if chunks else "")


def verification_status(state: VerificationState) -> str:
    if state.failure.status == "failed":
        return "failed"
    if len(state.completed_pages) == len(state.selected_pages):
        return "success"
    return "in_progress"


def verification_report(state: VerificationState) -> dict[str, Any]:
    return {
        "status": verification_status(state),
        "source_document_path": state.source_document_path,
        "source_pdf": state.source_pdf,
        "codex_thread_id": state.codex_thread_id,
        "codex_boot_response": state.codex_boot_response,
        "selected_pages": state.selected_pages,
        "completed_pages": state.completed_pages,
        "failure": asdict(state.failure),
        "failed_page": state.failure.page_index,
        "last_error": state.failure.error or None,
        "last_bad_prompt_path": state.failure.prompt_path,
        "last_bad_response_path": state.failure.response_path,
        "last_error_path": state.failure.error_path,
        "tip": asdict(state.tip),
        "emission_count": len(state.emissions),
        "drop_count": len(state.drops),
        "flag_count": len(state.flags),
        "emissions": [asdict(item) for item in state.emissions],
        "drops": [asdict(item) for item in state.drops],
        "flags": [asdict(item) for item in state.flags],
        "runs": [asdict(item) for item in state.runs],
    }


def persist_outputs(output_dir: Path, state_path: Path, state: VerificationState) -> None:
    save_state(state_path, state)
    write_json(output_dir / "verification.report.json", verification_report(state))
    (output_dir / "document.verified.md").write_text(render_verified_markdown(state), encoding="utf-8")


def register_failure(
    state: VerificationState,
    *,
    page_index: int | None,
    attempt: int | None,
    error: Exception,
    prompt_path: Path | None,
    response_path: Path | None,
    error_path: Path | None,
) -> None:
    state.failure = FailureState(
        status="failed",
        page_index=page_index,
        attempt=attempt,
        error=str(error),
        prompt_path=str(prompt_path) if prompt_path is not None else None,
        response_path=str(response_path) if response_path is not None else None,
        error_path=str(error_path) if error_path is not None else None,
    )


def clear_failure(state: VerificationState) -> None:
    state.failure = FailureState()


def retry_feedback(error: Exception, allowed_block_ids: list[str]) -> str:
    return (
        f"Validation or turn failure: {error}. "
        f"Allowed block ids for this page are exactly: {allowed_block_ids}."
    )


def trusted_working_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> int:
    args = parse_args()
    input_path = resolve_document_path(args.input)
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    pages_root = output_dir / "pages"
    state_path = output_dir / "state.json"

    document = json.loads(input_path.read_text(encoding="utf-8"))
    pages = list(document["pages"])
    selected_pages = parse_page_spec(args.pages, len(pages))

    state = load_state(state_path)
    if state is None:
        state = VerificationState.new(
            source_document_path=input_path,
            source_pdf=document["source_pdf"],
            selected_pages=selected_pages,
        )
    else:
        if state.source_document_path != str(input_path):
            raise ValueError("existing verification state points at a different OCR ledger")
        if state.selected_pages != selected_pages:
            raise ValueError("existing verification state was created with a different page selection")

    working_root = trusted_working_root()

    if state.codex_thread_id is None:
        try:
            thread_id, boot_response = run_codex_turn(
                prompt=BOOT_PROMPT,
                schema=BOOT_SCHEMA,
                session_id=None,
                image_paths=[],
                working_root=working_root,
            )
        except Exception as error:
            error_path = output_dir / "boot.error.txt"
            error_path.write_text(str(error), encoding="utf-8")
            register_failure(
                state,
                page_index=None,
                attempt=1,
                error=error,
                prompt_path=None,
                response_path=None,
                error_path=error_path,
            )
            persist_outputs(output_dir, state_path, state)
            raise
        state.codex_thread_id = thread_id
        state.codex_boot_response = boot_response
        clear_failure(state)
        persist_outputs(output_dir, state_path, state)

    page_lookup = {page["page_index"]: page for page in pages}
    pending_pages = [page_index for page_index in selected_pages if page_index not in state.completed_pages]

    for page_index in pending_pages:
        page = page_lookup[page_index]
        page_output_dir = pages_root / f"{page_index:04d}"
        page_output_dir.mkdir(parents=True, exist_ok=True)
        carry_block_ids = set(state.tip.block_ids) if state.tip.status == "carry" else set()
        allowed_block_ids = sorted({block["block_id"] for block in page["blocks"]} | carry_block_ids)
        validation_note: str | None = None
        previous_invalid_response: dict[str, Any] | None = None

        for attempt in range(1, MAX_PAGE_ATTEMPTS + 1):
            prompt = build_page_prompt(
                state,
                page,
                allowed_block_ids=allowed_block_ids,
                validation_feedback=validation_note,
                previous_invalid_response=previous_invalid_response,
            )
            prompt_path = page_output_dir / f"request.attempt-{attempt:02d}.txt"
            prompt_path.write_text(prompt, encoding="utf-8")
            (page_output_dir / "request.txt").write_text(prompt, encoding="utf-8")

            response: dict[str, Any] | None = None
            response_path = page_output_dir / f"response.attempt-{attempt:02d}.json"
            error_path = page_output_dir / f"error.attempt-{attempt:02d}.txt"
            try:
                thread_id, response = run_codex_turn(
                    prompt=prompt,
                    schema=PAGE_SCHEMA,
                    session_id=state.codex_thread_id,
                    image_paths=page_image_attachments(page),
                    working_root=working_root,
                )
                if thread_id is not None and thread_id != state.codex_thread_id:
                    state.codex_thread_id = thread_id
                write_json(response_path, response)
                write_json(page_output_dir / "response.json", response)
                error_path.unlink(missing_ok=True)
                account_blocks(page, response, carry_block_ids=carry_block_ids)
            except Exception as error:
                if response is not None:
                    write_json(response_path, response)
                    write_json(page_output_dir / "response.json", response)
                error_path.write_text(str(error), encoding="utf-8")
                register_failure(
                    state,
                    page_index=page_index,
                    attempt=attempt,
                    error=error,
                    prompt_path=prompt_path,
                    response_path=response_path if response is not None else None,
                    error_path=error_path,
                )
                persist_outputs(output_dir, state_path, state)
                if attempt >= MAX_PAGE_ATTEMPTS:
                    raise
                validation_note = retry_feedback(error, allowed_block_ids)
                previous_invalid_response = response
                continue

            state.runs.append(
                PageRunRecord(
                    page_index=page_index,
                    attempt=attempt,
                    prompt_path=str(prompt_path),
                    response_path=str(response_path),
                    image_path=page["image_path"],
                )
            )
            append_page_response(state, response)
            clear_failure(state)
            persist_outputs(output_dir, state_path, state)
            break

    flush_tip(state)
    clear_failure(state)
    persist_outputs(output_dir, state_path, state)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
