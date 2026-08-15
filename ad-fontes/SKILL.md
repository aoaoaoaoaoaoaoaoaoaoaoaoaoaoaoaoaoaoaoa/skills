---
name: ad-fontes
description: Maintain a gitignored repository-local corpus of external papers and reference materials without repeated retrieval or repeated full-source ingestion. Use whenever Codex is about to search for, download, retain, reopen, summarize, or inventory a paper, report, preprint, standard, or similar source. Preserves exact artifacts, neutral same-stem synopses, and a compact local references index without committing external evidence to the project.
---

# Ad Fontes

## Mandate

Maintain `references/` as the repository's durable local evidentiary corpus. The
corpus inhabits the worktree for proximity and discovery, but it is not project
source and must never enter Git's index.

A reference enters the corpus once as an immutable source artifact, a neutral synopsis, and an index entry. The artifact preserves evidence; the synopsis preserves understanding; the index preserves discovery.

Read the corpus before the network. Read the synopsis before the source. Open the source when the synopsis cannot supply the precision, evidence, or detail the present task requires.

The synopsis states what the source contains, not why one transient campaign happens to care about it. Project-specific reliance may be recorded separately, but it must not determine or substitute for the neutral account.

## Version-Control Boundary

Ensure the repository-root `.gitignore` contains the anchored rule
`/references/` before creating or retrieving any corpus material. Verify the
rule with `git check-ignore`; never defeat it with `git add -f`.

If `references/` is already tracked, remove it from Git's index while preserving
the working-tree corpus, then commit the ignore rule and index deletion as a
coherent migration. Do not commit artifacts, sidecars, digests, or the local
corpus index. Durable project conclusions belong in project documentation or
the relevant external state system, not in a vendored evidence dump.

## Corpus Contract

Store lawfully retainable source material under `references/` with stable, descriptive names such as:

```text
author-year-short-title.pdf
author-year-short-title-v2.pdf
author-year-short-title-journal.pdf
```

Every retained source artifact has an adjacent same-stem Markdown sidecar. A source that cannot lawfully be retained may have a metadata-only sidecar whose absent artifact and access restriction are explicit.

Distinguish the intellectual work from the retained artifact. DOI, arXiv identity, title, and authors identify the work; version, retrieval source, and SHA-256 identify exact bytes. Never overwrite one artifact with another version. Preserve materially distinct versions and state their relation.

`references/README.md` is the local corpus catalogue. Every retained or metadata-only reference appears there. The catalogue links to sidecars rather than directly to large artifacts; “index” in this document never means Git's index.

Source artifacts are immutable. Synopses and the index may improve when inspection reveals a more exact account, correction, version relation, or hazard.

## Assimilation

Before retrieving anything, inspect `references/README.md` and search existing sidecars by title, author, DOI, arXiv identifier, canonical URL, and likely filename. Reuse an existing artifact when it is the required work and version.

When acquisition is necessary, prefer a canonical or author-controlled source. Verify that the retrieved object is the intended document, identify its exact version, compute its SHA-256 digest, and record its provenance and retention status.

Write the sidecar from the source rather than from the current task. Its neutral synopsis must recover the work's scope, principal results and their conditions, material methods or constructions, important negative results or limitations, and enough theorem, section, or page anchors to permit targeted reopening. Proportion detail to the work; do not force uniform length or narrate every section.

State the basis of the synopsis honestly: full-text inspection, bounded partial inspection, abstract or metadata only, OCR-limited inspection, or another material constraint. A synopsis is an orientation surface, not a substitute proof premise or citation authority.

Close assimilation only when the artifact or metadata-only status, sidecar,
digest, and catalogue entry agree and the whole corpus is confirmed ignored and
absent from Git's index.

## Sidecar Form

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

<Corrections, defects, disputed claims, supersession, related retained versions,
and unresolved source-level hazards. State when none are known from the present inspection.>

## Project Use

<Optional. A terse account of durable project reliance required by local policy.
Do not restate or distort the synopsis through the current task.>
```

## Index Form

Use one compact entry per work, grouping retained versions where that improves orientation:

```markdown
| Work | Status | Pointer |
|------|--------|---------|
| [<author, year, short title>](<sidecar>.md) | <publication/version status> | <one or two neutral sentences identifying the subject, principal result, and any decisive hazard> |
```

Let the corpus determine whether topical sections improve navigation. Do not impose a taxonomy or replace neutral pointers with roles in the current investigation.
