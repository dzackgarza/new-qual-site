# Outstanding work

## Fast local checks and complete CI acceptance

Local hooks reject basic defects in the actual changed content; CI owns full test suites,
corpus-wide validation, builds, rendering, and broad audits. QC-01 through QC-05 and
QC-07 through QC-11 are closed. Two items remain open.

| ID | Task | Needs |
| --- | --- | --- |
| QC-06 | Run the complete shared acceptance tier in hosted CI | none |
| QC-12 | Close the workstream against a complete hosted run | QC-06 |

- [ ] **QC-06 — Wire the hosted acceptance tier for this repository's workflow.**
  **Owner:** ai-review-ci's supported workflow integration and `.github/workflows/`.
  The hosted workflows are `development.yml` (build, link crawl, deploy, and the
  `corpus-reports` job) and `ambient.yml` (the shared `_qc.yml` workflow). The shared
  reusable workflow runs all diagnostics and can either report their failures or enforce
  all of them; it has no supported result that enforces only the test suite. The full
  doctor reports a missing PR workflow and branch protection. Determine the supported
  integration for the repository's direct-to-main policy before changing repository
  protection or requiring PRs. Full acceptance needs the Python, Pandoc, LaTeX, and filter
  dependencies, must not inherit the local pytest file selection, and must not run the
  complete suite twice.
  **Acceptance:** a hosted run demonstrates execution of the complete intended acceptance
  tier, with a real comparison base for diff checks and explicit failure propagation.
  Any workflow-policy decision still requiring owner choice is stated before changing it.

- [ ] **QC-12 — Close against the full completion condition.**
  Verify a single current revision through hosted acceptance, report publication, site
  build, crawl, and deployment. Confirm the deployed revision stamp. Reconcile resolved
  complaint entries with the delivered state.
  **Acceptance:** cheap errors are caught locally; expensive checks run in CI; generated
  reports are usable; remaining failures are explicitly owned. Successful local hooks
  alone do not close this workstream.

## Execution DAG

A prerequisite `A` on task `B` means `A -> B`. `none` denotes a ready root.
Before committing a dependency change, verify unique IDs, resolved references, and absence of cycles.
Closed nodes are not executable work; their evidence is in Git history.
For a newly selected repair, name its card or issue ID, its immediate Needs and its acceptance
beside the existing items, and link its complaint.

Read [CONTRIBUTING.md](CONTRIBUTING.md#named-policies) and record issues as they arise in [COMPLAINTS.md](COMPLAINTS.md).

### Current route

`publication-milestone`, `unsolved-contribution`, `slogans`, `lamport-conversion`,
`solution-section-restoration`, and `copy-policy-repair` are closed. The next ready node is
`audited-deployment`.

Copy is reader-facing prose: wiki pages, remarks, and site strings. Problem statements and
proofs are mathematics, not copy. A defect in a statement or proof is repaired as a
mathematical correction under its own node, not under copy policy.

- **`audited-deployment`**. **Needs:** none. Push so `development.yml` deploys, then audit
  the deployed site at <https://dzackgarza.github.io/new-qual-site/> in open-ended rounds.
  Each round reads the deployed pages against the [CONTRIBUTING.md](CONTRIBUTING.md#policy-families)
  policies and checks their mathematics for incorrect facts, statements, and solutions; it is
  a reading of the site, not a lint or crawl count.
  Every finding becomes a node in this DAG, named by its card or page, with its immediate
  Needs and acceptance, and `audited-deployment` gains it as a prerequisite.
  A round with any finding resets the count; repair the injected nodes, redeploy, and start again.
  **Acceptance:** three consecutive rounds against the same deployed revision (its stamped
  commit) find nothing.

### Marking a node closed

When a node meets its acceptance, mark it closed in this file in the same delivery so it
cannot be selected again. A later regression is repaired at its current owner rather than by
replaying the historical node.

### Terminal nodes

These nodes run after `audited-deployment` closes. They are finite cleanup work, not a
recurring reporting programme.

- **`refactor-audit`**. **Needs:** `audited-deployment`.
  Inspect the tooling and site sources — `tools/`, `site/`, generators, and checkers, not authored mathematics — for concrete defects in ownership, encapsulation, duplicated sources of truth, unnecessary bespoke machinery, and maintainability that affects reliable behavior.
  Repair a defensible finding at its actual owner rather than creating an audit receipt, inventory-only node, or approval stage.
  A genuinely large cross-owner repair may become a concrete DAG node with its real dependencies and behavioral acceptance; the audit itself does not recursively manufacture scheduling nodes.
  **Acceptance:** every finding from the pass has been repaired at its owner, and a final repository-wide pass over the same scope finds no further concrete defect requiring work.

- **`type-paydown`**. **Needs:** `refactor-audit`. Repair the tooling type defects for which stronger typing materially improves legibility, comprehension, or static reasoning about correctness.
  The objective is the resulting program structure, not a diagnostic count.
  Do not add contortions whose only value is silencing a checker.
  **Acceptance:** the type defects selected by the refactor pass have been repaired at their owning interfaces, with behavior preserved and the resulting annotations/interfaces clearer than the state they replace.

- **`bloat-audit-loop`**. **Needs:** `type-paydown`.
  Make one final whole-tooling/site convergence pass using the relevant lenses already established for this repository: publisher/tool architecture, proof-bearing tests, API and type design, dependency/offload opportunities, duplicated sources of truth, dead compatibility bridges, generated-versus-authored boundaries, build/preview cost, and AI-slop patterns.
  Compare bespoke Markdown parsing/rendering against Pandoc and the existing Markdown toolchain before polishing local machinery that should disappear.
  Inspect representative public behavior; source-text churn is not acceptance evidence.
  Repair each defensible finding at its owner.
  **Acceptance:** all findings from the pass are repaired and a final pass across those lenses finds no further defensible change.

Live issue state is on [GitHub issues](https://github.com/dzackgarza/new-qual-site/issues).
Do not mirror it here.

## 7. Author solutions

Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2)

Every current `kind: problem` card has an authored `solution` section. A newly added problem
without a solution is new authoring work under this procedure.

The per-card tasks are `select:P-…`, `read:P-…`, `source-review:P-…`, `prove:P-…`,
`attach:P-…`, and `commit:P-…`, each keyed by the card ID; names in Needs refer to the same
card's instance, and `select` needs nothing. Returning to selection creates an instance for a
different card. Work one card at a time in source order; independent subject streams may work
on different cards in the one checkout, on `main`, under [`QUAL-09`](CONTRIBUTING.md#named-policies).

`source-review` applies when incorporating a source solution; an original proof has no source
solution to review. Source reading and review of the authored proof are required in either
case. An unfinished source correction needed by a proof precedes that card's proof.
