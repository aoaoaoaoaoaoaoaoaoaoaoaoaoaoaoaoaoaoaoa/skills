# Python Addendum

This addendum extends [universal.md](universal.md).

A Python program is statically specified and hosted by a dynamic runtime. Every core value and callable has a shape the type checker can read. `Any` erases what the checker knows: wrap untyped dependencies, I/O, and reflection in typed façades that refine their output, and treat the typed representation as authoritative once a value is inside the core.

Model closed sets of values as unions of frozen, slotted records, and exhaust them with `match` and `assert_never`. Model open capabilities with `Protocol` and exact generics. Give identities and units distinct static types. `T | None` denotes exactly one absence, never an unlabeled sequence of phases.

Make domain objects participate directly in the data model, through iteration, context management, calling, indexing, and operators, instead of surrounding them with helper functions. Dynamic machinery, including decorators, descriptors, metaclasses, and code generation, is subject to the type checker: use it only where the checker can see its result, as with `dataclass_transform`, and spend it centrally to produce typed interfaces instead of spreading reflection through live logic.

Target the latest Python that live dependencies permit; dependency support, not habit, sets the floor. Write the current dialect throughout, and delete obsolete spellings and compatibility scaffolding.

Express transformations with iterators, comprehensions, pattern matching, and dispatch tables keyed by enums or types, so that the whole operation stays visible. Interpreter work is real cost: choose the right algorithm, push bulk work into builtins or native libraries, and avoid needless object creation.

Model expected failure with structured result or exception types. `dict.get` with an invented default and redundant `None` guards are the Python forms of dummy defaults. `assert` states an internal proof obligation; it does not validate input.

## Tooling

- uv owns environments, dependencies, locking, and execution. `pyproject.toml` is the canonical metadata, and maintained projects commit `uv.lock`.
- Ruff owns formatting, linting, and modernization, with the `UP` rules enabled.
- `ty check` runs as a strict build step.
- `Any`, suppressions, and lint exceptions are narrow, local, and explicit.
- Standalone scripts use PEP 723 inline metadata and `#!/usr/bin/env -S uv run --script`.
