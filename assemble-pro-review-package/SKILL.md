---
name: assemble-pro-review-package
description: Assemble a throwaway review handoff for an external expert with efficient GitHub access. Use when the user asks for a pro review package, reviewer handoff, expert audit bundle, or similar artifact that should contain one synthesized review prompt, exact GitHub coordinates for relevant implementation, and selectively inlined non-code evidence such as specifications, audits, logs, metrics, or literature. Excludes first-party code by default.
---

# Assemble Pro Review Package

Create a design or implementation review handoff for an expert reviewer working outside this session. Lock the task or subproblem the user supplies, and resolve any ambiguity that would materially change the review.

Material prepared for an external reviewer never contains credentials, unrelated private data, or content outside that reviewer's authorized disclosure boundary.

GitHub is the transport for implementation; the document is the semantic handoff. Do not duplicate first-party code the reviewer can inspect directly; identify the exact source identity and inspection surface instead.

The deliverable is one markdown document containing the review contract, a source map, and labeled inlined evidence. Create it in a subdirectory of `/tmp` unless the user asks otherwise, and never commit it. Do not create attachments, helper archives, overflow artifacts, or companion files. Write the document under `$vox-nihili`.

Select material by one rule: include it only when it materially sharpens the review question or the reviewer's understanding of intended behavior, active pressure, or the relevant solution space. Cut anything whose relevance cannot be defended.

Append sections with `scripts/inline_section.py`, which enforces a fixed hard ceiling of 200k tokens counted with `o200k_base`. The ceiling is a constraint, not a target: neither minimize nor fill it, and optimize only clarifying value within it.

## Source policy

By default, inline only non-code material: objectives and constraints, normative specifications, design rationale, audit or review reports, benchmark results, logs and traces, experiment ledgers, issue or discussion prose, and relevant literature. Normative pseudocode may be inlined when it defines intended behavior instead of reproducing an implementation.

Source, tests, schemas, manifests, build and packaging logic, patches and diffs, generated output, and code excerpts embedded in prose are code-bearing material. Do not inline them by default, regardless of ownership, and do not evade the rule by transcribing source into the review narrative.

For first-party implementation, record:

- the canonical GitHub repository identity
- an immutable commit, or a PR or branch together with its head commit
- the relevant paths and symbols
- the question each surface should answer

Prefer the same stable coordinates for public rival or prior-art code. Inline a code-bearing span only under an explicit user override; state why a stable source reference is insufficient, and include the smallest decisive span.

Do not pretend that uncommitted or unpushed first-party code is visible on GitHub. If such state can materially change the review, obtain a published source identity or an explicit override to inline the code before assembling the handoff.

## Workflow

1. Infer the review target: the specific implementation goal, design question, or problem statement.
2. Lock the source map. Resolve each relevant repository and exact revision, then identify the paths and symbols the reviewer should inspect. Record material uncommitted or unpublished state.
3. Open the document with the front-matter note below, then state:
   - the broad objective
   - the current tactical objective
   - the live benchmark, failure regime, or open uncertainty
   - the exact question the reviewer should focus on
4. Present the source map before the inlined evidence. Give direct inspection instructions, not summaries of code the reviewer can read.
5. Inline only material admitted by the source policy and the selection rule, using the decisive span instead of an entire file when possible.
6. Verify that the document reads as one coherent handoff, not a stack of fragments. Use explicit section headings and refer to inlined material by section label. Confirm that every code reference resolves through the source map and that no unauthorized code-bearing material was inlined.

## Reviewer-facing copy rules

- Address the reviewer as `you`.
- Write direct instruction and context, not notes about how the document was assembled.
- Do not use `this package`, `the package`, or any other bundling metaphor.
- Except in an explicitly authorized code-inline section, refer to implementation only through the exact GitHub coordinates in the source map.
- Do not refer to local paths, unspecified repositories, or the ambient conversation.
- Apart from the front-matter note, do not comment on the prompt's size or construction.

## Front-matter note

Place this near the top of the document without elaborating on it:

> First-party code is intentionally omitted. Inspect the exact GitHub repositories,
> revisions, paths, and symbols named below. The inlined sections contain the review
> contract and non-code evidence.

If the user explicitly authorized a code-inline exception, amend the first sentence to name each authorized section as the sole exception.

## Output

Report only:

- the package root
- the path of the review document
- a short note on the code identities referenced and the non-code evidence inlined
