# Java Addendum

This addendum extends [universal.md](universal.md).

Target the newest viable JDK and class-file level, including preview features under a pinned toolchain. Old bytecode levels, Java 8 idioms, bean conventions, framework compatibility, serialization shapes, and deployment assumptions survive only under a live contract. Modernize the design, not only its spelling.

Model products as records and closed sums as sealed interfaces with record or enum variants, and make pattern switches exhaustive. Control construction so that domain values are valid from birth, and use package and module visibility as proof boundaries. Null is never an implicit domain variant; represent absence and richer alternatives explicitly. Keep value graphs immutable and give every mutation an explicit owner. Delete mutable beans, DTO twins, telescoping constructors, and ceremonial builders.

Interfaces play the role of traits: they state laws, capabilities, and type relations, not service-layer indirection. Use generics, sealing, and default and static methods until the algebra is exact. Annotation processors and source generation let one domain declaration emit every mechanical projection. Keep reflection, method handles, and `invokedynamic` behind typed interfaces.

Bind resource ownership lexically with try-with-resources. Use virtual threads for abundant blocking concurrency, with structured task ownership and cancellation instead of detached futures or callback graphs. Scoped context stays lexical; do not use ambient `ThreadLocal` state.

The object graph is the machine representation: allocation, boxing, copying, dispatch, retention, and reflection are real costs. Choose streams, collectors, or loops by the work each generates. Drive hot data through primitives, arrays, or native and vector facilities where the cost model demands. Settle performance claims with JMH, JFR, allocation profiles, and compiler output.

Expected alternatives that callers must handle are sealed result types; exceptions carry nonlocal or environmental failure.

## Tooling

- The build runs formatting, compiler warnings as errors, dependency analysis, static nullness checking, and Error Prone-style bug checks.
- One nullness regime applies across the project.
