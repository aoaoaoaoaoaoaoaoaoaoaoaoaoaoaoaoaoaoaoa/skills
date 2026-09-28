---
name: ad-fontes
description: Maintain a gitignored repository-local corpus of external papers and reference materials without repeated retrieval or repeated full-source ingestion. Use whenever Codex is about to search for, download, retain, reopen, summarize, or inventory a paper, report, preprint, standard, or similar source. Preserves exact artifacts, neutral same-stem synopses, and a compact local catalogue without committing external evidence to the project.
---

# Ad Fontes

## Mandate

Maintain `references/` as the repository's durable local corpus of evidence. The corpus lives in the worktree for proximity and discovery, but it is not project source and never enters Git's index.

A reference enters the corpus once, as an immutable source artifact, a neutral synopsis, and a catalogue entry. The artifact preserves evidence, the synopsis preserves understanding, and the catalogue preserves discovery.

Read the corpus before the network, and the synopsis before the source. Open the source when the synopsis cannot supply the precision, evidence, or detail the present task requires.

The synopsis states what the source contains, not why a passing task cares about it. Project-specific reliance may be recorded separately, but it never shapes or replaces the neutral account.

## Version-control boundary

Before creating or retrieving any corpus material, ensure that the repository-root `.gitignore` contains the anchored rule `/references/`. Verify it with `git check-ignore`; never defeat it with `git add -f`.

If `references/` is already tracked, remove it from Git's index while preserving the corpus in the working tree, then commit the ignore rule and the index deletion as one migration. Do not commit artifacts, sidecars, digests, or the catalogue. Durable project conclusions belong in project documentation or the relevant external state system, not in a vendored dump of evidence.

## Corpus contract

Store lawfully retainable source material under `references/` with stable, descriptive names such as:

```text
author-year-short-title.pdf
author-year-short-title-v2.pdf
author-year-short-title-journal.pdf
```

Every retained artifact has an adjacent same-stem Markdown sidecar. A source that cannot lawfully be retained may have a metadata-only sidecar that states the absent artifact and the access restriction.

Distinguish the work from the retained artifact. DOI, arXiv identifier, title, and authors identify the work; version, retrieval source, and SHA-256 identify the exact bytes. Never overwrite one artifact with another version: preserve materially distinct versions and state how they relate.

`references/README.md` is the catalogue. Every retained or metadata-only reference appears in it, linked through its sidecar rather than directly to a large artifact.

Source artifacts are immutable. Synopses and the catalogue may improve when inspection reveals a more exact account, a correction, a version relation, or a hazard.

## Assimilation

Before retrieving anything, read the catalogue and search the existing sidecars by title, author, DOI, arXiv identifier, canonical URL, and likely filename. Reuse an existing artifact when it is the required work and version.

When acquisition is necessary, prefer a canonical or author-controlled source. Verify that the retrieved object is the intended document, identify its exact version, compute its SHA-256 digest, and record its provenance and retention status.

Write the sidecar from the source, not from the current task. Its neutral synopsis recovers the work's scope, principal results and their conditions, material methods or constructions, important negative results or limitations, and enough theorem, section, or page anchors to permit targeted reopening. Proportion the detail to the work; do not force a uniform length or narrate every section.

State the basis of the synopsis honestly: full-text inspection, bounded partial inspection, abstract or metadata only, OCR-limited inspection, or another material constraint. A synopsis orients; it is not a proof premise or a citation authority.

Assimilation is complete only when the artifact or its metadata-only status, the sidecar, the digest, and the catalogue entry agree, and the whole corpus is confirmed ignored and absent from Git's index.

## Sidecar form

```markdown
# <author or authors> (<year>): <title>

**Citation.** <full citation>

- Work identity: <DOI, arXiv identifier, or other stable identity>
- Canonical source: <URL>
- Local artifact: <same-stem filename, or none with reason>
- Version and status: <exact version; publication, preprint, withdrawn, etc.>
- Retrieved: <date>
- SHA-256: <digest, or not applicable>
- Access and retention: <known license, distribution basis, or restriction>
- Synopsis basis: <extent and quality of inspection>

## Synopsis

<Neutral, context-efficient account of the work and its major findings.>

## Source Assessment

<Corrections, defects, disputed claims, supersession, related retained versions, and unresolved source-level hazards. State when none are known from the present inspection.>

## Project Use

<Optional. A terse account of durable project reliance required by local policy. Do not restate or distort the synopsis through the current task.>
```

## Catalogue form

Use one compact entry per work, grouping retained versions where that helps orientation:

```markdown
| Work | Status | Pointer |
|------|--------|---------|
| [<author, year, short title>](<sidecar>.md) | <publication/version status> | <one or two neutral sentences identifying the subject, principal result, and any decisive hazard> |
```

Let the corpus decide whether topical sections improve navigation. Do not impose a taxonomy or replace neutral pointers with roles in the current investigation.
