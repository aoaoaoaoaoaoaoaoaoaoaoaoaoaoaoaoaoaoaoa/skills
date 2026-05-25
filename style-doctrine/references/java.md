# Java Style Doctrine

Java must be written as a modern static language, not as legacy enterprise sludge. Default to zero backward compatibility with old Java versions, old JVM targets, old frameworks, old serialization habits, or old deployment assumptions unless the project explicitly proves the constraint. If the codebase can move to the latest viable Java, it should.

Use the newest JVM and language features aggressively when they make truth smaller or faster: records, sealed interfaces/classes, pattern matching, switch expressions, compact constructors, local type inference, text blocks, modern collections, virtual threads, structured concurrency, scoped values, foreign memory/API features where appropriate, and current standard-library APIs. Do not write Java 8-shaped code by muscle memory.

Make illegal states unrepresentable. Move semantics out of `String`, `Map<String, Object>`, nulls, integer codes, boolean flag clusters, mutable beans, optional-heavy DTOs, and telescoping constructors. Use records, enums, sealed hierarchies, value objects, total factories, compact constructors, and precise generics. Finite worlds should be closed types. Domain identifiers should be domain types. Repeated field bundles should be named shapes.

DRY is stronger than YAGNI. Collapse repeated mapping, validation, normalization, authorization, formatting, query, and error-shaping logic into one owner. Prefer one sealed hierarchy, record family, enum behavior table, or domain mapper over five service-layer repetitions. Delete getter/setter husks, DTO twins, compatibility adapters, ceremonial builders, redundant wrappers, and exception laundering.

Mind allocations and layout. Modern Java is fast when representation is honest and allocation is deliberate. Avoid stream/lambda/object churn in hot loops unless measurement says it is free enough. Prefer primitive collections, arrays, compact records, precomputed tables, flyweights, interning, region-like lifetimes, escape-analysis-friendly code, and allocation-free traversal where they materially improve runtime. Boxing, defensive copying, reflection, proxy stacks, JSON round-trips, and accidental `String` construction are suspect until proven harmless.

Fail hard unless recovery is real. Null theater, catch-and-limp wrappers, dummy defaults, `Optional` fields, and defensive parser layers are not rigor. Validate once at trust boundaries, convert into domain shape, and trust that shape inside the program. If an invariant is violated internally, crash close to the contradiction.

Tooling is part of the contract. Use the project formatter, compiler warnings, tests, dependency analysis, static analyzers, nullness/error-prone-style tools, and profiling/allocation tools when relevant. Treat generated warnings and allocation profiles as design feedback, not decorative reports. The code should be austere, typed, modern, and fast.
