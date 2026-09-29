# Outstanding work

## Execution DAG

A prerequisite `A` on task `B` means `A -> B`. `none` denotes a ready root.
Before committing a dependency change, verify unique IDs, resolved references, and absence of cycles.
Preserve the complete mathematical obligation.

Completed historical queues are not executable work.
Their detailed per-item evidence remains in Git history; this file keeps only the closure facts needed to understand the live DAG. For an additional selected repair, use its issue or card ID, name its immediate Needs and acceptance beside the existing item, and link its complaint.

Read [CONTRIBUTING.md](CONTRIBUTING.md#named-policies) and record issues as they arise in [COMPLAINTS.md](COMPLAINTS.md).

### Current route

`publication-milestone` is **closed** (2026-09-17, `0c2a0b3ff`). Its source-intake, correctness, tooling, adjudication, migration, and complaint-remediation prerequisites are also closed and are not executable work unless a concrete later regression reopens their actual owner.

The current milestone is **`audited-deployment`**: a deployed site whose copy is policy-aligned and which survives three consecutive open-ended audits.
Its completed prerequisites include `unsolved-contribution` and `slogans`; the remaining route is `copy-policy-repair`, then the audit rounds.
[Author solutions](#7-author-solutions) waits behind this milestone: solution authorship mutates the prose population the audits are judging.

#### Steward checkpoint — 2026-09-26

This section records the 2026-09-26 wind-down checkpoint. The workstream was subsequently resumed later on 2026-09-26 at `copy-policy-repair`; the closure facts and deployment evidence below remain valid.

- `unsolved-contribution` is complete at `29eebe3b4`: unsolved problems are reachable from navigation and each unsolved card has a prefilled GitHub solution-submission route.
- `slogans` is complete. At this checkpoint every current theorem, proposition, lemma, corollary, and fact card has an authored slogan read against its statement; the schema, badge renderer, suggestion link, and issue form are present. `just check` passes, `just build` passes, and the focused rendered-site slogan tests pass.
- `copy-policy-repair` is **open and not yet semantically completed**. Resume here. Recompute the current reader-facing surface population, then read every in-scope surface against all policy families in [CONTRIBUTING.md](CONTRIBUTING.md#policy-families), including the public copy introduced by `unsolved-contribution` and `slogans`. Repair each actual violation while preserving the mathematics. An inventory, grep result, crawler result, lint count, or audit receipt is only a lead and cannot close this node.
- `audited-deployment` remains blocked on `copy-policy-repair`. The repository owner explicitly approved deploying this parked checkpoint during the 2026-09-26 wind-down; that deployment does **not** close `copy-policy-repair` or start the three required clean audit rounds. When `copy-policy-repair` later closes, deploy that completed revision and begin the required three consecutive clean open-ended audits against one stamped deployed revision; any finding is injected into this DAG and resets the count.
- Author-solution selection remains blocked on `audited-deployment`; do not resume section 7 before that dependency closes.

A cold resume starts at **`copy-policy-repair`**, not at slogans, solution authorship, or an audit round. The checkpoint deployment was only a handoff verification of that source state; the live workstream has now resumed from this point.

- **`site-renderability-repair`**. **Closed:** 2026-09-25 (`99a19db5e`, `884078a10`, `540665817`). **Needs:** none.
  At discovery, the corpus build stopped before site emission on authored math that used undefined notation aliases or had unterminated display-math delimiters in 16 problem cards (`\pr`, `\Specm`, `\ev`, `\Span`, `\mfn`, `\isom`, `\End`, `\Supp`, `\dashmapsto`, and three missing closing `\]` delimiters).
  Normalize each occurrence to the repository's existing notation or ordinary MathJax-supported TeX; do not add duplicate aliases merely to preserve accidental spellings.
  **Acceptance:** `uv run qualc build` exits successfully from the current corpus with no unrenderable-TeX diagnostic.

- **`unsolved-contribution`**. **Closed:** 2026-09-25 (`29eebe3b4`). **Needs:** `site-renderability-repair`. Make unsolved problems a first-class destination in the site: a reader can reach them from the main navigation and browse or filter them the way the problem index already allows.
  Every unsolved card offers a way to submit a solution as a GitHub issue on this repository, through an issue form under `.github/ISSUE_TEMPLATE/` whose link prepopulates the card ID, title, source appearance, and card URL, so a submission names exactly the card it answers.
  [formalization-corpus](https://github.com/dzackgarza/formalization-corpus) already does this for source leads (`site/contribute.html` linking `issues/new?template=source-lead.yml`); follow that mechanism rather than inventing another.
  **Acceptance:** on a built site, the unsolved view is reachable from navigation and lists exactly the corpus's unsolved cards, and following a card's submission link opens the issue form with that card's fields already filled.

- **`slogans`**. **Closed:** 2026-09-26 (`6269b3aca`). **Needs:** none.
  Give results a slogan in the way the [Stacks project](https://stacks.math.columbia.edu/) does: a short badge attached to a theorem, proposition, lemma, corollary, or fact card that condenses the result into a pithy, memorable mnemonic.
  A slogan is authored card data, validated by `just check` like any other field, and rendered as a badge wherever the result appears.
  It must be true of the result it labels and faithful to its hypotheses; a catchy slogan that overstates the theorem is an incorrect fact.
  Readers can suggest a slogan for a result through the same prefilled GitHub issue-form mechanism `unsolved-contribution` builds.
  **Acceptance:** the slogan field exists in the card schema, renders as a badge on the built site, carries a working suggestion link, and every theorem, proposition, lemma, corollary, and fact card has an authored slogan read against its statement.

- **`copy-policy-repair`**. **Needs:** `policy-consolidation` (closed).
  Read every current reader-facing prose surface against the policies in [CONTRIBUTING.md](CONTRIBUTING.md#policy-families) and rewrite actual violations while preserving the mathematics.
  This includes the copy `unsolved-contribution` and `slogans` add.
  A solution still written with typed `<n>m.` steps violates `STYLE-08`; convert it to the Lamport filter's syntax in the same reading of that card, never as a separate structure-only pass over the corpus.
  When no card holds a typed-step proof, delete qualc's typed-step renderer (`_lamport_*` in `emit.py`) and `normalize_fenced_divs`, and let `qualc check` reject a fence line Pandoc reads as paragraph text.
  Recompute the surface population when this pass is active; inventories and review-crawl candidates are leads, not semantic findings or acceptance evidence.
  **Acceptance:** every in-scope surface has been read against the policies and every violation found in that pass is repaired; no surface is closed by a receipt, inventory, lint count, or audit note.

- **`audited-deployment`**. **Needs:** `unsolved-contribution`, `slogans`, `copy-policy-repair`. Push so `pages.yml` deploys, then audit the deployed site at <https://dzackgarza.github.io/new-qual-site/> in open-ended rounds.
  Each round reads the deployed pages against the [CONTRIBUTING.md](CONTRIBUTING.md#policy-families) policies and checks their mathematics for incorrect facts, statements, and solutions; it is a reading of the site, not a lint or crawl count.
  Every finding becomes a node in this DAG, named by its card or page, with its immediate Needs and acceptance, and `audited-deployment` gains it as a prerequisite.
  A round with any finding resets the count; repair the injected nodes, redeploy, and start again.
  **Acceptance:** three consecutive rounds against the same deployed revision (its stamped commit) find nothing.

### Solutions after the milestone

The solution tasks in [Author solutions](#7-author-solutions) carry stable IDs and immediate **Needs** lists; `select` needs `audited-deployment`. Each instance is keyed by its actual card ID: `select:P-…`, `read:P-…`, `source-review:P-…`, `prove:P-…`, `attach:P-…`, and `commit:P-…`. Names in Needs refer to the same card's instance.

This is a finite DAG for each selected collection's authored card population.
Returning to selection creates an instance for a different card, not a back-edge from commit to the same select node.
Work one card at a time in source order; independent subject streams may work on different cards in the one checkout, on `main`, under [`QUAL-09`](CONTRIBUTING.md#named-policies).
Use the existing collection checklist and card audit/commit evidence, not a second status ledger.

The source-review prerequisite applies when incorporating a source solution; for an original proof it has no source-solution input to review.
Source reading and review of the authored proof remain required in either case.
An unfinished source correction needed by a proof must precede that card's proof.

### Marking a node closed

When a live DAG node meets its acceptance, mark it closed in this file in the same delivery so it cannot be selected again.
Reuse its revision-scoped evidence while the delivered artifact is unchanged; a later regression is repaired at its current owner rather than by replaying the historical node.

### Terminal nodes

These repository-level nodes run only after `publication-milestone` and the solution obligations are closed.
They are finite cleanup work, not a recurring reporting programme.

- **`refactor-audit`**. **Needs:** every substantive queue closed.
  Inspect the tooling and site sources — `tools/`, `site/`, generators, and checkers, not authored mathematics — for concrete defects in ownership, encapsulation, duplicated sources of truth, unnecessary bespoke machinery, and maintainability that affects reliable behavior.
  Repair a defensible finding at its actual owner rather than creating an audit receipt, inventory-only node, or approval stage.
  A genuinely large cross-owner repair may become a concrete DAG node with its real dependencies and behavioral acceptance; the audit itself does not recursively manufacture scheduling nodes.
  **Acceptance:** every finding from the pass has been repaired at its owner, and a final repository-wide pass over the same scope finds no further concrete defect requiring work.
  A later regression is a new owner-local defect; it does not keep this historical audit open forever.

- **`type-paydown`**. **Needs:** `refactor-audit`. Repair the tooling type defects for which stronger typing materially improves legibility, comprehension, or static reasoning about correctness.
  The objective is the resulting program structure, not a diagnostic count.
  Do not add contortions whose only value is silencing a checker.
  **Acceptance:** the type defects selected by the refactor pass have been repaired at their owning interfaces, with behavior preserved and the resulting annotations/interfaces clearer than the state they replace.

- **`bloat-audit-loop`**. **Needs:** `type-paydown`. The identifier is retained for history; the work is finite.
  Make one final whole-tooling/site convergence pass using the relevant lenses already established for this repository: publisher/tool architecture, proof-bearing tests, API and type design, dependency/offload opportunities, duplicated sources of truth, dead compatibility bridges, generated-versus-authored boundaries, build/preview cost, and AI-slop patterns.
  Compare bespoke Markdown parsing/rendering against Pandoc and the existing Markdown toolchain before polishing local machinery that should disappear.
  Inspect representative public behavior; source-text churn is not acceptance evidence.
  Repair each defensible finding at its owner.
  Do not create a complaint, dashboard entry, or DAG node merely to prove that the pass ran.
  **Acceptance:** all findings from the pass are repaired and a final pass across those lenses finds no further defensible change.
  A no-finding pass makes no receipt commit.
  Later regressions are repaired when they occur rather than keeping this node permanently open.

## Issues and queue logs

Live issue state is on [GitHub issues](https://github.com/dzackgarza/new-qual-site/issues); queue state is in [`queues/README.md`](queues/README.md).
Do not mirror either here.

* * *

Work through this queue one item at a time.
Read the source mathematics before each change.
Commit each completed item before starting the next item.

`BACKLOG.md` supplies measured candidates.
A candidate leaves that queue only after a source-based disposition.

## 1. Repair authored corpus data

Closed.
The collection-membership audit was completed.
Historical per-collection findings and repair commits remain in Git history; empty audit commits and separate queue-receipt commits are not part of the current workflow.
## 2. Complete source documents and collection membership

Closed.
Source-document completion and collection membership were reconciled under the repository source-fidelity rules.
Historical per-source evidence remains in Git history.
## 3. Reconcile imported sources

Closed.
Imported-source reconciliation is complete; later source defects are repaired at their current owner rather than reopening this historical queue.
## 4. Finish publication behavior

Closed.
Publication behavior and its repository-owned acceptance were delivered; later rendering regressions are owner-local defects.
## 5. Complete source-preservation closeout

Closed.
Source-preservation closeout is complete under the current provenance and source-owner contracts.
## 6. Resolve remaining owner decisions

Closed.
The recorded owner decisions were resolved; current owner decisions belong to the live issue/card that requires them.
## 7. Author solutions

Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2)

- [ ] **`select`**. **Needs:** `audited-deployment`. Select one unsolved card.

- [ ] **`read`**. **Needs:** `select`. Read the problem and its source.

- [ ] **`prove`**. **Needs:** `read`, `source-review`. Write a complete Lamport-style structured proof.

- [ ] **`attach`**. **Needs:** `prove`. Add a `solution` section to the card.

- [ ] **`source-review`**. **Needs:** `read`. Integrate a source solution only after independent mathematical review.

- [ ] **`commit`**. **Needs:** `attach`. Review the complete authored proof and commit the completed solution before selecting another card.

## 8. Close the roadmap

Closed.
The publication roadmap and satisfied issues were closed; issue #2 remains open only for the live solution programme in section 7.
## 9. Repair site information architecture

Closed.
The site information-architecture repairs were delivered.
Later navigation defects are repaired at their current renderer/content owner.
## 10. Repair wiki copy and organization

Closed.
The historical wiki-copy and organization repairs were delivered.
The separate corpus-wide `copy-policy-repair` node in the execution DAG remains the current presentation-convergence obligation.
## 11. Author the wiki as a study guide

Closed.
The historical study-guide authoring programme was delivered; further authored mathematics is selected through the current corpus/solution owners, not this closed queue.
## 12. Close out the branch consolidation

Closed.
Branch consolidation and its mathematical adjudication obligations were completed; later regressions are repaired at the current owner.
