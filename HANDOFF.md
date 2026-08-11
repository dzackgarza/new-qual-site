---
schema: handoff@3
generated_at: 2026-08-01T20:43:04+08:00
repository: new-qual-site
status: project-in-progress
overall_plan: .hermes/plans/features/FEATURE-QUAL-CORPUS/plans/PLAN-QUAL-BUILDPIPE-001/PLAN-QUAL-BUILDPIPE-001.md
---

# Handoff: qualifying-exam mathematical wiki

## Actual objective

Turn the existing authored mathematics into a subject-organized, Stacks-like qualifying-exam wiki.
Most of the mathematics is already written.
The substantive work is organizing it into readable dependency-ordered branches, composing connective prose, integrating problems with the theory, and preserving stable identities, provenance, relations, search, and the existing make-me-a-qual behavior.

PDF transcription and OCR review are one source-ingestion workstream.
They are not the project objective and are not the finish line.

The governing plan is .hermes/plans/features/FEATURE-QUAL-CORPUS/plans/PLAN-QUAL-BUILDPIPE-001/PLAN-QUAL-BUILDPIPE-001.md.

## What is already complete

The first real vertical slice is implemented and production-proven:

Algebra -> Finite Groups -> Actions and Counting -> Sylow Theory -> Applications and Problems

The durable proof is artifacts/issue-17/build-proof.md.
It records:

- the five browser-visible guide routes and their reading order;

- coherent subject prose, breadcrumbs, sidebar navigation, cards, problems, hints, solutions, relations, backlinks, and typed Page/Card/Problem search;

- equality between the generator’s problem IDs and the SQLite problem catalog;

- a 5,218-card build producing 3,480 HTML pages;

- 25 manually inspected browser states at 375, 768, 1024, and 1440 pixels;

- successful production deployment and replay with no console/page errors or horizontal overflow.

That proof explicitly does not claim that the rest of the authored corpus has been organized or editorially completed.
Issue #21’s Node 20 Actions warning is a non-blocking operational follow-up.

## Current state

The current worktree contains subsequent source/card reconciliation work on top of the proven slice.
It is dirty and must be preserved; no clean-release claim applies to the current worktree.

The current PDF slice is only a subset:

- corpus/ws9 contains 618 P-card files; this is not the project’s full card catalog.
  (`find corpus/ws9 -name 'P-*.md' | wc -l` -> 618. The 5,218 figure this line used to quote is the count at the issue-17 build proof, not the current catalog: see the Measured state section below.)

- sources/attachment-extraction-ledger.jsonl contains 49 PDF rows and 70 pages.
  Its 416 unique problem IDs are not a complete corpus count.

- MinerU was used through /home/dzack/zotero-library/lib/extraction_loop.py.
  Provider Markdown is a draft lead; rendered PDF pages are authoritative.

- A direct Mistral upload returned 401 Unauthorized.
  Do not substitute pdftotext or another mathematical-PDF fallback.

- Temporary provider artifacts under /tmp are disposable and are not the durable project state.

## Measured state (2026-08-10)

Every figure below was measured with the command beside it, in this working tree.
Re-run them rather than trusting this section.

| Fact | Command | Value |
| --- | --- | --- |
| corpus card files | `find corpus -name '*.md' \| wc -l` | 6,906 |
| tracked wiki pages | `find wiki -name '*.md' \| wc -l` | 403 |
| cards from qual-review-and-solutions | `find corpus/qrs -name '*.md' \| wc -l` | 830 |
| make-me-a-qual reconciliation rows | `wc -l < sources/mmaq-reconciliation.jsonl` | 508 |
| ws9 P-cards | `find corpus/ws9 -name 'P-*.md' \| wc -l` | 618 |
| attachment ledger | `wc -l < sources/attachment-extraction-ledger.jsonl` | 49 rows |

The 5,218-card / 3,480-page figures in the build proof above describe the revision that proof was taken at.
They are not the current catalog.

Three obligations that earlier records carried as outstanding have landed, and reading them as outstanding mis-orders the work:

- **The `[[TAG]]` resolver and the asset catalog are implemented.** `rg -n 'parse_pages|resolve_links|build_asset_catalog' tools/qualc/cli.py` shows the compiler parsing `wiki/`, building the asset catalog, and resolving links; all 3,644 card-shaped `[[TAG]]` references in `wiki/` (2,876 distinct) resolve to a corpus card id, none unresolved.
  Implemented is not complete: the acceptance for issue #23 is 403 pages in / 403 routes out plus browser inspection, which needs `uv run qualc build`.

- **qual-wiki markdown ingestion is finished.** All 271 qual-wiki markdown files carry a disposition in `sources/migration-ledger.jsonl` and none is `queued` (260 migrated, 8 generated, 3 dropped).
  What remains for that source is expository factoring, not extraction.

- **The make-me-a-qual join is a complete 508-row reconciliation**, rows 1-508 with no gap or duplicate.
  Its 104 `ambiguous-exact` near matches are recorded but not adjudicated.

**Reported but not verified here:** `uv run qualc check` exits 0 and reports 6,906 cards and 403 wiki pages.
The two file counts above corroborate the figures; the exit status is unverified because the command takes about four minutes and another process held the tree.
Running `uv run qualc check` settles it.

The grunt-work slice of the remaining corpus obligations is planned in `.hermes/plans/features/FEATURE-QUAL-CORPUS/plans/PLAN-QUAL-VENDOR-001/plans/PLAN-QUAL-GRUNT-001/PLAN-QUAL-GRUNT-001.md`. That plan does not replace the completion contract below; it feeds it.

The source-backed corrections already made in this local slice include the Day 9 topology quotient and S^1 statements, T08A3’s closed-image conclusion, malformed math delimiters, omitted symbols, the x >= 0 condition, the (a,b] interval, and the separable spelling correction.
Preserve those edits while resuming the larger wiki work.

## Work required to finish the project

### 1. Build the next real subject branch

Choose the next subject branch from the authored corpus, then define one continuous reader route: prerequisites -> exposition -> results/proofs -> examples -> applications/problems.
Do not begin with a ledger cleanup, bulk OCR pass, test count, or taxonomy exercise.

### 2. Organize existing material

Reuse authored prose and canonical cards.
Add only the connective prose needed for a coherent page.
Place problems and exercises where they support the mathematics.
Keep warnings with the mathematics they qualify.

For every branch, preserve the same contracts already proven in the first slice:

- Pages own exposition and reading order.

- Cards own stable independently linkable mathematical objects.

- Problems retain historical occurrences, institutions, years, and source locators.

- Hints and solutions remain separately addressable and attached to problems.

- Authored relations remain distinct from derived appearances and backlinks.

- The existing make-me-a-qual generator consumes the same canonical problem catalog.

### 3. Use source extraction only where the branch needs it

For a source gap encountered in the chosen branch:

1. Read the owning source ledger and derive the exact document/page/card set.

2. Run MinerU through the canonical extraction loop.

3. Render and inspect the original pages directly.

4. Compare every mathematical symbol and delimiter against the page.

5. Edit only source-proven discrepancies; never promote raw OCR into authored cards.

6. Record source page, locator, disposition, and any blocker in the owning durable source record.

Unreadable or genuinely ambiguous source text is a blocker, not an invitation to invent a statement.
A PDF row marked extracted is not semantic completion.

### 4. Prove the real user-facing branch

After each branch is organized, build the site and inspect the actual browser route:

- sidebar, breadcrumbs, and previous/next navigation;

- readable prose and dependency order;

- standalone card/problem routes;

- collapsed and opened hint/solution states;

- separated authored relations, appearances, and backlinks;

- Page/Card/Problem search;

- generation through the shared make-me-a-qual catalog;

- desktop and mobile layout with typeset mathematics and no console/page errors.

A green build, page count, schema check, or HTTP 200 alone is not proof.

### 5. Repeat until the authored corpus is a navigable wiki

Extend the demonstrated organization subject by subject.
Track each branch by its reader-visible route and proof artifact.
Do not substitute a lower bar such as “all PDFs extracted,” “all cards indexed,” “metadata reconciled,” or “tests pass.”

## Project completion contract

The project is complete only when:

- the authored corpus reads as a navigable subject/dependency-ordered wiki;

- the required subject branches have real connective prose and integrated problems;

- stable cards, historical occurrences, relations, search, and backlinks remain correct;

- the existing make-me-a-qual behavior uses the same canonical problem collection;

- each completed branch has browser evidence at its real route;

- the final build, generated-site integrity, and deployment proof cover the current revision, not merely the earlier finite-groups slice;

- intended changes are reviewed, committed, synchronized, and documented.

## Immediate resume sequence

1. Read the governing plan and artifacts/issue-17/build-proof.md.

2. Inspect the current diff and identify the next user-visible subject branch.

3. Implement that branch end to end, using PDF extraction only for source gaps it actually encounters.

4. Reproduce the real browser traversal and record the branch proof.

5. Continue branch by branch; only after substantive coverage is complete perform final build, deployment, cleanup, and commit handoff.

Until that sequence reaches the project completion contract, report the state as project-in-progress.
Do not report the PDF subtask as the project finish line.

## PLAN-QUAL-GRUNT-001 progress (2026-08-11)

Grunt-work completion run.
Landed and pushed through `7bbb7fe` (15 commits, `pytest` 67 green, `uv run qualc check` -> 7,207 cards and 403 wiki pages OK).

| workstream | state | commit | headline |
| --- | --- | --- | --- |
| G0 unblock the build | done | `77d42ea` | 25 schema errors + duplicate id cleared; 758 WS9 cards landed |
| G1 reconcile records | done | vault `1f7e739`, `d94d478`, `8f835cc` | 5 issues corrected; found M4/M5 never existed |
| G2 mis-dropped markdown | done | `3e9cc6c` | 32 rows adjudicated, 503 cards; 180-exercise chapter recovered |
| G3 duplicates + identity | done | `b1fcfeb` | 628 collapsed, duplicate-bodies 388 groups -> 0 |
| G4 card metadata | done | `394a8ec` | 419 empty areas -> 0 from one unregistered vocab entry |
| G5 heading formats | done | `7bbb7fe` | named scope already complete; 65 problems recovered from swallowed headings |
| G8 CI guards | partial | `64f90a1` | `payload.area` guard, CI test job, 4 invariant tests |
| G10 math-flashcards | done | `1d49862` | 372 cards, fifth source ledgered |
| G6 subject-tree merge | running | — | isolated worktree |
| G7 reachability | done | `e1a4ca6` | 32 pages emitted from recorded order; orphans 3,104 -> 19 documented |
| G9 source hygiene | running | — | non-destructive scope; archiving and token revocation await user approval |

Corpus: 6,907 -> 7,207 cards.
`tools/audit.py`: empty-areas ok, duplicate-bodies ok, ledger-totality ok, reason-truth ok, migrated-evidence ok.
Documented residuals: 1 degenerate title (`P-V33RL`), 10 UGA month-vs-term sittings needing the source.

Open defects found on the way: `dzackgarza/new-qual-site#31` (collapse tool builds its map from HEAD but deletes from the working tree) and `dzackgarza/flowmark#31` (footnote inside a fenced div crashes the formatter, open since 2026-07-24).

Four of the plan's own claims proved stale against the repo and are corrected in its Surprises section rather than silently edited.

## Resume here (2026-08-11, end of the GRUNT-001 run)

`main` = `050954f`, clean, pushed, `origin/main` level.
`uv run qualc check` -> **7,207 cards and 403 wiki pages OK**. `pytest` 67 green.

### Done and durable

G0, G1, G2, G3, G4, G5, G10, and G8's first slice.
11 commits this run (`ca289a8..050954f`). Corpus 6,907 -> 7,207: +503 routed authored markdown, +372 flashcards, +65 recovered from swallowed headings, -628 duplicates collapsed.

`uv run python tools/audit.py` final state:

```
duplicate-bodies   ok
empty-areas        ok
ledger-totality    ok
reason-truth       ok
migrated-evidence  ok
degenerate-titles  1   P-V33RL: title '?'
duplicate-sittings 10  UGA real-analysis month-vs-term pairs
orphans            19  17 recorded duplicates + 1 reconstructed problem and its solution
```

All three residuals are deliberate and documented, not backlog.
The 10 sittings need the source to settle: a month label against a semester label for one lossy derived season.
Two carry positive evidence of being *different* sittings (January/Spring 2014 set different problem 2; January/Spring 2017 different problem 3); `JUNE-2017` vs `MAY-2017` is flagged `unsettled` in `sources/g3-sitting-decisions.jsonl`.

### Not done

- **G6 — subject-tree merge.** Branch `g6-tree-merge` in `.claude/worktrees/g6`, 238 files changed, **uncommitted**. `wiki/` still carries both upstream layouts (numbered `10_Algebra…` and named `Algebra…`). Read that worktree before restarting; do not discard it.

- **G7 — reachability. Done** (`e1a4ca6`, branch `g7-reachability`). Orphans 3,104 -> 19.
  `tools/attach_pages.py` emits 32 pages from ledgers and card fields alone: a Source Archive per subject (273 source cards, institution then date), a page per math-flashcards deck (25, in each deck's own card order), the review doc's Extra Problems chapter (180 cards under its own heading path), and one hub page linked from `wiki/index.md`.
  Routes and their order sources are in `sources/g7-page-attachment.jsonl`; the residual is in `sources/g7-residual.jsonl`.
  Two things to know before changing it: the orphan closure in `tools/audit.py` now includes the source -> occurrence -> problem edge, because `emit.source_page` renders that listing; and 59 headings lost an empty `$$` left by the import's status-macro discard, which had been swallowing card references into display math (`sources/g7-heading-math-residue.jsonl`).

- **G8 remainder.** Guards still owed for queued->migrated without a card, upstream row count vs occurrence count, and reachability.

- **G9 archiving.** Deferred by owner decision: archiving would certify preservation while G7 has not made the preserved material reachable.
  Issue #11 requires a fresh-clone replay before archiving.

### One action for the owner

**Revoke the leaked PAT.** Classic `ghp_` token, 40 chars.
It was in `make-me-a-qual`, `Analysis-Qual-Compendium`, and `qual-review-and-solutions.broken-pack-preserved` -- the same token in all three.
All remotes are now SSH and `grep -rl ghp_ */.git/config` returns 0, so it is off disk, but the token itself is still live until revoked at github.com/settings/tokens.

### State of the source repos

All five worktrees restored: `git ls-files -d` = 0 for `qual-wiki` (was 1,255 missing), `make-me-a-qual` (8), `Analysis-Qual-Compendium` (1), `math-flashcards`, `qual-review-and-solutions`. The last has a working SSH clone with 542 tracked files matching its 542 ledger rows.

`qual-review-and-solutions.broken-pack-preserved` is **unrecoverable and preserved**: `git index-pack` reaches 34,784 of 35,135 objects then `fatal: early EOF`. The pack is truncated.
Nothing depends on it.

### Open defects found during this run

- `dzackgarza/new-qual-site#31` — `collapse_duplicates.py` builds its retired->survivor map from `HEAD` but deletes from the working tree, so any pass that edits card bodies then collapses leaves silent dangling references.
  Cause of both dangling incidents in this run, and because the pre-push gate tests the working tree, each one blocked pushing every other workstream's verified commits.

- `dzackgarza/flowmark#31` — a footnote definition inside a fenced div raises `'CustomFencedDiv' object has no attribute 'footnotes'`, failing the commit gate for the whole repo and naming no file.
  Open since 2026-07-24.

- `dzackgarza/new-qual-site#16` — its premise is contradicted by `tools/migration_ledger.py`; recommended for closure.
  See the comment on the issue.

### Operational note for whoever runs the next batch

Running several workstreams in one working tree was this run's dominant cost.
The commit gate formats and scans `git diff --cached`, so any agent's staged violations block every agent's commit; two gates cannot hold `.git/index.lock` at once; and the pre-push gate tests the working tree, so one agent's in-flight state blocks pushing finished work.
Use one isolated git worktree per workstream.

Also: the plan's own numbers drift.
Four of its factual claims were stale against the repo this run (see its Surprises section).
Measure before trusting any count in it.
