#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.13.*"
# dependencies = []
# ///

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the noo-harvest paper extraction and phase-2 verification pipeline."
    )
    parser.add_argument("input_pdf")
    parser.add_argument("output_dir")
    parser.add_argument("--model-path", help="Explicit local DeepSeek-OCR-2 snapshot for paper_ocr.py")
    parser.add_argument("--ocr-python", help="Explicit Python interpreter for the OCR runtime")
    parser.add_argument("--pages", help="Comma-separated 1-based pages and ranges, e.g. 1,3-5")
    parser.add_argument(
        "--extract-only",
        action="store_true",
        help="Run OCR extraction only; do not invoke phase-2 verification",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Run phase-2 verification from an existing extracted/document.blocks.json",
    )
    parser.add_argument(
        "--force-extract",
        action="store_true",
        help="Rerun OCR extraction even if extracted/document.blocks.json already exists",
    )
    return parser.parse_args()


def run_step(argv: list[str], *, cwd: Path | None = None) -> None:
    subprocess.run(argv, check=True, cwd=cwd)


def discover_ocr_python(explicit: str | None) -> str:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())

    env_python = os.environ.get("NOO_HARVEST_OCR_PYTHON")
    if env_python:
        candidates.append(Path(env_python).expanduser())

    repo_root = Path(__file__).resolve().parents[2]
    candidates.append(repo_root / ".tmp/deepseek-ocr2/.venv/bin/python")

    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)

    return sys.executable


def main() -> int:
    args = parse_args()
    if args.extract_only and args.verify_only:
        raise SystemExit("--extract-only and --verify-only are mutually exclusive")

    script_root = Path(__file__).resolve().parent
    trusted_root = script_root.parents[1]
    input_pdf = Path(args.input_pdf).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    extracted_dir = output_dir / "extracted"
    verified_dir = output_dir / "verified"
    document_path = extracted_dir / "document.blocks.json"
    ocr_python = discover_ocr_python(args.ocr_python)

    if not args.verify_only and (args.force_extract or not document_path.is_file()):
        ocr_cmd = [ocr_python, str(script_root / "paper_ocr.py"), str(input_pdf), str(extracted_dir)]
        if args.model_path:
            ocr_cmd.extend(["--model-path", args.model_path])
        if args.pages:
            ocr_cmd.extend(["--pages", args.pages])
        run_step(ocr_cmd, cwd=trusted_root)
    elif not document_path.is_file():
        raise SystemExit(f"missing extracted ledger at {document_path}; rerun without --verify-only")

    if args.extract_only:
        return 0

    verify_cmd = [sys.executable, str(script_root / "paper_verify.py"), str(extracted_dir), str(verified_dir)]
    if args.pages:
        verify_cmd.extend(["--pages", args.pages])
    run_step(verify_cmd, cwd=trusted_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
