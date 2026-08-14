# Rust Style Doctrine

Rust is a proof-bearing systems language. Use ownership, borrowing, lifetimes, visibility, and RAII as semantic machinery: encode authority, topology, temporal validity, and destruction rather than appeasing the compiler after the design is settled. Borrow-checker resistance is architectural evidence. Cloning, leaking, interior mutability, synchronization, and allocation are deliberate domain and cost choices, never mere escape hatches.

RAII is the default law for OS resources. Construction must return an owner that closes, kills and waits, unlocks, unmaps, unregisters, or removes on `Drop`; partial construction must unwind through already-created owners. A freshly created temporary directory represented only by `PathBuf`, a raw child process separated from its reaper, or cleanup postponed to the bottom of a function is an ownership defect. Use `TempDir`, guard types, scoped tasks, and process-group owners directly or forge the missing owner. `mem::forget`, leaked handles, detached children, and `TempDir::keep` are explicit lifetime transfers and must be justified as such. Add an OS supervisor or startup reaper when process death can bypass `Drop`.

Rust types are simultaneously propositions and layouts. Make module boundaries proof boundaries: keep representations private and expose constructors and transformations whose signatures preserve invariants. Use exhaustive enums to close actual closed worlds and newtypes to create genuine identity, units, capability, or representation power. Design state space and machine representation together; abstraction should resolve into the intended code rather than conceal accidental cost.

Reach for traits eagerly. Traits state laws, capabilities, and type relations; they are not merely object-oriented method bags. Use the trait system at full depth, including associated types, GATs, higher-ranked bounds, const generics, sealing, and generic constraints, to express those relations exactly. Let strong trait structure replace repeated concrete plumbing.

Reach for macros with equal confidence. Declarative macros, procedural macros, derives, and code generation are primary abstraction machinery. Use them to make one source of truth emit every necessary projection, create domain syntax, enforce structural uniformity, and collapse hand-maintained regularity. Dense generative machinery belongs behind lean expansions and call sites.

Use `unsafe` as an explicit theorem boundary. State and discharge the safety invariant, concentrate the proof, then expose a lawful safe surface or an exact caller obligation. Reach beyond the safe type system where representation, performance, foreign machinery, or a stronger abstraction requires it. The safe subset is not the design ceiling.

`Result` models an expected domain or environmental alternative crossing an API boundary; it is not ritual anxiety. `Option` denotes one exact absence state. Panic or `expect` on violated invariants, with domain context. Keep errors structured until the presentation boundary; do not launder them into strings, defaults, or ambient logging.

Build dense local vocabularies with direct imports. Intentional prelude and enum-variant glob imports are proper tools for cheap notation. Suppress naming lints concerned only with lexical appearance; retain those that encode binding intent, API semantics, or module topology.

Formatting and lint policy are build law. Enforce `cargo fmt` and manifest-owned rustc and Clippy lints. Deny warnings and pedantic lints by default. Function line and parameter counts are not complexity measures. Internal tooling does not owe boilerplate API documentation. Canonical house exceptions are global; make every other exception precise, local, and recorded where lint taste conflicts with stronger design.

Rust unit tests obey `$unit-test-doctrine`. A patch does not owe a new `#[test]`.
