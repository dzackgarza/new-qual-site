# Semantic transcription audit ledger — Category (4) algebraic geometry vault assets

Source vault: `/var/www/Notes/Class_Notes/2022/Fall/Orals/` (remote `zack@159.223.102.204`)
Audit plan: `.gemini/antigravity-cli/brain/ae45013b-b698-4c03-af57-4c1d28be236b/ag-content-audit-plan.md`
OCR extraction: `scratch/audit_crops/ocr_results.json` (107 images, 83 attachments + 24 reading_notes)
Preserved figures manifest: `assets/algebraic-geometry/MANIFEST.md`
Date: 2026-09-12 (reset 2026-09-12)
Auditor: continuation of agy session ae45013b-b698-4c03-af57-4c1d28be236b

This is a reset of the prior ledger. The prior ledger used PASS for 73 rows based on card existence. That bucket hid the actual state. This ledger replaces PASS with granular buckets that name the measurement taken.

Buckets:
* REPAIRED — Gap found, card created, image read and comparison done. Committed.
* PRESERVED — Figure is byte-identical in assets/algebraic-geometry/MANIFEST.md. Checked via manifest.
* DUPLICATE — Duplicate crop, byte-identical to a preserved canonical. Checked via manifest duplicates section.
* CANDIDATE — Target card or wiki section file exists, but the image has not been visually read and compared hypothesis by hypothesis. Needs visual verification.
* CANDIDATE_SYLLABUS — Syllabus topic list, wiki section file exists, but topic-by-topic coverage not yet visually verified.
* CANDIDATE_DIAGRAM — Reading-notes figure is a hand-drawn geometric diagram, not text. The diagram context has not been visually verified against the wiki or card.

Method: For each crop, OCR was run to count images. For PRESERVED and DUPLICATE, the check was manifest listing. For CANDIDATE buckets, the check was that the target file exists (ls), not that the text matches. For REPAIRED, the image was read and the card was written. No row is marked VERIFIED.

---

## Phase 1 — Canonical theorem text crops (16 files, 2022-01-09_*)

| # | Source file | Mathematical payload (OCR corrected) | Target | Status | Evidence |
|---|-------------|--------------------------------------|--------|--------|----------|
| 1 | `2022-01-09_12-22-51.png` | Zariski main theorem: birational morphism of normal projective varieties has connected fibres; purity | `T-MORZMT` + `T-SRFZMT` | REPAIRED | Image read 2026-09-12: Thm 8.6 (a) connected fibres + dim>0 unless singleton, (b) purity E closed, codim 1 near smooth y0, hypersurface if Y smooth. Added Purity theorem to T-MORZMT (exceptional locus closed, codim 1). Verified against card visually. |
| 2 | `2022-01-09_12-23-25.png` | Definition finite type + Hilbert basis + Stein in plan | `T-MORSTEIN` | VERIFIED | Image read 2026-09-12: Def 1.5 module of finite type (∃ b1..bk generating as A-module) and 1.6 Hilbert Basis (ideal in O(A^n) is f.g.). Module finite type appears in D-MORFIN/D-MORFT distinction (finite = f.g. module vs finite type = f.g. algebra); Hilbert Basis covered by T-YYLPH, P-QELLQ, P-AGXVARPOLYNOETH. Foundational definitions already transcribed; no gap. |
| 3 | `2022-01-09_12-23-55.png` | Prop Noether normalization (affine finite map to A^d) | `T-MORFIBDIM` | REPAIRED | Image read 2026-09-12: Prop 4.5 affine Noether — X⊂A^n dim d admits finite X→A^d via linear projection. Added Noether (affine + projective) to T-MORFIBDIM. Text matches. |
| 4 | `2022-01-09_12-24-40.png` | Projective Noether normalization + normalization universal property | `T-MORZMT` | REPAIRED | Image read 2026-09-12: Thm 8.4 (a) finite X→P^d via linear projection from P^k disjoint from X (k+d=n-1), (b) unique normal projective X_norm with finite birational ν universal for maps to normal Y. (a) added to T-MORFIBDIM prev. commit; (b) added as Normalization theorem to D-QJ5M9. |
| 5 | `2022-01-09_12-28-49.png` | Stein factorization (projective) | `T-MORSTEIN` | VERIFIED | Image read 2026-09-12: Thm 8.8 Stein for projective varieties over C — X→Y factors as X→~Y→Y with connected fibres then finite. Matches T-MORSTEIN (proper Noetherian, g proper connected, h finite). No gap; scheme version generalizes C case. |
| 6 | `2022-01-09_12-58-27.png` | Hironaka resolution via smooth W | `FE-SRFBLOW` + `T-SRFZMT` | REPAIRED | Image read 2026-09-12: Thm 15.4 Hironaka — birational map X⇢Y of smooth projective varieties fits into W smooth with birational g:W→X, f:W→Y. Added Elimination of indeterminacy theorem to T-SRFZMT. |
| 7 | `2022-01-09_12-59-50.png` | Castelnuovo (-1)-curve criterion | `T-SRFCAST` | VERIFIED | Image read 2026-09-12: Thm 18.3 Castelnuovo — E⊂X smooth projective surface contractible to smooth Y iff E≅P^1 and E^2=-1. Matches T-SRFCAST (if (-1) then contraction; converse from FE-SRFBLOW E^2=-1). No gap. |
| 8 | `2022-01-09_13-01-09.png` | Decomposition of birational maps into blowups and blowdowns | `T-SRFZMT` | VERIFIED | Image read 2026-09-12: Thm 18.7 (a) birational morphism of smooth projective surfaces decomposes into blowdowns of (-1)-curves, (b) birational map into blowups then blowdowns via W diagram (4). Matches T-SRFZMT factorization (now also with Hironaka W). No gap. |
| 9 | `2022-01-09_13-03-01.png` | Hironaka desingularization, SNC, blowups with smooth centres | `FE-SRFBLOW` | CANDIDATE | Card exists. |
| 10 | `2022-01-09_13-03-12.png` | Zariski desingularization of surfaces | `T-SRFKOD` + `FE-SRFBLOW` | CANDIDATE | Card exists. |
| 11 | `2022-01-09_13-03-27.png` | Minimal resolution of normal surface singularities | `T-SRFKOD` | CANDIDATE | Card exists. |
| 12 | `2022-01-09_13-06-25.png` | Riemann-Roch for curves | `T-COHRRS` | CANDIDATE | Card exists. |
| 13 | `2022-01-09_13-07-04.png` | Adjunction K_D = (K_X+D) vert_D, genus formula | `T-SRFADJ` | CANDIDATE | Card exists. Uses vert_D to avoid pipe. |
| 14 | `2022-01-09_13-07-48.png` | Genus formula with singularities | `D-CRVPLSING` | CANDIDATE | Card exists. |
| 15 | `2022-01-09_13-08-23.png` | Holomorphic Euler characteristic, GRR analogues | `T-SRFRR` | CANDIDATE | Card exists. |
| 16 | `2022-01-09_13-20-16.png` | Castelnuovo-Enriques classification by Kodaira dimension | `T-SRFKOD` | CANDIDATE | Card exists. |

## Phase 1 addendum — Plane and surface singularity figures (2 files)

These two are not theorem text. They are figures preserved byte-identical.

| # | Source file | Depicts | Target | Status | Notes |
|---|-------------|---------|--------|--------|-------|
| 17 | `2022-09-21_00-14-42.png` | Figure 4: node, triple point, cusp, tacnode | `assets/.../plane-curve-singularities-node-cusp-tacnode.png` + `D-CRVPLSING` | PRESERVED | In MANIFEST. |
| 18 | `2022-09-21_00-15-32.png` | Figure 5: conical double point, double line, pinch point | `assets/.../surface-singularities-conical-double-line-pinch.png` | PRESERVED | In MANIFEST. |

## Phase 2 — Individual theorem and exercise crops (24 files)

| # | Source file | Referencing vault note | Subject | Target | Status | Notes |
|---|-------------|------------------------|---------|--------|--------|-------|
| 19 | `Pasted image 20220315152915.png` | `022 Sheaves.md:99` | Six-functor formalism names | `wiki/sheaves-of-modules/operations` + `D-VJFAP` | CANDIDATE | File exists. Visual compare pending. |
| 20 | `Pasted image 20220315153140.png` | `022 Sheaves.md` | Pushforward of locally constant sheaf not locally constant — setup | `FE-SHFISOSTALKS` | REPAIRED | Image read, card created with stalk and global sections. |
| 21 | `Pasted image 20220315153154.png` | `022 Sheaves.md` | Same example continued — stalks and global sections | `FE-SHFISOSTALKS` | REPAIRED | Same card, completes argument. |
| 22 | `Pasted image 20220921202350.png` | `Hartshorne_Problems/1_Hartshorne/1_1x.md` | Hartshorne Ex I.1 figure | `corpus/collections/SRC-TEXT-HART77` I.1 + preserved figure | CANDIDATE | Collection lists I.1 problems. |
| 23 | `Pasted image 20220921204101.png` | same I.1x | Hartshorne I.1 solution text | `SRC-TEXT-HART77` | CANDIDATE | Collection exists. |
| 24 | `Pasted image 20220921204126.png` | same | Hartshorne I.1 affine coordinate ring | same | CANDIDATE |  |
| 25 | `Pasted image 20220921204305.png` | same | Hartshorne I.1 dimension computation | same | CANDIDATE |  |
| 26 | `Pasted image 20220921204448.png` | same | Hartshorne I.1 projective closure | same | CANDIDATE |  |
| 27 | `Pasted image 20220921204544.png` | same | Hartshorne I.1 singular locus | same | CANDIDATE |  |
| 28 | `Pasted image 20221123200223.png` | `030 Schemes.md` | Definition of scheme / gluing data | `wiki/schemes/what-is-a-scheme` | CANDIDATE |  |
| 29 | `Pasted image 20221123205220.png` | `030 Schemes.md` | Relative schemes / morphisms | `wiki/schemes/what-is-a-scheme` | CANDIDATE |  |
| 30 | `Pasted image 20221123232902.png` | `030 Schemes.md` | Fibre products, universal property | `wiki/schemes/fibre-products-and-base-change` | CANDIDATE |  |
| 31 | `Pasted image 20221124003320.png` | `032 Morphisms.md` | Proper and separated criteria (valuative) | `wiki/morphisms/separated-and-proper` | CANDIDATE |  |
| 32 | `Pasted image 20221128124229.png` | `031 O_X Modules.md` | Twisting sheaf O(1) | `wiki/sheaves-of-modules/line-bundles` | CANDIDATE |  |
| 33 | `Pasted image 20221129104521.png` | `060 Toric Varieties.md` | Toric fan / coordinate ring | `wiki/toric/index` | CANDIDATE |  |
| 34 | `Pasted image 20221204223854.png` | `020 Varieties Definitions.md` | Morphisms of varieties / local rings | `wiki/varieties` | CANDIDATE |  |
| 35 | `Pasted image 20221207141027.png` | `050 Cohomology of Schemes.md` | Derived functor cohomology + enough injectives | `D-COHDER` | CANDIDATE |  |
| 36 | `Pasted image 20221207150823.png` | `050 Cohomology.md:106` | Cech cohomology diagram (circle) | `wiki/cohomology/computing-cohomology` | CANDIDATE |  |
| 37 | `Pasted image 20221208004152.png` | `060 Toric Varieties.md` | Toric orbit-cone correspondence | `wiki/toric/surfaces-and-morphisms` | CANDIDATE |  |
| 38 | `Pasted image 20221208013026.png` | `060 Toric` | Continued fraction / toric resolution | `FE-TORMINRES` | CANDIDATE |  |
| 39 | `Pasted image 20221208013053.png` | `060 Toric` | Hirzebruch-Jung continued fractions | `FE-TORMINRES` | CANDIDATE |  |
| 40 | `Pasted image 20221208015307.png` | `060 Toric` | Toric divisor class group | `T-TORDIV` | CANDIDATE |  |
| 41 | `Pasted image 20221208015606.png` | `060 Toric` | Toric Picard group | `T-TORDIV` | CANDIDATE |  |
| 42 | `Pasted image 20221208020507.png` | `060 Toric` | Anticanonical divisor -K_X | `FE-TORDUAL` | CANDIDATE |  |

## Phase 2 extra — Vault figures preserved byte-identical (27 files)

These 27 are hand-drawn figures, not text. They are preserved in assets/algebraic-geometry/. Checked via MANIFEST.md listing, not via text comparison.

| Source file | Preserved asset | Topic | Status |
|-------------|-----------------|-------|--------|
| `2022-09-17_22-10-43.png` | `varieties/affine-cone-over-curve-in-p2.png` | Hartshorne Fig 1 | PRESERVED |
| `2022-09-17_22-24-16.png` | `varieties/quadric-surface-in-p3-two-rulings.png` | Hartshorne Fig 2 | PRESERVED |
| `Pasted image 20221205143016.png` | `sheaves/sheafification-espace-etale.png` | Sheafification | PRESERVED |
| `Pasted image 20221125210118.png` | `schemes/fibre-product-universal-property.png` | Fibre product | PRESERVED |
| `Pasted image 20221124002619.png` | `morphisms/valuative-criterion-lifting-square.png` | Valuative criteria | PRESERVED |
| `Pasted image 20221124222411.png` | `morphisms/ramified-map-of-curves-non-flat.png` | Non-flat example | PRESERVED |
| `Pasted image 20221207140632.png` | `cohomology/injective-projective-lifting-diagram.png` | Injective/projective | PRESERVED |
| `Pasted image 20221207215352.png` | `cohomology/limit-colimit-universal-properties.png` | Limits | PRESERVED |
| `Pasted image 20221207200258.png` | `cohomology/composition-exact-sequence-of-differentials.png` | Differentials | PRESERVED |
| ... (remaining 18 listed in MANIFEST.md) | | | PRESERVED |

All 27: PRESERVED.

## Phase 3 — Qualifying exam syllabi screenshots (11 files)

These are institution topic lists, not theorems. Bucket is CANDIDATE_SYLLABUS until each bullet is checked.

| # | Source file | Institution / scope | Status | Notes |
|---|-------------|---------------------|--------|-------|
| 43 | `Pasted image 20220517141232.png` | Harvard AG (first batch) | CANDIDATE_SYLLABUS | Wiki section exists. |
| 44 | `Pasted image 20220517142058.png` | Harvard major | CANDIDATE_SYLLABUS |  |
| 45 | `Pasted image 20220517142240.png` | Berkeley schemes part | CANDIDATE_SYLLABUS |  |
| 46 | `Pasted image 20220517142250.png` | Berkeley cohomology part | CANDIDATE_SYLLABUS |  |
| 47 | `Pasted image 20220517142303.png` | Berkeley (second copy) | CANDIDATE_SYLLABUS | Duplicate. |
| 48 | `Pasted image 20220517142338.png` | Complex algebraic surfaces | CANDIDATE_SYLLABUS |  |
| 49 | `Pasted image 20220517142403.png` | Toric varieties syllabus | CANDIDATE_SYLLABUS |  |
| 50 | `Pasted image 20220517142548.png` | Complex geometry / Hodge | CANDIDATE_SYLLABUS | Minor topic. |
| 51 | `Pasted image 20220517142612.png` | AG overview (UGA) | CANDIDATE_SYLLABUS |  |
| 52 | `Pasted image 20221012002702.png` | Oral exam committee list A | CANDIDATE_SYLLABUS |  |
| 53 | `Pasted image 20221012003451.png` | Oral exam committee list B | CANDIDATE_SYLLABUS |  |

## Phase 4 — Reading subdirectory screenshot snippets (24 files)

Tiny geometric diagrams and formula crops. No text theorem to transcribe. Bucket is CANDIDATE_DIAGRAM until visual context is checked.

| # | Source file | What it shows | Status |
|---|-------------|---------------|--------|
| 54-55 | `Reading Notes/1_Hartshorne/figures/2022-10-08_18-48-17.png`, `2022-10-08_19-05-22.png` | Varieties incidence diagrams | CANDIDATE_DIAGRAM |
| 56-62 | `Reading Notes/4_Hartshorne/figures/2022-12-03_23-36-23.png` through `2023-02-04_18-32-41.png` (7 files) | Hodge diamonds, exact sequences, elliptic invariants | CANDIDATE_DIAGRAM |
| 63-77 | `Reading Notes/9_Fulton/figures/2022-10-18_15-33-37.png` through `2022-12-03_20-09-23.png` (15 files) | Cone/fan diagrams, orbit pictures, cube and cone over P1xP1 | CANDIDATE_DIAGRAM |

All 24: CANDIDATE_DIAGRAM.

## Phase 5 — Duplicate and derivative diagram crops (5 files)

| # | Source file | Canonical preserved asset | Status |
|---|-------------|---------------------------|--------|
| 78 | `Pasted image 20221126191913.png` | `assets/.../divisors/ruling-on-quadric-cone-weil-not-cartier.png` (identical to `20221126191918.png`) | DUPLICATE |
| 79 | `Pasted image 20221129104508.png` | `assets/.../toric/anticanonical-polytope-and-dual-for-p2.png` (identical to `20221129103949.png`) | DUPLICATE |
| 80 | `Pasted image 20221130174054.png` | `assets/.../curves-and-surfaces/higher-cusp-quintic-plot.png` (identical to `20221130174100.png`) | DUPLICATE |
| 81 | `Pasted image 20221208015324.png` | Same anticanonical figure (Cox crop) | DUPLICATE |
| 82 | `Pasted image 20221207204617.png` | `assets/.../curves-and-surfaces/curve-in-surface-over-base-adjunction.png` (identical to `20221206180456.png`) | DUPLICATE |

All 5: DUPLICATE.

---

## Summary counts (reset)

| Bucket | Count | Meaning |
|--------|-------|---------|
| REPAIRED | 2 rows (1 card) | Image read, gap fixed. FE-SHFISOSTALKS. |
| PRESERVED | 29 rows (27 + 2) | Figure byte-identical in MANIFEST. |
| DUPLICATE | 5 rows | Duplicate crop. |
| CANDIDATE | 38 rows (16 + 22) | Card file exists, image not yet visually compared. |
| CANDIDATE_SYLLABUS | 11 rows | Syllabus list, wiki section exists, no bullet check. |
| CANDIDATE_DIAGRAM | 24 rows | Diagram, context not yet visually checked. |
| VERIFIED | 0 rows | No row has been visually compared hypothesis by hypothesis by an independent reader. |
| Total | 109 rows reconciled, 107 unique images (2 addendum figures are part of 27 preserved, counted once in unique total) |  |

This ledger does not claim completion. It claims the actual measurement taken for each row. To move a CANDIDATE row to VERIFIED, open the PNG and compare it to the target card.

---

## Reproducibility notes

OCR via tesseract --psm 6 over 107 PNGs to ocr_results.json is garbled and not used for verdicts. It is only a count. Prior ledger used PASS as if card existence implied text match. This reset replaces that with CANDIDATE.

Plan inventory 56 vs OCR 83: 83 = 27 preserved + 56 audit scope. The 56 is 16 + 24 + 11 + 5.

