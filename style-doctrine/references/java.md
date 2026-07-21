# Java Style Doctrine

Target the newest viable JDK and class-file level. Old bytecode, Java 8 idioms, bean conventions, framework compatibility, serialization shapes, and deployment assumptions carry no presumption; only a live contract keeps them. Use current language and runtime features, including preview facilities under a pinned toolchain. Modernize the design, not merely its spelling.

Model products as records and closed sums as sealed interfaces with record or enum variants; make pattern switches exhaustive. Control construction so domain values are born lawful, and use package and module visibility as proof boundaries. Null is never an implicit domain variant: represent real absence or richer alternatives explicitly. Keep value graphs immutable; mutation belongs to an explicit owner. Delete mutable beans, DTO twins, telescoping constructors, and ceremonial builders.

Treat interfaces as traits: use them to state laws, capabilities, and type relations, not to manufacture service-layer indirection. Apply generics, sealedness, and default or static methods until the algebra is exact. Annotation processors and source generation are primary abstraction machinery; one domain declaration should emit every mechanical projection. Concentrate reflection, method handles, and `invokedynamic` behind typed surfaces rather than smearing stringly machinery through live logic.

Make lifetime and concurrency structural. Use try-with-resources to bind resource ownership lexically. Use virtual threads for abundant blocking concurrency and structured task ownership and cancellation instead of detached future or callback graphs. Scoped context must remain lexical, never ambient `ThreadLocal` folklore.

Treat the object graph as machine representation. Allocation, boxing, copying, dispatch, retention, and reflection are real costs. Choose streams, collectors, or direct loops by the work they generate, not by stylistic allegiance. Drive hot data through primitives, arrays, or current native and vector facilities as the cost model demands. Adjudicate performance claims with JMH, JFR, allocation profiles, and compiler evidence.

Expected alternatives that callers must handle belong in explicit sealed result types; exceptions carry nonlocal or environmental failure. Catch only to recover or translate semantically, and preserve causes. Validate once at trust boundaries, then trust the domain representation. Crash close to an internal contradiction. Reject null theater, dummy defaults, catch-and-limp wrappers, and exception laundering.

Formatting, compiler warnings, tests, dependency analysis, and static nullness and bug analysis are build law. Enforce one project-wide nullness regime and strict Error Prone-style checks. Deny warnings by default; make suppressions precise, local, and recorded where tool taste conflicts with stronger design.
