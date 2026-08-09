#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# ///
"""Extract human messages from a public ChatGPT shared conversation."""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Final, TypeAlias, cast
from urllib.parse import urlparse

Json: TypeAlias = None | bool | int | float | str | list["Json"] | dict[str, "Json"]
Materialized: TypeAlias = (
    None | bool | int | float | str | list["Materialized"] | dict[str, "Materialized"]
)

_ENQUEUE: Final = re.compile(
    r'streamController\.enqueue\(("(?:\\.|[^"\\])*")\)', re.DOTALL
)
_ROLES: Final = frozenset({"assistant", "user"})


class ExtractionError(RuntimeError):
    """The supplied artifact does not contain a supported shared conversation."""


def _read_source(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme not in {"http", "https"}:
        return Path(source).read_text(encoding="utf-8")
    if (
        parsed.scheme != "https"
        or parsed.hostname != "chatgpt.com"
        or not parsed.path.startswith("/share/")
    ):
        raise ExtractionError("expected an https://chatgpt.com/share/... URL")
    result = subprocess.run(
        ["curl", "--location", "--fail", "--silent", "--show-error", source],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def _serialized_table(page: str) -> list[Json]:
    for match in _ENQUEUE.finditer(page):
        chunk = cast(str, json.loads(match.group(1))).strip()
        if not chunk.startswith("["):
            continue
        candidate = cast(Json, json.loads(chunk))
        if isinstance(candidate, list):
            return candidate
    raise ExtractionError(
        "React Router conversation table not found; the share format may have changed"
    )


class _Unflattener:
    def __init__(self, table: list[Json]) -> None:
        self._table = table
        self._memo: dict[int, Materialized] = {}

    def get(self, reference: int) -> Materialized:
        if reference < 0:
            return {-2: math.nan, -3: math.inf, -4: -math.inf, -6: -0.0}.get(reference)
        if reference in self._memo:
            return self._memo[reference]
        try:
            value = self._table[reference]
        except IndexError as error:
            raise ExtractionError(f"invalid flattened reference {reference}") from error
        if not isinstance(value, (list, dict)):
            return value
        if isinstance(value, list):
            materialized: Materialized = []
            self._memo[reference] = materialized
            cast(list[Materialized], materialized).extend(
                self.get(item)
                if isinstance(item, int) and not isinstance(item, bool)
                else item
                for item in value
            )
            return materialized
        materialized = {}
        self._memo[reference] = materialized
        output = cast(dict[str, Materialized], materialized)
        for encoded_key, encoded_value in value.items():
            if not encoded_key.startswith("_"):
                raise ExtractionError(f"invalid flattened key {encoded_key!r}")
            key = self.get(int(encoded_key[1:]))
            if not isinstance(key, str):
                raise ExtractionError("flattened object key is not a string")
            output[key] = self.get(_reference(encoded_value))
        return materialized


def _reference(value: Json) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ExtractionError(f"expected flattened integer reference, found {value!r}")
    return value


def _object(value: Materialized, context: str) -> dict[str, Materialized]:
    if not isinstance(value, dict):
        raise ExtractionError(f"{context} is not an object")
    return value


def _array(value: Materialized, context: str) -> list[Materialized]:
    if not isinstance(value, list):
        raise ExtractionError(f"{context} is not an array")
    return value


def _conversation(page: str) -> dict[str, Materialized]:
    root = _object(_Unflattener(_serialized_table(page)).get(0), "root")
    loader = _object(root.get("loaderData"), "loaderData")
    route = next(
        (value for key, value in loader.items() if key.startswith("routes/share.")),
        None,
    )
    response = _object(
        _object(route, "share route").get("serverResponse"), "serverResponse"
    )
    return _object(response.get("data"), "conversation")


def _messages(conversation: dict[str, Materialized]) -> Iterable[tuple[int, str, str]]:
    nodes = _array(conversation.get("linear_conversation"), "linear_conversation")
    for index, node_value in enumerate(nodes):
        node = _object(node_value, f"node {index}")
        message_value = node.get("message")
        if not isinstance(message_value, dict):
            continue
        message = cast(dict[str, Materialized], message_value)
        author_value = message.get("author")
        content_value = message.get("content")
        if not isinstance(author_value, dict) or not isinstance(content_value, dict):
            continue
        role = cast(dict[str, Materialized], author_value).get("role")
        parts_value = cast(dict[str, Materialized], content_value).get("parts")
        if not isinstance(role, str) or not isinstance(parts_value, list):
            continue
        text = "\n".join(part for part in parts_value if isinstance(part, str)).strip()
        if role in _ROLES and text:
            yield index, role, text


def _has_final_response(conversation: dict[str, Materialized]) -> bool:
    current_id = conversation.get("current_node")
    mapping = conversation.get("mapping")
    if not isinstance(current_id, str) or not isinstance(mapping, dict):
        return False
    node = mapping.get(current_id)
    if not isinstance(node, dict):
        return False
    message = node.get("message")
    if not isinstance(message, dict):
        return False
    author = message.get("author")
    content = message.get("content")
    metadata = message.get("metadata")
    if not isinstance(author, dict) or not isinstance(content, dict):
        return False
    parts = content.get("parts")
    has_text = isinstance(parts, list) and any(
        isinstance(part, str) and part.strip() for part in parts
    )
    return (
        author.get("role") == "assistant"
        and message.get("status") == "finished_successfully"
        and message.get("end_turn") is True
        and message.get("recipient") == "all"
        and has_text
        and not (
            isinstance(metadata, dict)
            and metadata.get("is_thinking_preamble_message") is True
        )
    )


def _render(source: str, last: str | None, require_final: bool) -> str:
    conversation = _conversation(_read_source(source))
    if require_final and not _has_final_response(conversation):
        raise ExtractionError("shared conversation has not reached a final response")
    messages = list(_messages(conversation))
    if last is not None:
        try:
            return (
                next(text for _, role, text in reversed(messages) if role == last)
                + "\n"
            )
        except StopIteration as error:
            raise ExtractionError(f"no nonempty {last} message found") from error
    title = conversation.get("title")
    heading = title if isinstance(title, str) else "Shared ChatGPT Conversation"
    sections = [f"# {heading}"]
    sections.extend(
        f"## {role.title()} · node {index}\n\n{text}" for index, role, text in messages
    )
    return "\n\n".join(sections) + "\n"


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source", help="ChatGPT share URL or previously downloaded HTML file"
    )
    parser.add_argument(
        "--last", choices=sorted(_ROLES), help="emit only the last message by role"
    )
    parser.add_argument(
        "--require-final",
        action="store_true",
        help="fail unless the shared conversation currently ends in a final response",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    arguments = _parser().parse_args(argv)
    try:
        print(_render(arguments.source, arguments.last, arguments.require_final), end="")
    except (
        ExtractionError,
        OSError,
        subprocess.CalledProcessError,
        json.JSONDecodeError,
    ) as error:
        raise SystemExit(f"extract_shared_chat: {error}") from error
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
