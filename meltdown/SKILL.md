---
name: meltdown
description: Distill arXiv links, PDFs, and similar scholarly sources into ultra-dense agent-facing notes. Use when Codex must fetch one or more academic or academic-ish sources, reconstruct them into clean plaintext by understanding them rather than preserving layout, and emit a deletion-first `meltdown/slug/core.md` plus `appendix.md` pair containing only the semantic core needed to implement, compare, rederive, or assess the work.
---

# Meltdown

Treat each source as raw ore. Melt it down. Recast it into a sparse technical artifact.

Do not summarize for humans. Do not preserve section structure out of respect for the paper. Do not preserve prose because the authors wrote it. Preserve only what survives a fresh technical judgment.

If given multiple sources, run this exact process independently for each unique paper. Deduplicate obvious duplicates first. Do not merge papers into one node unless explicitly asked.

## Contract

- Presume every unit should be deleted.
- Keep a unit only if deleting it would materially impair an agent's ability to implement, rederive, compare, or falsify the paper's core claims.
- Treat the unit of judgment as a `claim chunk`, not a source paragraph or section.
- Reconstruct plaintext semantically. Do not preserve layout, visual rhythm, or original markdown structure for its own sake.
- Preserve the paper's formulation when precision matters. Compress brutally, but do not paraphrase away technical content.
- Treat the appendix as a second-pass support surface, not a landfill. First write one ultra-dense artifact; then split it into `core` and `appendix`.
- Default to one input paper -> one output directory -> exactly two markdown files.

## Output Root And Slugs

If the user supplies an output root, use it.

Otherwise:

1. Look for an existing `meltdown/` directory in the current project or working directory.
2. If one exists, reuse it.
3. Otherwise create `meltdown/`.

Write each unique paper under:

```text
meltdown/<paper-slug>/
```

Write exactly:

```text
meltdown/<paper-slug>/core.md
meltdown/<paper-slug>/appendix.md
```

### Slug Rules

Prefer a stable slug shaped like:

```text
<firstauthor>-<year>-<short-title-stem>
```

Fallbacks:

- `arxiv-<id>`
- `doi-<normalized-id>`
- `paper-<domain>-<title-stem>`

Normalize slugs aggressively:

- lowercase ASCII only
- collapse whitespace and punctuation to `-`
- remove duplicate `-`
- trim leading and trailing `-`
- keep enough title to remain distinguishable
- once a slug exists for the same paper, reuse it rather than renaming casually

## File Schema

Both files must begin with YAML frontmatter.

Populate only fields that can be supported from the source with reasonable confidence.

Use this shape:

```md
---
kind: core | appendix
slug: <paper-slug>
title: <paper title>
year: <year>
authors:
  - <author>
source_urls:
  - <original supplied or fetched url>
canonical_url: <best canonical source url>
companion: appendix.md | core.md
---
```

## Core File

Write `core.md` in this order.

Omit a section only if it truly does not apply.

### `Read When`

Write exactly 2-3 sentences.

Use it as a routing surface. Answer questions like:

- what technical problem this paper actually helps with
- what kind of reader should continue
- what kind of reader can safely stop
- what makes the paper distinctive relative to nearby work

Do not write hype, scene-setting, or biography.

### `Abstract`

Write one crushed paragraph.

Preserve the idea of an abstract, not the paper's original wording. State the problem, method, and main result as tersely as possible without losing the paper's actual shape.

Do not quote the original abstract unless the exact formulation is unusually load-bearing.

### `Contribution Kernel`

Write a short bullet list.

Keep only the paper's surviving technical contributions or decisive claims. Each bullet should be a factual proposition, not a sales pitch.

### `Method / Construction`

Write the core technical mechanism in the paper's own formulation where possible.

Keep, as applicable:

- formal problem statement
- assumptions and setup
- definitions and notation that are strictly necessary
- algorithm, procedure, recurrence, construction, reduction, or protocol
- search space, state representation, or decomposition
- optimization program, objective, or constraint system
- data structure, encoding, invariant, or update rule
- proof strategy only when it is inseparable from the method

Delete:

- generic background
- intuitive warmups
- prose repetition
- implementation trivia unless it explains the result

Use bullets, short numbered procedures, displayed formulas, or terse prose as needed. Prefer structure over narration.

### `Main Claims / Theorems`

Keep theorem, proposition, lemma, or corollary labels when present and useful.

For each surviving claim, include:

- the claim itself
- the essential assumptions
- any bound, guarantee, limitation, or caveat
- a pointer into the appendix when proof support survives

Use local appendix anchors such as `P1`, `P2`, and so on.

### `Main Evaluations / Comparisons`

Keep only decisive evidence.

Depending on the paper, this may include:

- computational experiments
- benchmark or instance-family comparisons
- approximation or complexity comparisons
- simulation studies
- numerical tables
- sensitivity checks
- counterexamples
- lower or upper bound comparisons
- failure cases that materially limit the claim

For each surviving result, include the smallest factual surface that still supports comparison:

- setting, instance family, benchmark, or regime
- comparison point
- metric, criterion, or quantity of interest
- numeric or formal result when available
- what conclusion the result actually supports

Do not narrate evaluation sections. Do not preserve ornamental tours through many secondary cases.

Very small tables may survive inline if they are truly load-bearing and cheaper than prose. Otherwise move them to the appendix.

### `Appendix Map`

List the appendix anchors that matter to the core.

Use short lines such as:

- `P1`: proof skeleton for Theorem 2
- `T1`: full comparison table for the main computational study
- `R1`: prior method this paper directly improves on
- `U1`: extraction uncertainty affecting a surviving claim

## Appendix File

Write `appendix.md` in this order.

Omit a section only if it truly does not apply.

### `Proof Skeletons / Derivations`

Default all proofs and longer derivations here.

Do not dump full pedagogical proofs by default. Keep only the minimal support needed to rederive, trust, or challenge the main claim:

- hinge lemmas
- reduction structure
- proof skeleton
- crucial algebraic or combinatorial step
- key invariant or monotonicity argument
- duality argument, exchange argument, or charging step
- point where the argument could fail

Label proof items `P1`, `P2`, and so on.

### `Supporting Results / Tables`

Default supporting tables here unless they are very small and core-critical.

Flatten tables aggressively. Do not preserve visual formatting if a list or compact block conveys the same information.

Keep only results that materially sharpen understanding of the core:

- secondary comparisons that change interpretation
- sensitivity checks that alter how the method should be used
- boundary cases or adversarial instances
- negative results or failure modes
- numerical details needed to assess the main comparison
- deferred constructions or case splits that are load-bearing

Label table or result items `T1`, `T2`, and so on.

### `Critical References`

Default surviving references here.

Do not emit a bibliography dump.

Keep only references that are indispensable for one of these reasons:

- the paper's direct precursor
- the method, theorem, or construction it directly builds on
- the comparison point it is actually evaluated against
- the contrast case needed to situate the contribution
- the external result required to interpret a surviving claim

For each surviving reference, write:

- short citation
- one-line reason it survives

Label reference items `R1`, `R2`, and so on.

### `Extraction Uncertainties`

Record extraction problems only when they affect trust or interpretation.

Examples:

- scanned or garbled PDF text
- figure-only evidence with uncertain values
- notation collisions introduced by bad extraction
- ambiguity about whether a claim is original or inherited
- unresolved mismatch between statement, derivation, and comparison surface

Label uncertainty items `U1`, `U2`, and so on.

## Retention Rubric

Keep a claim chunk only if it does at least one of these:

- state the paper's problem in a way needed to interpret the rest
- state a novel algorithm, method, reduction, construction, formulation, encoding, or protocol
- state a theorem, guarantee, limitation, impossibility result, or counterexample
- report a decisive comparison, computational result, sensitivity check, failure mode, or empirical finding
- define notation, objects, or setup that are strictly necessary for a surviving chunk
- identify prior work that is indispensable for understanding contrast or lineage
- record an uncertainty that materially affects trust in the artifact

Delete by default:

- introductions as genre
- motivation as genre
- literature tours as genre
- summaries of summaries
- conclusion sections as genre
- rhetorical transitions
- pedagogical repetition
- vague claims of significance
- future-work fluff
- any sentence whose only function is to sound human

## Fetch And Reconstruction

Use `noo-harvest` to acquire the source set. This skill does not contain its own downloader doctrine.

Require from the harvest:

- stable paper identity
- title and authors
- a canonical identifier or landing page
- a readable abstract or equivalent summary surface
- one validated full-text artifact, preferably a direct PDF
- a manifest recording the chosen source, alternates, and access failures

If `noo-harvest` cannot produce a sufficient source set, stop and report the blockage. Do not improvise a parallel acquisition workflow here.

Do not treat any extraction tool as authoritative. Treat raw extraction as ore. Reconstruct the paper's meaning yourself.

When converting to plaintext:

- omit charts and figures unless they contain information unavailable elsewhere
- extract the proposition a figure establishes rather than reproducing the figure
- flatten tables rather than preserving layout
- preserve equations, labels, notation, and symbolic structure when they carry real precision
- refuse ornamental formatting

## Flow

### 1. Resolve identity and deduplicate

Resolve the paper's identity through the `noo-harvest` manifest before writing output.

If the same paper appears twice in the input under different links, keep one node and merge the source URLs.

Do not accidentally produce two slugs for the same paper.

### 2. Fetch the raw ore

Fetch the source material needed to understand the paper via `noo-harvest`.

Read enough of the full source to identify the true technical load-bearing content. Do not assume the core is confined to any original section; novelty may be buried anywhere.

Do not keep searching once `noo-harvest` has secured a sufficient source set.

### 3. Extract claim chunks

Break the paper into technical claim chunks.

Think in terms of:

- problems
- assumptions
- definitions
- constructions
- equations
- recurrences
- algorithms
- theorems
- comparisons
- references
- uncertainties

Ignore original section boundaries.

### 4. Run the zero-based survival pass

Assume every chunk dies.

Keep a chunk only if it survives the retention rubric. Delete aggressively.

If two chunks carry the same content, keep the denser or more precise one.

If a chunk is technically important but bloated, rewrite it from scratch into a tighter form rather than preserving its prose.

### 5. Write one dense internal draft

Before splitting into `core` and `appendix`, mentally write one dense artifact containing everything that survived.

Treat this as the true payload.

Do not let the existence of an appendix relax the retention bar.

### 6. Split the artifact into `core` and `appendix`

Move supporting matter out of the core first:

- proofs
- derivations
- nontrivial tables
- secondary comparisons
- references
- extraction uncertainties

Keep the core as the fast path through the paper.

Keep the appendix as support, not residue.

Write the output pair before any optional cleanup of temporary fetch artifacts.

### 7. Run a second crushing pass

After splitting, crush both files again.

Ask of every remaining line:

- does this line still earn its existence
- does it belong in the smaller of the two files that can honestly carry it
- can two lines become one without loss
- is this support actually support, or just slop that escaped the first pass

Delete again.

### 8. Verify the node

Verify:

- the slug is stable and normalized
- exactly two files exist
- frontmatter is present in both
- `Read When` is 2-3 sentences
- the abstract is crushed, not copied by reflex
- the core points to appendix anchors where needed
- the appendix contains no bibliography dump and no proof landfill
- nothing survives merely because it appeared in the source

## Hard Prohibitions

- Do not preserve original section headings as a matter of respect.
- Do not output a cold cut from frontmatter into theorem soup; keep a routing surface and abstract.
- Do not preserve narrative cadence, motivational prose, or conclusion prose.
- Do not dump copied PDF text into either file.
- Do not keep the same content in both `core` and `appendix`.
- Do not let the appendix become a trash can.
- Do not emit giant markdown tables.
- Do not fabricate missing numeric values, formal claims, or derivation details.
- Do not pretend confidence when extraction is compromised.
- Do not merge separate papers into one node unless explicitly asked.

## Failure Handling

If the source cannot be fetched, is paywalled beyond reach, or is too corrupted to read reliably:

- create no fake node
- report the failure plainly
- preserve any resolved metadata only if it is useful for a retry
- state the uncertainty rather than hallucinating substance

If parts of the source are readable but important evidence is compromised, write the node and record the problem in `Extraction Uncertainties`.

Precision outranks smoothness. Density outranks friendliness. Survival must be earned line by line.
