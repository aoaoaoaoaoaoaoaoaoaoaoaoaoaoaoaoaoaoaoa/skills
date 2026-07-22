# Java Lens

Use this note when Java materially participates in the audited surface. It sharpens the generic protocol without supplying a smell checklist.

## Surface

The default implementation manifest contains handwritten `*.java` files. Include Maven or Gradle metadata, schemas, and configuration when they materially define the scoped component. Generated sources, annotation-processor output, build products, fixtures, snapshots, and vendored code remain outside the audit manifest unless explicitly included.

## Semantic Posture

Treat Java as a modern static language. Records, sealed hierarchies, enums, pattern matching, switch expressions, precise generics, compact constructors, immutable collections, and current standard-library facilities are available whenever the project's viable language level permits them.

Separate structures survive because they carry distinct laws, lifecycle, boundary, representation, or performance roles, not because framework history generated multiple classes. Mutable beans, DTO projections, mappers, services, builders, and interfaces are neither guilty nor innocent by category; judge the independent truths and translation obligations they create.

Allocation, layout, boxing, reflection, proxying, and defensive copying may be architectural costs. Preserve them when demanded by performance or framework boundaries, and contract them when they are accidental mediation.

Primitive and nullable external representations may be correct at JSON, SQL, messaging, CLI, or legacy protocol boundaries. Quarantine them there and preserve only genuine boundary projections.

## Navigation

Use the Java language server, compiler structure, and Maven or Gradle dependency graph alongside textual search. Follow the anchors that resolve the current semantic question rather than privileging declarations or call sites categorically.

## Implementation Phase

When implementation is authorized, use the repository's existing compile, test, formatter, static-analysis, nullness, and allocation tooling. The audit phase itself must not depend on executing or modifying the target tree.
