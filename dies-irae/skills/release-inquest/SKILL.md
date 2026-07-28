---
name: release-inquest
description: Conduct a hostile, whole-product release-readiness inquest. Use when Codex should decide whether a repository and its actual release artifacts deserve shipment by reconstructing the declared release envelope; verifying canonical gates, dependencies, packaging, installation, lifecycle, user-system conduct, supported targets, author subtraction, and first-contact self-sufficiency; and returning or explicitly executing a dependency-ordered path to an evidence-backed RELEASE or HOLD verdict without inventing features or support.
---

# Release Inquest

## Mandate

Try to stop the release.

The fixed point is:

> Ship only a candidate that can be identified, built, verified, packaged, installed, encountered for the first time, operated, failed, recovered, updated where promised, and removed as promised from clean declared environments, without author memory, hidden privilege, accidental parochialism, or residue.

This is the final integration gate between a repository and a product worthy of another person's system. Judge the actual candidate, not the amount of work invested in it, the greenness of one test command, or the plausibility of its source tree. Every shipped surface must look intentional under hostile professional scrutiny.

The objective is not a larger feature set, generic polish, or compliance theater. It is an honest release claim backed by sufficient evidence. Freeze the product's declared charter and attempt to falsify it from source identity through artifact and lifecycle.

Default to `inquest_report`. Change the repository only under explicit `execute_after_inquest` authority, and only after the complete report exists.

## Candidate And Authority

A release candidate is a specific source identity, dependency resolution, toolchain and release configuration, artifact set, target envelope, and distribution path. Record dirt, generated inputs, mutable external dependencies, and anything else that can make two nominally identical builds different. A verdict attaches only to that identity.

Recover the release claim from present product contracts, package metadata, command and API surfaces, installation paths, supported targets, durable formats, external services, and distribution machinery. Distinguish advertised, enforced, observed, and merely inferred claims. None is automatically sovereign; expose contradictions and authority decisions rather than choosing the convenient side.

Freeze supported behavior, public contracts, platforms, languages, audiences, and operational promises unless the user separately authorizes change. The inquest may demand that every claimed path become real. It may not manufacture new platforms, translations, accessibility modes, integrations, or features because another product could plausibly want them.

Load the repository instructions and the `product-doctrine` skill, including every applicable platform projection. Load the relevant `style-doctrine` guides when source or manifest quality bears on release fitness.

Release Inquest owns the integrated ship judgment, not every specialist campaign. Consume source-matched reports from Qui Custodit, Chronicler, Fahrenheit 451, Bare Metal ALARA, Exterminate Slop, and Majestic Magisteria when available. If a deep campaign is required, specify an exact handoff and continue the inquest; do not silently launch a rewrite, documentation reconstruction, performance campaign, or test-suite redesign.

## Release Law

### No Evidence, No Release

Configured gates are intended witnesses, not accomplished evidence. Run the canonical verification contract at the locked identity when authority and environment permit. Inspect the artifacts it produces. A passing development build does not prove release configuration, a passing unit suite does not prove assembly, and source review does not prove installation or cleanup.

Use `RELEASE` only when every material release claim has credible evidence and no undispositioned blocker remains. Use `HOLD` for a known defect, a material claim left unproved, or an authority conflict that can change the released product. Mark each hold reason as `defect`, `unproven`, or `authority`. A complete read-only inquest may correctly end in `HOLD`; uncertainty is not an optimistic pass.

Residual risks may survive only when they are bounded, explicit, evidence-backed, and outside the declared release claim. There is no “conditional release” that launders a missing material proof.

### Subtract The Author

The author is not an implicit input or platform. No undeclared fact of the author's machine, identity, locale, geography, timezone, accounts, data, accumulated state, network, or habits may become product law.

Hold the declared charter fixed and vary the ambient coordinates the actual product exposes. Behavior may depend on them only where the contract requires it, and then through explicit user intent or lawful host policy rather than an author-shaped fallback. A product with one language need not gain another; a UTC product need not localize time; a single-platform product need not grow a portability matrix. But supported plurality must not secretly collapse to the author's preferred member.

### First Contact Is Self-Sufficient

A new user may be expert, but arrives without repository history, private vocabulary, remembered bootstrap ritual, preexisting application state, privileged credentials, or knowledge of the author's workstation. Within the declared audience and prerequisites, the entrypoint, state, costs, next actions, and failures must be intelligible without author memory.

This does not require tutorials, wizards, simplification, or lowest-common-denominator design. A demanding instrument may remain demanding. It may not require occult initiation.

### The Actual Artifact Is The Product

Trace the candidate across the complete release lifecycle appropriate to its kind. A desktop application, service, library, CLI, plugin, model, and container expose different release graphs; let the product reveal its own. Inspect package contents, metadata, executable entrypoints, runtime dependencies, defaults, permissions, side effects, persistence, external conduct, failure behavior, and removal rather than inferring them from source intent.

Dependency age, TODO markers, warnings, debug symbols, generated files, or unconventional packaging are sensors, not automatic verdicts. Ask what reaches the release, what law it violates, and what user-visible or operational risk it creates. Conversely, absence from a familiar checklist does not excuse a defect the candidate's own topology reveals.

## Protocol

### 0. Open The Inquest

When writes are available, create resumable state before deep reading:

```text
/tmp/release-inquest-<repo>-<candidate>-<run-id>.md
/tmp/release-inquest-<repo>-<candidate>-<run-id>-report.md
```

Create a companion `-high-severity.md` register only if a qualifying defect appears.

Record mode, source identity, candidate, release envelope, applicable doctrine, context budget, release graph, surface and evidence manifests, claim ledger, ambient-coordinate register, reductions, fold hierarchy, blockers, handoffs, verdict, verification, and frontier. The worklog preserves orientation; the report owns the final argument. If all writes are forbidden, carry the same state into the final response and mark the run nonresumable.

### 1. Lock The Release Claim

Identify the candidate version and source state; expected artifacts and their consumers; build and distribution path; declared targets and prerequisites; installation, upgrade, migration, recovery, and removal promises; public interfaces and durable formats; external systems; and the canonical verification contract.

Infer the narrowest honest envelope when the project is silent, and mark the missing authority. Do not promote development conveniences, aspirational prose, dormant code, or historical targets into release promises. Do not narrow an explicit claim merely because one target is inconvenient to prove.

Establish what would constitute a material release blocker before inspecting individual findings. The threshold follows the product's consequences and promises, not a universal severity table.

### 2. Build The Release Graph

Map the path from owned source and dependency inputs through generation, verification, build, package assembly, publication, acquisition, installation, first contact, ordinary and adverse operation, persistence, update or migration where promised, recovery, and removal. Include user-system effects and external services wherever they can alter the claim.

Build two bounded manifests:

- release surfaces whose contents or configuration can change the shipped product
- evidence that actually witnesses release claims at the locked identity

Treat source, manifests, lockfiles, build and packaging logic, installers, generated inputs, legal material, user-facing contracts, test and lint configuration, release artifacts, and distribution metadata according to their actual role. Keep irrelevant tracked files outside the census. Record vendored, generated, machine-consumed, and externally owned surfaces before excluding them.

Run a cheap `wc -l -c` preflight over file-backed release surfaces. Use these default circuit breakers for all raw material entering one deep-reading clique:

```text
context_line_ceiling: 3000
context_byte_ceiling: 131072
```

Either ceiling trips the budget. Count source, configuration, documentation, history, dependency metadata, artifact listings, logs, and command output when their contents enter context. Broad indexes and narrow probes may range widely; voluminous output is a deep read. Split oversized surfaces into coherent semantic slices.

### 3. Seed An Adaptive Inquest Cover

Group release claims, governed surfaces, artifact transitions, lifecycle stages, targets, and evidence into overlapping cliques that resolve coherent ship questions under budget. Let the candidate's release graph determine the cover. Do not march through a universal release checklist or treat repository directories as product boundaries.

Every material claim, release surface, artifact transition, supported target, and lifecycle promise must belong to at least one planned clique. Cross-cut the cover with author subtraction and first contact wherever ambient coordinates or human interpretation can change behavior. Split, merge, overlap, or replace cliques as the inquest develops.

### 4. Interrogate And Reduce

For each clique, attempt to construct a valid reason to reject the release. Determine the governing claim and authority, how it can fail, what reaches the artifact or user, which evidence is independent, and whether clean construction and lifecycle trials agree with source intent.

Search freely for professional disqualifiers: failed or missing canonical gates, secrets and private material, unfinished release-reachable paths, developer residue, stale claims, accidental debug conduct, unnecessary or vulnerable dependency exposure, malformed packages, nonreproducible inputs, destructive migrations, unbounded resource use, hidden networking or privilege, platform drift, failure corruption, uninstall residue, and anything else the actual product makes relevant. This is a threat vocabulary, not a multiple-choice audit.

Dependency fitness includes necessity, ownership, selected features, version posture, advisories, provenance, license compatibility, lock and update policy, and operational consequence. “Latest” is not automatically correct and “it builds” is not sufficient. Consult current authoritative registries, upstream releases, and advisory sources when currency matters and network access is allowed; otherwise mark the claim unproved.

Run builds, checks, artifact inspection, and lifecycle trials in clean isolated environments when allowed. Keep temporary profiles, homes, caches, credentials, display servers, ports, and installation prefixes outside the user's live system. Use the `x11-gui-testing` skill for graphical Linux applications. Never turn an inquest into an uncontrolled live deployment or destructive uninstall test.

The ambient user's profile and accumulated application data are private territory, not a convenient fixture or telemetry corpus. Do not enumerate, read, hash, or summarize them merely because the sandbox permits access. Establish product conduct from clean trials, code, artifacts, and explicitly supplied evidence. Consult live user state only with separate explicit authorization and a narrow evidentiary need.

Before opening another clique, reduce the current one into the smallest account another intelligent model can fold without rereading raw material. Preserve claims, release surfaces, artifact and lifecycle evidence, author-coordinate findings, first-contact findings, blockers, counterevidence, handoffs, and frontier. Merely running a scanner or command does not constitute coverage.

Record catastrophic defects immediately in the high-severity register and continue the inquest. Discovery neither authorizes rectification nor excuses incomplete coverage.

### 5. Conduct Author-Subtraction And First-Contact Trials

Derive ambient coordinates from the candidate rather than a canned internationalization catalogue. Look for facts supplied implicitly by the development environment, fixtures, defaults, paths, account state, locale-sensitive parsing or ordering, clocks, geography, network topology, hardware, prior runs, and distribution channel. Perturb every material coordinate within the declared envelope or establish why it cannot affect the claim.

Exercise the product from a sterile user state through the real distributed entrypoint. Observe discovery, initial invocation, acquisition or creation of the first useful result, ordinary failure and recovery, persistence, restart, and removal as applicable. For a library or developer surface, use a clean downstream consumer rather than importing it from its own repository.

Classify every apparent parochiality as explicit product law, user choice, host policy, leaked author biography, or out-of-envelope feature request. Only leaked biography is intrinsically defective; explicit laws may still conflict with advertised claims.

### 6. Fold And Adjudicate

Fold related clique reductions into bounded branch syntheses, then reconcile branches through bridge reductions until one release thesis remains. Higher folds consume reductions, not raw files or complete logs. The same context ceilings govern fold inputs; add another level rather than flooding the final pass.

Use the folds to find cross-surface failures: gates that omit shipped targets, documentation that describes a different artifact, packages that exclude runtime material, clean builds that depend on untracked state, first runs that depend on author state, platform branches no canonical path exercises, upgrades that strand old data, or removals that violate ownership.

Specialist cleanliness is not enough if the assembled release graph fails. Conversely, do not block release on aesthetic preferences, hypothetical features, or specialist perfection beyond the locked claim and material risk.

### 7. Render The Verdict And Closure Program

Issue `RELEASE` or `HOLD` against the exact candidate identity. Every hold must name the failed or unproved claim, evidence, consequence, blocking threshold, and closure proof. Every surviving risk must name its boundary and why it does not invalidate the claim.

Professionalization is not accumulation. Derive the smallest release graph that can substantiate the frozen claim. Prefer removing dormant paths, unnecessary dependencies, duplicate gates, redundant configuration, and release machinery with no unique evidentiary or product role. Add a gate, job, scanner, package layer, or lifecycle mechanism only when an unmet release obligation cannot be discharged by strengthening or consolidating an existing owner.

Produce a dependency-ordered closure program precise enough to execute without repeating the inquest. Establish missing evidence and receiving surfaces before destructive cleanup; correct authorities before their projections; repair build and packaging roots before downstream artifact symptoms; and rerun lifecycle trials on newly built artifacts after every candidate-changing fix.

Within each closure disposition, state its `release_delta`: machinery retired or subsumed, the terminal owner, and irreducible additions. A purely additive closure item must name the release obligation that requires it.

Name specialist handoffs by semantic objective, scope, required evidence, and return condition. Do not emit “improve tests,” “update docs,” “optimize,” or “clean up code.” The release remains on hold until a handoff's release-relevant return condition is proved.

### 8. Report, Then Optionally Execute

Write the complete inquest report from the folds. Stop there unless execution was explicit.

For a project-wide inquest, render every report section and the complete release claim ledger. A section may record a clean result, an intentional absence, or an unresolved proof, but it may not silently vanish. The blocker register is a decision surface, not a substitute for exhaustive claim coverage. For bounded scope, retain every section that can materially bear on the named release claim.

Under `execute_after_inquest`, authorization covers repository-owned changes necessary to close the accepted release program while preserving the frozen behavior and public contract. Feature additions, support-envelope expansion, contract breaks, destructive data policy, publication, signing, credential use, and deployment require separate explicit authority.

Recheck source identity before mutation. Work in dependency order, use specialist doctrine where a handoff enters its domain, and keep the candidate identifiable. Rebuild artifacts from clean inputs and repeat the relevant installation, first-contact, adverse-operation, recovery, and removal trials. A verdict after edits applies only to the rebuilt and reverified candidate.

## Embedded Forms

### Run State

```text
mode: inquest_report | execute_after_inquest
repository:
source_identity:
candidate_version:
candidate_artifacts:
release_envelope:
distribution_path:
applicable_doctrine:
worklog_path:
report_path:
high_severity_path: none
context_line_ceiling: 3000
context_byte_ceiling: 131072

release_graph:
surface_manifest:
evidence_manifest:
claim_ledger:
ambient_coordinate_register:
clique_cover:
clique_reductions:
fold_hierarchy:
blockers:
specialist_handoffs:
verdict:
frontier:
execution:
verification:
residual:
```

### Release Claim Ledger

```text
| claim | authority | target_and_stage | failure_modes | evidence | artifact_or_lifecycle_anchor | judgment | blocker | disposition | coverage |
|-------|-----------|------------------|---------------|----------|------------------------------|----------|---------|-------------|----------|
```

### Ambient Coordinate Register

```text
| coordinate | present_authority | intended_authority | variation_within_envelope | evidence | judgment | disposition |
|------------|-------------------|--------------------|---------------------------|----------|----------|-------------|
```

### Clique Reduction

```text
clique_id:
ship_question:
release_surfaces:
evidence_set:
surface_lines:
surface_bytes:
coverage_delta:

claims_and_authority:
artifact_and_lifecycle_judgment:
author_subtraction:
first_contact:
blockers_and_counterevidence:
specialist_handoffs:
cross_clique_dependencies:
frontier:
supersedes:
```

### Inquest Report

```markdown
# Release Inquest: <candidate>

## Executive Verdict
## Locked Candidate And Release Envelope
## Coverage And Evidence
## Release Graph And Artifact Chain
## Verification And Repository Hygiene
## Dependencies, Provenance, And Packaging
## Product Lifecycle And User-System Conduct
## Subtract The Author
## First Contact
## Supported Targets And External Boundaries
## Release Blockers
## Dependency-Ordered Closure Program
## Specialist Handoffs
## High-Severity Register
## Reverification Program
## Residual Risks And Unknowns

### Complete Release Claim Ledger

| claim | target and stage | evidence | judgment | blocker or residual | disposition | dependencies |
|-------|------------------|----------|----------|---------------------|-------------|--------------|
```

## Hard Failures

- do not issue `RELEASE` without a locked source identity, artifact set, and release envelope
- do not certify source intent without inspecting the actual artifact and applicable lifecycle
- do not treat configured gates, stale CI, scanners, coverage, or a green unit suite as sufficient evidence
- do not convert missing material evidence into a conditional pass
- do not broaden platforms, languages, accessibility modes, audiences, integrations, or features under release authority
- do not mistake sophistication for poor first contact or demand lowest-common-denominator design
- do not let the author's environment, state, geography, locale, timezone, identity, or habits become an invisible prerequisite
- do not call dependencies current or safe without current authoritative evidence when the claim matters
- do not treat every TODO, old dependency, unconventional choice, or residual file as a blocker without tracing its release consequence
- do not ignore dirty inputs, generated state, package contents, migration paths, or removal residue
- do not mutate the live user system to prove respect for it
- do not mine the ambient user's profile or accumulated application state as unauthorized release evidence
- do not let a high-severity defect or specialist rabbit hole truncate the inquest
- do not replace the complete claim ledger with a shortlist of blockers
- do not emit vague handoffs or fixes without closure evidence
- do not exceed context or fold budgets through logs, artifacts, dependency output, or source dumps
- do not turn the worklog into a shadow report
- do not edit before the complete report or without explicit execution authority
