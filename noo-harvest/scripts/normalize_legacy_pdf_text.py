#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.13.*"
# dependencies = []
# ///

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


TEXT_KEYS = {"text", "orig"}

ACUTE_MAP = str.maketrans(
    {
        "a": "á",
        "e": "é",
        "i": "í",
        "o": "ó",
        "u": "ú",
        "y": "ý",
        "A": "Á",
        "E": "É",
        "I": "Í",
        "O": "Ó",
        "U": "Ú",
        "Y": "Ý",
    }
)

TILDE_MAP = str.maketrans(
    {
        "a": "ã",
        "o": "õ",
        "n": "ñ",
        "A": "Ã",
        "O": "Õ",
        "N": "Ñ",
    }
)

SIMPLE_REPLACEMENTS = {
    "\x03": "*",
    "\x07": "",
    "\x0f": "",
    "\x10": "i",
    "\x12": "⊆",
    "\x14": "κ",
    "\x15": "≥",
    "\x19": "ß",
    "\x1b": "σ",
    "\x1c": "ø",
    "\x1d": "",
    "\x1e": "≺",
    "\x7f": "",
}


def normalize_legacy_pdf_text(text: str) -> str:
    # Legacy TeX/PostScript accent markers.
    text = text.replace("\x13\x10", "í")
    text = re.sub("\x13([AEIOUYaeiouy])", lambda m: m.group(1).translate(ACUTE_MAP), text)
    text = re.sub("\x18([cC])", lambda m: "ç" if m.group(1) == "c" else "Ç", text)
    text = text.replace("\x18", "~")
    text = re.sub("\x16([A-Za-z])", lambda m: m.group(1) + "\u0304", text)

    # Ligatures and overloaded glyph slots. The \x0c slot is context-sensitive:
    # inside a word it is usually the "fi" ligature; otherwise it is usually β.
    text = re.sub("\x0e(?=[A-Za-z])", "ffi", text)
    text = re.sub("\x0b(?=[A-Za-z])", "ff", text)
    text = re.sub("\x0c(?=[A-Za-z])", "fi", text)
    text = text.replace("\x0c", "β")

    for src, dst in SIMPLE_REPLACEMENTS.items():
        text = text.replace(src, dst)

    # TeX-ish accent remnants that lost their backslash.
    text = re.sub(r"~([aAoOnN])", lambda m: m.group(1).translate(TILDE_MAP), text)

    # Small cleanup passes that are common in this extraction family.
    text = text.replace("sub ject classifications", "subject classifications")
    text = text.replace("subject classiﬁcations", "subject classifications")
    text = re.sub(r"(?m)^y(?=[A-Z])", "†", text)
    text = re.sub(r"\*{3,}", "**", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


def normalize_docling_json(node: Any) -> Any:
    if isinstance(node, dict):
        out: dict[str, Any] = {}
        for key, value in node.items():
            if isinstance(value, str) and key in TEXT_KEYS:
                out[key] = normalize_legacy_pdf_text(value)
            else:
                out[key] = normalize_docling_json(value)
        return out
    if isinstance(node, list):
        return [normalize_docling_json(item) for item in node]
    return node


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Normalize legacy TeX/PostScript glyph corruption in extracted PDF text. "
            "Accepts Markdown/plaintext directly, or a Docling JSON document."
        )
    )
    parser.add_argument("input", type=Path, help="Input file")
    parser.add_argument("-o", "--output", type=Path, help="Output file; default is stdout")
    parser.add_argument(
        "--docling-json",
        action="store_true",
        help="Treat the input as a DoclingDocument JSON file and normalize text-bearing fields",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw = args.input.read_text(errors="replace")

    if args.docling_json:
        data = json.loads(raw)
        normalized = json.dumps(normalize_docling_json(data), ensure_ascii=False, indent=2)
    else:
        normalized = normalize_legacy_pdf_text(raw)

    if args.output is None:
        sys.stdout.write(normalized)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(normalized)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
