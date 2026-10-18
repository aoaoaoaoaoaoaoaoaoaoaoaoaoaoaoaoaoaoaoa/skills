---
name: merge-upstream
description: Merge an upstream release into a downstream fork in a dedicated worktree, contrasting upstream intent with the fork's documented design before resolving conflicts. Use for upstream integrations and their conflict resolution, with owner decisions before design-sensitive changes and validation before landing.
---

# Merge Upstream

A compiling merge can still undo a fork decision. Resolve against upstream's
intent and the fork's design, not merely the two local implementations.

## Establish the merge

Read repository instructions, the fork's teleology document, and the relevant
architecture and release guidance. Record the fork HEAD, last merged upstream
release, requested release, and their commit IDs. Verify the upstream remote
and fetch the exact release; never substitute a moving branch for a requested
tag. Preserve unrelated work.

Create a branch and worktree under the repository's gitignored `.worktrees/`.
Start the merge without committing. Keep a concise worktree-local ledger of
conflicts, affected design invariants, evidence, resolutions, open decisions,
and validation. It is a recovery record, not a second design document.

## Autonomous first pass

For each conflict, examine the base, fork, and upstream versions. Identify
every upstream commit contributing to the conflicting change, then read its
message and relevant patch, including related callers and tests. Use PR context
when the code and commit leave intent uncertain. A title or hunk alone does
not establish the purpose of a change; record uncertainty instead of guessing.

Map each conflicted path to the teleology index and trace affected contracts
beyond the hunk. The index is a starting point: renamed owners, new callers,
defaults, and cleanly merged changes can also bypass a fork invariant. Review
such interactions where the upstream change overlaps the fork's design.

Classify resolutions by behavior, not textual size:

- Resolve mechanical conflicts, compatible refactors, and demonstrated bug
  fixes autonomously when their upstream purpose and the fork's invariants
  both survive. Record why a teleology-adjacent resolution is neutral.
- Leave design-sensitive or uncertain choices open for the owner. A small
  change to a default, lifecycle, protocol, prompt, or capability can reverse
  a fork decision. Passing tests do not authorize that reversal.

Adapt fork behavior to upstream's new structure rather than restoring an old
file wholesale. Do not use blanket `ours` or `theirs`, disable a check, accept
snapshots in bulk, or delete unfamiliar upstream behavior merely to obtain a
working tree. Whole-file choices require evidence covering the whole file.

## Owner decisions

After the safe first pass, present a consolidated list of unresolved design
choices. Group by behavior rather than repeating one question per file. Each
decision states:

- The upstream intent, with commit or PR evidence.
- The fork invariant and its teleology reference.
- Where the two conflict or where evidence is insufficient.
- The viable options, their behavioral consequences, and a recommendation.

Distinguish observations from inference. Ask about product behavior, not which
side of a diff to keep. State the default implied by existing design, but wait
for explicit answers before resolving a genuine design conflict. Continue
independent mechanical work while waiting; silence is not approval. Surface
new contradictions if later implementation changes a settled decision.

## Complete and validate

Record the owner's decisions and finish the remaining conflicts. Update the
canonical design documentation only where the owner changed the contract;
do not rewrite teleology to excuse an accidental implementation.

Review the resulting merge against both parents. Confirm that every conflict
has a rationale and that relevant clean merges preserve the same invariants.
Then run the repository's required lint, build, and test gates, including the
affected teleology tripwires. Use existing integration cases for consequential
interactions; add permanent tests only when the repository's test doctrine
justifies them. Inspect each snapshot change against the intended behavior.

Compilation and tests provide evidence, not a replacement for design review.
If they expose a new design choice, return it to the owner. Do not relax a
gate to land the merge. Report checks that could not run and block landing
when a required gate is incomplete.

## Land

Once decisions and required checks are complete, commit the merge and
integrate it into the destination branch without overwriting concurrent work.
If that branch advanced, review and validate the actual combined tree before
landing. Report the release and commit IDs, substantive decisions, validation,
and unresolved issues. Remove the merged worktree and its disposable build
artifacts; retain only useful evidence in the repository's normal location.

Merging does not itself authorize deployment, service restarts, pushes, or
changes to running conversations. Follow separate repository grants and owner
approval, including any temporary deployment hold.
