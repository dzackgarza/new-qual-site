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

- **`lamport-conversion`**. **Needs:** none.
  A proof written with typed step numbers (`<1>2.`) violates `STYLE-08`. Convert every such proof to the syntax of pandoc-config's `lamport_proof.lua` filter. This is a syntax conversion: no mathematics and no prose changes.
  On 2026-09-29 agents converted 1,808 cards and a one-time script converted 4,579 more. The script refused a card whose structure it could not read unambiguously, and it wrote a card only when every source word survived and the filter accepted the result. On 2026-09-30 agents converted the 449 refused and 96 skipped cards, and no typed step remains; every batch row is `converted`. A word check of those cards against their text before the conversion, and a fence count over the corpus, found lost claims and 220 cards with an unclosed section; both are repaired. Close step 1 is next.

  **Batches.** The batch files `queues/lamport-conversion/batch-00.tsv` through `batch-19.tsv` list every card in path order. A `pending` row's note gives the script's refusal reason; read the card with that reason in mind.
  Each row is `path<TAB>status<TAB>note`. The status is one of:

  | Status | Meaning | Action |
  | --- | --- | --- |
  | `pending` | The card holds typed steps. A note `partly converted; finish it` marks a card that was stopped in the middle of its conversion. | Convert it. |
  | `verify` | The conversion was written but never read back. | Read it back (step 3 below). |
  | `skipped` | An earlier agent found the step structure uncertain. The note gives the reason. | Leave it. A person reads it at close. |
  | `converted` | Done. | None. |

  Give one batch to one Sonnet agent. The agent uses only Read, Edit and Write; it edits only the cards in its batch and its own batch file. It does not run commands, tests, `qualc`, git, builds or formatters, does not commit or push, and does not start other agents.
  Twenty agents at one time hit the server rate limit and made no progress for hours, so run about five at one time and start the next batch when one finishes. An agent that stops continues from the first row of its batch that is still `pending` or `verify`.

  **Before the first card**, the agent reads the `STYLE-08` section of [CONTRIBUTING.md](CONTRIBUTING.md) and the two finished conversions `corpus/collections/SRC-UGA-TOP-FALL-2004/P-QN7OP.md` and `corpus/problems/Algebra/E-AMD-O2OGRSJP.md` (nested substeps). It reads them again after any context compaction.

  **Source layout.** A step is a line that starts with `<k>m.`, possibly indented: `k` is the level and `m` the number inside the level. A step proved directly is followed by a `::: {.proof}` or `::: proof` block. A step proved by substeps is followed by steps one level down. A step can have both. A `Q.E.D.` step closes a level. Prose cites steps as `<1>2`, `step <2>3`, `<1>1.4`, and ranges such as `<1>1--<1>3`.

  **Target layout.**
  - The whole proof becomes one `::: pf` block. Prose before the first step (notation, setup) stays before it, outside the block.
  - Each step becomes `::: pf-step` with its claim as the first paragraph; the `<k>m.` marker is removed.
  - The step's proof block becomes `::: pf-proof` inside the step, after the claim. Substeps go inside that pf-proof, after any proof prose, as nested pf-step blocks. A step with substeps but no proof block gets a pf-proof that holds only the substeps. A step with neither stays a bare pf-step.
  - A `Q.E.D.` step becomes `::: pf-qed`. Its proof prose goes directly inside it, with no pf-proof, unless it has substeps; then it holds a pf-proof with them. Delete the words "Q.E.D.". A Q.E.D. step with no proof prose and no substeps is deleted: the filter labels the last step of each level QED.
  - Never add a pf-qed or any sentence to close a level.
  - A step that another step cites gets an identifier, `::: {.pf-step #s1-2}`: the step's original typed path, unique in the card. The script used this form; a card with several typed proofs prefixes each proof's identifiers with `p1-`, `p2-`, and so on. Replace each typed citation with `[](#s1-2){.pf-ref}`, keeping or adding the word "step"/"steps" before it once. A range becomes the individual citations joined by commas and "and", or "… through …" if the source said "through". Resolve a hierarchical citation such as `<2>3` by reading which step it means. A step nobody cites gets no identifier.
  - The only fence lines are `::: pf`, `::: pf-step`, `::: pf-proof`, `::: pf-qed`, `::: {.pf-step #name}` and the bare closer `:::`. Put a blank line before and after every fence line, openers and closers alike.
  - Remove the hand indentation of step lines and proof bodies. Keep indentation inside display math, lists and code.
  - A `::: pf` block holds only steps. A pf-proof that holds substeps holds only steps, except that it may open with proof prose before its first substep. Anything else between two sibling steps is not allowed there:
    - A sentence that continues a step's proof goes to the end of that step's pf-proof. If that pf-proof holds substeps, the sentence becomes the content of a `::: pf-qed` as the last child of the pf-proof, with its words unchanged. Never move it before the substeps.
    - For a heading or other section-level prose between top-level steps, close the `::: pf` block before it and open a new `::: pf` block after it. Identifiers stay unique across the card, so citations still resolve across blocks.
  - Convert every typed proof in the card: solutions, hints and proofs of theorems. Independent typed proofs in one card (for example, one per part) each become their own `::: pf` block.

  **Preserve.** Every other word and every character of mathematics stays as written: no rewording, typo fixes, reflowing, math changes, deleted prose or added explanation. The only words the agent may add are "step"/"steps"/"and" around citations. Front matter, the problem statement and all other sections stay unchanged. A stray sentence between a proof block's closer and the next step belongs to the preceding step.

  **When not to convert.** If the step structure is not certain from reading (skipped levels, duplicate or out-of-order numbers, markers in the middle of a paragraph that could mean several trees, citations of steps that do not exist), leave the card byte-for-byte unchanged, set its status to `skipped`, and write the reason in the note.

  **Per card.**
  1. Read the card.
  2. Convert it with Edit.
  3. Read it again and confirm that every fence opens and closes, that the nesting matches the original numbering, that every pf-ref names an identifier in the card, and that no prose or mathematics changed.
  4. Set the row's status to `converted` or `skipped` in the batch file, then go to the next row.

  **Commits.** The orchestrator, not the agents, commits the cards whose rows say `converted`, together with their batch files, using `git commit --no-verify --pathspec-from-file=…`. It runs no check or build between commits.

  **Close.**
  1. When no batch row is `pending` or `verify`, run `uv run qualc check` once over the corpus and repair each `lamport-proof-invalid` diagnostic.
  2. Read each `skipped` card, decide its step structure, and convert it.
  3. Push; `pages.yml` builds the site.
  4. Delete qualc's typed-step renderer (`_lamport_*` in `tools/qualc/emit.py`) and `normalize_fenced_divs`, make `qualc check` reject a fence line that Pandoc reads as paragraph text, and delete `queues/lamport-conversion/`.

  **Acceptance:** `git grep -E '^[[:space:]]*<[0-9]+>[0-9]+\.' -- corpus wiki` finds no file, `qualc check` reports no `lamport-proof-invalid`, and the typed-step renderer is deleted.

- **`copy-policy-repair`**. **Needs:** `policy-consolidation` (closed), `lamport-conversion`.
  Read every current reader-facing prose surface against the policies in [CONTRIBUTING.md](CONTRIBUTING.md#policy-families) and rewrite actual violations while preserving the mathematics.
  This includes the copy `unsolved-contribution` and `slogans` add.
  A solution still written with typed `<n>m.` steps is converted under [`lamport-conversion`](#lamport-conversion).
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
