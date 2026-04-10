#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.13.*"
# dependencies = ["tiktoken==0.12.0"]
# ///

from __future__ import annotations

import argparse
import contextlib
import fcntl
import sys
import tempfile
from collections.abc import Iterator
from pathlib import Path

import tiktoken


LANGUAGE_BY_SUFFIX = {
    ".c": "c",
    ".cc": "cpp",
    ".conf": "text",
    ".cpp": "cpp",
    ".css": "css",
    ".csv": "csv",
    ".go": "go",
    ".h": "c",
    ".hpp": "cpp",
    ".html": "html",
    ".java": "java",
    ".js": "javascript",
    ".json": "json",
    ".jsonl": "json",
    ".kt": "kotlin",
    ".log": "text",
    ".lua": "lua",
    ".md": "markdown",
    ".patch": "diff",
    ".proto": "proto",
    ".py": "python",
    ".rb": "ruby",
    ".rs": "rust",
    ".sh": "bash",
    ".sql": "sql",
    ".toml": "toml",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".txt": "text",
    ".xml": "xml",
    ".yaml": "yaml",
    ".yml": "yaml",
}

HARD_MAX_TOKENS = 75_000
GLOBAL_APPEND_LOCK = Path(tempfile.gettempdir()) / "assemble-pro-review-package-inline-section.lock"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Append a labeled markdown section containing a file or excerpt to a "
            "target document, while enforcing the skill's fixed 75k-token hard budget."
        )
    )
    parser.add_argument("source", type=Path, help="Source file to inline.")
    parser.add_argument("target", type=Path, help="Markdown file to append into.")
    parser.add_argument(
        "--label",
        help="Section label. Defaults to the source path as provided.",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="One-indexed start line, inclusive. Defaults to 1.",
    )
    parser.add_argument(
        "--end",
        type=int,
        help="One-indexed end line, inclusive. Defaults to EOF.",
    )
    parser.add_argument(
        "--heading-level",
        type=int,
        default=2,
        help="Markdown heading level for the section. Defaults to 2.",
    )
    parser.add_argument(
        "--encoding",
        default="o200k_base",
        help="Tiktoken encoding name used for the hard budget. Defaults to o200k_base.",
    )
    parser.add_argument(
        "--model",
        help=(
            "Optional model name for encoding lookup. If unavailable, the script falls "
            "back to --encoding."
        ),
    )
    return parser.parse_args()


def fail(message: str) -> "NoReturn":
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(2)


def normalize_span(start: int, end: int | None, total_lines: int) -> tuple[int, int]:
    if start < 1:
        fail("--start must be at least 1")
    if start > total_lines:
        fail(
            f"--start {start} exceeds the source length of {total_lines} line"
            f"{'' if total_lines == 1 else 's'}"
        )
    resolved_end = total_lines if end is None else min(end, total_lines)
    if resolved_end < start:
        fail("--end must be greater than or equal to --start")
    return start, resolved_end


def resolve_language(path: Path) -> str:
    return LANGUAGE_BY_SUFFIX.get(path.suffix.lower(), "text")


def load_encoding(model: str | None, encoding_name: str) -> tuple[tiktoken.Encoding, str]:
    if model is not None:
        try:
            encoding = tiktoken.encoding_for_model(model)
            return encoding, f"model:{model}->{encoding.name}"
        except KeyError:
            pass
    return tiktoken.get_encoding(encoding_name), f"encoding:{encoding_name}"


def choose_fence(body: str) -> str:
    longest_run = 0
    current_run = 0
    for char in body:
        if char == "`":
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0
    return "`" * max(3, longest_run + 1)


@contextlib.contextmanager
def hold_global_append_lock() -> Iterator[None]:
    GLOBAL_APPEND_LOCK.parent.mkdir(parents=True, exist_ok=True)
    with GLOBAL_APPEND_LOCK.open("a+", encoding="utf-8") as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


def render_section(
    *,
    label: str,
    source_name: str,
    start: int,
    end: int,
    body: str,
    language: str,
    heading_level: int,
) -> str:
    if heading_level < 1:
        fail("--heading-level must be at least 1")
    heading = "#" * heading_level
    lines_label = f"{start}" if start == end else f"{start}-{end}"
    fence = choose_fence(body)
    if body and not body.endswith("\n"):
        body = f"{body}\n"
    return (
        f"{heading} {label}\n\n"
        f"Source: `{source_name}`\n"
        f"Lines: `{lines_label}`\n\n"
        f"{fence}{language}\n"
        f"{body}"
        f"{fence}\n"
    )


def main() -> None:
    args = parse_args()
    source = args.source
    target = args.target

    if not source.is_file():
        fail(f"source file not found: {source}")

    source_text = source.read_text(encoding="utf-8", errors="replace")
    source_lines = source_text.splitlines(keepends=True)
    if not source_lines:
        fail("source file is empty")

    start, end = normalize_span(args.start, args.end, len(source_lines))
    excerpt = "".join(source_lines[start - 1 : end])
    label = args.label or str(source)
    section = render_section(
        label=label,
        source_name=str(source),
        start=start,
        end=end,
        body=excerpt,
        language=resolve_language(source),
        heading_level=args.heading_level,
    )

    encoding, encoding_label = load_encoding(args.model, args.encoding)
    section_tokens = len(encoding.encode(section))

    with hold_global_append_lock():
        existing = ""
        if target.exists():
            if target.is_dir():
                fail(f"target is a directory: {target}")
            existing = target.read_text(encoding="utf-8", errors="replace")

        separator = "\n\n" if existing else ""
        rendered = f"{existing}{separator}{section}"
        total_tokens = len(encoding.encode(rendered))
        existing_tokens = len(encoding.encode(existing))

        if total_tokens > HARD_MAX_TOKENS:
            fail(
                "refusing append because the projected document would exceed the hard budget: "
                f"{total_tokens} > {HARD_MAX_TOKENS} ({encoding_label}; existing={existing_tokens}; "
                f"section={section_tokens})"
            )

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")

    print(f"appended: {label}")
    print(f"source: {source}")
    print(f"target: {target}")
    print(f"lines: {start}-{end}")
    print(f"encoding: {encoding_label}")
    print(f"section_tokens: {section_tokens}")
    print(f"total_tokens: {total_tokens}")


if __name__ == "__main__":
    main()
