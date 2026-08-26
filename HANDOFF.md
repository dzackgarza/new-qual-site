# Qual corpus handoff and restart plan

> Tier: workstream Parent: vault plan `PLAN-QUAL-OUTSTANDING-001` Roadmap owner: [GitHub issue #1](https://github.com/dzackgarza/new-qual-site/issues/1) State boundary: repository revision `380a48d0`, synchronized with `origin/main` on 2026-08-14

This file is a restart map.
It is not the live work tracker.

GitHub issues own public requirements, decisions, and current execution state.
Vault plans preserve the project structure and earlier reasoning.
Committed proof artifacts own technical evidence.

Update this file only at a handoff boundary.
Do not mirror each issue update here.

## Contents

- [1. Result](#1-result-that-the-remaining-work-must-deliver)

- [2. Authority and routing](#2-authority-and-routing)

- [3. Starting boundary](#3-starting-boundary)

- [4. Dependency order](#4-dependency-order)

- [5. Issue completion work](#5-workstream-r1-issue-specific-completion-work)

- [6. Deployment proof](#6-workstream-r2-current-deployment-and-issue-30)

- [7. Independent migration review](#7-workstream-r3-independent-source-migration-review)

- [8. Record results](#8-workstream-r4-record-results-and-reconcile-github-state)

- [9. User decisions](#9-user-decisions-and-issue-routes)

- [10. Proof and stop rules](#10-proof-and-stop-rules)

- [11. Final closure](#11-final-closure-order)

## 1. Result that the remaining work must deliver

Complete the publication and preservation roadmap in issue #1.

The first priority is the foundational product layer.
Close the shared publication, subject-branch, problem-explorer, and MakeMeAQual surfaces before treating source migration, rendered-page residue, or independent review as the main execution path.
Those later workstreams depend on this layer.

A reader must be able to do all of the following on the deployed site:

- enter each subject branch;

- browse the complete problem catalog with search and facet filters;

- generate a MakeMeAQual practice set from the shared catalog;

- read the authored mathematics in a supported order;

- reach stable pages, cards, problems, collections, sources, hints, and solutions;

- use search, filters, and statements-only exam generation;

- view diagrams, citations, assets, and mathematical notation correctly.

The source migration must also have a valid independent closeout review.

Issue #2 remains a separate, long-term mathematics program.
It does not block statements-only publication.
It does block honest solution-bearing exam generation.

## 2. Authority and routing

Use one owner for each kind of state.

### Public work state

- [Issue #1](https://github.com/dzackgarza/new-qual-site/issues/1) owns the full roadmap.

- [Issue #6](https://github.com/dzackgarza/new-qual-site/issues/6) owns publisher and subject publication.

- Issues [#23](https://github.com/dzackgarza/new-qual-site/issues/23) through [#30](https://github.com/dzackgarza/new-qual-site/issues/30) own its publication work units.

- Issues [#5](https://github.com/dzackgarza/new-qual-site/issues/5) through [#11](https://github.com/dzackgarza/new-qual-site/issues/11) own source and product workstreams.

- [Issue #14](https://github.com/dzackgarza/new-qual-site/issues/14) owns the remaining upstream macro-source decision.

- [Issue #41](https://github.com/dzackgarza/new-qual-site/issues/41) owns the small rendered-page residue.

- [Issue #2](https://github.com/dzackgarza/new-qual-site/issues/2) owns mathematical corrections and structured solutions.

### Planning records

- `PLAN-QUAL-OUTSTANDING-001` defines the active workstream structure.

- `PLAN-QUAL-GRUNT-001` defines the larger corpus-repair program.

- `PLAN-QUAL-HANDOFF-CLOSEOUT-001` defines the source-migration review criteria.

The issue tree is now the live execution tracker.
Treat the vault plans as derivation records where their status text is stale.

The closeout plan contains contradictory old status statements about archive action.
Do not use those statements as current evidence.
Issue #11 and `artifacts/issue-11/` own the current closeout record.

### Proof artifacts

- `artifacts/issue-23/publisher-proof.md` owns the publisher proof.

- `artifacts/issue-24/branch-proof.md` through `artifacts/issue-29/branch-proof.md` own branch proof.

- `artifacts/issue-30/replay-proof.md` owns the earlier browser findings.

- `artifacts/issue-30/deploy-proof.md` owns the earlier deployed proof.

- `artifacts/issue-11/` owns source migration and review evidence.

Do not copy proof results into a second ledger.
Link the relevant artifact from the owning issue.

## 3. Starting boundary

The repository state described here is committed and pushed.
The working tree was clean at `380a48d0`.

The remaining work is direct semantic, source, rendered, deployed, and independent-review work.
Record each result on GitHub after the evidence exists.

The following repository work exists and must not be repeated without a failed criterion:

- all six subject classifications and branch manifests;

- all six branch proof files;

- the second publisher proof run;

- the named content correction rounds;

- the MakeMeAQual reconciliation and intake inventory;

- the first deployed proof and browser replay;

- the source migration proof set.

The earlier audit worktrees no longer exist.
Use committed artifacts for resumption.

Before any new edit, verify the boundary:

```bash
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
gh issue list --state open --limit 100
uvx --python 3.14 --from git+https://github.com/dzackgarza/agent-memory \
  agent-memory plan show PLAN-QUAL-OUTSTANDING-001
```

Stop if the checkout has unknown changes.
Do not delete, restore, stash, or rewrite them.

## 4. Dependency order

Use this order unless a live issue records a newer dependency.

```text
R0  Verify repository, deployment, issue, and plan state
 |
 v
R1  Complete the foundational product layer
|   (#8, #10, #23-#29)
 |
 v
R1b Complete remaining semantic and source work
|   (#5-#7, #9, #41)
 |
 v
R2  Deploy current main and complete issue #30 replay
 |
 +--> R3  Complete fresh independent review for issue #11
             without using this handoff as the review frame

R2 + R3
 |
 v
R4  Record results and reconcile the owning GitHub issues
 |
 v
R5  Reconcile issue #6 and roadmap issue #1
```

Decision-gated work can run only after the user gives the named decision.
Section 9 routes each decision.

## 5. Workstream R1: issue-specific completion work

### 5.0 Foundational product layer: issues #8, #10, and #23 through #29

This is the first implementation priority.
It establishes the shared substrate for every later workstream:

- publish the authored corpus and every required subject branch;

- make the full problem catalog reachable through the reader and explorer;

- make search, facets, disclosure, and statements-only generation use that catalog;

- make MakeMeAQual generation and its source provenance agree with the catalog.

Do not close this layer from a page count or a successful build alone.
Each issue must prove its user-facing behavior on the current revision.

### 5.1 Publisher and authored pages: issues #5 and #23

Use `artifacts/issue-23/publisher-proof.md` as the primary proof record.

The second run records these results at its named revision:

- source pages and emitted routes are set-equal;

- authored prose is retained;

- static fragment validation passes;

- the browser proof has no remaining publisher defect.

Later commits add citation links, panel titles, heading mathematics, and one macro repair.

Before closing issue #23, confirm that later commits preserve all four proof obligations.
Do not replace the proof with a new count-only check.

Issue #5 has a wider source-preservation claim.
Close it only after its card-reference and authored-position criteria are also mapped.

### 5.2 Subject branches: issues #24 through #29

Read each `artifacts/issue-N/branch-proof.md` before posting a disposition.

For each branch:

- confirm the proof revision and branch manifest;

- map every issue criterion to the proof;

- retain every stated nonclaim;

- post mathematical defects on issue #2;

- close only after all branch-specific gaps are settled.

Issue #28 needs one new reachability measurement.
Its proof records 121 unaddressed Topology cards.
Commit `965a9e76` removed the repeated-panel-title constraint.

Rebuild the current Topology branch and repeat the proof's reachability query.
Close #28 only if every required card is addressable under issue #28's meaning.

The collection-membership interpretation is user-gated.
Do not silently weaken “every extracted card is reachable.”
Section 9 routes this decision to issue #6 and the branch issues.

Issue #6 remains open until its full acceptance is proved.
Its body includes the full-site proof as its eighth child work unit.
Therefore issue #30 must close before issue #6 can close.

### 5.3 Source reconciliation: issues #7 and #8

Issue #7 owns all `qual-review-and-solutions` bundles, variants, citations, and assets.

The current handoff records working citation routes and current validators.
Those facts do not prove every variant or collapse decision.

Before closing #7:

- map every source bundle to a canonical card, variant, or reviewed collapse;

- verify all six textbook source routes;

- run the current reconciliation and route validators;

- record all remaining source wording differences.

Issue #8 owns the 508-row MakeMeAQual join.

Before closing #8:

- verify all 508 rows on the current revision;

- confirm each exact-match decision has one semantic target;

- compare institution, area, date, season, source, and membership counts;

- prove an isolated import does not change curated output;

- settle the regeneration-versus-curation ownership decision in Section 9.

Do not use “508 rows exist” as the completion claim.

### 5.4 Attachment extraction: issue #9

The repository contains a frozen document inventory and page-level dispositions.

Issue #9 remains open for these required facts:

- every retained document has a page-level disposition;

- every transcription has an independent reread;

- `F08phdtop` has a second read and a settled date label;

- the 30 image-only Anki answer placeholders have a recorded disposition.

### 5.5 Reader and generator: issues #10 and #41

Issue #41 now contains mostly presentation residue.
Verify each item against the current rendered page before closing it.

Issue #10 owns the complete reader, search, filter, collection-link, diagram, citation, and generator behavior.

Before closing #10:

- compare browser and generator problem sets with the built catalog;

- exercise each supported facet and combined filters;

- inspect a statements-only generated exam;

- inspect a diagram, citation, collection link, hint, and solution;

- settle typed facets and `tikzcd` in Section 9.

## 6. Workstream R2: current deployment and issue #30

The existing browser replay covers deployed revision `bba5c28a`. The existing deployment proof covers revision `95e2d626`. Neither proves the current published artifact.

After R1, deploy the current `main` revision.
Record the exact commit, workflow run, deployment URL, and deployed revision.

Repeat issue #30 at the deployed boundary:

- verify route and catalog manifests;

- visit every subject branch root and terminal route;

- exercise search, filters, collection links, disclosure, diagrams, citations, and generation;

- inspect 375, 768, 1024, and 1440 CSS-pixel snapshots;

- inspect console and network results;

- confirm local and deployed artifacts use the same revision;

- state every unexercised path and nonclaim.

Use the existing `artifacts/issue-30/replay-proof.md` format.
Write a current proof instead of extending the stale verdict.

Issue #30 closes only when its own proof list has no unmet criterion.

## 7. Workstream R3: independent source migration review

All five source repositories are already archived by owner decision.
Do not repeat archive action.

The remaining obligation is independent sign-off.
The existing M5 record is a failure at target `763dbdb1`. Later work closed its content findings, including the hidden `PSets.zip` material.

Assign the next review to a fresh context.
Give it only these inputs:

- `PLAN-QUAL-HANDOFF-CLOSEOUT-001`;

- the pinned source revisions;

- the current target tree;

- `sources/migration-ledger.jsonl`;

- raw files under `artifacts/issue-11/`.

Do not give the reviewer this handoff or an earlier completion summary.

The review must establish:

- reviewer identity and task separation for each repository review;

- direct source-to-target semantic coverage at the current boundary;

- a current cross-repository criterion-to-evidence map;

- an explicit disposition for every prior M5 failure;

- no unresolved evidence that contradicts permanent migration.

After a passing review, give the result to R4. R4 reconciles issue #11 and the closeout plan.
Remove stale claims that no archive action occurred.

## 8. Workstream R4: record results and reconcile GitHub state

Record current evidence only after R1, R2, or R3 produces it.
GitHub comments do not replace the work or its proof.

### 8.1 Publish content findings on issue #2

Post the correction and finding records from the branch proofs and content reports.

The comment must distinguish these classes:

- corrected false statements;

- source-backed corrections;

- unresolved mathematical choices;

- missing mathematics;

- card-kind or source-structure defects;

- duplicate candidates that still need reading.

Do not describe issue #2 as complete.
Its full structured-proof program remains open.

### 8.2 Restore commit provenance on the owning issues

Post the known cross-lane provenance facts on their issue owners.

- Issue #26 must identify `65b926c5` as the Real Analysis classification commit.

- Issue #24 must identify `0bed0189` as the Prelims branch-proof commit.

- Issue #2 must identify the seven round-one fixes that carry another lane's commit hash.

Use the existing reports for the exact mapping.
Do not infer authorship from the commit summary alone.

### 8.3 Reconcile issue claims after verification

Several issue bodies contain old inventory counts and old implementation claims.

For each issue, compare its full acceptance text with current committed evidence.
Then post one current evidence comment.

The comment must include:

- the exact repository revision;

- the obligation under review;

- the proof artifact or direct observation;

- any nonclaim or residue;

- the disposition of each unmet criterion.

Close an issue only when its own acceptance text is fully satisfied.
A parent issue, passing check, or proof count cannot replace that test.

## 9. User decisions and issue routes

Ask for these decisions as one concise batch.
Do not infer an answer from existing content.

1. **Normal-family convention.** Route to issue #2. Choose Stein–Shakarchi or Ahlfors for the canonical definition.

2. **`tikzcd` publication.** Route to issue #10. Decide the supported diagram boundary for the 44 affected cards.

3. **Importer ownership.** Route to issue #8. Decide whether curated topics belong in importer input or outside its output subtree.

4. **Twenty-seven solution write-ups stored as problems.** Route to issues #5 and #24. Approve new problem cards and membership corrections.

5. **Disabled `\sech` definition.** Route to issue #14. Decide whether to remove the commented upstream line.

6. **Typed facets.** Route to issue #10. Decide whether area, institution, year, and topic need separate controls.

7. **Problem reachability.** Route to issue #6 and issues #24 through #29. Decide whether collection and problem pages satisfy reachability for every problem.

8. **Small mathematical and editorial choices.** Route by ownership.
   Use issue #2 for notation, duplicate statements, and competing mathematical repairs.
   Use issue #9 for missing image-only answers.
   Reopen #40 or file a narrow issue before any mass title work.

Record each answer on its owning issue.
Do not keep the decision only in this file.

## 10. Proof and stop rules

- Read the mathematics before any classification, merge, title, or canonicality decision.

- Do not create a semantic classifier or deduplication tool.

- Verify claims at the current source, target, rendered, or deployed boundary.

- Treat a focused check as evidence only for its named obligation.

- Run targeted checks during an edit.

- Let commit and push hooks run the configured full checks.

- Render and inspect the real page before closing visual work.

- Use `trash`, never `rm`.

- Commit each coherent change and push before handoff.

- Do not close a parent issue because its children look complete.

- Do not stop after a status update while safe issue work remains.

Stop and ask the user only when:

- a decision in Section 9 is required;

- two mathematical sources give inequivalent answers;

- a source is unreadable;

- the requested change needs deletion or another irreversible action;

- live issue requirements contradict and no owning decision resolves them.

## 11. Final closure order

Use this order after all workstreams finish:

1. Reconcile and close satisfied issues #5 through #11, #23 through #29, and #41.

2. Close issue #30 on the current deployed proof.

3. Close issue #6 after all publisher and branch obligations hold.

4. Update roadmap issue #1 with remaining open work.

5. Keep issue #2 open unless its full mathematics program is complete.

The project is not complete while issue #1 has an unmet requirement.
This handoff is not evidence that any issue is complete.
