---
name: assemble-pro-review-package
description: Assemble a throwaway review handoff for an external expert with efficient GitHub access. Use when the user asks for a pro review package, reviewer handoff, expert audit bundle, or similar artifact that should contain one synthesized review prompt, exact GitHub coordinates for relevant implementation, and selectively inlined non-code evidence such as specifications, audits, logs, metrics, or literature. Excludes first-party code by default.
---

# Assemble Pro Review Package

Create a design or implementation review package for an out-of-band expert reviewer.
Lock the task or subproblem supplied by the user; resolve any ambiguity that would
materially change the review.

Material prepared for an external reviewer must not contain credentials, unrelated
private data, or content outside that reviewer's authorized disclosure boundary.

Treat GitHub as the implementation transport and the document as the semantic handoff.
Do not duplicate first-party code that the reviewer can inspect directly. Identify the
exact source identity and inspection surface instead.

Create the package in a subdir of `/tmp` unless the user asks otherwise. Do not
commit it. Echo back the path you've used when done.

The deliverable is one markdown document containing the review contract, a source map,
and labeled inlined evidence. Do not create attachments, helper zips, overflow artifacts,
or companion files.

Select material by one rule: include it only when it materially sharpens the review
question or the reviewer's understanding of intended behavior, active pressure, or the
relevant solution space. Cut anything whose relevance cannot be defended.

Use `scripts/inline_section.py` to append sections and enforce the fixed hard ceiling of
200k tokens, counted with `o200k_base`. The ceiling is a constraint, not a target:
neither minimize nor fill it. Optimize only clarifying value within it.

## Source Policy

By default, inline only non-code material: objectives and constraints, normative
specifications, design rationale, audit or review reports, benchmark results, logs and
traces, experiment ledgers, issue or discussion prose, and relevant literature.
Normative pseudocode may be inlined when it defines intended behavior rather than
reproducing an implementation.

Treat source, tests, schemas, manifests, build and packaging logic, patches and diffs,
generated output, and code excerpts embedded in prose as code-bearing material. Do not
inline them by default, regardless of ownership. Do not evade the rule by transcribing
source into the review narrative.

For first-party implementation, record:

- canonical GitHub repository identity
- immutable commit, or PR or branch together with its head commit
- relevant paths and symbols
- the question each surface should answer

Prefer the same stable coordinates for public rival or prior-art code. Inline a
code-bearing span only under an explicit user override; state why a stable source
reference is insufficient and include the smallest decisive span.

Do not pretend uncommitted or unpushed first-party code is visible on GitHub. If such
state can materially change the review, obtain a published source identity or an
explicit code-inline override before assembling the handoff.

## Workflow

1. Infer the review target.
   Determine the specific implementation goal, design question, or problem statement.

2. Lock the source map.
   Resolve each relevant repository and exact revision, then identify the paths and
   symbols the reviewer should inspect. Record material dirty or unpublished state.

3. Open the document with the front-matter note below, then state:
   - broad objective
   - current tactical objective
   - live benchmark, failure regime, or open uncertainty
   - the exact question the reviewer should focus on

4. Present the source map before the inlined evidence. Give direct inspection
   instructions rather than summaries of code the reviewer can read.

5. Inline only material admitted by the source policy and selection rule. Use the
   decisive span rather than an entire file when possible.

6. Verify the document reads as one coherent handoff rather than a stack of fragments.
   Use explicit section headings and refer to inlined material by section label. Confirm
   that every code reference resolves through the source map and that no unauthorized
   code-bearing material was inlined.

## Reviewer-Facing Copy Rules

- Address the reviewer as `you`.
- Write as direct instruction and context handoff, not as notes about how the document was assembled.
- Do not use `this package`, `the package`, or any other bundling metaphor.
- Except for an explicitly authorized code-inline section, refer to implementation only
  through the exact GitHub coordinates in the source map.
- Do not refer to local paths, unspecified repositories, or ambient conversation.
- Apart from the front-matter note below, do not comment on the prompt's size or construction.

## Front-Matter Note

Place this near the top of the document and do not elaborate on it:

> First-party code is intentionally omitted. Inspect the exact GitHub repositories,
> revisions, paths, and symbols named below. The inlined sections contain the review
> contract and non-code evidence.

If the user explicitly authorized a code-inline exception, amend the first sentence to
name each authorized section as the sole exception.

## Output

Report only:
- package root
- main review prompt doc path
- a short note on the code identities referenced and non-code evidence inlined
