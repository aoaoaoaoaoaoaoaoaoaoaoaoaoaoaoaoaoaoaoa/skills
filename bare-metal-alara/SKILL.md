---
name: bare-metal-alara
description: "Use when the user wants a standard Bare Metal ALARA performance goal: lock the workload and correctness oracle, write a terse .goals/ acceptance contract, install it as a Codex /goal when possible, then profile and optimize runtime as low as reasonably achievable without semantic drift or gratuitous uglification."
---

# Bare Metal ALARA

Bring the specified implementation's runtime As Low As Reasonably Achievable for the agreed workload while preserving existing business behavior and public contracts. Use measurement and profiling to discover the true limiting structure, then reshape code, data, and algorithms freely when the result is materially faster and not gratuitously contorted.

Lock the target before optimizing. Inspect enough of the repo to identify the implementation surface, but if any uncertainty remains about the representative workload, benchmark command, input distribution, correctness oracle, public contract, scope boundary, performance metric, or forbidden tradeoff, explicitly ask the user to clarify. Do not proceed under a guessed workload.

Create a repo-root `.goals/<slug>.md` contract before the long optimization pass. Create `.goals/` if needed. Ensure `.goals/` is gitignored; if it is not ignored, add `.goals/` to the repo-root `.gitignore`. Keep the document short and acceptance-first. Do not prescribe tactics unless the user explicitly freezes them. Prefer named references over copied plans or benchmark notes.

Use this goal shape:

```markdown
# Goal: Bare Metal ALARA For <target>

## Objective
Reduce runtime for <workload> as low as reasonably achievable while preserving the existing business behavior and public contracts of <target>.

## References
- `<benchmark or command>`: authoritative performance measurement
- `<tests or oracle>`: authoritative behavior preservation check
- `<paths>`: implementation surface in scope

## Acceptance Criteria
- Behavior remains preserved according to <oracle>.
- The agreed workload is benchmarked before and after optimization.
- Runtime improves materially on the agreed workload, or the final report shows why remaining plausible gains are unreasonable.
- No semantic changes, gratuitous obscurity, or unjustified high-risk low-level techniques are introduced.

## Verification
- `<behavior command>`
- `<benchmark command>`
- Inspect changed implementation for disproportionate complexity or risk.
```

Install the goal directly if goal tools are available and no goal already exists: call `get_goal`, then `create_goal` with this objective:

```text
Read .goals/<slug>.md and complete every acceptance criterion in it. Mark the goal complete only after the verification evidence required by that file is satisfied.
```

If goal tools are unavailable, or if a goal already exists and cannot be safely replaced through tools, output the exact copyable command sequence:

```text
/goal clear
/goal Read .goals/<slug>.md and complete every acceptance criterion in it. Mark the goal complete only after the verification evidence required by that file is satisfied.
```

If the user asked only to prepare the goal, stop there. Otherwise execute the ALARA pass immediately: establish the baseline, profile, change, verify behavior, remeasure, and repeat. Continue while evidence or strong mechanical reasoning suggests meaningful speed remains available at reasonable complexity and risk. Stop only when further gains require semantic change, ungrounded workload assumptions, unacceptable fragility, or uglification disproportionate to the win.

Low-level code is allowed. Gratuitous cleverness is not. Unsafe code, precision loss, lossy approximation, hidden global state, concurrency hazards, cache invalidation traps, and platform-specific contortions require explicit justification and usually explicit user permission.

Final reporting must include the baseline, final measurement, commands used, the main structural changes, and any remaining plausible optimizations judged unreasonable.
