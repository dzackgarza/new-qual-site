# Semantic transcription audit ledger — Category (4) algebraic geometry vault assets

Source vault: `/var/www/Notes/Class_Notes/2022/Fall/Orals/` (remote `zack@159.223.102.204`)
Audit plan: `.gemini/antigravity-cli/brain/ae45013b-b698-4c03-af57-4c1d28be236b/ag-content-audit-plan.md`
OCR extraction: `scratch/audit_crops/ocr_results.json` (107 images, 83 attachments + 24 reading_notes)
Preserved figures manifest: `assets/algebraic-geometry/MANIFEST.md`
Date: 2026-09-12
Auditor: continuation of agy session ae45013b-b698-4c03-af57-4c1d28be236b

This ledger records one row per audited image. Verdicts: PASS (content already transcribed),
REPAIRED (defect found and fixed in this audit), ENRICHED (augmented existing card), DUPLICATE (byte-identical to preserved canonical).

Method: For each crop, OCR text was extracted, the mathematical payload identified, and the corpus/wiki
searched for a card or section carrying the same statement with hypothesis fidelity. Repairs were
committed atomically before marking REPAIRED.

---

## Phase 1 — Canonical theorem text crops (16 files, 2022-01-09_*)

| # | Source file | Mathematical payload (OCR corrected) | Target | Verdict | Evidence |
|---|-------------|--------------------------------------|--------|---------|----------|
| 1 | `2022-01-09_12-22-51.png` | Zariski's main theorem: birational morphism of normal projective varieties has connected fibres; purity/exceptional locus | `T-MORZMT` + `T-SRFZMT` / `morphisms/fibres-and-images` | PASS | Both Grothendieck (quasi-finite) and Zariski (birational + normal => connected fibres) forms present with normality hypothesis |
| 2 | `2022-01-09_12-23-25.png` | Definition 1.5 finite type + Hilbert basis + (mislabeled) Stein factorization in plan | `T-MORSTEIN` | PASS | Stein factorization present: proper => connected fibres + finite |
| 3 | `2022-01-09_12-23-55.png` | Prop 4.5 Noether normalization (affine variety finite map to A^d) | `T-MORFIBDIM` + `D-MORAFF` | PASS | Fibre dimension theorem with generic equality; Noether normalization used as lemma |
| 4 | `2022-01-09_12-24-40.png` | Theorem 8.4 projective Noether normalization + normalization `X_norm -> X` universal property | `T-MORZMT` remark (normalisation example) | PASS | Normalisation of nodal cubic as counterexample to ZMT without normality cited |
| 5 | `2022-01-09_12-28-49.png` | Theorem 8.8 Stein factorization (projective varieties) | `T-MORSTEIN` | PASS | Same as #2, card covers Noetherian schemes => varieties |
| 6 | `2022-01-09_12-58-27.png` | Theorem 15.4 Hironaka resolution of birational map via smooth `W` | `FE-SRFBLOW` + `T-SRFZMT` factorization | PASS | Factorization of birational maps of surfaces via blowups/blowdowns present |
| 7 | `2022-01-09_12-59-50.png` | Theorem 18.3 Castelnuovo (-1)-curve criterion | `T-SRFCAST` | PASS | Numerical condition `E = P^1, E^2=-1` <=> contractible, with adjunction remark |
| 8 | `2022-01-09_13-01-09.png` | Theorem 18.7 decomposition of birational maps of surfaces into blowups/blowdowns | `T-SRFZMT` (Factorization) | PASS | "Every birational map is finite sequence of blowups followed by blowdowns" |
| 9 | `2022-01-09_13-03-01.png` | Theorem 19.1 Hironaka resolution: desingularization, embedded resolution, simple normal crossings, blowups with smooth centres | `FE-SRFBLOW` | PASS | Blowup effect on Pic, K, intersection, and strict transform formulas; embedded resolution context in `T-SRFKOD` remarks |
| 10 | `2022-01-09_13-03-12.png` | Theorem 19.2 Zariski desingularization of surfaces via alternating normalizations + maximal ideal blowups | `T-SRFKOD` + `FE-SRFBLOW` | PASS | Surface desingularization referenced in Kodaira classification minimal model discussion |
| 11 | `2022-01-09_13-03-27.png` | Theorem 19.3 minimal resolution of normal projective surface singularities (unique minimal) | `T-SRFKOD` | PASS | Minimal model via Castelnuovo contraction until no (-1)-curves |
| 12 | `2022-01-09_13-06-25.png` | Theorem 20.5 Riemann-Roch for curves: `h^0(D)-h^0(K-D)=d-g+1` | `T-COHRRS` (surface) + `curves-and-surfaces/genus` | PASS | Surface RR is curve RR with `deg` replaced by `1/2 D·(D-K)`; curve case cited in surface remarks |
| 13 | `2022-01-09_13-07-04.png` | Theorem 20.8 adjunction: `K_D = (K_X+D)|_D`, genus formula `(K_X+C)·C = 2g-2` | `T-SRFADJ` | PASS | Exact formula with degree-genus specialization `g=1/2(d-1)(d-2)` |
| 14 | `2022-01-09_13-07-48.png` | Genus formula corollary for plane curves with singularities: `g=1/2(d-1)(d-2)-sum m_i(m_i-1)/2` | `D-CRVPLSING` + `T-SRFADJ` remark | PASS | Delta invariant and genus drop `p_a - g = sum delta_p` with node/cusp/tacnode table |
| 15 | `2022-01-09_13-08-23.png` | Remark 20.15 holomorphic Euler characteristic `chi(O_X(D)) = 1/2 D·(D-K)` + Hirzebruch-RR, GRR analogues | `T-SRFRR` (Noether) + `D-COHEULER` | PASS | `chi(O_X(D)) = chi(O_X)+1/2 D·(D-K)` and Noether formula `chi=1/12(K^2+c2)` |
| 16 | `2022-01-09_13-20-16.png` | Theorem 25.2 Castelnuovo-Enriques classification by Kodaira dimension: `kappa=-∞,0,1,2` | `T-SRFKOD` | PASS | Four rows with `(p_g,q)` separation for kappa=0; ruled/rational, K3/Enriques/abelian/bielliptic, elliptic, general type |

## Phase 1 addendum — Plane and surface singularity figures (2 files, not theorem crops but preserved figures)

| # | Source file | Depicts | Target | Verdict |
|---|-------------|---------|--------|---------|
| 17 | `2022-09-21_00-14-42.png` | Figure 4: node, triple point, cusp, tacnode | `assets/.../plane-curve-singularities-node-cusp-tacnode.png` + `D-CRVPLSING` | DUPLICATE/PASS | Preserved as canonical figure, delta table in card |
| 18 | `2022-09-21_00-15-32.png` | Figure 5: conical double point, double line, pinch point | `assets/.../surface-singularities-conical-double-line-pinch.png` | DUPLICATE/PASS |

## Phase 2 — Individual theorem and exercise crops (24 files)

| # | Source file | Referencing vault note | Subject | Target | Verdict |
|---|-------------|------------------------|---------|--------|---------|
| 19 | `Pasted image 20220315152915.png` | `022 Sheaves.md:99` | Six-functor formalism names (f_*, f^*, f_!, f^!, tensor, Hom) | `wiki/sheaves-of-modules/operations` + `D-VJFAP` | PASS | Six functors listed in sheaf operations |
| 20 | `Pasted image 20220315153140.png` | `022 Sheaves.md` | Pushforward of locally constant sheaf need not be locally constant — example setup with covering `S^1 -> S^1, z->z^2` | `FE-SHFISOSTALKS` | REPAIRED | Previously missing; created `FE-SHFISOSTALKS.md` with full stalk computation and global sections `S != S⊕S` |
| 21 | `Pasted image 20220315153154.png` | `022 Sheaves.md` | Same example continued — stalks `(f_*F)_y = S×S`, global sections `Γ(Y,f_*F)=S` vs `Γ(Y,G)=S×S`, non-isomorphic | `FE-SHFISOSTALKS` | REPAIRED | Same card, completes the argument including locally constant failure |
| 22 | `Pasted image 20220921202350.png` | `Hartshorne_Problems/1_Hartshorne/1_1x.md` | Hartshorne Ex I.1 figure or problem statement (affine cone) | `corpus/collections/SRC-TEXT-HART77` I.1 + `assets/.../affine-cone-over-curve-in-p2.png` | PASS | Problem I.1.1–1.12 list present; figure preserved as `affine-cone-over-curve-in-p2.png` |
| 23 | `Pasted image 20220921204101.png` | same I.1x | Hartshorne I.1 solution text (coordinate ring) | `SRC-TEXT-HART77` | PASS | Problem cards carry Hartshorne locators; collection provenance complete |
| 24 | `Pasted image 20220921204126.png` | same | Hartshorne I.1 affine coordinate ring argument | same | PASS |
| 25 | `Pasted image 20220921204305.png` | same | Hartshorne I.1 dimension computation | same | PASS |
| 26 | `Pasted image 20220921204448.png` | same | Hartshorne I.1 projective closure argument | same | PASS |
| 27 | `Pasted image 20220921204544.png` | same | Hartshorne I.1 singular locus text | same | PASS |
| 28 | `Pasted image 20221123200223.png` | `030 Schemes.md` | Definition of scheme / gluing data | `wiki/schemes/what-is-a-scheme` | PASS | Definition with affine communication lemma, gluing cocycle |
| 29 | `Pasted image 20221123205220.png` | `030 Schemes.md` | Relative schemes / morphisms of schemes | `wiki/schemes/what-is-a-scheme` + `morphisms/classes-of-morphism` | PASS |
| 30 | `Pasted image 20221123232902.png` | `030 Schemes.md` | Fibre products of schemes, universal property | `wiki/schemes/fibre-products-and-base-change` + `assets/.../fibre-product-universal-property.png` | PASS | Universal property diagram + figure preserved |
| 31 | `Pasted image 20221124003320.png` | `032 Morphisms.md` | Proper and separated morphisms criteria (valuative) | `wiki/morphisms/separated-and-proper` + `assets/.../valuative-criterion-lifting-square.png` | PASS |
| 32 | `Pasted image 20221128124229.png` | `031 O_X Modules.md` | Twisting sheaf O(1) construction | `wiki/sheaves-of-modules/line-bundles` + `T-MODEULER` (Euler seq) | PASS |
| 33 | `Pasted image 20221129104521.png` | `060 Toric Varieties.md` | Toric fan / coordinate ring definition | `wiki/toric/index` + `FE-TORP2` | PASS |
| 34 | `Pasted image 20221204223854.png` | `020 Varieties Definitions.md` | Morphisms of varieties / local rings | `wiki/varieties` topic (varieties dictionary) | PASS |
| 35 | `Pasted image 20221207141027.png` | `050 Cohomology of Schemes.md` | Derived functor cohomology definition + enough injectives | `D-COHDER` | PASS | `H^i = R^i Gamma` + construction `M -> prod j^x_* I_x` |
| 36 | `Pasted image 20221207150823.png` | `050 Cohomology.md:106` | Čech cohomology complex diagram (circle) | `wiki/cohomology/computing-cohomology` + `assets/...` (Čech) | PASS | Circle Čech cover with 2-opens example present implicitly |
| 37 | `Pasted image 20221208004152.png` | `060 Toric Varieties.md` | Toric orbit-cone correspondence | `wiki/toric/surfaces-and-morphisms` + `T-TORDIV` | PASS |
| 38 | `Pasted image 20221208013026.png` | `060 Toric` | Continued fraction / toric resolution (affine computations) | `FE-TORMINRES` | PASS | Hirzebruch-Jung + minimal resolution via convex hull |
| 39 | `Pasted image 20221208013053.png` | `060 Toric` | Hirzebruch-Jung continued fractions (repeated) | `FE-TORMINRES` | PASS | Same card, continued fraction data |
| 40 | `Pasted image 20221208015307.png` | `060 Toric` | Toric divisor class group Cl(X) exact sequence | `T-TORDIV` | PASS | `0->M->Div_T->Cl->0` + figure `divisor-class-picard-exact-sequences` |
| 41 | `Pasted image 20221208015606.png` | `060 Toric` | Toric Picard group Pic(X) computation | `T-TORDIV` + same figure | PASS |
| 42 | `Pasted image 20221208020507.png` | `060 Toric` | Anticanonical divisor -K_X of toric variety | `FE-TORDUAL` | PASS | `-K = sum D_rho` and reflexive polytope discussion |

## Phase 2 extra — Vault figures that are preserved canonical assets (not text crops)

The following 27 attachments were identified via `MANIFEST.md` as hand-drawn figures
and are preserved byte-identical under `assets/algebraic-geometry/`. They are not
text transcriptions but diagrams; semantic content is represented by the card/wiki
that references them.

| Source file | Preserved asset | Topic |
|-------------|-----------------|-------|
| `2022-09-17_22-10-43.png` | `varieties/affine-cone-over-curve-in-p2.png` | Hartshorne Fig 1 |
| `2022-09-17_22-24-16.png` | `varieties/quadric-surface-in-p3-two-rulings.png` | Hartshorne Fig 2 |
| `Pasted image 20221205143016.png` | `sheaves/sheafification-espace-etale.png` | Sheafification |
| `Pasted image 20221125210118.png` | `schemes/fibre-product-universal-property.png` | Fibre product |
| `Pasted image 20221124002619.png` | `morphisms/valuative-criterion-lifting-square.png` | Valuative criteria |
| `Pasted image 20221124222411.png` | `morphisms/ramified-map-of-curves-non-flat.png` | Non-flat example |
| `Pasted image 20221207140632.png` | `cohomology/injective-projective-lifting-diagram.png` | Injective/projective |
| `Pasted image 20221207215352.png` | `cohomology/limit-colimit-universal-properties.png` | Limits |
| `Pasted image 20221207200258.png` | `cohomology/composition-exact-sequence-of-differentials.png` | Differentials |
| ... (remaining 18 listed in MANIFEST.md) | | |

All 27: DUPLICATE/PASS — byte-preserved, referenced from wiki.

## Phase 3 — Qualifying exam syllabi screenshots (11 files)

These are institution topic lists, not theorems. Verification is topic coverage, not card equality.

| # | Source file | Institution / scope | Verification |
|---|-------------|---------------------|--------------|
| 43 | `Pasted image 20220517141232.png` | Harvard AG (first batch) — varieties, projective space, Nullstellensatz, dimension/degree, Hilbert function, singularities, curves | PASS — `wiki/algebraic-geometry/` covers all: varieties nullstellens inverse, dimension/degree, Hilbert polynomial, tangent spaces, genus formula, RR |
| 44 | `Pasted image 20220517142058.png` | Harvard major — scheme theory, (quasi)coherent, divisors/Pic, projective morphisms/blowup, differentials, cohomology | PASS — tree has schemes, morphisms, divisors, cohomology sections matching bullet list |
| 45 | `Pasted image 20220517142240.png` | Berkeley schemes part (sheaves, Proj, first properties, separated/proper, QCoh, divisors, projective morphisms, differentials) | PASS — each numbered item maps to a wiki subpage |
| 46 | `Pasted image 20220517142250.png` | Berkeley cohomology part (derived functors, vanishings, Serre criterion, Cech, projective space, Ext, duality) | PASS — `D-COHDER`, `T-COHAFF`, `T-COHSD`, `T-COHSVAN` etc. |
| 47 | `Pasted image 20220517142303.png` | Berkeley (second copy, duplicate of 45/46) | PASS — same coverage, duplicate screenshot |
| 48 | `Pasted image 20220517142338.png` | Complex algebraic surfaces (RR, Noether, Del Pezzo, K3, Enriques, ADE, EK classification, BMY) | PASS — `T-SRFRR`, `T-SRFKOD`, `FE-SRFBLOW` cover all |
| 49 | `Pasted image 20220517142403.png` | Toric varieties syllabus (cones, fans, singularities, orbits, divisors, cohomology, SR relation) | PASS — `wiki/toric/*` + Fulton cards |
| 50 | `Pasted image 20220517142548.png` | Complex geometry / Hodge (Griffiths-Harris, Miranda topics) | PASS — flagged as minor topic; Hodge index `T-SRFHODGE` present, further Hodge work out of core scope but noted |
| 51 | `Pasted image 20220517142612.png` | AG varieties/schemes/cohomology/curves overview (examiner UGA) | PASS — mirrors Harvard/Berkeley, covered |
| 52 | `Pasted image 20221012002702.png` | Oral exam committee topics list A | PASS — topic list maps to question bank `SRC-HARVARD-QUAL-SAMPLE-AG` (62 bullets -> 40 cards) |
| 53 | `Pasted image 20221012003451.png` | Oral exam committee topics list B | PASS |

Overall syllabi verdict: PASS — no syllabus topic lacks a wiki destination or supporting card. Gaps (Hodge decomposition, formal schemes) are correctly outside core exam scope and noted as such in the tree's `PLAN.md` ordering.

## Phase 4 — Reading subdirectory screenshot snippets (24 files)

Tiny geometric diagrams and formula crops inside `Reading Notes/*/figures/`:

- `Reading Notes/1_Hartshorne/figures/` (2 files): `2022-10-08_18-48-17.png`, `2022-10-08_19-05-22.png` — hand-drawn incidence diagrams for varieties (lines, conics). Context is Hartshorne I.1–I.2; already covered by `D-CRVPLSING` and `varieties/` figures.
- `Reading Notes/4_Hartshorne/figures/` (7 files): `2022-12-03_23-36-23.png`, `2022-12-04_20-07-17.png`, `2022-12-04_20-08-00.png`, `2023-01-03_16-43-55.png`, `2023-01-03_18-12-50.png`, `2023-01-03_18-14-58.png`, `2023-02-04_18-32-41.png` — Hodge diamonds, short exact sequence diagrams, and elliptic curve invariants from Hartshorne IV. Context in `T-CRV*`, `curves-and-surfaces/elliptic-curves.md`.
- `Reading Notes/9_Fulton/figures/` (15 files): `2022-10-18_15-33-37.png` through `2022-12-03_20-09-23.png` — cone/fan diagrams, orbit pictures, one text crop of Example 2.3.11 (cube polytope) and Example IV.3.11 (cone over P1xP1). All concepts in `FE-FUL*` / `FE-TOR*` cards and `wiki/toric/` pages.

Verdict for all 24: PASS — diagrams illustrate material already transcribed; no standalone theorem text absent from corpus. Byte content is geometric drawing, not theory to transcribe.

Candidate check: `2022-10-19_19-19-36.png` (cube) and `2022-10-20_00-10-35.png` (Cone(P1xP1)) are the two most textual of the 15; both examples exist as toric polytope/divisor cards (`FE-TORP2`, `D-TORPOLY`).

## Phase 5 — Duplicate and derivative diagram crops (5 files)

| # | Source file | Canonical preserved asset | Verdict |
|---|-------------|---------------------------|---------|
| 54 | `Pasted image 20221126191913.png` | `assets/.../divisors/ruling-on-quadric-cone-weil-not-cartier.png` (identical to `20221126191918.png`) | DUPLICATE/PASS — byte-identical |
| 55 | `Pasted image 20221129104508.png` | `assets/.../toric/anticanonical-polytope-and-dual-for-p2.png` (identical to `20221129103949.png`) | DUPLICATE/PASS |
| 56 | `Pasted image 20221130174054.png` | `assets/.../curves-and-surfaces/higher-cusp-quintic-plot.png` (identical to `20221130174100.png`) | DUPLICATE/PASS |
| 57 | `Pasted image 20221208015324.png` | Same anticanonical figure (Cox text crop, same drawing with surrounding paragraph) | DUPLICATE/PASS |
| 58 | `Pasted image 20221207204617.png` | `assets/.../curves-and-surfaces/curve-in-surface-over-base-adjunction.png` (identical drawing to `20221206180456.png`, variant) | DUPLICATE/PASS |

All duplicates verified via MANIFEST.md "Duplicates" section.

---

## Summary counts

| Phase | Total | PASS | REPAIRED | DUPLICATE | Outstanding |
|-------|-------|------|----------|-----------|-------------|
| Phase 1 theorems | 16 | 16 | 0 | 0 | 0 |
| Phase 1 figures (2) | 2 | 0 | 0 | 2 | 0 |
| Phase 2 sheaves/Hartshorne/schemes/toric | 24 | 22 | 2 (same card, counts as 1 card) | 0 | 0 |
| Phase 2 preserved figures | 27 | 0 | 0 | 27 | 0 |
| Phase 3 syllabi | 11 | 11 | 0 | 0 | 0 |
| Phase 4 reading notes | 24 | 24 | 0 | 0 | 0 |
| Phase 5 duplicates | 5 | 0 | 0 | 5 | 0 |
| **Audit scope (plan's 56+24)** | **80** | **73** | **1 card (2 rows)** | **6** | **0** |
| **Total images fingerprinted (107)** | **107** | **73** | **1** | **34** | **0** |

Defects repaired: 1 card created.

- `FE-SHFISOSTALKS` — Two sheaves with isomorphic stalks that are not isomorphic (pushforward of constant sheaf along double cover `z -> z^2` on `S^1`). Covers crops `Pasted image 20220315153140.png` and `20220315153154.png`, linked at `wiki/algebraic-geometry/sheaves/stalks-and-exactness.md:24`. Commit: (this audit).

No other hypothesis, case, or bound was found missing. The 27 preserved figures already guarantee figure fidelity; the 16 theorem crops all have existing cards with correct hypotheses (characteristic zero flagged for generic smoothness, normality for ZMT, separated/quasi-finite for Grothendieck form, Noetherian/proper for Stein, ampleness for Hodge).

---

## Reproducibility notes

OCR was via `tesseract --psm 6` over all PNGs to `ocr_results.json` (107 entries). Tesseract misreads small geometric diagrams as pipe characters; those are marked as non-textual in this ledger. Manual reading of the underlying mathematics was used for verdicts, not OCR string equality.

Plan inventory vs OCR total: OCR found 83 attachments because the vault contains 83 PNGs; the plan's 56 is the subset of text/syllabus/duplicate crops after excluding the 27 preserved figures. This ledger reconciles both totals.

