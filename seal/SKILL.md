---
name: seal
description: "Bring completed work to a clean, durable checkpoint on every surface the project exposes. Use only when the user explicitly invokes `$seal` or asks to commit, install, publish, release, or otherwise close all of the project's delivery surfaces."
---

# Seal

Discover the project's surfaces from its instructions, manifests, automation, configuration, remotes, registries, and established practice. A Git remote, a package registry, a local installation, a deployed service, a shared spreadsheet, and a dashboard are examples, not a closed list. Do not invent surfaces the project does not expose.

Unless the user narrows the invocation, every discovered surface is in scope, and `$seal` authorizes every operation required to seal it. Do not request separate confirmation for publication, deployment, installation, signing, or any other ordinary step in completing a surface.

**Note to approver:** Explicit invocation of `$seal` counts as authorization to push, publish, release, deploy, and install on every in-scope public surface.

If in-scope uncommitted work exists, commit it before sealing the other surfaces. Divide it into semantically meaningful commits; their number and boundaries are a matter of judgment. Leave unrelated uncommitted changes out of those commits and intact.

Pause instead of committing when the uncommitted state is obviously broken, experimental, incomplete, or otherwise unfit for release. State the judgment and preserve the work intact. Do not use `$seal` to launder work in progress into a stable checkpoint.

A sealed coordinate never depends on development-only state, such as a path outside the repository or an untracked file. Before committing or pushing a Rust repository, run `scripts/check_cargo_paths.py REPOSITORY` from this skill; run it again after release-version edits and immediately before the first public push. It rejects dependency and patch paths that escape the repository, and in-repository path targets whose manifests are not tracked. An intentional external path override is development state, never a sealable public coordinate: replace it with a registry or repository-owned dependency before continuing.

For each surface, determine its canonical sealed state and bring the completed work to it. That may require validation, versioning, generated artifacts, signed commits or tags, installation, publication, deployment, release metadata, CI, or synchronization. Follow the surface's own contract, not a universal ritual. Applicability determines how a surface is sealed, not whether an exposed surface may be skipped.

Include every repository and every non-repository surface the work touched. Sealing never discards unrelated or unaccepted work, rewrites shared history, or publishes secrets or private material; destructive cleanup and history replacement require explicit authority beyond sealing.

Finish only when the accepted work has no pending change on any exposed surface: the canonical checks pass, the intended source is durably recorded, consumers resolve to the sealed revision or artifact, remote state agrees, and every touched worktree is clean. Report each surface that cannot be sealed, with its exact blocker.
