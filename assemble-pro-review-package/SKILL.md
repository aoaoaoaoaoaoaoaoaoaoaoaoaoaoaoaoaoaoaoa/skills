---
name: assemble-pro-review-package
description: Assemble a throwaway review bundle for an external expert or professional reviewer. Use when the user asks for a pro review package, reviewer handoff, expert audit bundle, or similar package that should include a single synthesized review prompt, the most relevant current design/spec/audit material for a specific goal, and aggressively inlined code, logs, and other text surfaces from the local repo plus any relevant rival or prior-art codebases.
---

# Assemble Pro Review Package

You are creating a design or implementation review package for an out-of-band expert
reviewer. This package should focus on the task or subproblem supplied by the user in
context. If you feel the problem is too vague for targeted review, push back and help the
user sharpen it.

Create the package in a subdir of `/tmp` unless the user asks otherwise. Do not
commit it. Echo back the path you've used when done.

The deliverable is one markdown document. Inline all review-relevant textual material into
that document as labeled sections. Do not create attachments, helper zips, overflow
artifacts, or companion files. If a textual artifact cannot be inlined under the ceiling,
cut it.

Use `scripts/inline_section.py` to append labeled sections into the document and enforce
the skill's fixed hard ceiling of 200k tokens, counted with `o200k_base`. It is not an
objective to reduce the token count, and there is no harm in going all the way up to the
limit if the material being included is genuinely relevant and the problem is complex.
Spend the ceiling on material that sharpens the review question. Cut material whose
relevance you cannot defend. The standard is the most clarifying document under the
ceiling, not the broadest dump.

## Workflow

1. Infer the review target.
   Determine the specific implementation goal, design question, or problem statement.

2. Open the document with the front-matter note below, then state:
   - broad objective
   - current tactical objective
   - live benchmark, failure regime, or open uncertainty
   - the exact question the reviewer should focus on

3. Inline the relevant material as labeled sections. Inline from these categories as
   applicable:
   - current pseudocode or normative spec
   - current design, audit, or experiment notes
   - core local implementation files
   - comparable mechanisms in rival implementations, reference literature, and tightly
     relevant logs or metrics

   Every section must bear directly on the review question. Irrelevant bulk degrades
   review quality. Do not dump entire source trees, unfiltered logs, or large files unless
   the review turns on them.

4. Verify the document reads as one coherent handoff rather than a stack of fragments.
   Use explicit section headings. Refer to inlined material by section label.

## Reviewer-Facing Copy Rules

- Address the reviewer as `you`.
- Write as direct instruction and context handoff, not as notes about how the document was assembled.
- Do not use `this package`, `the package`, or any other bundling metaphor.
- Do not refer to anything outside the document.
- Apart from the front-matter note below, do not comment on the prompt's size or construction.

## Front-Matter Note

Place this near the top of the document and do not elaborate on it:

> You are receiving a large inlined prompt. This is deliberate. The relevant source,
> logs, and reference material are included directly in this document.

## Selection Rule

Inline a file only if it:
- defines intended behavior
- explains the active failure or design pressure
- implements the hot path in question
- implements the external mechanism or reference point being compared, when such a comparison is relevant
- records the measurement motivating the review

Inline the relevant span rather than merely listing the file path.

## Output

Report only:
- package root
- main review prompt doc path
- a short note on what was inlined
