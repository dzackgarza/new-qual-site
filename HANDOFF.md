---
schema: handoff@3
generated_at: 2026-08-01T20:43:04+08:00
repository: new-qual-site
status: project-in-progress
overall_plan: .hermes/plans/features/FEATURE-QUAL-CORPUS/plans/PLAN-QUAL-BUILDPIPE-001/PLAN-QUAL-BUILDPIPE-001.md
---

# Handoff: qualifying-exam mathematical wiki

## Actual objective

Turn the existing authored mathematics into a subject-organized, Stacks-like
qualifying-exam wiki. Most of the mathematics is already written. The substantive
work is organizing it into readable dependency-ordered branches, composing connective
prose, integrating problems with the theory, and preserving stable identities,
provenance, relations, search, and the existing make-me-a-qual behavior.

PDF transcription and OCR review are one source-ingestion workstream. They are not
the project objective and are not the finish line.

The governing plan is
.hermes/plans/features/FEATURE-QUAL-CORPUS/plans/PLAN-QUAL-BUILDPIPE-001/PLAN-QUAL-BUILDPIPE-001.md.

## What is already complete

The first real vertical slice is implemented and production-proven:

Algebra -> Finite Groups -> Actions and Counting -> Sylow Theory ->
Applications and Problems

The durable proof is artifacts/issue-17/build-proof.md. It records:

- the five browser-visible guide routes and their reading order;
- coherent subject prose, breadcrumbs, sidebar navigation, cards, problems,
  hints, solutions, relations, backlinks, and typed Page/Card/Problem search;
- equality between the generator's problem IDs and the SQLite problem catalog;
- a 5,218-card build producing 3,480 HTML pages;
- 25 manually inspected browser states at 375, 768, 1024, and 1440 pixels;
- successful production deployment and replay with no console/page errors or
  horizontal overflow.

That proof explicitly does not claim that the rest of the authored corpus has been
organized or editorially completed. Issue #21's Node 20 Actions warning is a
non-blocking operational follow-up.

## Current state

The current worktree contains subsequent source/card reconciliation work on top of
the proven slice. It is dirty and must be preserved; no clean-release claim applies
to the current worktree.

The current PDF slice is only a subset:

- corpus/ws9 contains 618 P-card files; this is not the project's full card catalog.
  (`find corpus/ws9 -name 'P-*.md' | wc -l` -> 618. The 5,218 figure this line used to
  quote is the count at the issue-17 build proof, not the current catalog: see the
  Measured state section below.)
- sources/attachment-extraction-ledger.jsonl contains 49 PDF rows and 70 pages.
  Its 416 unique problem IDs are not a complete corpus count.
- MinerU was used through /home/dzack/zotero-library/lib/extraction_loop.py.
  Provider Markdown is a draft lead; rendered PDF pages are authoritative.
- A direct Mistral upload returned 401 Unauthorized. Do not substitute pdftotext
  or another mathematical-PDF fallback.
- Temporary provider artifacts under /tmp are disposable and are not the durable
  project state.

## Measured state (2026-08-10)

Every figure below was measured with the command beside it, in this working tree.
Re-run them rather than trusting this section.

| Fact | Command | Value |
|---|---|---|
| corpus card files | `find corpus -name '*.md' \| wc -l` | 6,906 |
| tracked wiki pages | `find wiki -name '*.md' \| wc -l` | 403 |
| cards from qual-review-and-solutions | `find corpus/qrs -name '*.md' \| wc -l` | 830 |
| make-me-a-qual reconciliation rows | `wc -l < sources/mmaq-reconciliation.jsonl` | 508 |
| ws9 P-cards | `find corpus/ws9 -name 'P-*.md' \| wc -l` | 618 |
| attachment ledger | `wc -l < sources/attachment-extraction-ledger.jsonl` | 49 rows |

The 5,218-card / 3,480-page figures in the build proof above describe the revision that
proof was taken at. They are not the current catalog.

Three obligations that earlier records carried as outstanding have landed, and reading
them as outstanding mis-orders the work:

- **The `[[TAG]]` resolver and the asset catalog are implemented.**
  `rg -n 'parse_pages|resolve_links|build_asset_catalog' tools/qualc/cli.py` shows the
  compiler parsing `wiki/`, building the asset catalog, and resolving links; all 3,644
  card-shaped `[[TAG]]` references in `wiki/` (2,876 distinct) resolve to a corpus card
  id, none unresolved. Implemented is not complete: the acceptance for issue #23 is 403
  pages in / 403 routes out plus browser inspection, which needs `uv run qualc build`.
- **qual-wiki markdown ingestion is finished.** All 271 qual-wiki markdown files carry a
  disposition in `sources/migration-ledger.jsonl` and none is `queued` (260 migrated, 8
  generated, 3 dropped). What remains for that source is expository factoring, not
  extraction.
- **The make-me-a-qual join is a complete 508-row reconciliation**, rows 1-508 with no gap
  or duplicate. Its 104 `ambiguous-exact` near matches are recorded but not adjudicated.

**Reported but not verified here:** `uv run qualc check` exits 0 and reports 6,906 cards
and 403 wiki pages. The two file counts above corroborate the figures; the exit status is
unverified because the command takes about four minutes and another process held the tree.
Running `uv run qualc check` settles it.

The grunt-work slice of the remaining corpus obligations is planned in
`.hermes/plans/features/FEATURE-QUAL-CORPUS/plans/PLAN-QUAL-VENDOR-001/plans/PLAN-QUAL-GRUNT-001/PLAN-QUAL-GRUNT-001.md`.
That plan does not replace the completion contract below; it feeds it.

The source-backed corrections already made in this local slice include the Day 9
topology quotient and S^1 statements, T08A3's closed-image conclusion, malformed
math delimiters, omitted symbols, the x >= 0 condition, the (a,b] interval, and
the separable spelling correction. Preserve those edits while resuming the larger
wiki work.

## Work required to finish the project

### 1. Build the next real subject branch

Choose the next subject branch from the authored corpus, then define one continuous
reader route: prerequisites -> exposition -> results/proofs -> examples ->
applications/problems. Do not begin with a ledger cleanup, bulk OCR pass, test
count, or taxonomy exercise.

### 2. Organize existing material

Reuse authored prose and canonical cards. Add only the connective prose needed for a
coherent page. Place problems and exercises where they support the mathematics.
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
6. Record source page, locator, disposition, and any blocker in the owning durable
   source record.

Unreadable or genuinely ambiguous source text is a blocker, not an invitation to
invent a statement. A PDF row marked extracted is not semantic completion.

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

Extend the demonstrated organization subject by subject. Track each branch by its
reader-visible route and proof artifact. Do not substitute a lower bar such as
“all PDFs extracted,” “all cards indexed,” “metadata reconciled,” or “tests pass.”

## Project completion contract

The project is complete only when:

- the authored corpus reads as a navigable subject/dependency-ordered wiki;
- the required subject branches have real connective prose and integrated problems;
- stable cards, historical occurrences, relations, search, and backlinks remain
  correct;
- the existing make-me-a-qual behavior uses the same canonical problem collection;
- each completed branch has browser evidence at its real route;
- the final build, generated-site integrity, and deployment proof cover the current
  revision, not merely the earlier finite-groups slice;
- intended changes are reviewed, committed, synchronized, and documented.

## Immediate resume sequence

1. Read the governing plan and artifacts/issue-17/build-proof.md.
2. Inspect the current diff and identify the next user-visible subject branch.
3. Implement that branch end to end, using PDF extraction only for source gaps it
   actually encounters.
4. Reproduce the real browser traversal and record the branch proof.
5. Continue branch by branch; only after substantive coverage is complete perform
   final build, deployment, cleanup, and commit handoff.

Until that sequence reaches the project completion contract, report the state as
project-in-progress. Do not report the PDF subtask as the project finish line.
