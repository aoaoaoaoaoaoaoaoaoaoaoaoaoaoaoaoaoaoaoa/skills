---
name: goal-smith
description: "Use when the user wants to turn a rough long-running objective into a durable Codex /goal: clarify scope, write a terse .goals/ acceptance contract, and either install it with create_goal or emit the exact /goal command to install it."
---

# Goal Smith

Forge a long-running Codex goal from a rough ask. A `/goal` is not a plan. It is a durable launch contract for autonomous work: the model may choose tactics, but completion must be judged against explicit acceptance criteria.

First resolve the user's references. If they say "this plan", "the above", "that issue", or similar, inspect the relevant conversation context and on-disk artifacts, then name stable file paths or identifiers in the goal. The final goal text must contain no deictic references: no "this", "above", "as discussed", "current", or unstated ambient context.

Before writing the goal, lock scope. Ask concise clarification questions whenever any uncertainty remains about the intended outcome, acceptance criteria, exclusions, verification, or authoritative references. Do not paper over ambiguity. Do not install a goal until the success condition is concrete enough that a later model can audit completion from the repository and named evidence alone.

Write the goal document under repo-root `.goals/<slug>.md`. Create `.goals/` if needed. Ensure `.goals/` is gitignored; if it is not ignored, add `.goals/` to the repo-root `.gitignore`. Keep the document short. Prefer references over inlining: if a planning document, issue, spec, or design note already exists, link it and state why it is authoritative instead of copying it. Focus on acceptance criteria and verification, not design prescription, unless the user explicitly freezes a tactic.

Use this shape:

```markdown
# Goal: <stable name>

## Objective
<one concise paragraph naming the desired end state>

## References
- `<path or identifier>`: <why it is authoritative>

## Acceptance Criteria
- <observable condition>
- <observable condition>

## Verification
- `<command>` proves <criterion or criteria>
- Inspect `<path>` for <condition>

## Out Of Scope
- <only if needed>
```

After writing the document, install the goal directly if the goal tools are available and no goal already exists: call `get_goal`, then `create_goal` with an objective like:

```text
Read .goals/<slug>.md and complete every acceptance criterion in it. Mark the goal complete only after the verification evidence required by that file is satisfied.
```

If goal tools are unavailable, or if a goal already exists and cannot be safely replaced through tools, output the exact copyable command sequence instead:

```text
/goal clear
/goal Read .goals/<slug>.md and complete every acceptance criterion in it. Mark the goal complete only after the verification evidence required by that file is satisfied.
```
