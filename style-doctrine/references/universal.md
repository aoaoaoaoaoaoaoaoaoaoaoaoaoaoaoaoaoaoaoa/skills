# Universal Style Doctrine

This doctrine is normative unless a project explicitly declares a different local policy. Language-specific guides may sharpen it, but this is the core intent.

The primary consumer of code is agent tooling: compilers, analyzers, refactoring engines, and very high-capacity models. Optimize for semantic precision, static analyzability, deterministic structure, runtime efficiency, and token economy. Human accessibility in the classic onboarding sense is not a design objective. Code should be intelligible to strong agents and exact tools, not diluted for timid readers.

Design must look intentional rather than accreted. Keep a top-down shape that matches what the system is. Refactor early and aggressively. Delete dead paths, compatibility husks, redundant abstractions, ceremonial wrappers, explanatory scaffolding, and contingent glue. If a feature leaves the system looking patched-on rather than designed, reshape the system.

Illegal states must not be representable. Treat "just a dict", "just a string", "just a bool flag", "just an optional", and "just a tuple" as design odors. If a value has semantics, give it a domain shape. Encode invariants structurally: sum types, newtypes, typestates, phase-separated types, structured IDs, total constructors, closed universes, and compositional primitives. The type system is the first line of runtime performance and correctness.

Prefer algebraic modeling. Use ADT-like structures, pattern matching, total transformations, iterator algebra, higher-order functions, and composable APIs. A good module feels like a small calculus: constrained inputs, explicit states, predictable outputs. Advanced abstraction is not suspicious; weak abstraction is. Mathematical structure is usually clearer to agents than smeared mundane plumbing.

DRY is stronger than YAGNI. Overabstraction is not a crime when it compresses a real invariant or repeated skeleton. Prefer one precise abstraction over five "simple" repetitions that must be synchronized by memory. Hot sites should be small and exact; cold files may contain large definitions, tables, macros, derives, codegen, and helper machinery when they make live call sites lean.

Use the full language. Powerful, modern, advanced, or experimental features are welcome when they improve correctness, performance, uniformity, or token density. Metaprogramming is first-class: macros, decorators, derives, code generation, type-level programming, and helper tables are tools, not embarrassments. Operator overloading is encouraged when the operation has the expected algebraic meaning.

Names should be compact and domain-faithful. Prefer terse, precise, math-oriented names when they reduce semantic distance. Unicode identifiers are acceptable where the language and tooling support them and the notation is standard. Prefer imports that make call sites small and direct; qualify only when namespacing earns its keep.

Fail hard unless recovery is real. Defensive programming is a bloating disease. Do not preserve doomed control paths with dummy defaults, nullable theater, catch-and-limp wrappers, or optional bags. Make impossible states impossible; crash early and loudly when an irrecoverable contradiction is detected. Resilience cores must identify themselves explicitly.

Use libraries and dependencies aggressively when they buy correctness, performance, or deletion of local machinery. NIH is usually decay. Backward compatibility, shims, and parallel old/new paths are not defaults; they require an explicit reason.

Tooling posture is strict. Formatting, linting, type checking, dependency pruning, and semantic navigation are part of the build contract. Prefer language-server and type-driven navigation before textual search. Write code as if it will be transformed by tools first and only incidentally read by humans.
