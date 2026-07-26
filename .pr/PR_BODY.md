Closes #17
Closes #18

## Original objective

Publish one continuous, dependency-ordered finite-groups branch:

`Algebra -> Finite Groups -> Actions and Counting -> Sylow Theory -> Applications and Problems`

The branch must be a practical build artifact, not an hour-scale render or a set of
routes without a readable traversal.

## Claim map

- [x] The subject sidebar, breadcrumbs, and previous/next links implement the five-page
  mathematical reading order.
  - Proof: `tests/test_invariants.py::test_corpus_layout_is_semantically_inert`
  - Visual evidence: `artifacts/issue-17/screenshots/{desktop-1440,mobile-375}-0*.png`
- [x] Connective prose and independently addressable cards cover the complete named
  finite-groups spine, including all linked workshop problems and the
  `P-P2UAH` / `D-7TQ2M` / `H-2JK8Q` / `S-4WQ1R` chain.
  - Proof: the `named_spine <= rendered_spine` invariant in
    `tests/test_invariants.py`
- [x] Card/problem routes remain stable independently of page placement, and problem
  statements precede collapsed hints and solutions.
  - Proof: the appearance-move rebuild and problem-state assertions in
    `tests/test_invariants.py`
  - Visual evidence:
    `artifacts/issue-17/screenshots/{desktop-1440,mobile-375}-problem-*.png`
- [x] Authored dependencies, derived appearances, and backlinks are separate rendered
  groups.
  - Proof: relation-group assertions in `tests/test_invariants.py`
  - Visual evidence:
    `artifacts/issue-17/screenshots/{desktop-1440,mobile-375}-relation-groups.png`
- [x] Search includes visible Page, Card, and Problem results with explicit type labels.
  - Proof: search-record and visible-window assertions in `tests/test_invariants.py`
  - Visual evidence:
    `artifacts/issue-17/screenshots/{desktop-1440,mobile-375}-search-result-types.png`
- [x] The practice generator and subject pages consume the same SQLite catalog
  projection, and generated statements are executable semantic HTML.
  - Proof: catalog-ID equality and Node syntax assertions in
    `tests/test_invariants.py`
  - Visual evidence:
    `artifacts/issue-17/screenshots/tablet-1024-generator-shared-catalog.png`
- [x] Independent conversions cross one build-scoped Pandoc server boundary and emit
  production HTML directly.
  - Proof: `artifacts/issue-17/build-proof.md`
- [x] The exact clean build and generated site satisfy the performance and integrity
  boundary.
  - Clean build: 5,218 cards in 51.59 seconds, 480,416 KiB peak RSS, two descendant
    Pandoc invocations.
  - Output validation: 3,480 HTML pages, 31,077 local references, zero parse errors,
    missing targets, missing fragments, or `.qmd` links.
  - Browser replay: 25 inspected screenshots across 375, 768, 1024, and 1440 px widths;
    zero console or page errors.
- [x] The commit-tier QC baseline is green without suppressions or hook bypasses.
  - Proof: the branch passes the repository's Semgrep, Ruff, Mypy, syntax, commit, and
    push gates, resolving #18.

## Verification

The repository push gate passed all 47 tests. Exact build, link-validation, browser, and
visual-inspection receipts are preserved in `artifacts/issue-17/build-proof.md`.

## Nonclaims

This PR does not claim bulk editorial completion for other subjects or a redesign of
the exam-selection behavior.
