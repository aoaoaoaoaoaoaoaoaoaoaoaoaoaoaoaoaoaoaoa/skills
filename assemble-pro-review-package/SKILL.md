---
name: assemble-pro-review-package
description: Assemble a throwaway review bundle for an external expert or professional reviewer. Use when the user asks for a pro review package, reviewer handoff, expert audit bundle, or similar package that should include a single synthesized review prompt, the most relevant current design/spec/audit material for a specific goal, and aggressively inlined code, logs, and other text surfaces from the local repo plus any relevant rival or prior-art codebases.
---

# Assemble Pro Review Package

You are creating a design or implementation review package for an out-of-band pro model
or other expert to review. This package should focus on the task or subproblem supplied
by the user in context. If you feel the problem is too vague for targeted review, push back
and help the user sharpen it.

Create the package in a subdir of `/tmp` unless the user asks otherwise. Do not
commit it. Echo back the path you've used when done.

The reviewer-facing markdown surface must be a single top-level concatenated document.
Assume the prompt text itself is the primary payload and that helper zips are secondary
spillover only. Write that document so its full text can be copied directly into a
one-shot pro-model prompt without further assembly. Use theory of mind: write for a
highly capable reviewer who has no hidden context beyond the prompt text and any uploaded
overflow artifacts.

Default to a giga-prompt posture. OpenAI currently documents a 400k context window for
manually selected GPT-5.4 Thinking on the ChatGPT Pro tier, with 272k input tokens and
128k max output. Spending roughly 100k input tokens on a single review handoff is
acceptable when the material is load-bearing. Do not be shy about inlining large logs,
code paths, or external reference surfaces when they materially bear on the question. Do
not pad with junk either.

Use `scripts/inline_section.py` to append labeled sections into the prompt doc while
enforcing a hard 100k-token ceiling counted with `o200k_base` by default. OpenAI publicly
documents `tiktoken` as the tokenizer family to use programmatically for OpenAI models,
but does not publicly document the exact ChatGPT-web tokenizer mapping for GPT-5.4 Pro, so
`o200k_base` is the operative approximation unless better evidence is available.

## Workflow

1. Infer the review target.
   Determine the specific implementation goal, design question, or problem statement.

2. Write one top-level review prompt document.
   Include:
   - broad objective
   - current tactical objective
   - current live benchmark, failure regime, or otherwise uncertainty
   - the exact question the reviewer should focus on

   Address the pro model directly. The document should read as an instruction
   and context handoff to the reviewer, not as notes about a bundle someone
   else prepared.

3. Smart-concatenate the most relevant docs into sections of that document.
   Usually:
   - current pseudocode or normative spec
   - current design note
   - current audit or experiment note

   Include only what directly bears on the review target.
   Do not emit multiple markdown docs when one structured document will do.
   The prompt doc should normally contain the actual textual payload rather than an index
   pointing to helper artifacts.

4. Curate the largest useful inlined source surface that still clears the budget.
   Include:
   - the core local implementation files
   - when relevant, relevant external reference files that encode e.g.
     comparable mechanism in a rival implementation, reference literature
     materials, tightly-relevant logs or metrics, etc.

   Use the budget aggressively when the omitted context would otherwise force the reviewer
   to infer too much. Inline real source, real logs, and real rival code rather than
   summarizing them away. Reviewer performance still degrades on irrelevant sludge, so
   never lazily dump the whole source tree or giant logs without hand-attesting their
   relevance. The standard is not "smallest possible bundle"; it is "maximally clarifying
   bundle under the hard token ceiling."

5. Keep markdown singular, raw, and top-level.
   The package should have exactly one primary markdown handoff document in the
   package root. Any reviewer-facing markdown content should be merged into that
   document as sections rather than emitted as separate files.

6. Treat zips as overflow, not as the primary review surface.
   Zip only when:
   - the payload is binary
   - the payload is enormous and only partly load-bearing
   - inlining it would burst the hard budget
   - the reviewer may still benefit from optional deep inspection

   Prefer inlining textual artifacts directly. Do not put `.md` files inside the zips.

7. Build a clear throwaway package.
   Prefer:
   - one top-level raw review prompt doc
   - top-level zip files
   - optional subdirectories only for unzipped source or artifact staging

8. Make the prompt doc self-sufficient.
   It should read as one coherent handoff prompt, not as a bag of fragments.
   Use explicit section headings and refer to uploaded helper zips by filename
   only when needed.
   Do not use phrases like `this package` or `the package` inside the prompt
   document. Write as if speaking directly to the reviewer about the task,
   context, questions, and attached artifacts.

9. Put an explicit front-matter note near the top of the prompt.
   The note should explain that:
   - the reviewer is expected to consume a very large inlined prompt
   - this is intentional rather than accidental
   - the current GPT-5.4 ChatGPT reasoning tier has enough context for it
   - the reviewer should prefer the inlined text over any helper zip unless the prompt
     explicitly points to the zip for overflow detail

   Suggested wording:
   `This prompt intentionally inlines a very large amount of primary material. That is
   deliberate rather than accidental: current GPT-5.4 ChatGPT reasoning tiers perform
   better when the relevant source, logs, and reference implementations are present in the
   prompt itself instead of hidden behind attachments. OpenAI currently documents 400k
   context for manually selected GPT-5.4 Thinking on the Pro tier (272k input + 128k max
   output), so spending roughly 100k input tokens on a single high-stakes review handoff
   is well within the intended operating range. Treat the inlined text as the primary
   review surface; use any uploaded overflow artifacts only when this prompt points you to
   them explicitly.`

## Selection Rule

Include a file only if it:
- defines intended behavior
- explains the active failure or design pressure
- implements the hot path in question
- implements the external mechanism or reference point being compared, when such a comparison is relevant
- records the measurement motivating the review

Prefer inlining the relevant span rather than merely listing the file path.

## Output

Report only:
- package root
- main review prompt doc path
- zip paths
- a short note on what was included
