#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = [
#   "shazamio==0.8.1",
# ]
# ///

import argparse
import asyncio
import json
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning)

from shazamio import Shazam


def album(track: dict) -> str | None:
    return next(
        (
            item.get("text")
            for section in track.get("sections", [])
            for item in section.get("metadata", [])
            if item.get("title") == "Album"
        ),
        None,
    )


async def recognize(paths: list[Path]) -> list[dict]:
    shazam = Shazam()
    results = []
    for path in paths:
        response = await shazam.recognize(str(path))
        track = response.get("track")
        results.append(
            {
                "file": str(path),
                "match": None
                if track is None
                else {
                    "artist": track.get("subtitle"),
                    "title": track.get("title"),
                    "album": album(track),
                    "isrc": track.get("isrc"),
                    "genre": track.get("genres", {}).get("primary"),
                    "url": track.get("url"),
                },
            }
        )
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Recognize local audio clips with Shazam.")
    parser.add_argument("clips", nargs="+", type=Path)
    args = parser.parse_args()
    missing = [str(path) for path in args.clips if not path.is_file()]
    if missing:
        parser.error(f"not a file: {', '.join(missing)}")
    print(json.dumps(asyncio.run(recognize(args.clips)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
