---
name: haussmann
description: Perform a zero-based Rust source-tree audit and reorganization pass. Use when Codex needs to fix incoherent module layout, thin or bloated subtrees, misplaced files, weak crate boundaries, or scattered shared support code by planning a target tree and executing disciplined path surgery rather than ad hoc moves.
---

# Haussmann

Read the target repo's `AGENTS.md` first if it exists.

Rust only. This skill is about source layout, module topology, and path ownership. It is not the general abstraction-refactor skill.

## Contract

- Require a concrete Rust subtree, crate, or crate set.
- Default to `audit_plus_refactor` unless the user clearly wants findings only.
- Inventory every directory, every `Cargo.toml`, and every `*.rs` file in scope.
- Do not deep-read every file. File reorg is structural work first.
- Create one persistent `/tmp` worklog before the first deep read. Chat is summary only; the worklog is the durable source of truth.
- Run a cheap whole-tree symbol sweep before planning moves.
- Partition the tree into intentional logical cliques before deep reading.
- Write a `/tmp` checkpoint after every wave before reading more files.
- Do not move code until the target tree and move map both exist.
- Force one final path decision for every file and directory in scope.
- Restrict any edits to serve the reorg: module declarations, imports, reexports, etc. No business logic changes are in scope.
- Create domain-scoped support modules when repeated subtree-local operations clearly want a shared home.

## Layout Smells

Actively look for:

- gigafiles: monoliths that ought to be broken up into a tree
- thin subtrees: directories with one meaningful child and no real boundary
- false depth: extra nesting with no conceptual payload
- conceptually void support sinks: ownerless `util`, `common`, `helpers`, `misc`
- suppressed shared support: obvious repeated subtree-local helper logic left scattered
- thin helper diffusion: many sibling files each carrying one tiny support routine for the same owner
- split domains: one concept scattered across unrelated peers
- buried core: central domain code hidden under historical or mechanical paths
- top-level noise: low-value implementation detail promoted to root visibility
- temporal naming: `old`, `new`, `tmp`, `v2`, `legacy`
- cross-crate leakage: code living in a crate or subtree that does not own the concept

## Flow

### 0. Create the worklog

Create a path shaped like:

```text
/tmp/haussmann-<repo-or-dir>-<subtree-slug>.md
```

Seed it with the embedded worklog skeleton from `Embedded Forms`.

### 1. Lock scope and inventory

Enumerate the full tree before making any move plan.

Use fast discovery, for example:

```bash
find <subtree> -type d | sort
rg --files <subtree> -g '*.rs' -g 'Cargo.toml'
```

Persist both manifests into the worklog immediately.

Every file row must eventually receive one final path decision.
Every directory row must eventually be justified or removed.

### 2. Run a structural pass before content reads

Do not start by reading source files linearly.

First inspect structure only:

- current directory tree
- crate boundaries
- `lib.rs`, `main.rs`, `mod.rs`
- package and crate names
- obvious test, bench, example, and support directories
- obvious naming pathologies
- obvious thin or bloated subtrees

Record structural hotspots in the worklog.

### 3. Run a cheap whole-tree symbol sweep

Sweep all Rust files cheaply. Do not deep-read them yet.

Collect signals like:

- file stems
- module roots
- top-level `fn`, `struct`, `enum`, `trait`, and `type` names
- repeated helper-name families
- repeated operation families across sibling files
- tiny files that appear to be support fragments for the same owner concept

The point is to spot likely shared-support candidates without turning the task into a read-every-file slog.

### 4. Plan logical cliques

Group ambiguous or related paths into small logical cliques before deep reading.

Good clique causes:

- one suspected thin subtree chain
- one conceptually void support directory and its likely rightful homes
- one domain split across multiple peers
- one public API surface plus its internal implementation subtree
- one crate-boundary question
- one repeated helper family revealed by the symbol sweep
- one likely shared-support extraction under a clear parent domain

Cliques may overlap. Keep deep-read waves to 2-8 files.

### 5. Run bounded deep-read waves

Deep-read only what is needed to resolve ownership and boundary questions.

For each wave:

- read at most 8 files
- prefer module roots, public entrypoints, move candidates, and shared-support candidates
- use `rust_analyzer` aggressively for references, definitions, rename feasibility, and boundary tracing
- prefer live use sites over declaration-first wandering
- update the worklog before reading more files

Not every file needs deep reading.
Every ambiguous move candidate and every flagged shared-support candidate does.

### 6. Write the target tree before moving anything

After structural coverage and targeted deep reads, write the desired tree shape first.

For every kept directory, state its owning concept in one short line.
If you cannot state the owner, the directory probably should not exist.

The target tree must answer:

- what belongs at the root
- which directories are real domain boundaries
- which directories are clutter and should die
- where each source file should live
- which crate or subtree owns each concept
- where shared support should live, if it should exist at all

### 7. Populate the move map

Use one row per file or directory that matters.

If the same support operation appears in 3+ files under a clear owner subtree, either extract a support module or record an explicit rejection reason.

### 8. Execute mechanical tree surgery

Only after the move map exists:

- create target directories
- move and rename files
- repair `mod` declarations
- repair `pub use` surfaces
- repair imports and path references
- repair manifest paths and test references
- extract small shared support modules when the move map called for them
- remove empty directories and dead wrapper modules

Do not perform broad semantic redesign under cover of layout work.
If a file obviously wants splitting or abstraction cleanup beyond layout-serving edits, record it as follow-on work.

### 9. Verify

After moves:

- run the narrowest valid `cargo check` or `cargo test` surface first
- widen if needed
- search for stale module paths and imports
- scan for empty directories
- scan for newly created thin subtrees
- update the residual sweep

The residual sweep must answer:

- what moved
- what stayed and why
- what shared support was extracted
- what blockers remain
- what semantic follow-on work is now exposed

## Embedded Forms

### Worklog Skeleton

```text
worklog_path:
scope_root:
inspection_mode: audit_only | audit_plus_refactor
wave_size_limit: 8

directory_manifest:
file_manifest:
structural_hotspots:
symbol_sweep:
clique_plan:
wave_checkpoints:
target_tree:
move_map:
blocker_register:
residual_sweep:
```

Rules:

- create this file before the first deep read
- update it after every 8-file wave before reading more files
- treat it as the durable source of truth for the run
- report the final worklog path in the user-facing response

### Wave Checkpoint

```text
clique_id:
purpose:
files_read:
ownership_hypotheses:
move_candidates:
shared_support_candidates:
blockers:
likely_rereads:
```

Rules:

- checkpoint every deep-read wave
- do not read a 9th file before writing the checkpoint
- keep checkpoints concrete and structural
- a file may appear in multiple cliques when ownership or support extraction reasoning demands it

### Move Map

```text
| kind | current_path | owner_concept | action | target_path | reason | required_rewrites |
|------|--------------|---------------|--------|-------------|--------|-------------------|
| dir  | src/common | none_stable | flatten_dir | src/ | thin directory with no boundary value | mod paths, imports |
| file | src/util/id.rs | identity | move | src/identity/id.rs | domain file buried in ownerless support path | mod decls, uses, tests |
| dir  | src/mip | mip | keep_path | src/mip | real domain owner | |
| file | src/mip/node_bounds.rs | mip_support | move | src/mip/bounds.rs | repeated subtree-local bounds operations want one home | imports, tests |
| file | src/http/client.rs | transport_client | keep_path | src/http/client.rs | stable boundary already in the right place | |
```

Allowed `action` values:

- `keep_path`
- `rename`
- `move`
- `flatten_dir`
- `split_dir`
- `merge_dir_then_remove`
- `extract_support_module`
- `extract_subtree`
- `flag_blocker`

Rules:

- every file in scope must end in exactly one final path decision
- every directory in scope must be justified or removed
- `flag_blocker` is only for genuine ambiguity where a wrong move would distort a public surface or crate boundary
- do not hide indecision in vague prose; put it in the move map

## Final Response

Always include:

- the `/tmp` worklog path
- inventory coverage summary
- structural hotspot summary
- target-tree summary
- move-map summary
- verification summary
- residual blockers or follow-on work

If you edited code, also include:

- directories removed
- files moved or renamed
- support modules created or consolidated
- public-surface changes, if any

## Hard Failure Modes

- do not turn file reorg into a read-every-file exercise
- do not start with random deep reads before inventory and symbol sweep
- do not preserve a directory that cannot state an owning concept
- do not create a subtree with one file unless the boundary is already real
- do not leave obvious subtree-local duplication scattered merely to avoid creating a shared support module
- do not perform broad semantic rewrites under the banner of reorg
- do not leave path decisions implicit or unrecorded
- do not preserve temporal names like `old`, `new`, or `v2` by inertia
- do not guess on crate-boundary blockers; flag them explicitly
- do not stop after moves without verification
