#!/usr/bin/env python3
"""Reject Cargo path dependencies that escape the repository."""

from __future__ import annotations

import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any


DEPENDENCY_TABLES = ("dependencies", "dev-dependencies", "build-dependencies")


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, check=False, capture_output=True, text=True
    )
    if result.returncode:
        raise SystemExit(result.stderr.strip() or "git failed")
    return result.stdout


def dependency_tables(document: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    found: list[tuple[str, dict[str, Any]]] = []
    for name in DEPENDENCY_TABLES:
        table = document.get(name)
        if isinstance(table, dict):
            found.append((name, table))

    workspace = document.get("workspace")
    if isinstance(workspace, dict):
        table = workspace.get("dependencies")
        if isinstance(table, dict):
            found.append(("workspace.dependencies", table))

    targets = document.get("target")
    if isinstance(targets, dict):
        for target, target_table in targets.items():
            if not isinstance(target_table, dict):
                continue
            for name in DEPENDENCY_TABLES:
                table = target_table.get(name)
                if isinstance(table, dict):
                    found.append((f"target.{target}.{name}", table))

    patches = document.get("patch")
    if isinstance(patches, dict):
        for source, table in patches.items():
            if isinstance(table, dict):
                found.append((f"patch.{source}", table))
    replacements = document.get("replace")
    if isinstance(replacements, dict):
        found.append(("replace", replacements))
    return found


def main() -> None:
    start = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    root = Path(git(start, "rev-parse", "--show-toplevel").strip()).resolve()
    tracked = {
        (root / line).resolve()
        for line in git(root, "ls-files", "--", "Cargo.toml", "*/Cargo.toml", "**/Cargo.toml")
        .splitlines()
        if line
    }
    violations: list[str] = []

    for manifest in sorted(tracked):
        document = tomllib.loads(manifest.read_text(encoding="utf-8"))
        for table_name, table in dependency_tables(document):
            for dependency, declaration in table.items():
                if not isinstance(declaration, dict) or not isinstance(
                    declaration.get("path"), str
                ):
                    continue
                target = (manifest.parent / declaration["path"]).resolve()
                target_manifest = target / "Cargo.toml"
                try:
                    target.relative_to(root)
                except ValueError:
                    violations.append(
                        f"{manifest.relative_to(root)} [{table_name}] {dependency}: "
                        f"path escapes repository ({target})"
                    )
                    continue
                if target_manifest not in tracked:
                    violations.append(
                        f"{manifest.relative_to(root)} [{table_name}] {dependency}: "
                        f"target manifest is not tracked ({target_manifest.relative_to(root)})"
                    )

    if violations:
        print("Cargo path preflight refused:", file=sys.stderr)
        for violation in violations:
            print(f"  {violation}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Cargo path preflight passed: {root}")


if __name__ == "__main__":
    main()
