---
name: advocatus-diaboli
description: "Conduct a hostile, whole-product release inquest: decide whether an exact candidate and its actual artifacts deserve shipment by verifying canonical gates, correctness, dependencies, packaging, installation, lifecycle, conduct on the user's system, supported targets, author subtraction, and first contact, and return an evidence-backed RELEASE or HOLD verdict with a dependency-ordered closure program. Never invents features or support. Produces a report; executes the closure program only when explicitly authorized."
---

# Advocatus Diaboli

## Mandate

Try to stop the release.

The fixed point is:

> Ship only a candidate that can be identified, built, verified, packaged, installed, encountered for the first time, operated, failed, recovered, updated where promised, and removed as promised from clean declared environments, without author memory, hidden privilege, accidental parochialism, or residue.

This is the final integration gate between a repository and a product worthy of another person's system. Judge the actual candidate, not the work invested in it, the greenness of one test command, or the plausibility of its source tree. Every shipped surface must look intentional under hostile professional scrutiny.

The objective is not a larger feature set, generic polish, or compliance theater. It is an honest set of release claims backed by sufficient evidence: freeze the claims and attempt to falsify them from source identity through artifact and lifecycle.

Default to `report`. Change the repository only under explicit `execute` authority, and only after the complete report exists.

## Candidate and claims

A candidate is a specific source identity, dependency resolution, toolchain and release configuration, artifact set, target set, and distribution path. Record uncommitted changes, generated inputs, mutable external dependencies, and anything else that can make two nominally identical builds differ. The verdict attaches to that candidate: it holds for any delivery that ships exactly the judged content with the judged resolution, toolchain, and configuration, and any change to that content voids it.

When a charter is supplied, take the product's claims from it and add the release-specific claims: artifacts, targets, distribution, and lifecycle promises. Otherwise recover the claims from product contracts, package metadata, command and API surfaces, installation paths, supported targets, durable formats, external services, and distribution machinery. Distinguish advertised, enforced, observed, and merely inferred claims; none is automatically authoritative, and a contradiction that can change the released product is an authority question.

Freeze supported behavior, public contracts, platforms, languages, audiences, and operational promises. The inquest may demand that every claimed path become real. It may not manufacture platforms, translations, accessibility modes, integrations, or features because another product could plausibly want them.

Read the repository's `AGENTS.md` files and load `$product-doctrine` with every applicable platform projection; its author-subtraction and first-contact rules are the standard for the trials below. Load `$ui-doctrine` when the product has a visible interface, and `$style-doctrine` when source or manifest quality bears on release fitness.

Advocatus Diaboli owns the integrated ship judgment, not every specialist campaign. Consume current reports for the same candidate from Confutatis, Tabula Rasa, Scriptorium, Damnatio Memoriae, Delenda, Imperium, and Bare Metal ALARA when they exist. When a deep campaign is required, specify an exact handoff and continue the inquest; do not silently launch a rewrite, a documentation reconstruction, a performance campaign, or a test-suite redesign.

## Evidence and verdict

Configured gates are intended witnesses, not accomplished evidence. Run the canonical verification at the locked candidate when authority and environment permit, and inspect the artifacts it produces. A passing development build does not prove the release configuration, a passing unit suite does not prove assembly, and source review does not prove installation or cleanup.

Return `RELEASE` only when every material claim has credible evidence and no blocker remains. Return `HOLD` otherwise, and mark each blocker with its reason: `failed` for a claim shown not to hold, `unproven` for a material claim without credible evidence, and `authority_question` for an unresolved decision that can change the released product. A complete read-only inquest may correctly end in `HOLD`; uncertainty is not a pass.

A `critical` or `high` finding within the claims is a blocker. Lesser findings are blockers too when together they show that the candidate would not survive hostile professional scrutiny; name the pattern and its evidence. Do not hold the release for aesthetic preference, hypothetical features, or specialist perfection beyond the claims.

A residual risk survives only when it is bounded, explicit, evidenced, and outside the claims. There is no conditional release that launders a missing material proof.

The actual artifact is the product. Trace the candidate across the lifecycle its kind implies: a desktop application, service, library, CLI, plugin, model, and container each expose a different release graph. Inspect package contents, metadata, entrypoints, runtime dependencies, defaults, permissions, side effects, persistence, external conduct, failure behavior, and removal instead of inferring them from source. Dependency age, TODO markers, warnings, debug symbols, generated files, and unconventional packaging are sensors, not verdicts: ask what reaches the release, what it violates, and what risk it creates. Absence from a familiar checklist does not excuse a defect the candidate's own structure reveals.

## Procedure

### 1. Open the inquest

Create the worklog and report before deep reading:

```text
/tmp/advocatus-diaboli-<repo>-<candidate>-<run-id>.md
/tmp/advocatus-diaboli-<repo>-<candidate>-<run-id>-report.md
```

In a tribunal, use the directory the tribunal assigns. Record the mode, source identity, candidate, claims, and applicable doctrine. Create a critical register beside the report only when a `critical` finding appears; record it and continue coverage. If writes are forbidden, carry the same state in the final response and state that the run cannot be resumed.

### 2. Lock the claims

Identify the candidate version and source state; the expected artifacts and their consumers; the build and distribution path; the declared targets and prerequisites; the installation, upgrade, migration, recovery, and removal promises; the public interfaces and durable formats; the external systems; and the canonical verification.

When the project is silent, infer the narrowest honest claims and record the missing authority. Do not promote development conveniences, aspirational prose, dormant code, or historical targets into release promises, and do not narrow an explicit claim because one target is inconvenient to prove. Before inspecting individual findings, establish what consequence would hold this product's release.

### 3. Map the release graph

Map the path from owned source and dependency inputs through generation, verification, build, packaging, publication, acquisition, installation, first contact, ordinary and adverse operation, persistence, update or migration where promised, recovery, and removal. Include effects on the user's system and external services wherever they can alter a claim.

### 4. Interrogate

Run `$clique-fold` with:

- `subject`: for each claim or release surface, how it can fail between source identity and removal, the independent evidence at the locked candidate, and whether it holds the release
- `columns`: `authority | target_and_stage | failure_modes | evidence | anchor | judgment | blocker | disposition`

The manifest holds every material claim, every release surface whose contents or configuration can change the shipped product, and every artifact transition, supported target, and lifecycle promise. Evidence that witnesses a claim, including command and trial output, belongs to the fringe. Keep irrelevant tracked files out, and record vendored, generated, machine-consumed, and externally owned surfaces before excluding them. Group claims, surfaces, lifecycle stages, targets, and evidence into cliques that each resolve one ship question, and cut across the cover with author subtraction and first contact wherever ambient coordinates or human interpretation can change behavior. Each reduction preserves the claims and authority, the artifact and lifecycle judgment, author-subtraction and first-contact findings, blockers and counterevidence, and handoffs. Running a scanner or command is not coverage.

In each clique, attempt to construct a valid reason to reject the release. Search freely for professional disqualifiers: failed or missing canonical gates, a gate weaker than the style doctrine's enforcement, correctness defects, secrets and private material, unfinished paths the release can reach, developer residue, stale claims, accidental debug conduct, unnecessary or vulnerable dependencies, malformed packages, nonreproducible inputs, a version that misstates the change to the public contract, destructive migrations, unbounded resource use, hidden networking or privilege, platform drift, corruption on failure, residue after removal, and anything else the product makes relevant. This is a vocabulary of threats, not a checklist.

Dependency fitness includes necessity, ownership, selected features, version posture, advisories, provenance, license compatibility, lock and update policy, and operational consequence. "Latest" is not automatically correct, and "it builds" is not sufficient. Consult current registries, upstream releases, and advisory sources when currency matters and network access is allowed; otherwise mark the claim unproven.

Run builds, checks, artifact inspection, and lifecycle trials in clean, isolated environments when allowed, keeping temporary profiles, homes, caches, credentials, display servers, ports, and installation prefixes outside the user's live system. Use `$x11-gui-testing` for graphical Linux applications. The live system and the user's profile are private production state, not fixtures: destructive or privacy-invasive trials require separate, narrow authorization and otherwise run in disposable isolation.

### 5. Run the author-subtraction and first-contact trials

Derive the ambient coordinates from the candidate, not from a stock internationalization catalogue: facts supplied implicitly by the development environment, fixtures, defaults, paths, account state, locale-sensitive parsing or ordering, clocks, geography, network topology, hardware, prior runs, and distribution channel. Vary every material coordinate within the claims, or establish why it cannot affect them. A product with one language need not gain another, and a single-platform product need not grow a portability matrix, but a supported plurality must not quietly collapse to the author's preferred member. Classify each apparent parochialism as an explicit product rule, user choice, host policy, leaked author biography, or an out-of-scope feature request; only leaked biography is intrinsically a defect, though an explicit rule may still contradict an advertised claim.

Exercise the product from a sterile user state through the real distributed entrypoint: discovery, first invocation, the first useful result, ordinary failure and recovery, persistence, restart, and removal, as applicable. For a library or developer surface, use a clean downstream consumer instead of importing it from its own repository.

### 6. Adjudicate

Use the folds to find failures that cross surfaces: gates that omit shipped targets, documentation that describes a different artifact, packages that exclude runtime material, clean builds that depend on untracked state, first runs that depend on author state, platform branches no canonical path exercises, upgrades that strand old data, and removals that violate ownership. Clean specialist reports are not enough if the assembled release graph fails.

Issue `RELEASE` or `HOLD` against the exact candidate. Every blocker names the claim, evidence, consequence, reason, and closure proof. Every residual risk names its boundary and why it does not invalidate a claim.

Professionalization is not accumulation. Derive the smallest release graph that can substantiate the claims. Prefer removing dormant paths, unnecessary dependencies, duplicate gates, redundant configuration, and release machinery with no unique role. Add a gate, job, scanner, package layer, or lifecycle mechanism only when an unmet release obligation cannot be discharged by strengthening or consolidating an existing owner.

Produce a dependency-ordered closure program precise enough to execute without repeating the inquest: establish missing evidence and receiving surfaces before destructive cleanup, correct authorities before their projections, repair build and packaging roots before downstream artifact symptoms, and rerun lifecycle trials on newly built artifacts after every change to the candidate. For each item, state its release delta: the machinery retired or subsumed, the terminal owner, and any irreducible addition with the obligation that requires it. Name handoffs by objective, scope, required evidence, and return condition, never as "improve tests," "update docs," "optimize," or "clean up code." The release stays on hold until a handoff's release-relevant return condition is proved.

### 7. Report

Write the report from the folds. For a project-wide inquest, render every report section and the complete ledger; a section may record a clean result, an intentional absence, or an unresolved proof, but may not vanish. For a narrower scope, keep every section that can bear on its claims. Stop after the report unless `execute` was authorized.

### 8. Execute

`execute` covers the repository-owned changes needed to close the accepted closure program while preserving frozen behavior and the public contract. Feature additions, support expansion, contract breaks, destructive data policy, publication, signing, credential use, and deployment require separate explicit authority.

Recheck the source identity before changing anything. Work in dependency order, apply the relevant judge's doctrine where a handoff enters its jurisdiction, and keep the candidate identifiable. Rebuild artifacts from clean inputs and repeat the relevant installation, first-contact, adverse-operation, recovery, and removal trials. A verdict after changes applies only to the rebuilt and reverified candidate, which stays in the working tree for delivery.

## Forms

### Worklog

```text
mode: report | execute
repository:
source_identity:
candidate_version:
candidate_artifacts:
claims:
distribution_path:
applicable_doctrine:
worklog_path:
report_path:
critical_register: none

release_graph:
clique_fold:
coordinate_table:
blockers:
handoffs:
verdict:
execution:
verification:
residual:
```

### Coordinate table

```text
| coordinate | present_authority | intended_authority | variation_within_claims | evidence | judgment | disposition |
|------------|-------------------|--------------------|-------------------------|----------|----------|-------------|
```

### Report

```markdown
# Advocatus Diaboli: <candidate>

## Verdict
## Candidate and claims
## Coverage and evidence
## Release graph and artifact chain
## Verification and repository hygiene
## Correctness
## Dependencies, provenance, and packaging
## Lifecycle and conduct on the user's system
## Author subtraction
## First contact
## Supported targets and external boundaries
## Blockers
## Closure program
## Handoffs
## Critical register
## Reverification program
## Residual risks and unknowns

### Ledger

The complete clique-fold ledger, one row per claim or release surface.
```
