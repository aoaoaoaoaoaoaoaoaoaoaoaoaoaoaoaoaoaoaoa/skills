---
name: pro-plan
description: "Build a self-contained Pro planning prompt after locally locking a rough feature, refactor, or design ask into concrete goals. Use when the user wants Pro's strategic insight before implementation: hidden structure, optimal types and data structures, elegant architecture, surprising simplifications, non-obvious pitfalls, or a plan shape that an implementation model can cross-check and execute."
---

# Pro Plan

Use this skill when the user has a rough implementation idea and wants a Pro
planning pass before coding.

Pro is not being asked to act as a diligent implementation clerk. The local
model can inspect the repo, run tools, write code, and test the result. Pro is
being consulted for reach: the rare conceptual move, the hidden trap, the
cleaner representation, the implementation shape that becomes obvious only
after staring through the code rather than at it.

The skill is biphasic:

1. lock the ask locally
2. assemble a self-contained Pro planning prompt from the locked ask and the
   most insight-bearing context

Do not skip the first phase. A vague prompt produces a vague oracle.

## Phase 1: Lock The Ask

Start from the user's rough sketch. Inspect the repo enough to see the actual
surfaces involved. Then sharpen the request with the user until it is concrete
enough to plan against.

Push on:

- desired behavior
- explicit non-goals
- affected APIs, data paths, commands, UI surfaces, protocols, or storage formats
- constraints the implementation must respect
- acceptance criteria or observable success conditions
- compatibility, migration, performance, or security constraints when they are
  actually part of the feature
- ambiguities that would materially change the implementation

Keep this phase conversational. Do not turn it into a questionnaire unless the
ask is genuinely under-specified. The point is to converge on a locked target,
not to create paperwork.

When the scope is clear, write a short locked-ask brief. This brief becomes the
first inlined section of the Pro prompt. If the user explicitly asks to proceed
despite uncertainty, name the assumptions instead of pretending they are facts.

## Phase 2: Assemble The Prompt

Create one markdown document under `/tmp` unless the user asks otherwise. Do not
commit it.

Reuse the inliner from the sibling review-package skill:

`/home/main/programming/projects/skills/assemble-pro-review-package/scripts/inline_section.py`

Use it to append labeled sections and enforce the shared hard token ceiling.
Do not copy or fork the inlining logic.

Inline material that helps Pro see the true implementation shape:

- the locked-ask brief
- the domain files where the important concepts live
- the current implementation around the target behavior
- representative call sites
- compact specs, design notes, schemas, or protocol docs
- prior attempts, audit notes, benchmark notes, or bug reports when they reveal
  the pressure behind the change
- tests only when they encode behavior or invariants not obvious from source and
  prose

Do not dump the repo. Do not include files merely because they are nearby. Spend
tokens on context that changes the plan.

## Pro Prompt

Address Pro as `you`. Ask for a plan, not code.

The prompt should make clear that Pro has only the inlined context. Use language
like this:

```markdown
You are planning an implementation from an inlined repository excerpt. The local
implementation model will perform a final repository cross-check before editing,
then implement.

Prioritize:
- the deepest interpretation of the locked request
- the cleanest architecture or local representation
- optimal types and data structures, written explicitly where possible
- maximal type safety and runtime efficiency
- hidden constraints, surprising simplifications, and leverage points
- where the naive implementation would become awkward or wrong
- the ordered implementation shape
- assumptions that would materially change the plan

Do not pad the response with generic testing, command, rollout, or risk
checklists. Mention validation, migration, performance, or security only when
there is a specific non-obvious issue in this code.

Return a concrete implementation plan that an expert implementation model can
cross-check against the full repo and then execute. Take your time: we are
turning to you because we are interested in finding the absolute best possible
solution.
```

## Output Shape

The Pro prompt should request a response roughly shaped as:

```markdown
# Understanding

Restate the locked request in the most precise form.

# Core Insight

Name the main implementation idea, representation, or architectural move.

# Types And Data Structures

Sketch the key types, data structures, invariants, and ownership boundaries
where the plan benefits from making them explicit.

# Plan

Give the ordered implementation plan. Be concrete enough that another model can
execute after checking the full repo.

# Non-Obvious Pitfalls

Include only pitfalls specific to this code or request.

# Assumptions

List assumptions that would materially alter the plan if false.
```

Do not demand sections that are irrelevant to the request. The shape is a
default, not a cage.

## Final Response To User

Report only:

- prompt document path
- what context was inlined
- any assumptions or unresolved scope questions carried into the prompt
