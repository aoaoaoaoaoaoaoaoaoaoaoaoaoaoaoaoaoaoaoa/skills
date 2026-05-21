---
name: zero-based-assimilation
description: "Use when the user wants to take ownership of an upstream repository by zero-based copying: start from deletion, keep only the files needed for the intended local build/use/modify loop plus legal obligations, and purge CI, release machinery, public-facing docs, contribution surfaces, generated bulk, large comments, and upstream compatibility baggage."
---

# Zero-Based Assimilation

Assimilate an upstream repository as owned local material. This is not a smaller fork. This is a new local artifact whose ancestry is incidental.

The posture is zero-based: everything is deleted unless it proves it belongs to the intended local operation. Siphon out the functional essence. Discard the husk.

## Lock The Intent

Before cutting, identify the intended local use:

- what must build, run, load, or otherwise work
- what the local edit loop needs
- what command or smoke oracle proves the essence survived
- what legal notices must remain
- where the assimilated repo should live

If the intended use or verification oracle is materially ambiguous, ask. Otherwise infer boldly and record the assumption.

## Light Ledger

Create a compact ledger in `/tmp`:

```text
/tmp/zero-based-assimilation-<source-slug>-<target-slug>.md
```

Keep it short. It is for orientation, not ritual.

```text
intent:
source:
destination:
verification_oracle:

kept:
- path or root :: why it survives

purged:
- path or root :: why it dies

legal:
- path :: obligation preserved

comments_and_prose:
- what was stripped or intentionally kept

verification:
- command :: result

residual_uncertainty:
```

Do not ledger every file unless the repo is small or a decision is subtle. Ledger roots, categories, and exceptions. The important invariant is that kept material has a reason.

## Retention Rule

A file survives only if it is part of the minimal closure for the intended local use:

- product source
- build or load metadata
- runtime assets
- lockfiles or vendored pieces actually needed for local reproducibility
- small local scripts needed for build, run, inspection, or modification
- tests/examples only when they are the cheapest behavior oracle
- legal attribution
- a terse local README if it materially helps operate the repo

Everything else is presumed dead.

Delete upstream-facing structure: CI, release machinery, publishing config, contribution docs, issue templates, PR templates, badges, changelogs, websites, screenshots, demos, broad examples, public packaging cruft, stale editor settings, generated output, caches, coverage, benchmarks, and docs that explain upstream social context rather than local operation.

## Method

Prefer clean-room retention over pruning. If practical, clone or unpack upstream into a temporary staging area, then copy only the retained closure into the destination. If working in-place, treat the current tree as condemned scaffolding and delete down to the retained closure.

Break upstream posture. Remove remotes, scripts, config, names, and docs whose purpose is merging back, publishing releases, accepting contributors, feeding CI, or maintaining a public project surface.

Simplify build metadata to the local use. Remove matrix targets, upload paths, signing, coverage, docs builds, lint fleets, packaging targets, and release tasks unless they are genuinely part of the local edit loop.

## Code And Prose Purge

Retained code should be stripped of husk:

- large banner comments
- decorative block headers
- disabled code
- changelog fragments
- tutorial prose
- comments that restate syntax
- upstream narrative
- TODOs aimed at public maintainers

Keep comments only when they defend a real invariant, non-obvious algorithm, format trap, hardware/runtime constraint, or legal obligation. Rewrite survivors short.

Keep at most a terse README: what this repo is now, how to build/use it, and any local caveats. No marketing, badges, history, contribution ritual, or upstream apology.

## Verification

Run the narrowest meaningful command proving the retained essence survived. Prefer one build/load command and one smoke/use command when both are cheap.

If verification requires temporary retained examples or tests, use them, then decide whether they deserve permanent survival. Temporary oracle material should not linger by sentiment.

## Final Response

Report:

- source and destination
- ledger path
- intended local use
- retained essence
- major purged categories
- legal notices kept
- verification commands and results
- residual uncertainty
- obvious next remodeling pass, if any
