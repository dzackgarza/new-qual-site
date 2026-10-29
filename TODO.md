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
    **Acceptance:** each read and repaired. **Closed.** Every CARD-04 group was one
    statement and is merged into the surviving card named first; the workshop theorem cards
    merged into their pairs, and D-RA-WORKSHOP-D7-CONVERGENCE into D-IYDZU and D-YZC3C, with
    the series forms as remarks. T-RA-WORKSHOP-D7-6-7 stays as Stone--Weierstrass, which no
    other card states; Weierstrass approximation lives on T-3QNBQ. FS-5FKPD stays apart from
    FF-IAUQG: it is the strategy for showing a series converges uniformly and cites the
    $M$-test. P-7XPOK merged into E-MFCCS, E-EJN4Q, E-M3CGY, E-L3F4O and T-OTR5M.
  - **`ad2-topology-content`**. **Needs:** none. Citation-only `concept` blocks on about 80
    topology cards (D-EBNUE, D-IGUUS, …); FF-AE7ID/C-CT2NX merge; fundamental-group/theorems
    change-of-basepoint restatement; curves-in-projective-space opening and projection
    paragraphs; T-2YTCZ proof notation. **Acceptance:** each read and repaired.
    **Closed.** D-BUAYX, a second injective-map card, was merged into D-3ZBXG, and
    D-CNLBT, D-JW63I and D-K5MLW (orientation, local orientation, orientable) into D-6CI7D;
    the fundamental-class theorem stays on D-TS7TZ. D-QTJ7T and T-TUXBP (complex analysis) keep citation-only
    `concept` blocks.
  - **`ad2-style-03-corpus`**. **Needs:** none. Raw blackboard bold replaced by semantic macros,
    one per meaning, defined in the pandoc-config preamble. **Closed.** Codemods 579287fd3f,
    8176772bad and 2b05c0f015; the card check rejects any raw `\mathbb` or `\Bbb`.
    Bold vectors and points written `\mathbf` (P-GRECH3-04, P-AGH5415GENPOSITION) stay raw.
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

  Round 3 (revision `5ba163ac9`, algebra and applied algebra) injected the nodes below;
  `audited-deployment` needs both.
  - **`ad3-renderer`**. **Needs:** none. Citation labels such as `[DuFo04]` and `[Hung74]` on
    wiki and tag pages (D-IPR4B, D-FK47C, PR-E4T3S) render with no bibliography entry or link,
    and the `data-cites` key differs from the label; the `<title>` of P-ALGQUAL18W-I1 carries
    expanded TeX for nested `\sqrt`; the syllabus locator `[@Smi96, sec. 844-1]` renders as a
    section range; `tikzcd` diagrams are still missing on groups pages (D-KRKV7, FF-TSZNT,
    T-NFQBO; open under `ad-tikzcd`). Site surfaces (round 3): the SRC-CALCULUS-PRACTICE-TEST3
    MD chip opens a hand-edited partial `extracted/` file, not the MinerU extraction beside the
    PDF; `problems.html` splits URL filter values on commas, so comma-named institutions match
    nothing; the default problem order puts multi-area cards and `algebraic-geometry` before
    `algebra`; SRC-MATH8100-FALL-2019-ASSIGNMENTS says "0 problems" although its child
    collections hold 70; P-2J6HK renders its remark before its hint and solution (`STYLE-07`);
    search excerpts cut inside math; collection-mode panes with no values show "No data
    available in table"; `?solution=unsolved` reads as an invalid filter when the count is zero.
    Analysis round 3: `(a)` and `(i)` lists render as `(A)` and `(I)` because the `ol[type]`
    selectors in `site/styles.css` lack the case-sensitive `s` flag; appearance comments
    print a literal `--`; the P-4FH62 sub-part labels run on as one list. The `tikzcd` item
    does not reproduce: all three diagrams render at `5ba163ac9`.
    **Acceptance:** each corrected on the deployed pages. **Closed.**
  - **`ad3-algebra-content`**. **Needs:** none. Wrong mathematics: P-APAS18H invariant-ring
    generators omit $xy(x^2-y^2)$; P-APA22F(a) value; PR-OODAV slogan (an abstract
    $B\cong A\oplus C$ does not split); P-RPSTO(b) fixed-field tower indexed backwards;
    P-WBK5B $k=2$ equation; PR-GV5CF proof covers finite families only; classify-this-module
    $\langle 2,x\rangle$ example does not separate flat from torsion-free.
    CARD-04: T-SZRXI/E-NNTQB/E-DKMHL; E-47X7Y/E-VPWK4; PR-PYYRK/E-BSGSM; T-SVJUN/E-R6I7G;
    FT-ZENUU/T-WRMBM/T-EF2MZ/T-S5T5C; PR-IGLFV/E-6AOD7(b)/FF-C3SN4; PR-73MCN/E-PHSV5;
    T-AILFB/PR-LXSGE; D-ZJJ7G/FD-BPUNZ; E-XH2QU/E-HOJKE/PR-DDDXH/PR-GEHJF; T-6ABNR/FT-BC6S2;
    PR-4GQIZ/PR-GBL6P/PR-OF7ZW; D-HGMOW/D-GIGM2; P-HGRO2/P-HGRO4; P-HGRO7/P-HGRO8/P-HGRO31.
    Page restatements (`THEOREM-01`, `DEF-1`): sylow, the-class-equation, is-this-group-abelian,
    orbit-stabilizer, series-and-solvability, groups-of-small-order, fields/extensions,
    splitting-and-normal, separability, the-correspondence, worked-examples,
    compute-this-galois-group, ideals-and-quotients, domains-and-factorization (valuation ring
    and DVR, D-DEFREGLR), commutative-algebra, number-theory, which-kind-of-ring,
    free-and-projective, classify-this-module, exact-sequences, characters, the-spectral-theorem,
    minimal-and-characteristic-polynomials, determinants-and-eigenvalues, matrix-counterexamples.
    Notation (`NOT-3`): series indexing and the D-BGNME lower central series; `\maxspec` against
    `\mspec` (E-AMD-V3WFKTM6, E-AMD-DCVAD27P, P-W8CJF, E-AMD-EBIC3Z5S); over-a-pid $M_{(p)}$;
    the sylow exponent letter. Titles: E-BAOST (`CARD-01`), P-APAS18D "octogon", P-HGRO* group
    names (`CARD-06`). Screenshots: compute-this-galois-group $S_4$ tables, review-sheet-1
    homework 1 image, minimal-and-characteristic-polynomials long division. Topics
    (`TAXON-01`): the-correspondence, worked-examples. `STYLE-08`: P-ZIMYA, E-XH2QU, E-HOJKE,
    E-VFEWT, E-G4KAC, E-M6J67, P-AMD-QBEEJKCX, E-LJ7PF, P-4XOCE (attribution, $C_x$ notation,
    bullet solution), P-VI6QM literal lists, P-APAS18A–H, P-APA22A–H, P-APAF20A/D/H, the
    P-ALGQUAL18W cards. Scope: E-G4KAC noncommutative on a commutative page; which-kind-of-ring
    Gorenstein section; determinants-and-eigenvalues matrix groups over $F$ linked to
    $\RR$/$\CC$ cards. Sources: SRC-AMHERST-ALGEBRA-STUDY-GUIDE-2016 exam dates in statements
    (`CARD-02`); SRC-HARVARD-GROUPS-ORAL invented sections and institution (and the COMM-ALG
    and FIELDS orals); rings-and-ideals/solutions Gallian headings and MIT pointer; groups
    resources "Chapter N solutions" (`RES-01`). **Acceptance:** each read and repaired, or kept
    with the reason. **Closed.** Merges (survivor first): E-NNTQB/T-SZRXI/E-DKMHL;
    E-47X7Y/E-VPWK4; E-BSGSM/PR-PYYRK (a collection lists E-BSGSM); E-R6I7G/T-SVJUN;
    T-WRMBM, T-EF2MZ, T-S5T5C/FT-ZENUU; PR-73MCN/E-PHSV5; T-AILFB/PR-LXSGE; D-ZJJ7G/FD-BPUNZ;
    E-HOJKE/PR-DDDXH; FT-BC6S2/T-6ABNR; PR-4GQIZ/PR-GBL6P/PR-OF7ZW; D-GIGM2/D-HGMOW. Kept
    apart after reading: E-6AOD7 and PR-IGLFV (PR-IGLFV also classifies the groups; FF-C3SN4
    now cites it); PR-GEHJF loses only its items owned by E-XH2QU and E-HOJKE; P-HGRO2/P-HGRO4
    (P-HGRO2 also counts order 35); P-HGRO7, P-HGRO8, P-HGRO31 (state against two different
    proofs); P-AMD-QBEEJKCX already argues in its QED step. The three oral sources name no
    institution and list Berkeley examiners from the MGSA files, so they are now
    SRC-MGSA-GROUPS-ORAL, SRC-MGSA-COMM-ALG-ORAL and SRC-MGSA-FIELDS-ORAL with no institution
    and one source section each. The homework 1 image became SRC-FIELDS-HOMEWORK-1 (PDF wrapped
    from the retained JPEG, MinerU extraction). `\maxspec` is retired for `\mspec`. The
    Gorenstein section moved to commutative-algebra. Open remainder: SRC-HARVARD-COMPLEX-ORAL
    has the same unsupported institution; the oral PDF and extraction filenames still say
    Harvard; P-FHW1 cards overlap PR-ABSJX, PR-OFBRQ, P-HBWYH and P-JXIIG and need a `CARD-04`
    reading; no card exists for the mod-$p$ irreducibility test, the degree-2-or-3 root test,
    finite extensions of finite fields being Galois, or algebraic closure; the D-2IO6Q
    noncommutative remark has no citation; orbit-stabilizer still restates the element-order
    clause of E-NNTQB.
  - **`ad3-algebra-followups`**. **Needs:** none. The open remainder of `ad3-algebra-content`:
    SRC-HARVARD-COMPLEX-ORAL institution; oral PDF and extraction filenames that say Harvard;
    `CARD-04` reading of the P-FHW1 cards against PR-ABSJX, PR-OFBRQ, P-HBWYH and P-JXIIG;
    statement cards for the mod-$p$ irreducibility test, the degree-2-or-3 root test, finite
    extensions of finite fields being Galois, and algebraic closure; a citation on the D-2IO6Q
    noncommutative remark; the E-NNTQB restatement on orbit-stabilizer. `audited-deployment`
    needs it. **Acceptance:** each read and repaired, or kept with the reason. **Closed.**
    The complex-analysis oral names no institution (MGSA files, McMullen, Calegari), so it is
    SRC-MGSA-COMPLEX-ORAL with one source section; the four oral PDFs and extractions are
    `MGSA_*`. PR-ABSJX merged into P-FHW1-02. Kept apart after reading: P-FHW1-05 (adds the
    characteristic-2 failure) from PR-OFBRQ and P-JXIIG, and P-FHW1-11 from P-HBWYH (adds
    $\alpha^{2020}$). The mod-$p$ test already existed as PR-PB6UE and is now on the
    polynomials page; new cards PR-I1T7M (root test), PR-OGUA5 (finite-field extensions) and
    D-99IUP (algebraic closure). D-2IO6Q cites Hungerford IX.2; orbit-stabilizer drops its
    Lagrange corollary, now carried by E-NNTQB.
  Round 3 (revision `5ba163ac9`, analysis provenance) injected the node below;
  `audited-deployment` needs it.
  - **`ad3-analysis-provenance`**. **Needs:** none. Round-3 analysis findings C1-C4: 16 UCLA
    real-analysis collections list the solution writeup `UCLA_Solutions.pdf` as provenance;
    SRC-UGA-CA-COMPILATION lists maintainer PDFs, wrong section labels and a repeated entry;
    eight UGA complex-analysis collections link dead department PDFs; one PDF is split across
    several collections (Lyall MATH4100-6100 A1-A9, the Wesleyan real- and complex-analysis
    PDFs, Cracking the GRE). **Acceptance:** no collection lists a solution writeup or a
    maintainer PDF; each UGA href resolves to a vendored paper; each PDF is one collection
    whose papers are sections, with every problem link kept. One collection at a time.
  Round 3 (revision `5ba163ac9`, topology and algebraic geometry) injected the node below;
  `audited-deployment` needs it.
  - **`ad3-topology-content`**. **Needs:** none. Wrong mathematics: P-TOPS05A (a free
    involution of $S^{2n}$ need not be the antipodal map; the quotient need not be
    homeomorphic to $\RP^{2n}$); P-TOPS06B title (higher-genus surfaces do cover lower-genus
    ones); P-TOPF23D title ("is" for "is homotopic to");
      wiki/algebraic-geometry/varieties/index.md
    (affine varieties correspond to finitely generated domains, not reduced algebras);
    sheaves-of-modules/projective-sheaves.md (very ample gives an immersion, closed when $X$ is
    proper); cw-complexes RREF row span over $\ZZ$; P-AT75W "$U \in X$"; P-TOPF09C
    $H_*$/$H^*$ hedge. `QUAL-10` proofs of standard results: fundamental-group/theorems.md
    (T-2YTCZ, T-BTPU4, PR-3APOT, PR-OO3DH, PR-EWJMJ), point-set.md tube lemma, homology.md
    PR-6PENU, D-FAIJX Mayer--Vietoris remark, FT-6WPJI corollary proof, FT-M5BHD (twice),
    D-KC4BS Moore spaces; review-page sentences that advertise them. `CARD-04`:
    D-WX7JH/PR-BQKHS (and the D-6CI7D remark that redefines $\tilde M$); D-QP7WI/PR-4X6G2;
    D-6UHU7/D-UH3L5; T-N6PYS/FT-M5BHD; T-TJBYR/PR-ZCUXL(1); PR-UBJ6P/D-BX3WD; T-O44GI/PR-HQE2T;
    D-GFM35/PR-EWJMJ; PR-B6BB2/D-IGUUS proposition; T-NBARV/FF-GBHJL/FF-IEHB2/FF-W3AIU
    (PR-LIXWH); P-FHLRF/P-24CMJ/P-CEVX4; P-VTB25/P-D6JY5/P-6HH2P. `THEOREM-01`, `DEF-1`:
    every topology guide lede in publications/topology-guide.yaml (British spellings too);
    D-WSFYS van Kampen remark; compute-pi-1 and compute-h-star local theorem blocks; AG pages
    what-is-a-scheme, subschemes-and-points, proj-and-gluing, fibre-products-and-base-change,
    the-sheaf-condition, stalks-and-exactness, line-bundles, differentials, canonical-class.
    Pages: topology resources/problems.md links raw PDFs (`RES-01`); point-set.md
    "Separability" heading; notation-and-background degree convention (`NOT-3`);
    the-standard-spaces-notes orphan page; surfaces-and-manifolds stray complex-manifold
    sentence and duplicated T-NBARV sentence; PR-SCHINT link text; covering-spaces diagrams
    (renderer, `ad-tikzcd`). Collections (`SEC-7`, `SOURCE-03`): appearance comments on
    SRC-MALONE-HOUSLEY-TOPOLOGY-PRELIM-ANSWERS-2007, SRC-UGA-TOP-FALL-2004/2009/2012,
    SRC-WESLEYAN-TOP-2004/2014/SUMMER-2008/SUMMER-2011/SUMMER-2013, and the SRC-UNL-MATH871
    grading notes; Perutz, UNL 871 and UT M392C bare section names; Maxim "Poincare Duality ´".
    Card defects: SRC-UGA-TOP-FALL-2013 problem 9 fixed-point title; P-AGXHWSUPPORT alignment;
    P-AGXVARSURFACESING doubled link text; P-WESTOP05-10, P-QUAL-REVIEW-HATCHER-10 and -11
    undefined symbols and in-solution headings; P-AGXHWREDUCED and P-8TF16 part labels.
    Titles (`CARD-01`, `CARD-06`): Malone--Housley imperative titles; raw ASCII TeX titles on
    the UCSD, MAT367, UGA 8230, PhD F08 and workshop collections.
    - Locator titles (`CARD-02`), one card at a time: P-AT75W, P-MAXAT-1-01, P-MAXAT-1-02,
      P-MAXAT-1-03, P-MAXAT-1-04, P-MAXAT-1-05, P-MAXAT-1-06, P-MAXAT-1-07, P-MAXAT-1-08,
      P-MAXAT-1-09, P-MAXAT-1-10, P-MAXAT-1-11, P-MAXAT-1-12, P-MAXAT-1-13, P-MAXAT-2-01,
      P-MAXAT-2-02, P-MAXAT-2-03, P-MAXAT-3-01, P-MAXAT-3-02, P-MAXAT-3-03, P-MAXAT-3-04,
      P-MAXAT-3-05, P-MAXAT-3-06, P-MAXAT-4-01, P-MAXAT-4-02, P-MAXAT-4-03, P-MAXAT-4-04,
      P-MAXAT-4-05, P-MAXAT-4-06, P-MAXAT-4-07, P-MAXAT-4-08, P-MAXAT-4-09, P-MAXAT-4-10,
      P-MAXAT-4-11, P-MAXAT-4-12, P-MAXAT-4-13, P-MAXAT-5-01, P-MAXAT-5-02, P-MAXAT-5-03,
      P-MAXAT-5-04, P-MAXAT-6-01, P-MAXAT-6-02, P-MAXAT-6-03, P-MAXAT-6-04, P-MAXAT-6-05,
      P-MAXAT-6-07, P-MAXAT-6-09, P-MAXAT-6-10, P-MAXAT-6-11, P-MAXAT-6-12, P-MAXAT-6-13,
      P-UNL872S14-10-A-1, P-UNL872S14-10-A-2, P-UNL872S14-10-A-3, P-UNL872S14-10-A-4,
      P-UNL872S14-10-B-1, P-UNL872S14-10-B-2, P-UNL872S14-10-B-3, P-UNL872S14-10-C-1,
      P-UNL872S14-10-C-2, P-UNL872S14-10-C-3, P-UNL872S14-10-C-4, P-UNL872S14-11-B-1,
      P-UNL872S14-11-B-2, P-UNL872S14-11-C-1, P-UNL872S14-11-C-2, P-UNL872S14-11-C-3,
      P-UNL872S14-11-C-4, P-UNL872S14-12-A-1, P-UNL872S14-12-A-2, P-UNL872S14-12-B-1,
      P-UNL872S14-12-B-2, P-UNL872S14-12-B-3, P-UNL872S14-6-A-1, P-UNL872S14-6-A-2,
      P-UNL872S14-6-A-3, P-UNL872S14-6-A-4, P-UNL872S14-6-A-5, P-UNL872S14-6-B-1,
      P-UNL872S14-6-B-2, P-UNL872S14-6-B-3, P-UNL872S14-7-A-1, P-UNL872S14-7-B-1,
      P-UNL872S14-7-B-2, P-UNL872S14-8-A-1, P-UNL872S14-8-A-2, P-UNL872S14-8-A-3,
      P-UNL872S14-8-B-1, P-UNL872S14-8-B-2, P-UNL872S14-8-C-1, P-UNL872S14-9-A-1,
      P-UNL872S14-9-B-1, P-UNL872S14-9-B-2, P-UNL872S14-9-B-3, P-UNL872S14-9-B-4,
      P-UNL872S14-9-C-1, P-UNL872S14-9-C-2, P-UNL872S14-9-C-3, P-UNL872S14-PP-1,
      P-UNL872S14-PP-2, P-UNL872S14-PP-3, P-UNL872S14-PP-4, P-UNL872S14-PP-5.
    - `**Goal**` paragraphs (`STYLE-08`), one card at a time: E-013M4, E-01BSA, E-04W6Q,
      E-069N4, E-0A010, E-0EZ4U, E-0GRG4, E-0K3QV, E-0LZE7, E-0MY4M, E-0NSGA, E-160XR, E-175IG,
      E-18MBF, E-1CMTE, E-1DM8W, E-1P97G, E-1QGID, E-1QY2X, E-1VSTU, E-24TY3, E-29WP0, E-2B91X,
      E-2BCY2, E-2BNJ6, E-2M0XQ, E-2NLYP, E-2P51H, E-2V2VL, E-3BSN7, E-3CFLD, E-3FN03, E-3JLUV,
      E-3KMYL, E-41BN2, E-432BL, E-4349Q, E-44O6O, E-4E1C9, E-4KGM4, E-4PQ1O, E-4RF8O, E-4S8XS,
      E-4TG52, E-4WKOG, E-4WQEM, E-52GF4, E-57O2M, E-5CC0M, E-5DDIL, E-5FLKZ, E-5GHY2, E-5NREC,
      E-5VNUL, E-5VWPC, E-5WDER, E-5Y4F7, E-66MV0, E-6C2JI, E-6RQWT, E-70TGS, E-71YOD, E-73JHB,
      E-74C1G, E-79XXG, E-7GVUH, E-7ML5F, E-81J56, E-873VF, E-8EX2G, E-8HR3A, E-8IBEP, E-8NCA4,
      E-8Q9TN, E-8T3QS, E-8VZD4, E-97HXB, E-99H07, E-9IP2I, E-9LY2B, E-9OT3C, E-9RR0I, E-9TQ6L,
      E-A3WS1, E-A7HJX, E-AGJM5, E-AHENA, E-AL52O, E-CJA01, E-DUQHF, E-E79BA, E-HAT-1.1-11,
      E-HAT-1.2-19, E-HAT-1.2-3, E-HAT-1.2-7, E-HAT-1.3-20, E-HAT-1.3-9, E-HAT-1.B-4,
      E-HAT-2.1-7, E-HAT-2.2-2, E-HAT-2.2-42, E-HAT-2.C-2, E-HAT-3.2-14, E-HAT-4.1-13,
      E-HAT-4.1-18, E-HAT-4.2-5, E-HAT-4.2-8, E-HAT-4.3-19, E-HAT-4.D-6, E-HAT-4.H-4, E-LV54B,
      E-MUN-6-5, E-VFXN4, P-AMD-2AFAX7LD, P-AMD-2GG7VEF2, P-AMD-4DYUOGAJ, P-AMD-5TW33AUF,
      P-AMD-6GFMKZVQ, P-AMD-6KL53YZC, P-AMD-6OJQMSOZ, P-AMD-6QDQY5HT, P-AMD-6RPCGOV7,
      P-AMD-7IWMHJHE, P-AMD-A2CPGINL, P-AMD-ALXD5IQN, P-AMD-AZWPAEUQ, P-AMD-D7IX7C4G,
      P-AMD-DDQM3X6Q, P-AMD-DX7L7EFB, P-AMD-E67LQFU5, P-AMD-EPCKWZSV, P-AMD-ES2H5QQF,
      P-AMD-F7UPRCWM, P-AMD-FW4WE7JA, P-AMD-GEBWFMJF, P-AMD-IUGBCO5R, P-FZIG3, P-KVMKV,
      P-LSJ7W, P-MHQ6A, P-PATOJ, P-SAEXG, P-TOPF08E, P-TOPF09G, P-TOPF20E, P-TOPF20H,
      P-TOPF21C, P-TOPF22E, P-TOPF24G, P-TOPF24H, P-TOPS13B, P-TOPS25G, P-UCTOP-SU09-8,
      P-UCTOP-SU14-7, P-WOFN2.
    - Solutions with no structured proof (`STYLE-08`), one card at a time: P-AGXHWGLOBALSECEX,
      P-AGXHWREDUCED, P-AGXHWSKYSCRAPER, P-AGXHWSUPPORT, P-AGXMISCPRODRATIONAL,
      P-AGXGATHVICLOSURE, P-AGXNSSNONCLOSED, E-MAT367-01, E-PER08-21.3, E-PER08-21.5,
      E-PER08-21.7, E-PER08-23.1, E-PER08-23.4, E-PER08-24.1, E-PER08-24.3, E-PER08-26.2,
      E-PER08-26.3, E-PER08-6.7, E-PER08-7.1, E-PER08-9.3, P-PSTM-01, P-PSTM-02, P-PSTM-03,
      P-PSTM-04, P-PSTM-05, P-PSTM-06, P-TOPF10C, P-DDUA3, P-IWMWM, P-AT75W.

    **Acceptance:** each read and repaired, or kept with the reason.

  Round 3 (revision `5ba163ac9`, site surfaces and prelims) injected the nodes below;
  `audited-deployment` needs both.
  - **`ad3-prelim-content`**. **Needs:** none. F8: prose solutions with no structured proof
    (`STYLE-08`) on P-PRACT20-W3-13, P-PRACT20-W4-06, P-PRACT20-W3-18, P-ALGPAN11-01. F9: wrong
    area on P-PRACT20-W4-06 (`applied-algebra`), P-PRACT20-W3-13 and P-PRACT20-W3-18
    (`real-analysis`). F10: P-ALGPAN11-01 answer choices only in an image (`CARD-03`). F11: the
    20 P-CALCPT3 cards have no topics (`TAXON-01`). F12: wiki/prelim/problems/berkeley-prelims.md
    and ucla-prelims.md link raw PDFs where a collection owns the exam (`RES-01`). F13: prelim
    wiki `order` does not follow wiki/prelim/index.md (`NAV-01`). F14: worked-exams pages hold
    no worked material, and the index link label differs from the page title. F15:
    "$\deg P + 1$ integrations by parts" on useful-tricks.md and which-technique.md.
    **Acceptance:** each read and repaired, or kept with the reason. **Closed.** The worked-exams
    pages are kept and renamed UGA prelim exams; the Berkeley syllabus PDF has no collection
    and stays a PDF link.
  - **`ad3-prelim-practice-areas`**. **Needs:** none. F9 extends past its three cards:
    SRC-PRELIM-PRACTICE-WEEK3-2020 (`real-analysis`), SRC-PRELIM-PRACTICE-WEEK4-2020
    (`applied-algebra`) and the other P-PRACT20-W3-* and P-PRACT20-W4-* cards carry core-qual
    areas for prelim practice drills (COMPLAINTS.md "2020 prelim practice weeks 3 and 4").
    **Acceptance:** each card and both collections read and given the area of the exam track
    they belong to. **Closed.** All 54 cards and both collections are `prelim`.

  Round 3 (revision `5ba163ac9`, real and complex analysis) injected the node below;
  `audited-deployment` needs it.
  - **`ad3-complex-analysis-content`**. **Needs:** none. Wrong mathematics: analytic-nt
    Dirichlet-test proof with the sequences swapped; P-W23PS ($O(R^{1-n})$, two integrals named
    $I$, lost $i$, two solutions); E-NZY3B image; P-CZ3R7 algebra and circle; P-37Z7J identity;
    E-3B2YA intermediate value; P-ER23C Rouché count; maximum-modulus-and-open-mapping $f(U)$;
    E-XQX6X, E-XKMVX Schwarz lemma on the closed disc; T-6F3GO codomain and D-TIHRR
    equicontinuity; P-CASP17A title bounds; complex-week-2-cauchy $\int_{\partial T}$.
    `QUAL-10` wiki proofs: computing-residues, arc-estimates, the-argument-principle,
    rouches-theorem, the-integral-formula, max-modulus, cauchys-theorem, cauchy-estimates,
    maximum-modulus-and-open-mapping, analytic-nt. Process text (`QUAL-08`): P-CASP17A,
    P-CASP15E, P-CASP17D, P-W23PS, P-TIE-S14-03, HARVARD-MATH213A-2017 "(repeats Exercise 3)",
    E-UVNVV and E-QVMUV step prose, Wesleyan complex extractor titles, tips-techs [Eur15].
    Titles (`CARD-01`, `CARD-06`) on the complex UCSD and UGA cards. `CARD-04`: the complex
    groups of the round-3 analysis report, section F. Restatements (`DEF-1`, `RENDER-02`):
    report H1-H8 and H12-H16. `STYLE-04`/`STYLE-08` on the complex cards of report section I.
    Guides: complex guide `parent:` chains (`NAV-01`) and the "grouped by type" ledes.
    **Acceptance:** each read and repaired, or kept with the reason.

  Round 3 (revision `5ba163ac9`, real analysis) injected the node below; `audited-deployment`
  needs it.
  - **`ad3-real-analysis-content`**. **Needs:** none. Wrong mathematics: P-RASP11E title names
    Carleson's theorem; D-2MJRE closure; E-M5MWL interval; P-YIC3K cites the intermediate value
    theorem for the extreme value theorem; the undergraduate notation page $\norm{f}_\infty$
    against D-3PVRB, `\dd` and a double arrow; P-X1WOB(d) vacuous converse. Process text
    (`QUAL-08`, `SEC-7`): "exact existing owner" appearance comments (SRC-AZOFF-PROBLEMS-BY-TOPIC,
    SRC-MATHEMATICAL-TRIVIUM, MATH4100 A1 and A8, Wesleyan summer exams); P-FPWLY; raw Proof and
    Solution on P-I73ZD, P-PUYFS, P-YIC3K; E-QVMUV "two preceding steps"; extractor wording in
    Wesleyan real-analysis titles; P-3SSNK source tag; SRC-RA-WORKSHOP locators in statements
    (D6-10, D4-07, D8-SEQ1) and the room number. Titles (`CARD-01`, `CARD-06`): P-WWNJC, P-XEEUX,
    P-WESRA12-4, P-AEWN6, E-SS4.PR-2, P-FTV4U, UMN, UCLA, UCSD, JHU, Math8100 and UGA
    formula-in-words titles, FT-FZERI, P-RA-WORKSHOP-D8-SEQ1, appendix-unsorted,
    P-RA-WORKSHOP-D3-SEQ-14. `CARD-04`: D-YWRVG/D-3PVRB; PR-XAVMU/FR-7YFAU; T-QBTWN/T-W5SDY;
    PR-A7UFG/PR-PRSKG; FE-LJRG2/FE-VT5N3/FE-BFDRF/FE-3RPMC against PR-TC76W; the PR-2JV43
    example in PR-TC76W; PR-ZI7M3/T-5AALA; P-VO7MI/P-2B2T5/P-8RB01; D-HHVPT/D-WGYSB;
    D-TVKFM/D-KJBAK; D-PAEDW/D-HOKQD; FS-5FKPD/FF-IAUQG; FS-FZL2X/PR-WUZSG; condensation block
    against PR-4EVYE; negation block against FS-THMMW; PR-25GM2/T-YOZX6; FF-AVBFU Lebesgue
    criterion against PR-TDH2A; repeated commuting-limits counterexamples; advice H⊔N bullet
    against PR-PIVFR; P-PCOHF/P-T7IKN; P-5CM5W/P-KC3PY; P-DFDX4/P-RA-WORKSHOP-D8-SEQ1;
    P-UMNCP-F12-01/P-JHUSP02CAF; P-3IDAX/P-ZZO3P; T-AZSCN/FF-IAUQG; T-6F3GO/FF-XZGIY;
    D-PPYCK/D-2CCDB; FD-XUGN3 remark; the Folland exercise list on preface.md and problems.md.
    `QUAL-10` proofs: continuity.md, advice.md, the theorem-list pointer, T-OTR5M, PR-6OHTJ,
    T-MN6WQ, T-RIY2P, T-BFOJT, T-DTXIA, T-4BDE3, T-J3AN3, T-ERNLN, FF-IAUQG, D-YZC3C.
    Restatements (`DEF-1`, `THEOREM-01`): the measure-level pages, undergrad-appendix, week 2,
    sets-and-compactness. `STYLE-04`/`STYLE-08`: typed steps, vacuous QED steps, "a." part
    lists, notation and form on the real-analysis cards of the round-3 report (I1-I16), P-X1WOB
    heading claims. Guides: `NAV-01` parent chains in publications/real-analysis-guide.yaml; the
    workshops guide repeats P-6XW74 and P-KPEPM; the real-analysis-workshop-packet lede cites
    numbers no card shows. **Acceptance:** each read and repaired, or kept with the reason.

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
    reviews, and the page links that collection. **Closed:** ingested as `SRC-CALCULUS-PRACTICE-TEST3`.
  - **`ad-calcpt3-extraction`**. **Closed.** A per-page MinerU Flash extraction of
    calculus_practice_test3.pdf is checked in. Each `P-CALCPT3-*` card and each reused card
    was compared with it. Where they disagree (Questions 9, 11, 43, 44), the page render
    confirms the card.

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
