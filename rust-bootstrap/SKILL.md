---
name: rust-bootstrap
description: "Install or tighten the house Rust lint posture from this skill's template. Use when creating a Rust repository, setting up Rust linting, or ratcheting an existing Rust repository toward manifest-owned lint policy."
---

# Rust Bootstrap

This skill installs the Rust tooling posture that `$style-doctrine` prescribes; read the doctrine and its Rust addendum first. [assets/template](assets/template) implements the target state. Re-read the template when details matter instead of relying on memory. Existing projects are precedent only where this skill and the template leave a decision open.

## Target state

Both procedures converge on this state, which is also the acceptance checklist.

- The root `Cargo.toml` owns all lint levels in `[workspace.lints.rust]`, `[workspace.lints.rustdoc]`, and `[workspace.lints.clippy]`, including `warnings = "deny"`. Every member crate declares `[lints] workspace = true`. Cargo's own `[lints.cargo]` namespace is unstable and unused; Clippy's `cargo` group is unrelated.
- Clippy's `all`, `pedantic`, and `cargo` groups are denied. `restriction` lints are enabled individually, because the group is self-contradictory; `nursery` stays off, because it is unstable.
- The template's house exceptions are present and inherit their rationale from the template. Every project-specific exception has a concrete reason beside it; one comment may cover a coherent group. Local suppressions use `#[expect(..., reason = "...")]`, or `#[allow(..., reason = "...")]` when stable.
- Internal tools allow `missing_docs`, `missing_errors_doc`, and `missing_panics_doc`; a library keeps them when its API documentation is part of the product.
- `unsafe_code` is denied. A project that needs `unsafe` instead denies `unsafe_op_in_unsafe_fn` and `undocumented_unsafe_blocks`.
- `clippy.toml` holds only configuration knobs, such as allowing `expect`, `unwrap`, and `panic` in tests, or is absent. Its lookup is unstable, so it never holds allow or deny policy.
- `[workspace.metadata.rust-starter]` holds the format, Clippy, test, and doc command vectors and an ordered `canonicalize_commands` pipeline. Clippy covers the whole workspace, never with `--no-deps`, which skips member crates that are path dependencies.
- `[workspace.metadata.rust-starter.source_files]` sets `max_lines` deliberately, 3000 by default, with explicit `exclude` patterns for checked-in generated code. Clippy's `too_many_lines` measures functions and is a house exception; this cap measures files.
- `check.py`, or another runner that stays equally thin, executes that metadata: `check` enforces the file cap, canonicalizes, then verifies formatting, lints, and tests; `verify` does the same without writing files; `deep` adds docs; `fix` only canonicalizes. No runner, CI file, or editor configuration restates lint flags.
- The latest system toolchain is used. `rust-toolchain.toml` names the `stable` channel with `clippy` and `rustfmt`, or is omitted where rustup is not in use. Any `rust-version` is derived from the active `rustc --version`; a version copied from the template or from memory becomes silent policy.
- No committed file, runner, CI job, or command vector sets a Cargo target directory. Artifact placement belongs to the operator's ambient configuration; CI may set `CARGO_TARGET_DIR` ephemerally.
- `AGENTS.md` directs agents to `$style-doctrine` and `$unit-test-doctrine`, so that they inherit the doctrine without knowing this skill exists.
- Every OS resource the product acquires has an RAII owner, per the Rust addendum.
- The template-only `cargo_common_metadata` exception is removed once package metadata is filled in, or replaced with the project's own reason.

## Fresh repository

1. If the target directory is empty and outside any Git worktree, run `git init`.
2. Run `rustc --version` and `cargo --version`.
3. Copy the template, then decide each of these instead of copying it: workspace members, package names, license, `rust-version`, test allowances in `clippy.toml`, documentation lints, whether rustdoc lints belong in the fast gate, the `unsafe` policy, the file cap, project-specific exceptions, and the RAII owner of each OS resource the product acquires. Merge the template `AGENTS.md` into existing instructions without erasing local rules.
4. Run `./check.py check`.

## Existing repository

A retrofit ratchets a living repository toward the target state; it never pastes the template over it.

First inventory every place policy may live: root and member manifests, `.cargo/config.toml` and runner `--target-dir` flags, `AGENTS.md` files, runners (`check.py`, `xtask`, `justfile`, shell scripts), CI, canonicalization commands, `clippy.toml`, `rust-toolchain.toml`, editor settings, the active toolchain versions, and oversized source files and checked-in generated code. Establish what policy exists and where it is duplicated.

Keep every local rule stricter than the template: extra bans, stricter rustdoc policy, deeper gates, tighter `unsafe` policy, a lower file cap. Keep exceptions with a real local reason, moving repo-wide ones into the root manifest. Remove an exception inherited from an old shared profile when force-enabling the lint shows that no stronger concern remains. Where a repository diverges deliberately, adapt the pattern instead of forcing uniformity.

Then tighten in this order:

1. Add the `$style-doctrine` and `$unit-test-doctrine` directions to `AGENTS.md`, merged into local instructions.
2. Move to the latest system toolchain; keep a numeric pin only under an explicit external MSRV constraint.
3. Remove committed target-directory settings and runner flags; keep unrelated portable Cargo configuration, and never edit user-global configuration.
4. Install the workspace lint tables.
5. Add `[lints] workspace = true` to every member crate.
6. Move lint flags from scripts, CI, and `clippy.toml` into the manifest, deleting each copy only after the manifest owns the equivalent policy and the effective gate is unchanged. `-D warnings` becomes `warnings = "deny"`.
7. Put a reason on every local suppression.
8. Reduce the runner to orchestration, moving any existing auto-fix pass into `canonicalize_commands`.
9. Install the file cap, keeping a stricter existing one. Split, explicitly exclude, or accept under a tighter local rule each file already over the cap; do not raise the cap to fit it.
10. Add the deep gate if the repository can sustain it.

A global `expect_used = "allow"` usually serves tests: replace it with `expect_used = "deny"` and `allow-expect-in-tests = true` in `clippy.toml`. Domain-heavy code such as geometry, parsing, or numerics may keep justified exceptions; the goal is explicit, centralized exceptions, not zero. CI calls the runner or the manifest commands, using `verify` when it must detect drift without rewriting files.

## Deep gate

For a mature repository, add:

- `cargo hack clippy --workspace --all-targets --feature-powerset` and `cargo hack test --workspace --feature-powerset`, degrading to `--each-feature` or grouped subsets if the powerset explodes
- `cargo doc --workspace --all-features --no-deps`
- `cargo deny check`
- `cargo nextest`, with doctests run separately, and `cargo semver-checks` for published libraries

Declare custom cfgs through `unexpected_cfgs` with `check-cfg`, so that misspelled cfg names fail. Point rust-analyzer's check command at Clippy with all targets and features, so that editor diagnostics match the gate. A scheduled, non-blocking CI job after toolchain updates surfaces new Clippy lints early.
