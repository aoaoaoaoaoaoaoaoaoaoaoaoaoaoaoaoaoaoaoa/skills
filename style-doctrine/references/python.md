# Python Style Doctrine

Python must be written as if it were statically compiled. The target is not "Pythonic" ease; the target is statically legible, brutally lean code that strong agents and type checkers can reason about. Dynamic affordances are acceptable only when they compress real structure without dissolving it.

Use strict typing to the hilt. Ban ambient `Any` in core code; quarantine untyped third-party and IO surfaces behind typed façades. Use `Protocol`, `NewType`, `Literal`, `Final`, `TypeAlias`, `Self`, generics, overloads, `Never`/`assert_never`, `TypeGuard`/`TypeIs`, `dataclass(slots=True, frozen=True)`, enums, and ADT-like unions aggressively. If a primitive carries domain semantics, give it static shape. Prefer total constructors and narrow parser boundaries over repeated checks.

## Latest Syntax

Use the latest Python syntax, full stop. Do not preserve syntactic backward compatibility with older Python versions. If dependency constraints do not force an older interpreter, target the latest viable Python and write code in that dialect.

This is not only about types. Use newer syntax wherever it saves tokens, sharpens static structure, or deletes compatibility ceremony: 3.12+ generic syntax (`class Box[T]`, `def f[T](x: T) -> T`, `type Json = ...`) instead of `TypeVar` scaffolding, builtin containers and modern abstract interfaces (`dict`, `list`, `set`, `tuple`, `collections.abc.Mapping`) instead of `typing.Dict`-style fossils, `A | B` instead of `Union`/`Optional`, structural `match`/`case` when it collapses branching, assignment expressions when they eliminate honest duplication, exception groups when the problem is truly aggregate, and any newer spelling that makes the program smaller and more exact.

This list is illustrative, not exhaustive. If newer syntax exists and the project can run it, use it. Ruff's pyupgrade rules (`UP`) are mandatory: enable them, run them, apply them, and finish any remaining modernization by hand.

Defensive programming is a bloating disease. Do not sprinkle `.get` defaults with no honest semantics, `None` guards proven impossible by construction, catch-and-limp wrappers, optional bags, or runtime validation theater. Fail early, loudly, and close to the violated invariant. Inside already-typed code, trust the typed representation.

Prefer algebraic, compositional Python: pure transforms, `match`/`case`, table-driven dispatch, protocols, higher-order functions, compact comprehensions, and small domain modules. Decorators and metaprogramming are legitimate when they reduce call-site noise or enforce uniformity. Operator overloading is encouraged when the operation has the expected algebraic meaning.

Bias toward token and line count reduction when it increases semantic density. Delete compatibility husks, duplicate builders, scattered casts, repeated fixture factories, parallel dict/list structures, ceremonial wrappers, and helper functions whose only purpose is surviving weak types. A compact typed representation beats ten "safe" branches synchronized by anxiety.

Default to zero backward compatibility with old Python versions. If dependency constraints do not forbid it and the review is global in scope, upgrade to the latest viable Python and modernize syntax. If it can be upgraded, it should be.

Astral tooling is mandatory doctrine: `uv`, `ruff`, and `ty` should be present unless the project has an explicit incompatible reason. `pyproject.toml` is canonical metadata, `uv.lock` should be checked in for projects, `uv run` is the execution primitive, Ruff formatting is mandatory, Ruff modernization rules should be used, and `ty check` is part of the build contract. Lint strictly by default and carve out only low-value human-readability theater with explicit intent.
