---
name: noo-harvest
description: Resolve academic and academic-ish inputs into validated open-access source sets. Use when Codex must turn a URL, DOI, arXiv ID, PMCID, OpenReview note, ACL/PMLR paper link, or similarly messy scholarly input into a stable paper identity, a direct downloadable full-text artifact if one is legally open, and a compact manifest that downstream tools can trust.
---

# Noo-Harvest

Acquire the paper. Do not summarize it. Do not interpret it. Do not crush it into prose. This skill exists to resolve identity, obtain the best open full-text artifact available, and record exactly how that happened.

Treat hostile publisher landing pages as obstacles, not as the center of the workflow. Prefer identifier-oriented metadata surfaces, venue-native PDF paths, and open-access locators over browser theater.

If given multiple inputs, run this exact process independently for each unique paper. Deduplicate obvious duplicates first.

## Contract

- Resolve the paper's stable identity before widening into generic search.
- Prefer direct PDFs, but accept readable full HTML when no open PDF exists.
- Produce a compact acquisition node that downstream work can consume without repeating the fetch logic.
- Stop as soon as a sufficient source set exists.
- If open full text cannot be obtained, fail plainly or emit a metadata-only manifest. Do not fake a PDF and do not pretend a blocked landing page is usable.

## Output Root And Slugs

If the user supplies an output root, use it.

Otherwise:

1. Look for an existing `noo-harvest/` directory in the current project or working directory.
2. If one exists, reuse it.
3. Otherwise create `noo-harvest/`.

Write each unique paper under:

```text
noo-harvest/<paper-slug>/
```

Write:

```text
noo-harvest/<paper-slug>/manifest.yaml
```

Write exactly one primary fetched artifact when acquisition succeeds:

```text
noo-harvest/<paper-slug>/paper.pdf
```

or, if no open PDF exists but readable full HTML does:

```text
noo-harvest/<paper-slug>/paper.html
```

Do not emit both unless the user explicitly asks for multiple retained artifacts.

### Slug Rules

Prefer:

```text
<firstauthor>-<year>-<short-title-stem>
```

Fallbacks:

- `arxiv-<id>`
- `doi-<normalized-id>`
- `pmc-<pmcid>`
- `paper-<domain>-<title-stem>`

Normalize aggressively:

- lowercase ASCII only
- collapse whitespace and punctuation to `-`
- remove duplicate `-`
- trim leading and trailing `-`
- reuse an existing slug for the same paper rather than renaming casually

## Manifest Schema

`manifest.yaml` must be concise and machine-legible.

Populate only fields supported by the evidence you actually resolved.

Use this shape:

```yaml
status: success | metadata_only | failed
slug: <paper-slug>
title: <paper title>
year: <year>
authors:
  - <author>
identifiers:
  doi: <doi or null>
  arxiv: <arxiv id or null>
  pmcid: <pmcid or null>
  pmid: <pmid or null>
  pii: <publisher id or null>
input_urls:
  - <user-supplied url>
canonical_url: <best canonical landing page or null>
chosen_source:
  type: pdf | html | none
  url: <resolved artifact url or null>
  local_path: <paper.pdf | paper.html | null>
  host: <source host or null>
  version: published | accepted | submitted | unknown
  open_license: <license string or unknown>
alternates:
  - url: <candidate url>
    host: <host>
    type: pdf | html | metadata
    reason: <why kept or rejected>
notes:
  - <brief factual note>
sufficient_for_downstream: true | false
```

Keep `notes` short. This is a ledger, not a diary.

## Sufficiency Bar

The source set is sufficient only when it contains all of:

- stable paper identity
- title and authors
- one canonical identifier or landing page
- one readable abstract or equivalent summary surface
- one validated full-text artifact, preferably direct PDF

If you have metadata but not full text, the result is `metadata_only`, not `success`.

## Candidate Preference Order

Prefer candidates in roughly this order:

1. direct open PDF from the canonical publisher
2. direct open PDF from a canonical repository
3. readable full HTML from the canonical publisher
4. readable full HTML from a canonical repository

Break ties by:

- exact identifier match over fuzzy match
- published version over accepted version over submitted version
- explicit open license over unclear license
- stable, non-interstitial URL over redirect mazes
- no-login, no-CAPTCHA access over anything hostile

Disqualify candidates that are:

- login-gated
- CAPTCHA or anti-bot interstitials
- abstract-only when a full-text source is required
- obvious mirror spam or junk indexing pages
- identifier mismatches

## Workflow

### 1. Normalize the input

Classify the input first:

- DOI
- arXiv ID or arXiv URL
- PMCID or PMID
- direct PDF URL
- scholarly landing page URL
- venue-specific URL such as OpenReview, ACL Anthology, or PMLR
- opaque publisher identifier such as a PII embedded in a landing page URL

Extract every stable identifier already present in the input before making network calls.

### 2. Try venue-native resolution first

If the input belongs to a source family with a predictable open path, try that before broader search.

Examples:

- arXiv: canonical `abs` page plus direct `/pdf/<id>.pdf`
- PMC: canonical article page plus OA service
- Europe PMC: hosted full text or external legal full text links
- OpenReview: note metadata plus PDF attachment
- ACL Anthology: canonical paper page plus direct `.pdf`
- PMLR: proceedings page plus direct PDF when obviously derivable

Validate the result rather than assuming the predicted URL works.

### 3. Resolve by identifier-oriented scholarly metadata surfaces

If the venue-native path did not already yield a sufficient source set, query identifier-oriented metadata services in parallel where possible.

Preferred surfaces:

- Unpaywall for DOI-first OA location resolution
- OpenAlex for work identity, OA locations, and cached content
- Crossref for DOI metadata and registered links
- PMC / Europe PMC for biomedical full text
- DOAJ when the journal is fully OA
- Semantic Scholar as a secondary metadata backstop

Use the narrowest exact query available:

- exact DOI
- exact arXiv ID
- exact PMCID or PMID
- exact landing page URL
- exact quoted title
- exact opaque identifier such as a PII

Do not immediately widen to generic search.

### 4. Inspect landing-page metadata only as a supporting move

If the input is a landing page and it is readable, inspect its metadata for:

- DOI
- title
- authors
- canonical URL
- `citation_pdf_url`
- JSON-LD
- license markers

Do not spend unbounded effort rendering or browsing the page. If the page is hostile, treat it as a blocked surface and move on.

### 5. Validate every candidate artifact

Before declaring success, validate the chosen artifact.

For PDFs:

- successful fetch without login or CAPTCHA
- content type plausibly PDF or first bytes begin with `%PDF-`
- file size is sane and not a tiny error page
- identifier, title, or venue evidence matches the resolved paper

For HTML:

- page is readable and not a shell page
- full text is actually present, not just abstract or teaser text
- identifier, title, or venue evidence matches the resolved paper

Do not let a nominal `200 OK` defeat you if the body is just an interstitial.

### 6. Stop early once the bar is met

As soon as the sufficient source set exists:

- choose the best primary artifact
- record alternates tersely in the manifest
- fetch and save the primary artifact
- stop

Do not keep shopping for a marginally prettier PDF.

### 7. Controlled widening

Only if identifier-oriented resolution failed, widen the search in a tightly bounded way.

Use at most a few exact or near-exact probes such as:

- quoted DOI
- quoted full title
- quoted opaque identifier such as a PII
- title plus first author

The purpose is to recover identity or a canonical mirror, not to wander the web.

If those probes fail to produce a validated full-text candidate, stop and emit `metadata_only` or `failed`.

## Hard Prohibitions

- Do not browse aimlessly through hostile landing pages.
- Do not let generic search become the primary workflow.
- Do not keep multiple duplicate artifacts by default.
- Do not keep broken HTML shells, CAPTCHA pages, or abstract-only pages as if they were full text.
- Do not infer a PDF URL without validating it.
- Do not record a candidate as open merely because a metadata service mentions it.
- Do not fabricate titles, authors, identifiers, or licenses.
- Do not write `paper.pdf` when the fetched file is not actually a PDF.

## Failure Handling

If the paper appears notionally open but you still cannot obtain a validated full-text artifact:

- write `manifest.yaml`
- set `status: metadata_only` if identity was resolved, otherwise `failed`
- set `sufficient_for_downstream: false`
- record the precise blockage in `notes`
- do not emit `paper.pdf` or `paper.html`

Examples of honest blockage notes:

- `publisher landing page returned CAPTCHA and no alternate OA source validated`
- `DOI resolved, but all candidate full-text links were login-gated or broken`
- `title and authors resolved from metadata, but no legal full-text artifact found`

## Success Criterion

This skill succeeds when a downstream agent can begin reading without re-solving identity, re-locating the artifact, or re-checking whether the chosen source is actually open and usable.

## Local OCR And Verification

For local reading preparation after acquisition, use the scripted phase-1 plus phase-2 pipeline.

Preferred entrypoint:

```text
scripts/paper_prepare.py <input-pdf> <output-dir>
```

This writes:

```text
<output-dir>/extracted/document.blocks.json
<output-dir>/extracted/document.md
<output-dir>/verified/document.verified.md
<output-dir>/verified/verification.report.json
```

Operational notes:

- `paper_prepare.py` is the supported wrapper; do not manually stitch the phases together unless debugging.
- `--extract-only` runs OCR and block extraction without Codex verification.
- `--verify-only` resumes from an existing `extracted/document.blocks.json`.
- `--pages` restricts both phases to a bounded page slice for trials.
- `--ocr-python` or `NOO_HARVEST_OCR_PYTHON` can force the OCR runtime interpreter.
- `--model-path` can force the local DeepSeek-OCR-2 snapshot.

Phase breakdown:

- `scripts/paper_ocr.py`: deterministic extraction; emits a block ledger plus formula-crop OCR.
- `scripts/paper_verify.py`: Codex-driven verification; reuses one non-interactive thread across pages, operates on the block ledger, and writes faithful markdown plus a structured verification report.

Verification contract:

- preserve wording, notation, and equations unless OCR is plainly broken
- drop only obvious boilerplate, empty garbage, or unusable table sludge
- keep unresolved page-boundary continuations in verifier state instead of duplicating them in output
- force spawned Codex turns out of fast mode
- retry a failed page-verification turn at most once, with explicit validation feedback and allowed block ids
- persist explicit verifier failure state in `verification.report.json` instead of failing silently
