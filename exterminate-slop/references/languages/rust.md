# Rust Lens

Use this note when Rust materially participates in the audited surface. It sharpens the generic protocol without supplying a smell checklist.

## Surface

The default implementation manifest contains handwritten `*.rs` files. Include `Cargo.toml`, `build.rs`, schemas, or configuration when they materially define the scoped component. Generated sources, `target`, fixtures, snapshots, and vendored code remain outside the audit manifest unless explicitly included; they may still belong to the context fringe.

## Semantic Posture

Treat Rust as a language for stating the domain, not for decorating an otherwise primitive program. Enums, newtypes, typestates, phase-specific structures, traits, generics, const generics, iterator algebra, macros, derives, and code generation are all legitimate when they reduce independent truths or make laws compiler-visible.

Ownership and borrowing are semantic structure. Distinguish necessary representation costs from clones, bounds, adapters, and lifetime machinery caused by erased ownership or a false abstraction. Genericity should name an algebra or reusable law, not merely collect operator syntax.

Unsafe code carries a proof obligation that participates in semantic description length. Do not condemn it ceremonially, but count folklore preconditions and duplicated safety arguments as real complexity.

Transport, serialization, database, CLI, and FFI representations may remain primitive at genuine boundaries. Convert once into the internal model and do not preserve an internal boundary merely because a conversion currently exists there.

## Navigation

Use rust-analyzer, Cargo metadata, compiler diagnostics already available from the repository, and textual search as complementary evidence. Start from whichever declaration, construction, use, or boundary anchor most efficiently resolves the current clique's question.

## Implementation Phase

When implementation is authorized, use the repository's existing formatting, checking, test, lint, and safety tooling. The audit phase itself must not depend on executing or modifying the target tree.
