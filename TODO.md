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
  Round 1 (revision `fe928e9a1`) injected the nodes below; `audited-deployment` needs all of them.

  Renderer and site nodes (owner `tools/qualc`, `site/`):
  - **`ad-citeproc`**. **Needs:** none. Citations in transcluded card bodies render as raw
    `[@key]`. **Acceptance:** no deployed page shows a literal `[@`. **Closed.**
  - **`ad-tikzcd`**. **Needs:** none. `tikzcd` blocks vanish on transclusion (D-KRKV7,
    T-SKJB2, E-B4ZSQ). **Acceptance:** every card diagram renders wherever the card appears.
  - **`ad-fancy-lists`**. **Needs:** none. A proof step opening with `(a)` splits into a
    bare number and a list. **Acceptance:** such steps render as one numbered claim. **Closed.**
  - **`ad-smart-titles`**. **Needs:** none. `--` and `$…$` reach titles, prompts, link
    text and `<title>`. **Acceptance:** dashes typeset; tab titles carry no TeX. **Closed.**
  - **`ad-bare-id-links`**. **Needs:** none. 148 wikilinks display a bare card id.
    **Acceptance:** link text is the card title or authored text. **Closed.**
  - **`ad-collection-pages`**. **Needs:** none. Drop cap splits the count; "1 problems.";
    derived "Problem N" locators; transcluded collections render empty (workshop packets).
    **Acceptance:** each corrected on the deployed pages. **Closed.**
  - **`ad-site-strings`**. **Needs:** none. Unmatched browser prefilter widens to all rows;
    `sourced` compatibility filter; Sources/Exams naming; area label spellings; Pagefind
    excerpts include page facts; "Choose topic" over areas; home contents list.
    **Acceptance:** each corrected on the deployed pages. **Closed.**

  Round 2 (revision `848f40677`) injected:
  - **`ad2-renderer`**. **Needs:** none. `--` in wikilink text, block qualifiers and slogans;
    citation style dropped locators such as `Section 10.1`. **Closed.**
  - **`ad2-algebra-content`**. **Needs:** none. CARD-04: PR-TAPZF/FF-UYMWY; FD-XT6HD/PR-TI6YA;
    PR-QDRB4/PR-3TYBE; PR-E4T3S/resolvent-cubic remark; T-V7JRG/FT-PUVIQ; P-UZDCX/T-NGBVC;
    P-ZYHXO/FD-3GZPO; C-BOM4E/PR-OFBRQ; FF-2AKVH/FF-HAMDC; separability cluster PR-TLBPS,
    PR-ENHVC, FD-6WSIA, C-C2GYX, E-6OUJV. which-kind-of-ring claims 3 and 3 are nonassociate.
    PR-DLPTR restates D-LIEMF. Page restatements: finite-fields, fields/polynomials,
    commutative-algebra, which-kind-of-ring, maschke-and-schur. **Acceptance:** each read and repaired.
    **Closed.** P-UZDCX stays distinct from T-NGBVC: it also asks why a finitely generated
    algebraic extension is finite.
  - **`ad2-real-analysis-content`**. **Needs:** none. PR-WUZSG uniform-convergence criterion
    needs "for all sufficiently large n"; the-convergence-theorems "on $L^1$" should read
    "on $\RR$"; P-RAF23C, P-RAF23F, P-RAF23G proof notation, part labels and step references;
    P-4EOE5 doubled arrow and typed step citations; CARD-04 groups on measure, integration and
    $L^p$ (T-BFOJT/FT-4ED3Q/PR-JX4YU, FT-O4DRR/FF-LA4J2, T-OTR5M/FR-CSUMF/FF-GNU7E/P-QZT5B,
    FF-UW3C7/FE-YOIJM, T-CGFCU/FT-XIVPL, T-5K3IO/FT-5G4Y3, T-IJQQG/FT-LCR5P, T-LDJNS/FT-P5UNP,
    T-MN6WQ/FS-BM2PV/PR-EHIXY/FR-KEWV2/PR-NKZBT/PR-YJJSY, D-R4VKE/FD-Q3XHG,
    FF-C7GY4/FF-LMANJ/PR-6OHTJ, T-RIY2P/FT-BV2AU/FF-FSDJP/PR-4OXGZ, PR-HFYSO/FR-6AHGM,
    T-X7XZX/FT-H6AWV, PR-V4MOK/PR-2CZUM, E-WXIRH/PR-TNFL4) and the PR-2JV43 repeated remark;
    CARD-04 groups on other pages (FF-AVBFU/FF-5EBCJ, PR-UJ64S/PR-LEDI3, FD-5I73B/FF-7JOOD,
    D-YZC3C/FD-ZTRHG/D-RA-WORKSHOP-D7-CONVERGENCE, FD-WN55Z/FF-HORGP, D-2MJRE/FF-HRUA3,
    D-5NODS/FD-JGBSF, D-PAEDW/FD-AI6XN/FF-JBCFQ, D-RPOGQ/FD-BBR6Q/FD-HGESN, FD-5T3HX/FF-NOX4C,
    D-3PVRB/FD-J5AFR, D-TS42Y/FF-4WIMZ, PR-JTFMW/C-44LL4, PR-ZI7M3/FT-NFMJW/T-5AALA,
    T-LDCZB/FF-UT5GL); workshop theorem cards T-RA-WORKSHOP-D5-4-2/T-OXNTU,
    T-RA-WORKSHOP-D4-3-3/T-O4UD3, T-RA-WORKSHOP-D7-6-2/FF-IAUQG, T-RA-WORKSHOP-D7-6-7/T-3QNBQ,
    T-RA-WORKSHOP-D7-6-1/C-3S4XS, T-RA-WORKSHOP-D5-4-3/T-2R7PC, T-RA-WORKSHOP-D7-6-5/FF-XZGIY;
    `STYLE-03`, `STYLE-04`, `STYLE-08` in P-ZCE6E, P-8RA35, P-4NYI7, P-4EOE5, T-W5SDY and the
    SRC-RA-WORKSHOP problem cards; real-analysis round-2 candidates (FS-5FKPD/FF-IAUQG,
    PR-DWOXP/FE-GN3CF, PR-YO7MV/FD-3BK6U, D-2CCDB/FD-XVMEE, D-HHVPT/FD-ST7TD, P-7XPOK and
    P-PEND3 overlaps, real-week-2-measure-theory process text, P-OPH7A prose solution,
    "orthonormal" in FT-NFMJW and PR-ZI7M3, Arzelà–Ascoli codomain, T-ERNLN notation).
    **Acceptance:** each read and repaired.
  - **`ad2-topology-content`**. **Needs:** none. Citation-only `concept` blocks on about 80
    topology cards (D-EBNUE, D-IGUUS, …); FF-AE7ID/C-CT2NX merge; fundamental-group/theorems
    change-of-basepoint restatement; curves-in-projective-space opening and projection
    paragraphs; T-2YTCZ proof notation. **Acceptance:** each read and repaired.
    **Closed.** D-BUAYX, a second injective-map card, was merged into D-3ZBXG, and
    D-CNLBT, D-JW63I and D-K5MLW (orientation, local orientation, orientable) into D-6CI7D;
    the fundamental-class theorem stays on D-TS7TZ. D-QTJ7T and T-TUXBP (complex analysis) keep citation-only
    `concept` blocks.
  - **`ad2-style-03-corpus`**. **Needs:** none. `STYLE-03` typefaces written raw instead of with
    the vocabulary macros. The letters with one meaning (N, Z, Q, R, C, F, D, RP, CP) were
    rewritten by codemod (579287fd3f, 8176772bad), and `qualc.authoring` now rejects them in any
    changed card. What remains needs reading, because the letter has several meanings: `\mathbb`
    H, P, T, A, S, G, E, M (215 files on 2026-10-30, `grep -rlE '\\(mathbb|Bbb)' corpus wiki`),
    unbraced forms such as `\mathbb Cx` and `\mathbb CP`, and `\mathbf` Z, Q, R, C, N
    (32 files). Kept on purpose: `\mathbb{P}` for the irrationals in E-AKPMH and
    `\mathbb{B}^2` for the open ball in E-2B91X. **Acceptance:** every remaining raw form is one
    that `STYLE-03` permits.
  - **`ad2-complex-analysis-content`**. **Needs:** none. The power-series Dirichlet's-test proof
    swaps the two sequences. CARD-04: PR-K57J6/E-TZJKN; E-6F2HU/E-THK2Z; PR-OOHUL/E-PAQPF;
    PR-Y36BS/D-E7A5W proposition/Cauchy–Riemann page remark; T-E76LX/P-Y5SS5; D-4CSPM/D-OMBQT;
    T-GROTS/T-SRY2V/C-7S2CO; PR-NZZ2C/E-EG3W7; T-77SHB/PR-FL6T7; PR-AQFRA/PR-PDYJC; T-DAETF/T-VM6MJ;
    E-TJ3WM/E-XQ4BA; T-W26VL/FF-4GUYL; D-MFPYG proposition/PR-ULJAJ; C-FVT4V/P-Z776N/E-I26BF/D-OHFRH
    proposition; T-MCB7V/T-4ALS2; E-ISFYB/E-C5QHZ; E-LXY7N/E-GFNDF; T-C5VEI/FT-2N57U; D-VAXQT/D-IWIA5;
    T-ZZJDP/FT-5NI77/FT-LGWHM/D-BQLJV/FD-BRJK5; D-VKP6N/FD-BACTZ/FD-ZPKLQ;
    D-AUD6K/FD-C7EQD/FD-EKGLW/PR-NITIQ; D-65VIK/PR-5A64G/PR-ITZIT; PR-VUBCC/PR-EWOP5/E-WNXIR;
    P-DO7TE/E-4GLUR. Candidates: E-SMOHZ isolated-singularity reason; PR-PDYJC needs α<2 but PR-BPP7D
    uses angle 2π; Montel page cites a D-IJMPJ remark; D-YKB3V "Toy contour" heading; E-QVMUV
    "exactly" on the annulus; extra proofs in remarks (PR-K57J6, Schwarz lemma, T-ZZJDP, PR-NITIQ,
    PR-EWOP5, PR-5A64G); possible duplicates E-UVNVV/E-I26BF, PR-YO7MV/FD-3BK6U, D-2CCDB/FD-XVMEE,
    D-HHVPT/FD-ST7TD; `STYLE-03` `\mathbb` on maximum-modulus-and-open-mapping and
    cauchy-estimates-and-liouville. Also: D-QTJ7T and T-TUXBP concept blocks that hold only a
    citation. Found while merging: FT-OEYLQ/C-FRF33 (open mapping), FT-5MASA/T-22RQZ (Cauchy
    inequalities). **Acceptance:** each read and repaired, or kept with the reason. **Closed.**
    Every CARD-04 group was one statement and is merged; PR-PDYJC into PR-AQFRA settles PR-BPP7D;
    D-IJMPJ into D-QTJ7T settles the Montel remark; the listed extra proofs left with their merged
    cards. E-UVNVV is kept apart from P-Z776N: it states that $f$ is locally $(n+1)$-to-one, a
    stronger statement. PR-YO7MV/FD-3BK6U, D-2CCDB/FD-XVMEE, D-HHVPT/FD-ST7TD are real-analysis
    cards and stay with `ad2-real-analysis-content` above.
  - **`ad2-site-surfaces`**. **Needs:** none. Renderer: a "problem N" locator is derived when an
    appearance comment is empty; solved counts include child-collection rows
    (SRC-MATH8100-FALL-2019-ASSIGNMENTS, SRC-RA-WORKSHOP); institution ids are upper-cased
    instead of named from the vocabulary; guide titles differ from area names; Pagefind indexes
    the slogan link, backlinks and the collection count; unlabelled page wikilinks show the raw
    path (wiki/archives/qual-workshop-index.md); the home `<title>` repeats the site name;
    SRC-RA-WORKSHOP provenance chips carry no document name. Corpus: E-AMD-4SSSVQJY,
    E-AMD-564ETBH5 and E-AMD-E3N4BHJH are in no collection; stem or truncated titles in
    SRC-RA-WORKSHOP and Berkeley 1977 (`CARD-01`); TeX outside math in titles (P-CAFA22B,
    P-CAFA22D, the 1-connected CW complex card); P-2J6HK remark before hint and solution
    (`STYLE-07`); the topology packets lede names sections that do not exist; SRC-RA-WORKSHOP
    has no institution. Renderer, analysis audit: block `title=` text skips citeproc and smart
    punctuation; "(a)" list markers render as "a."; PR-TC76W "(U)", "(P)", "(N)" parse as a
    list; the E-B4ZSQ diagram `<div>` sits in a `<p>`. Round-2 candidates C5, C6, C8 and C9
    remain for the owner. **Acceptance:** each item read and repaired. **Closed.** Open
    remainder: the three E-AMD orphans come from the maintainer's own review notes, so no
    collection lists them; they duplicate P-Q67AG/P-AMD-62OZUWBP (4SSSVQJY),
    P-MV6ZQ/P-AMD-ZIGVO4GJ/E-JAPBK (564ETBH5) and P-AMD-2NXEX5LK/E-AMD-V3WFKTM6 (E3N4BHJH)
    and wait on `CARD-04` merges. The Day PDFs name no institution, so SRC-RA-WORKSHOP keeps
    none. The "Suggest a slogan" issue link on result cards is a `QUAL-08` candidate for the
    owner. Pagefind may split full institution names at commas. The orphan merges are done
    (`CARD-04`): E-AMD-4SSSVQJY and P-AMD-62OZUWBP into P-Q67AG; E-AMD-564ETBH5, P-MV6ZQ and
    P-AMD-ZIGVO4GJ into E-JAPBK; E-AMD-E3N4BHJH and P-AMD-2NXEX5LK into E-AMD-V3WFKTM6.

  Content nodes (owner: the named cards and pages; one item at a time):
  - **`ad-algebra-content`**. **Needs:** none. CARD-04 merges confirmed in round 1
    (PR-U5CHT/FF-QVQXM, E-EMESP/E-P4LG6, D-FIB7S/FD-OR3BW, T-SVJUN/FT-7NMQR, E-DFUYC/E-R6I7G,
    T-4XKGD/L-6QBOJ, PR-GJLQP/P-5UUNM, T-GJNT5/C-HWX2P/E-NNTQB, P-AMD-QBEEJKCX/E-AMD-UEHZOJ3K);
    notation and structure defects in D-53LTN, PR-IOMVN, PR-SLWTB, T-WRMBM, PR-KGHJ2, E-P5BF6,
    the-class-equation, orbit-stabilizer, characteristic-subgroups, is-this-group-abelian.
    **Acceptance:** each item read and repaired. **Closed.** E-P5BF6 needed no card change: its
    split QED step is the `(e)` list defect owned by `ad-fancy-lists`.
  - **`ad-topology-ag-content`**. **Needs:** none. PR-QV4U5 proof does not prove its CW
    statement; C-ILVEB empty concept block; C-GJRYO dangling colon; T-BX4LD notation;
    E-JX67Q delimiters; separated-and-proper and curves-in-projective-space restatements;
    wiki/prelim/worked-exams/all.md stray remark. **Acceptance:** each item read and repaired. **Closed.**
  - **`ad-analysis-content`**. **Needs:** none. P-RAF23C step 2 fails for infinite measure;
    P-RAF23F/G titles carry TeX outside math; P-RAF23G "measurable space"; STYLE-05 part
    keying in P-SMK7Q, P-NYOLD, P-PEND3, P-7XPOK; GUIDE-REAL-ANALYSIS joint-exam intro
    describes complex analysis. **Acceptance:** each item read and repaired. **Closed.**
  - **`ad-public-notes`**. **Needs:** none. Curation notes on public pages
    (workshops-guide topology lede, SRC-RA-WORKSHOP remark) and RES-01 duplicate PDF links
    in wiki/prelim/resources/problems.md. **Acceptance:** each item read and repaired. **Closed.**
  - **`ad-prelim-resource-intake`**. **Needs:** none. `RES-02`: wiki/prelim/resources/problems.md
    links `assets/attachments/calculus_practice_test3.pdf`, which no collection lists as
    provenance. **Acceptance:** the PDF is ingested as a collection, like the GRE chapter
    reviews, and the page links that collection.

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
