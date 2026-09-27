# Rust Addendum

This addendum extends [universal.md](universal.md).

Ownership, borrowing, lifetimes, visibility, and RAII are design tools: use them to encode authority, topology, temporal validity, and destruction, instead of appeasing the borrow checker after the design is settled. Resistance from the borrow checker is evidence about the architecture. Cloning, leaking, interior mutability, synchronization, and allocation are deliberate domain and cost decisions, not escape hatches.

Every OS resource has an owner that releases it on `Drop`. Construction returns an owner that closes, kills and waits, unlocks, unmaps, unregisters, or removes; partial construction unwinds through the owners already created. A temporary directory held only as a `PathBuf`, a child process separated from its reaper, and cleanup deferred to the end of a function are ownership defects. Use `TempDir`, guard types, scoped tasks, and process-group owners, or write the missing owner. `mem::forget`, leaked handles, detached children, and `TempDir::keep` are explicit ownership transfers and need a stated contract. Where process death can bypass `Drop`, add an OS-level supervisor or a startup reaper.

Types are both propositions and memory layouts; design the state space and the representation together, so that abstractions compile to the intended code. Module boundaries are proof boundaries: keep representations private and expose constructors and transformations whose signatures preserve invariants. Use exhaustive enums for closed sets; newtypes for identities, units, capabilities, and representations; and typestates or phase-separated types for protocols.

Traits state laws, capabilities, and relations between types; they are not bags of methods. Use the trait system at full depth, including associated types, GATs, higher-ranked bounds, const generics, and sealing, and let trait structure replace repeated concrete plumbing. Declarative and procedural macros, derives, and code generation are primary means of abstraction: one source of truth emits every projection, domain syntax replaces boilerplate, and structural uniformity is generated instead of maintained by hand.

`unsafe` marks a proof boundary. State the safety invariant, concentrate its proof, and expose either a safe interface or an exact obligation for the caller. Go beyond the safe subset when representation, performance, foreign code, or a stronger abstraction requires it.

`Result` models an expected alternative that crosses an API boundary. `Option` models exactly one absence. A violated invariant panics, or fails an `expect`, with domain context.

Import the symbols you use and call them unqualified; prelude and enum-variant glob imports are proper tools for a dense local vocabulary. Destructure wherever it removes noise. Do not write Rust as Python with type annotations.

Rust unit tests follow `$unit-test-doctrine`. A patch does not owe a new `#[test]`.

## Tooling

- `cargo fmt` formats all code.
- The root `Cargo.toml` owns lint policy in `[workspace.lints.{rust,rustdoc,clippy}]`, and every member crate declares `[lints] workspace = true`.
- Deny warnings and Clippy's `pedantic` group. Enable `restriction` lints individually, never as a group.
- House exceptions: function length and argument count; naming lints about lexical appearance, while those that encode binding intent, API semantics, or module topology stay enabled; glob-import lints; Unicode and confusable-identifier lints; `multiple_crate_versions`, since source linting cannot settle transitive version convergence; missing-documentation lints in internal code.
- Every local suppression carries `reason = "..."`; a temporary one uses `#[expect]`.
- Use the latest system toolchain; never pin a Rust version from memory.
- `$rust-bootstrap` installs and tightens this posture in a repository.
- rust-analyzer is available through the `lsp` MCP.
