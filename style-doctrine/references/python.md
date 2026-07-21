# Python Style Doctrine

Treat Python as a statically specified program hosted by a dynamic runtime. Every core value and callable should have a type-checker-legible shape. Ambient `Any` is semantic amnesia; seal untyped dependencies, I/O, and reflective surfaces behind typed refinement façades. Once a value enters the core, its typed representation is authoritative.

Model closed value worlds as unions of slotted, frozen records and exhaust them with `match` and `assert_never`. Model open capabilities with `Protocol` and exact generics. Give identities and units distinct static types. `T | None` denotes exactly one absence alternative, never an unlabeled phase machine.

Command Python’s data model. Make domain objects participate directly in iteration, context management, callability, indexing, and algebra instead of surrounding them with ceremonial helper APIs. Decorators, descriptors, metaclasses, registration machinery, and code generation are primary abstraction tools. Spend dynamism centrally to generate lean, typed surfaces; do not smear reflection through live logic.

Target the latest Python permitted by live dependencies. Dependency support, not habit, sets the version floor. Maintain no syntactic backward compatibility without a live contract. Use the current dialect throughout and enforce Ruff’s `UP` rules; obsolete spellings and compatibility scaffolding must die.

Express transformations through iterator algebra, comprehensions, pattern matching, and data-driven dispatch so the whole operation remains visible. Treat interpreter work as real cost: choose the right algorithm, push bulk operations through builtins or native libraries, and eliminate object churn. Never purchase a tidy surface with repeated Python-level work.

Refine input at boundaries and trust the resulting representation inside. Model expected failure with structured result or exception types. Catch only to recover or translate semantically; otherwise propagate. Reject dishonest `.get` defaults, broad catch-and-limp wrappers, redundant `None` guards, and validation theater. `assert` states an internal proof obligation; it is not input validation.

The Astral stack is build law. `uv` owns environments, dependencies, locking, and execution; `pyproject.toml` is canonical metadata, and maintained projects check in `uv.lock`. Ruff owns formatting, linting, and modernization, with `UP` enabled. `ty check` is a strict build step; `Any`, suppressions, and lint exceptions must be narrow, local, and explicit. Standalone scripts use PEP 723 metadata and `#!/usr/bin/env -S uv run --script`.
