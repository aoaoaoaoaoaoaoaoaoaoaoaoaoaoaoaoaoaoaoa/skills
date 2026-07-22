# Python Lens

Use this note when Python materially participates in the audited surface. It sharpens the generic protocol without supplying a smell checklist.

## Surface

The default implementation manifest contains handwritten `*.py` files. Include `pyproject.toml`, package metadata, schemas, and configuration when they materially define the scoped component. Virtual environments, generated code, notebooks, migrations, fixtures, snapshots, and vendored code remain outside the audit manifest unless explicitly included; they may still serve as context-fringe evidence.

## Semantic Posture

Reason about Python as though it were statically compiled. Precise annotations, protocols, generics, overloads, `NewType`, literal worlds, enums, frozen slotted dataclasses, typed records, structural matching, and exhaustive local structure are available when they reduce semantic description length.

Dynamic behavior earns survival when it compresses a real pattern or serves a real trust boundary. Ambient `Any`, dictionary-shaped internal models, repeated runtime validation, casts, optionality, and exception paths are not automatically defects; judge whether they carry honest variability or compensate for missing static truth.

Use the latest viable Python syntax and the repository's declared tooling posture. A language or toolchain migration is outside the semantic envelope unless authorized, even when house doctrine would prefer it globally.

External payloads, environment variables, CLI values, database rows, dataframes, and untyped libraries may remain dynamic at their boundaries. Convert once into the internal model when the program relies on stronger truth.

## Navigation

Use the available type checker, import graph, entrypoints, and textual search together. Construction, consumption, serialization, and protocol sites may each be the right anchor for a clique.

## Implementation Phase

When implementation is authorized, use the repository's existing formatter, linter, type checker, and tests. The audit phase itself must not depend on executing or modifying the target tree.
