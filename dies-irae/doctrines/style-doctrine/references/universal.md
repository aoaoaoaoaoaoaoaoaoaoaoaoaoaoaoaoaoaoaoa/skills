# Universal Style Doctrine

This guide governs all house code. A language addendum extends it and is never read without it. Explicit project instructions override both.

## Premises

House code is written and maintained by agents. Five facts about that arrangement shape every rule below.

1. The maintainer is fluent in every language feature, type-level construction, metaprogramming technique, and mathematical notation. Unfamiliarity costs it nothing, and its successors will be more capable still.
2. The maintainer is cold. Each session starts without the code's history and sees only the files it opens; it will break any invariant it cannot see from where it edits.
3. No human reads the code. Types, the compiler, linters, and runtime failures are the only oversight.
4. Agent labor is cheap. Writing, refactoring, migrating, and rewriting cost little, and diff size is not a cost.
5. Tokens are expensive. Every token of code is paid again each time an agent reads it.

Conventional practice compensates for human limits: working memory, unfamiliarity, and the cost of rewriting. This doctrine drops those compensations and consequently inverts much conventional advice. Do not translate it back into conventional defaults. Where agent and human readability coincide, as they usually do, write the readable form; where they conflict, agent utility governs.

## Objectives

Change safety replaces readability as the design objective: the expected loss of correctness when a cold agent next edits the code should be minimal.

Resolve conflicts in this order: correctness, performance, change safety, token economy. Performance ranks second in performance-sensitive software and falls to third or fourth in code such as a short script; it is never irrelevant.

## Design

Code is a liability. With behavior held fixed, start by asking what can be removed, and prefer the smallest correct design. Every construct, including each dependency and configuration option, must be required by that behavior. New code must enforce a missing invariant or enable a larger deletion. Moving complexity into indirection, generated code, configuration, dependencies, or runtime work reduces it only if the whole system becomes smaller.

Design top-down, so that the structure of the code shows the structure of the domain. Refactor early and aggressively; when a feature fits only as a patch, reshape the system around it. Delete dead paths, redundant layers, wrappers that add nothing, and scaffolding.

Store each truth once and derive every projection of it.

Keep backward compatibility, shims, and parallel old and new paths only under a live contract. Every caller can be updated in one pass, and two paths leave a cold reader guessing which is canonical.

Use a library whenever it supplies stronger machinery than local code would. Imported code is still part of the system; judge it on whole-system merit.

Choose representations and algorithms for the actual machine. A simple surface bought with hidden work is a defect.

## Domain model

Design the domain model first. It is the skeleton of the program: when it is right, business logic composes from it; when it is wrong, control flow compensates with checks, conversions, and repeated validation. The domain model is the set of types that would appear in a medium-granularity pseudocode description of the program.

- Each entity has one canonical definition, program-wide, and one name.
- A definition's possible values correspond one-to-one with the entity's valid values: it holds exactly the fields that define the entity and admits no instance the domain forbids. Count them. A struct is the product of its fields' values, an enum the sum of its variants, and `Option<A>` is 1 + A; two optional fields of which exactly one must be set admit four shapes for two meanings, where the sum of the two types admits exactly two.
- Compose compound entities from primitive ones by products, sums, and collections, never by flattening them into flags and optional fields.
- Code that cannot change a canonical definition is bound by it, and the binding is the purpose: it removes the option of growing a local copy with flags. Local state the entity lacks belongs in a local type that contains the entity.
- A lossy conversion exposes its loss and a fallible one its failure. Identity conversions are deleted, boundary projections end at their boundary, phase transitions run one way, and validation has one owner.

## Types

Strong types dominate every other consideration of form. A type is an invariant the compiler checks on every later edit, including edits by agents that never learned the invariant.

- Make illegal states unrepresentable inside the trusted core. Stringly typed closed sets, ad hoc tuples, boolean flags, walls of optional fields, and invariants kept by convention are design failures; give every value with semantics a domain type.
- Parse input at boundaries into domain values instead of carrying unchecked data inward. Parsing may fail; transformations inside the core are total.
- Let the domain model carry the system's states, transitions, capabilities, effects, and failures.
- Treat types as architecture: each is at once a proof, a data representation, and an optimization surface.

## Abstraction

For agent-maintained code, abstraction saves tokens and lets the compiler enforce invariants at a distance. In practice, treat it as a goal in itself.

- Abstract an invariant as soon as it is visible; repetition is not a prerequisite. DRY outranks YAGNI. The cost of duplication to an agent is divergence: a later edit fixes one copy and misses the others, which lay outside its context.
- Agent-written code rarely fails from too much abstraction. It fails from plumbing: simple structs, flags, guards, and named intermediates that smear an invariant across the context window. Advanced mathematics is often clearer to an agent than bulk mundane code.
- Make abstractions deep: an interface much smaller than what it hides, so that call sites never need the implementation. A wrapper or pass-through layer hides nothing and costs tokens and a hop.
- Model algebraically. A good module is a small calculus: a precise vocabulary, explicit states and effects, and composable operations that obey stated laws. Mathematical structure compresses rules and gives tools exact handles.
- Use the whole language. Type-level machinery, metaprogramming, code generation, operator overloading, and mathematical or Unicode notation are ordinary tools; do not avoid one because it is advanced.
- Concentrate sophistication behind small interfaces. Code behind them may be as dense and generative as the design requires.

## Failure

Fail loudly unless recovery is real. Silenced errors are invisible when no human reads the code, and hiding errors is a habitual failure of agent-written code.

- Do not keep a doomed path alive with dummy defaults, null checks that only defer the failure, or handlers that catch an error and continue degraded.
- Catch an error only to recover from it or to translate it into a domain error, preserving the cause; otherwise let it propagate.
- Keep errors structured until the presentation boundary; do not reduce them to strings, defaults, or log lines.
- An unrecoverable contradiction terminates the program immediately, with domain context. Recovery is explicit, typed domain behavior.

## Names and comments

Within a project, each concept has one name and each name one concept; a cold agent learns the domain's vocabulary from the code. Keep names compact, precise, and faithful to the domain, and use standard mathematical or Unicode notation where it exists. Keep call sites short; qualify a name only when the qualification carries information.

Comments hold only what code and types cannot: rationale, proof obligations, external facts, and invariants the compiler cannot check. Internal code needs no API documentation; public documentation is a product decision.

## Navigation

A cold agent finds code through the language server and text search. Use the language server first for definitions, references, types, diagnostics, call structure, and refactoring; use text search for lexical and cross-language questions. Keep both effective:

- Avoid soft dispatch. String-keyed lookup, reflection, and dynamic attribute access hide definitions and call edges; confine unavoidable dynamism behind a typed interface.
- Every name a macro or generator creates appears literally at the invocation site.

## Enforcement

Any rule a machine can enforce belongs in tool configuration, not prose. A lint is an invariant checked on every edit by every agent, and for code no human reads, compiler and lint output is the review.

- Configure the strictest available lint posture when a project is created, deny warnings, and tighten the posture as the tools improve. Formatting, linting, type checking, and dependency pruning are part of the build.
- One manifest owns lint policy; scripts, CI, and editor configuration only execute it.
- House exceptions disable lints that enforce the human-reader conventions this doctrine rejects, such as limits on function length or parameter count, checks on the lexical appearance of names, and bans on glob imports or Unicode identifiers. They apply in every project without restated rationale.
- Any other exception is local and carries, beside it, the design reason that outweighs the lint. Prefer none; a justified exception is ordinary policy.
- Use compilers, analyzers, and automated refactoring tools at full strength.

## Tests

Unit tests follow `$unit-test-doctrine`. A change does not automatically earn a permanent unit test; prefer a type or a compile-time check to a test.

## Working method

Do not stop at the first familiar or adequate design; search for the strongest design the problem admits, however difficult. Improve what you touch: fix small defects and tighten nearby code, and report problems too large to fix in place.
