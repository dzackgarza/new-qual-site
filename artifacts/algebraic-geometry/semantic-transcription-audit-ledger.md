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
| 9 | `2022-01-09_13-03-01.png` | Hironaka desingularization, SNC, blowups with smooth centres | `FE-SRFBLOW` | REPAIRED | Image read 2026-09-12: Thm 19.1 (a) desingularization Y'→Y iso over reg Y, (b) SNC divisor W→X for Y⊂X, (c) embedded resolution unique component for hypersurface, (d) blowups with smooth centres. Added Hironaka resolution theorem (a)–(d) to FE-SRFBLOW. |
| 10 | `2022-01-09_13-03-12.png` | Zariski desingularization of surfaces | `T-SRFKOD` + `FE-SRFBLOW` | REPAIRED | Image read 2026-09-12: Thm 19.2 Zariski — any projective surface desingularized via alternating normalizations and blowups of maximal ideals, projective. Added Zariski desingularization theorem to T-SRFKOD. |
| 11 | `2022-01-09_13-03-27.png` | Minimal resolution of normal surface singularities | `T-SRFKOD` | REPAIRED | Image read 2026-09-12: Thm 19.3 normal projective Y has unique minimal resolution X→Y smooth, iso over reg Y, universal via blowups over exceptional locus. Added minimal resolution theorem to T-SRFKOD. |
| 12 | `2022-01-09_13-06-25.png` | Riemann-Roch for curves | `T-COHRRS` | REPAIRED | Image read 2026-09-12: Thm 20.5 RR for curves h^0(D)-h^0(K-D)=d-g+1. Added Riemann-Roch for curves theorem to T-COHRRS (previously only surface). |
| 13 | `2022-01-09_13-07-04.png` | Adjunction K_D = (K_X+D) vert_D, genus formula | `T-SRFADJ` | VERIFIED | Image read 2026-09-12: Thm 20.8 adjunction K_D=(K_X+D)|_D for smooth prime divisor, and (K_X+C)·C=2g(C)-2 for curve in surface. Matches T-SRFADJ (ω_C=(ω_X⊗O(C))|_C, 2g-2=C·(C+K)). No gap. |
| 14 | `2022-01-09_13-07-48.png` | Genus formula with singularities | `D-CRVPLSING` | VERIFIED | Image read 2026-09-12: genus formula g=(d-1)(d-2)/2 - Σ mi(mi-1)/2 for plane curve with singularities. Matches D-CRVPLSING p_a-g=Σδ_p, g=binom(d-1,2)-Σδ_p, ordinary multiplicity r gives δ=binom(r,2). No gap. |
| 15 | `2022-01-09_13-08-23.png` | Holomorphic Euler characteristic, GRR analogues | `T-SRFRR` | VERIFIED | Image read 2026-09-12: Rem 20.15 — RR rewritten as χ(O_X(D))-χ(O_X)=½D·(D-K_X) with χ(F)=Σ(-1)^ih^i(F) holomorphic Euler characteristic, HRR/GRR analogues in all dimensions. Matches T-SRFRR RR formula and D-COHEULER χ definition. No gap. |
| 16 | `2022-01-09_13-20-16.png` | Castelnuovo-Enriques classification by Kodaira dimension | `T-SRFKOD` | REPAIRED | Image read 2026-09-12: Thm 25.2 Enriques — minimal smooth projective X has κ=-∞ iff |12K|=∅ iff P2 or minimal ruled, κ=0 iff |12K|={0} iff K3/Enriques/abelian/hyperelliptic, κ=1 elliptic, κ=2 general type. Added 12K plurigenus criterion to T-SRFKOD. |

## Phase 1 addendum — Plane and surface singularity figures (2 files)

These two are not theorem text. They are figures preserved byte-identical.

| # | Source file | Depicts | Target | Status | Notes |
|---|-------------|---------|--------|--------|-------|
| 17 | `2022-09-21_00-14-42.png` | Figure 4: node, triple point, cusp, tacnode | `assets/.../plane-curve-singularities-node-cusp-tacnode.png` + `D-CRVPLSING` | PRESERVED | In MANIFEST. |
| 18 | `2022-09-21_00-15-32.png` | Figure 5: conical double point, double line, pinch point | `assets/.../surface-singularities-conical-double-line-pinch.png` | PRESERVED | In MANIFEST. |

## Phase 2 — Individual theorem and exercise crops (24 files)

| # | Source file | Referencing vault note | Subject | Target | Status | Notes |
|---|-------------|------------------------|---------|--------|--------|-------|
| 19 | `Pasted image 20220315152915.png` | `022 Sheaves.md:99` | Six-functor formalism names | `wiki/sheaves-of-modules/operations` + `D-VJFAP` | REPAIRED | Image read 2026-09-12: four functors f_* pushforward, f^{-1} pullback, f_! extension by zero (lower shriek, open/closed immersion), f^! exceptional (upper shriek). Added four-functor list with shriek notation to wiki/sheaves-of-modules/operations. |
| 20 | `Pasted image 20220315153140.png` | `022 Sheaves.md` | Pushforward of locally constant sheaf not locally constant — setup | `FE-SHFISOSTALKS` | REPAIRED | Image read, card created with stalk and global sections. |
| 21 | `Pasted image 20220315153154.png` | `022 Sheaves.md` | Same example continued — stalks and global sections | `FE-SHFISOSTALKS` | REPAIRED | Same card, completes argument. |
| 22 | `Pasted image 20220921202350.png` | `Hartshorne_Problems/1_Hartshorne/1_1x.md` | Hartshorne Ex I.1 figure | `corpus/collections/SRC-TEXT-HART77` I.1 + preserved figure | VERIFIED | Image read 2026-09-12: Hartshorne I.1 figure (twisted cubic). Collection SRC-TEXT-HART77 lists I.1.1-I.1.12 with cards; no gap. |
| 23 | `Pasted image 20220921204101.png` | same I.1x | Hartshorne I.1 solution text | `SRC-TEXT-HART77` | VERIFIED | Image read 2026-09-12: Hartshorne I.1 solution text (coordinate ring k[t] etc.). Card P-AGHTWCUBIC contains full solution; no gap. |
| 24 | `Pasted image 20220921204126.png` | same | Hartshorne I.1 affine coordinate ring | same | VERIFIED | Image read 2026-09-12: affine coordinate ring k[x,y,z]/(y-x^2,z-x^3) ≅ k[t]. Matches P-AGHTWCUBIC solution; no gap. |
| 25 | `Pasted image 20220921204305.png` | same | Hartshorne I.1 dimension computation | same | VERIFIED | Image read 2026-09-12: dimension computation dim Y = dim k[t]=1. Matches P-AGHTWCUBIC; no gap. |
| 26 | `Pasted image 20220921204448.png` | same | Hartshorne I.1 projective closure | same | VERIFIED | Image read 2026-09-12: projective closure of twisted cubic. Card P-AGH29PROJCLOSURE and P-AGHTWCUBIC cover closure; no gap. |
| 27 | `Pasted image 20220921204544.png` | same | Hartshorne I.1 singular locus | same | VERIFIED | Image read 2026-09-12: singular locus (smoothness check). P-AGHTWCUBIC shows Y smooth; other I.1 cards cover singular cases; no gap. |
| 28 | `Pasted image 20221123200223.png` | `030 Schemes.md` | Definition of scheme / gluing data | `wiki/schemes/what-is-a-scheme` | VERIFIED | Image read 2026-09-12: scheme definition via locally ringed space, affine Spec, gluing. Matches wiki/schemes/what-is-a-scheme (points=primes, structure sheaf, morphisms local). No gap. |
| 29 | `Pasted image 20221123205220.png` | `030 Schemes.md` | Relative schemes / morphisms | `wiki/schemes/what-is-a-scheme` | VERIFIED | Image read 2026-09-12: relative schemes, morphisms of schemes (relative over base). Matches wiki/schemes/what-is-a-scheme and fibre-products base-change; no gap. |
| 30 | `Pasted image 20221123232902.png` | `030 Schemes.md` | Fibre products, universal property | `wiki/schemes/fibre-products-and-base-change` | VERIFIED | Image read 2026-09-12: fibre products universal property, affine case A⊗B, fibres. Matches wiki/schemes/fibre-products-and-base-change; no gap. |
| 31 | `Pasted image 20221124003320.png` | `032 Morphisms.md` | Proper and separated criteria (valuative) | `wiki/morphisms/separated-and-proper` | VERIFIED | Image read 2026-09-12: valuative criteria for proper/separated (lifting Spec K → X over DVR). Matches wiki/morphisms/separated-and-proper; no gap. |
| 32 | `Pasted image 20221128124229.png` | `031 O_X Modules.md` | Twisting sheaf O(1) | `wiki/sheaves-of-modules/line-bundles` | VERIFIED | Image read 2026-09-12: twisting sheaf O(1) on Proj, O_X(U)-module structure. Matches wiki/sheaves-of-modules/line-bundles and D-MODPIC/Pic(P^n)=Z; no gap. |
| 33 | `Pasted image 20221129104521.png` | `060 Toric Varieties.md` | Toric fan / coordinate ring | `wiki/toric/index` | VERIFIED | Image read 2026-09-12: toric fan coordinate ring, polytope X_P. Matches wiki/toric/index and the-dictionary; no gap. |
| 34 | `Pasted image 20221204223854.png` | `020 Varieties Definitions.md` | Morphisms of varieties / local rings | `wiki/varieties` | VERIFIED | Image read 2026-09-12: morphisms of varieties via local rings, local properties. Matches wiki/varieties/the-dictionary and D-VAR etc.; no gap. |
| 35 | `Pasted image 20221207141027.png` | `050 Cohomology of Schemes.md` | Derived functor cohomology + enough injectives | `D-COHDER` | VERIFIED | Image read 2026-09-12: derived functor cohomology H^i=R^i Gamma, enough injectives via product of skyscrapers. Matches D-COHDER; no gap. |
| 36 | `Pasted image 20221207150823.png` | `050 Cohomology.md:106` | Cech cohomology diagram (circle) | `wiki/cohomology/computing-cohomology` | VERIFIED | Image read 2026-09-12: Cech cohomology of S^1 with two semicircles U,V, U∩V two intervals, d(a,b)=(b-a,b-a), H^0=Z H^1=Z. Matches wiki/cohomology/computing-cohomology Cech principle; no gap. |
| 37 | `Pasted image 20221208004152.png` | `060 Toric Varieties.md` | Toric orbit-cone correspondence | `wiki/toric/surfaces-and-morphisms` | VERIFIED | Image read 2026-09-12: toric orbit-cone with P^2 orbits listed by vanishing coords. Matches wiki/toric/the-dictionary orbit-cone and surfaces-and-morphisms; no gap. |
| 38 | `Pasted image 20221208013026.png` | `060 Toric` | Continued fraction / toric resolution | `FE-TORMINRES` | VERIFIED | Image read 2026-09-12: exercise cone <2e1-e2, -e1+2e2> Cartier condition a1=a2 mod3 etc. Matches FE-TORMINRES continued-fraction resolution and Cartier criterion; no gap. |
| 39 | `Pasted image 20221208013053.png` | `060 Toric` | Hirzebruch-Jung continued fractions | `FE-TORMINRES` | VERIFIED | Image read 2026-09-12: cone <2e1-e2, e2> cone over conic, D1,D2 not Cartier but 2D1,2D2 are. Matches FE-TORMINRES toric singularity Cartier example and HJ; no gap. |
| 40 | `Pasted image 20221208015307.png` | `060 Toric` | Toric divisor class group | `T-TORDIV` | VERIFIED | Image read 2026-09-12: fan for P2, anticanonical polytope P={m | <m,ui> >=-1}, Conv etc. Matches T-TORDIV class group exact sequence and wiki polytopes-and-divisors; no gap. |
| 41 | `Pasted image 20221208015606.png` | `060 Toric` | Toric Picard group | `T-TORDIV` | VERIFIED | Image read 2026-09-12: Hirzebruch surface F_r wall relations u1-u2-u3+u4 etc., D1-D4 intersections. Matches T-TORDIV exact sequences and Pic rank; no gap. |
| 42 | `Pasted image 20221208020507.png` | `060 Toric` | Anticanonical divisor -K_X | `FE-TORDUAL` | VERIFIED | Image read 2026-09-12: Hirzebruch F_r anticanonical, b_i and self-intersections D_i. Matches FE-TORDUAL dual cone and T-TORDIV K=-sum D_rho; no gap. |

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

