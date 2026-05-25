---
name: majestic-magisteria
description: "Use when the user wants a whole-project, narrow-scope data-model reconciliation pass, especially in Rust: audit type declarations, conversions, duplicated domain shapes, mirrored enums, ID/key wrappers, DTO twins, and subsystem-specific type silos; produce a prioritized canonicalization plan or execute it when explicitly requested."
---

# Majestic Magisteria

Unify the project's data model. This is not generic cleanup. This is a whole-project, narrow-scope campaign against accidental local ontologies: duplicate types, mirrored enums, conversion pinball, DTO twins, wrapper silos, and subsystem dialects that exist because past work happened in narrow context.

The goal is not fewer types. The goal is one lawful mathematical model: small irreducible atoms, composed everywhere, with translations only at real boundaries.

## Posture

Start from the suspicion that every local data type is part of a global algebra. A type survives as separate only if it has a distinct law: different invariant, lifecycle phase, representation need, ownership/borrowing role, external protocol, or bounded context.

Do not collapse legitimate boundaries. Boundary projections, wire formats, database rows, FFI types, parser tokens, and phase-specific types may be correct. But they must be explicit projections, not accidental rival definitions of the same concept.

## Scope

Require a concrete project root and a narrow semantic target: IDs, spans, paths, syntax nodes, diagnostics, package metadata, shader parameters, query keys, config, events, permissions, runtime state, or another named data-model region.

If the user gives only "the data model," choose a plausible high-leverage region after a quick manifest scan and state the assumption. This skill is whole-project in reach but narrow in subject.

## Language Lens

This skill is optimized for Rust. Use `rust_analyzer` aggressively: definitions, references, implementations, rename feasibility, call hierarchy, hover, and semantic search from live construction/conversion sites.

For non-Rust projects, apply the same model, but use the language's type checker, LSP, symbol index, and dependency graph where available.

## Light Ledger

Create a compact ledger:

```text
/tmp/majestic-magisteria-<repo>-<scope>.md
```

Use it for durable state:

```text
scope:
target_region:
language:
artifact_mode: concordance_report | execute_after_report

type_atlas:
conversion_edges:
silo_clusters:
legitimate_boundaries:
canonical_atoms:
read_waves:
report_checkpoints:
implementation_order:
verification:
residual_uncertainty:
```

Do not over-ledger. The ledger exists to preserve global orientation across a wide scan.

## Read Budget And Write Barriers

Context is mortal. Do not wait for the perfect whole-project atlas before writing. Create both the ledger and concordance report skeleton before deep reading.

Use broad indexing freely: `rg`, file manifests, symbol lists, type-name searches, conversion-name searches, and LSP reference counts may scan the whole project. Deep semantic reading is gated.

A deep-read wave may inspect at most:

- 8 source files, or
- 20 anchored symbols/conversion edges, or
- one coherent type cluster,

whichever comes first.

After each wave, stop reading and write out:

- new atlas entries
- conversion edges discovered
- candidate silo clusters
- boundary/projection judgments
- canonical atom hypotheses
- open questions
- next read wave

Append this to the `/tmp` ledger and update the concordance report draft. The report should grow throughout the audit, not appear at the end.

Do not begin another deep-read wave until the current evidence has been reduced into durable text. If the current state is incomplete, write the incompleteness explicitly under `Residual Questions` and continue.

## Type Atlas

Build a whole-project atlas for the target region. Search for:

- type declarations, newtypes, aliases, structs, enums, traits, type parameters
- constructors, smart constructors, parsers, normalizers, validators
- `From`, `Into`, `TryFrom`, `AsRef`, `Deref`, `Borrow`, `ToString`, `FromStr`
- `into_*`, `as_*`, `to_*`, `from_*`, `parse_*`, `normalize_*`, `validate_*`
- serialization, database, CLI, FFI, wire, and config boundaries
- repeated field bundles and argument clumps
- mirror enums and stringly discriminators
- duplicate IDs, keys, names, paths, spans, ranges, units, offsets, handles, indices
- local DTOs used beyond a true boundary

Record enough evidence to see the whole region at once. The enemy is local plausibility hiding global incoherence.

## Cluster And Judge

Cluster candidates by:

- name similarity
- field/variant shape
- conversion traffic
- shared validation or normalization
- shared call sites
- lifecycle phase
- representation/performance role
- boundary ownership

Classify each cluster:

- `canonicalize`: accidental duplicate concepts should become one atom or one composite
- `shared_kernel`: multiple contexts need the same tiny primitive
- `projection`: separate type is justified as IO, wire, DB, parser, or FFI shape
- `phase_type`: separate type is justified by lifecycle or invariant transition
- `view_or_borrow`: separate type is justified by ownership, borrowing, or representation
- `bounded_context`: separate type is justified by genuinely different domain meaning
- `false_positive`: superficial similarity only

The hard question is always: do these types have different laws, or merely different birthplaces?

## Canonical Model

Design the smallest shared kernel that can carry the region:

- irreducible ID/key/path/span/range/unit atoms
- enums for finite worlds
- opaque wrappers for validated tokens
- generic families when several wrappers differ only by tag or scope
- borrowed/view forms where representation requires them
- composites built by nesting atoms, not re-declaring their fields
- boundary projections converted once at the edge

Prefer powerful abstractions over local flatter structs. A small algebra of strong primitives is more legible to agents than many "simple" near-duplicates.

Avoid god types. Universally useful atoms should be small, law-bearing, and composable. Context-specific composites may remain when they encode real context.

## Concordance Report

Default to a standalone report before editing:

```text
/tmp/majestic-magisteria-<repo>-<scope>-concordance-report.md
```

Use this shape:

```markdown
# Majestic Magisteria Concordance Report: <scope>

## Executive Summary

## Target Region

## Current Type Atlas

## Conversion Graph

## Silo Clusters

## Legitimate Boundaries

## Proposed Canonical Atoms

## Canonicalization Plan

| order | cluster | decision | proposed owner | payoff | risk |
|-------|---------|----------|----------------|--------|------|

## Implementation Specifications

### <cluster id>: <title>

**Decision:**  
**Current Types:**  
**Evidence:**  
**Law / Invariant:**  
**Canonical Shape:**  
**Migration Steps:**  
**Conversions To Delete:**  
**Behavior Preservation:**  
**Verification:**  
**Risks:**  

## Residual Questions
```

The report must be directly executable. Do not merely say "unify these." Specify owner modules, target type shapes, migration order, conversions to delete, and verification surface.

## Execution

Execute only when the user explicitly asks. First write the concordance report, then implement from it in dependency order.

Preferred moves:

- introduce canonical atom, then migrate construction sites
- move validation/normalization into the atom owner
- collapse mirror enums into one enum plus context-specific methods
- replace duplicate wrappers with one generic/tagged family when the law is shared
- replace local owned duplicates with borrowed/view/projection forms
- convert transport/database/FFI shapes once at the boundary
- delete `From`/`TryFrom` edges made obsolete by canonical ownership
- move behavior to the type that owns the invariant
- inline or delete types whose only job was mediating a silo

Preserve public API compatibility only if requested.

## Verification

Use the narrowest meaningful checks for touched surfaces, then widen if the canonical type crosses module or crate boundaries.

Verification should include at least one structural check: conversion edge count reduced, duplicate declarations deleted, repeated validation removed, or call sites now constructing the canonical type directly.

## Final Response

Include:

- ledger path
- concordance report path
- target region
- atlas size and main clusters
- proposed canonical atoms
- legitimate boundaries preserved
- highest-priority canonicalization steps
- verification plan or result
- residual uncertainty

## Failure Modes

- do not run generic cleanup
- do not scan only the files that first mention the type
- do not collapse types with genuinely different laws
- do not preserve duplicate types because both are locally correct
- do not create a god object
- do not leave conversion pinball intact
- do not treat aliases as semantic unification
- do not edit before the concordance report unless the user explicitly requested a narrow hotfix
- do not perform more than one deep-read wave without updating the ledger and concordance report
