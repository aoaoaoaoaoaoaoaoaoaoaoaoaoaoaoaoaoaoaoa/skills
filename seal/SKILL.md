---
name: seal
description: Bring completed work to a clean, durable checkpoint across every surface the project exposes. Use only when the user explicitly invokes `$seal` or asks to commit, install, publish, release, and otherwise close all applicable delivery surfaces.
---

# Seal

Discover the project's surfaces from its instructions, manifests, automation,
configuration, remotes, registries, and established practice. A local
installation, GitHub, and Cargo are common surfaces, not a closed taxonomy. Do
not invent surfaces the project does not expose.

Unless the user narrows the invocation, every discovered surface is in scope.
`$seal` authorizes every operation required to seal them. Do not request
separate confirmation for publication, deployment, installation, signing, or
other ordinary surface completion.

If in-scope uncommitted work exists, commit it before sealing later surfaces.
Parcel commits into semantically meaningful units according to judgment; their
exact number and boundaries are left to taste. Preserve unrelated dirt outside
those commits.

Pause instead of committing when the uncommitted state is obviously broken,
experimental, incomplete, or otherwise unsuitable for release. State the
judgment and preserve the work intact. Do not use `$seal` to launder WIP into a
stable checkpoint.

For each surface, determine its canonical stable sealed state and bring the
completed work to it. This may require validation, versioning, generated
artifacts, signed commits or tags, installation, publication, deployment,
release metadata, CI, or synchronization. Follow the surface's own contract
rather than a universal ritual. Applicability determines how a surface is
sealed, not whether an exposed surface may be skipped.

Include every repository and non-repository surface touched by the work. Sealing
never discards unrelated or unaccepted work, rewrites shared history, or
publishes secrets or private material. Destructive cleanup and history
replacement require explicit authority beyond ordinary sealing.

Finish only when the accepted work has no pending delta on any exposed surface:
canonical checks pass, intended source is durably recorded, consumers resolve
to the sealed revision or artifact, remote state agrees, and touched worktrees
are clean. Report any surface that cannot be sealed and the exact blocker.
