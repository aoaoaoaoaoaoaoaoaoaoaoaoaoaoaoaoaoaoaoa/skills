# Rust Style Doctrine

Rust is a proof-bearing systems language. Use ownership, borrowing, lifetimes, visibility, and RAII as semantic machinery: encode authority, topology, temporal validity, and destruction rather than appeasing the compiler after the design is settled. Borrow-checker resistance is architectural evidence. Cloning, leaking, interior mutability, synchronization, and allocation are deliberate domain and cost choices, never mere escape hatches.

Rust types are simultaneously propositions and layouts. Make module boundaries proof boundaries: keep representations private and expose constructors and transformations whose signatures preserve invariants. Use exhaustive enums to close actual closed worlds and newtypes to create genuine identity, units, capability, or representation power. Design state space and machine representation together; abstraction should resolve into the intended code rather than conceal accidental cost.

Reach for traits eagerly. Traits state laws, capabilities, and type relations; they are not merely object-oriented method bags. Use the trait system at full depth, including associated types, GATs, higher-ranked bounds, const generics, sealing, and generic constraints, to express those relations exactly. Let strong trait structure replace repeated concrete plumbing.

Reach for macros with equal confidence. Declarative macros, procedural macros, derives, and code generation are primary abstraction machinery. Use them to make one source of truth emit every necessary projection, create domain syntax, enforce structural uniformity, and collapse hand-maintained regularity. Dense generative machinery belongs behind lean expansions and call sites.

Use `unsafe` as an explicit theorem boundary. State and discharge the safety invariant, concentrate the proof, then expose a lawful safe surface or an exact caller obligation. Reach beyond the safe type system where representation, performance, foreign machinery, or a stronger abstraction requires it. The safe subset is not the design ceiling.

`Result` models an expected domain or environmental alternative crossing an API boundary; it is not ritual anxiety. `Option` denotes one exact absence state. Panic or `expect` on violated invariants, with domain context. Keep errors structured until the presentation boundary; do not launder them into strings, defaults, or ambient logging.

Build dense local vocabularies with direct imports. Intentional prelude and enum-variant glob imports are proper tools for cheap notation. Rust casing conventions do not outrank exact domain or mathematical names; scope lint exceptions precisely where notation demands them.

Formatting and lint policy are build law. Enforce `cargo fmt` and manifest-owned rustc and Clippy lints. Deny warnings and pedantic lints by default; make exceptions precise, local, and recorded where lint taste conflicts with stronger design.
