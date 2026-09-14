# Document queue E: Source documents without collection cards

This queue inventories 354 vendored PDF sources that lacked collection cards when the queue was created.
Checked entries have since been dispositioned; unchecked entries still require intake.
All 354 were extracted to full markdown and read for the inventory.
Classification below is by document content, and each entry links to the extraction with line count, problem count, institution, subject, and date where identifiable.

Per AGENTS.md, the PDF is the provenance.
For an unchecked problem-bearing source, the remaining work is to create or reconcile the collection and extract/reuse its problem cards.
For reference-only material, intake may stop at bibliography/enrichment rather than manufacturing problem cards.

The #81 resource-page audit uses this as the sole backlog for vendored resource PDFs: every vendored PDF still linked from a subject resource page is either already collection provenance or has an entry here.
External links that are not vendored remain on the resource pages until a deliberate intake pass brings them into `assets/attachments/`.

## Qualifying exams (76)

- [ ] [8155-starter-problems.pdf](assets/attachments/extracted/8155-starter-problems.md) (59L, 7 problems) — applied-algebra

- [ ] [8210 Lecture Notes (Usher) Smooth Manifolds.pdf](assets/attachments/extracted/8210 Lecture Notes (Usher) Smooth Manifolds.md) (2574L, 5 problems) — UNL — alg-geom — FALL 2011

- [ ] [871-872January_2004_871-953.pdf](assets/attachments/extracted/871-872January_2004_871-953.md) (33L, 10 problems) — alg-geom

- [ ] [871-872January_2008_850-871.pdf](assets/attachments/extracted/871-872January_2008_850-871.md) (73L, 0 problems) — applied-algebra

- [x] [analysis_2003-2007.pdf](assets/attachments/extracted/analysis_2003-2007.md) (611L, 76 problems) — Wesleyan — analysis compilation — 2003–2007 — disposition 2026-09-14: reconciled from a fresh deterministic MinerU Flash extraction in commit `b0e08aa6d`. The retained packet contains 95 unique source positions: 45 real-analysis positions (2003–2007, with the 2006 sitting duplicated verbatim in the packet) and 50 complex-analysis positions (2004–2007). Canonical Wesleyan sitting collections represent every position; exact repeats reuse existing owners, and unresolved extraction glyphs are recorded explicitly rather than guessed. The inventory's `76 problems`, `applied-algebra`, and single-date labels were stale heuristic metadata.

- [x] [analysis_2008-2013.pdf](assets/attachments/extracted/analysis_2008-2013.md) (727L, 111 problems) — Wesleyan — analysis compilation — 2008–2013 — disposition 2026-09-14: reconciled from deterministic MinerU Flash in commit `f51240c6f`. The packet contains 122 numbered source positions across fourteen real/complex-analysis sittings: 2008, 2009, 2010, 2011, 2012, June 2013, and supplemental/August 2013. Canonical Wesleyan sitting collections represent all 122 positions; exact repeated statements reuse canonical cards and unresolved Flash defects remain explicit. The inventory's `111 problems`, `applied-algebra`, and single-sitting label were stale heuristic metadata.

- [x] [analysis_2014-2016.pdf](assets/attachments/extracted/analysis_2014-2016.md) (245L, 12 problems) — Wesleyan — analysis compilation — 2014–2016 — disposition 2026-09-14: reconciled from deterministic MinerU Flash in commit `5e7c0bfb4`. The retained eight-page packet has 33 represented source positions across five sittings: 2016 Complex (8), July 2016 Real (8), July 2015 Real (5 retained statements), July 2015 Complex (4 retained statements), and July 2014 Real (8). The 2015 instructions advertise 7 real and 8 complex problems, but the retained source contains only 5 and 4 statements respectively; absent problems were not invented. The inventory's `12 problems` and `topology` labels were stale heuristic metadata.

- [x] [analysis_jan2014.pdf](assets/attachments/extracted/analysis_jan2014.md) (39L, 12 problems) — Duke — real-analysis — Winter 2014 — disposition 2026-09-09: ingested as `SRC-DUKE-BASIC-ANALYSIS-WINTER-2014`; all twelve problems are represented in source order by solved, source-checked cards `P-DUKEBA14-1` through `P-DUKEBA14-12`.

- [x] [Applied-Algebra-FA17.pdf](assets/attachments/extracted/Applied-Algebra-FA17.md) (71L, 8 problems) — applied-algebra Disposition 2026-09-01: the collection SRC-UCSD-APALG-FALL-2017 already exists, complete, and its eight cards match the extracted paper in source order.
  The vendored paper added to provenance beside the department URL. One card was in doubt and is now settled by reading the mathematics rather than the file.
  P-APAF17C states "if $A-B$ is positive definite" where the extraction reads "$A \otimes B$". Under the standing hypotheses both matrices are already symmetric positive definite, so the Kronecker product $A \otimes B$ is positive definite automatically, as is the Hadamard product by the Schur product theorem; either reading makes the conditional do no work.
  $A-B$ is a genuine extra hypothesis and yields the standard question.
  The card's reading is the only one that states a problem, so it stands.
  The extraction is not reliable at single glyphs here: the same run dropped `$\sigma$` to a bare space in problem 6(c).

- [x] [Azoff Problems by Topic.pdf](assets/attachments/extracted/Azoff Problems by Topic.md) (363L, 88 problems) — UGA — complex-analysis — disposition 2026-09-14: ingested as `SRC-AZOFF-PROBLEMS-BY-TOPIC` in commit `8f9f8a19d` from a fresh deterministic MinerU Flash extraction. The packet contains 89 source positions across nine topic blocks; 74 source-owned cards represent genuine gaps and 15 exact existing canonical statements are reused. Concrete extraction defects are documented on affected cards. The inventory count of 88 was stale.

- [x] [Basic_Linear_Algebra_Review.pdf](assets/attachments/extracted/Basic_Linear_Algebra_Review.md) (559L, 47 problems) — linear algebra review sheet — disposition 2026-09-14: ingested as `SRC-BASIC-LINEAR-ALGEBRA-REVIEW` in commit `4db24ca57`. The source is predominantly expository Math 150-01 review notes; its final Review Problems section contains exactly seven numbered source problems, all represented by `P-BLAR-01` through `P-BLAR-07`. Definitions and worked examples remain reference material rather than artificial problem cards. The inventory count of 47 was a false positive from expository numbering/list structure.

- [x] [Big_List_of_Math_Problems.pdf](assets/attachments/extracted/Big_List_of_Math_Problems.md) (1966L, 249 problems) — *Mathematical Trivium* problem compilation — disposition 2026-09-14: ingested as `SRC-MATHEMATICAL-TRIVIUM` in commit `18241b134` from a 32-page deterministic MinerU Flash baseline. The source has 243 numbered positions across Linear Algebra (48), Real Analysis (62), Complex Analysis (34), Variational Principle (15), Differential Equations (51), and Probability (33). 242 source-owned cards plus exact reuse of `P-BKS04-7A` represent all positions; figure/extraction gaps are explicit. The inventory's `249 problems` and `alg-geom` labels were stale heuristics.

- [x] [cambride_analysis_ii.pdf](assets/attachments/extracted/cambride_analysis_ii.md) (4136L, 13 problems) — Cambridge — real-analysis — Michaelmas 2015 — disposition 2026-09-14: reference-only intake. A fresh 79-page deterministic MinerU Flash extraction identifies Dexter Chua's *Part IB — Analysis II*, based on lectures by N. Wickramasekera. The source is expository course notes (definitions, theorems, examples, and proofs) with occasional references to separate example sheets, not an authored problem collection; no cards are manufactured. The retained PDF is enriched on `wiki/real-analysis/resources/books-notes.md`. The inventory's `13 problems`, `UNL`, and `applied-algebra` labels were stale heuristics.

- [x] [Ch9Sltns.pdf](assets/attachments/extracted/Ch9Sltns.md) (161L, 0 problems) — algebra — factor groups — disposition 2026-09-14: problem-bearing solution packet ingested as `SRC-CH9-FACTOR-GROUP-SOLUTIONS`. A fresh six-page deterministic MinerU Flash baseline contains 28 sparse-numbered problem prompts: 25 Chapter 9 problems and three Team Problem Solutions. The prompts are represented as canonical cards; the worked answers remain in the retained PDF rather than being duplicated. The existing group-theory resource now points to the collection. The inventory's `0 problems` and `applied-algebra` labels were stale heuristics.

- [ ] [chapter-2.pdf](assets/attachments/extracted/chapter-2.md) (275L, 18 problems) — calculus **OCR: image placeholders**

- [ ] [Chapter-7.pdf](assets/attachments/extracted/Chapter-7.md) (259L, 21 problems) — UNL — complex-analysis **OCR: image placeholders**

- [ ] [Complex_Analysis_Exam_Prep_Solutions.pdf](assets/attachments/extracted/Complex_Analysis_Exam_Prep_Solutions.md) (237L, 14 problems) — complex-analysis

- [ ] [complex.pdf](assets/attachments/extracted/complex.md) (2307L, 0 problems) — UNL — applied-algebra — Spring 19

- [x] [Conrad_-_SOME_EXAMPLES_OF_THE_GALOIS_CORRESPONDENCE.pdf](assets/attachments/Conrad_-_SOME_EXAMPLES_OF_THE_GALOIS_CORRESPONDENCE_extracted.md) (174L, reference-only) — algebra — disposition 2026-09-14: deterministic MinerU Flash extraction is byte-identical to the retained extraction. Keith Conrad's note consists of five worked examples of the Galois correspondence and fixed-field/subgroup calculations, with only an inline exercise-style check rather than a standalone problem set. It is already routed through `wiki/algebra/resources/fields.md`; no duplicate problem collection is manufactured.

- [ ] [Cracking_the_GRE_Mathematics_Subject.pdf](assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md) (14062L, 722 problems) — UCSD — alg-geom

- [ ] [day_3_sep_counterex_defn.pdf](assets/attachments/extracted/day_3_sep_counterex_defn.md) (85L, 11 problems) — topology — June 2004

- [x] [DG Sample Problems 1.pdf](assets/attachments/DG Sample Problems 1_extracted.md) (267L, 20 problems) — differential geometry — disposition 2026-09-14: ingested as `SRC-MTH674-DIFFGEOM-MIDTERM-SAMPLE` from a deterministic MinerU Flash extraction. The source is titled *MTH 674 Differential Geometry of manifolds Midterm Sample Problems* and contains Problems I–XX; all twenty are represented in source order by `P-MTH674-01` through `P-MTH674-20`. Explicit local Flash defects and their deterministic-context repairs are recorded in the extraction provenance. The inventory's `0 problems` count was a false negative.

- [x] [DG Sample Problems.pdf](assets/attachments/extracted/DG Sample Problems.md) (267L, duplicate) — differential geometry — disposition 2026-09-14: exact byte duplicate of `DG Sample Problems 1.pdf` (SHA-256 `c76da1618392449b3d284ee8954f688d118ff2db0a192ffda6576bc8ac50512c`). Its contents are represented once by `SRC-MTH674-DIFFGEOM-MIDTERM-SAMPLE`; no duplicate extraction or cards are manufactured.

- [x] [f04.pdf](assets/attachments/f04_extracted.md) (77L, 18 problems) — Berkeley — prelim — Fall 2004 — disposition 2026-09-14: grounded in a deterministic MinerU Flash extraction that is byte-identical to the retained extraction. The source contains Part A Problems 1A–9A followed by Part B Problems 1B–9B, all already represented in paper order by the complete `SRC-BERKELEY-PRELIM-FALL-2004` collection. The inventory's `0 problems` and `applied-algebra` labels were stale heuristics.

- [x] [f05.pdf](assets/attachments/f05_extracted.md) (61L, 18 problems) — Berkeley — prelim — Fall 2005 — disposition 2026-09-14: grounded in a deterministic MinerU Flash extraction that is byte-identical to the retained extraction. The exam contains Part A Problems 1A–9A and Part B Problems 1B–9B; all eighteen agree with and are represented in paper order by `SRC-BERKELEY-PRELIM-FALL-2005`, whose provenance now includes the exam PDF in addition to its solution packet. The inventory's `0 problems` and `applied-algebra` labels were stale heuristics.

- [ ] [f06.pdf](assets/attachments/extracted/f06.md) (73L, 0 problems) — complex-analysis

- [ ] [f07.pdf](assets/attachments/extracted/f07.md) (48L, 0 problems) — complex-analysis — FALL 2007

- [ ] [Fall_2019_Assignments.pdf](assets/attachments/extracted/Fall_2019_Assignments.md) (919L, 70 problems) — UNL — applied-algebra — August 2019

- [ ] [Fall_2019_Assignment_Solutions.pdf](assets/attachments/extracted/Fall_2019_Assignment_Solutions.md) (2591L, 15 problems) — applied-algebra — October 23

- [x] [Fall_2019_SOLUTIONS.pdf](assets/attachments/extracted/Fall_2019_SOLUTIONS.md) (83L, 5 problems) — real-analysis — August 2019 — disposition 2026-09-09: UGA Fall 2019 Real Analysis; all five problems are already represented in `SRC-UGA-RA-FALL-2019`. This file is byte-identical to `Neil_Fall_2019_Solutions.pdf` (SHA-256 `a3d7d30454ada0b3a1071f234bd5b6a27b22e16cf615769b876fa8894eb2ebbc`), so no duplicate collection or provenance entry is needed.

- [x] [Fall78.pdf](assets/attachments/Fall78_extracted.md) (103L, 20 problems) — Berkeley — prelim — Fall 1978 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-FALL-1978` from a deterministic MinerU Flash extraction that is byte-identical to the retained extraction. All twenty source positions are represented in order by nineteen new source-local cards plus exact canonical reuse of `P-RA-WORKSHOP-D2-METRIC-11` for Problem 1. The three identified Flash defects in Problems 7, 9, and 15 are explicit in provenance and source-check notes. The inventory's `9 problems`, `applied-algebra`, and truncated `Fall 19` labels were stale heuristics.

- [x] [Fall84.pdf](assets/attachments/Fall84_extracted.md) (171L, 20 problems) — Berkeley — prelim — Fall 1984 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-FALL-1984` from a deterministic MinerU Flash extraction that is byte-identical to the retained extraction. All twenty source positions are represented in source order by source-local cards `P-BKF84-1` through `P-BKF84-20`; partial-overlap prior cards were not reused because they impose different hypotheses or additional obligations. The identified local Flash defects are recorded in provenance and on affected cards. The inventory's `14 problems`, `applied-algebra`, and truncated `Fall 19` labels were stale heuristics.

- [x] [Fall85.pdf](assets/attachments/Fall85_extracted.md) (127L, 20 problems) — Berkeley — prelim — Fall 1985 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-FALL-1985` from a deterministic MinerU Flash extraction that is byte-identical to the retained extraction. All twenty source positions are represented in order by nineteen new source-local cards plus exact canonical reuse of `P-BKF78-18` for Problem 4. The identified local Flash defects are recorded in provenance and on affected source-checked cards. The inventory's `8 problems`, `algebra`, and truncated `Fall 19` labels were stale heuristics.

- [ ] [Fall86.pdf](assets/attachments/extracted/Fall86.md) (125L, 2 problems) — algebra — Fall 19

- [x] [Fall88.pdf](assets/attachments/Fall88_extracted.md) (107L, 18 problems) — Berkeley — prelim — Fall 1988 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-FALL-1988` from a deterministic MinerU Flash extraction that is byte-identical to the retained extraction. All eighteen source positions are represented in source order by `P-BKF88-1` through `P-BKF88-18`; nearby prior cards had different hypotheses or extra obligations and were not reused. The identified local Flash defects are recorded in provenance and on affected cards. The inventory's `5 problems`, `algebra`, and truncated `Fall 19` labels were stale heuristics.

- [x] [Fall90.pdf](assets/attachments/Fall90_extracted.md) (101L, 18 problems) — Berkeley — prelim — Fall 1990 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-FALL-1990` from a deterministic MinerU Flash extraction that is byte-identical to the retained extraction. All eighteen source positions are represented in source order by `P-BKF90-1` through `P-BKF90-18`; nearby prior cards imposed different hypotheses or different tasks and were not reused. The identified local Flash defects are recorded in provenance and on the affected source-checked card. The inventory's `0 problems`, `algebra`, and truncated `Fall 19` labels were stale heuristics.

- [x] [Fall95.pdf](assets/attachments/Fall95_extracted.md) (84L, 18 problems) — Berkeley — prelim — Fall 1995 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-FALL-1995` from a deterministic MinerU Flash extraction that is byte-identical to the retained extraction. All eighteen source positions are represented in source order by seventeen new source-local cards plus exact canonical reuse of `P-BERK87S-19` for Problem 10. The identified local Flash defects are recorded in provenance and on affected source-checked cards. The inventory's `2 problems`, `applied-algebra`, and truncated `Fall 19` labels were stale heuristics.

- [x] [Fall97.pdf](assets/attachments/Fall97_extracted.md) (60L, 18 problems) — Berkeley — prelim — Fall 1997 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-FALL-1997` from a deterministic MinerU Flash extraction that is byte-identical to the retained extraction. All eighteen source positions are represented in source order by source-local cards `P-BKF97-1` through `P-BKF97-18`; nearby prior cards imposed different hypotheses or additional tasks and were not reused. Problem 12's dropped map arrows and minor typographic Flash noise are recorded in provenance. The inventory's `2 problems`, `complex-analysis`, and truncated `Fall 19` labels were stale heuristics.

- [x] [Hartshorne_Solutions.pdf](assets/attachments/Hartshorne_Solutions_extracted.md) (794L, 0 exam problems) — algebraic-geometry — reference-only — disposition 2026-09-14: deterministic MinerU Flash extraction assembled from pages 1-20 and 21-29 identifies a Hartshorne exercise-solution compendium for Chapters II-IV. The PDF is byte-identical (SHA-256 `d69a33b3dcdec0655edbb89a0a3851100de435aabbd75034032bd261120e917f`) to the already archived and linked `assets/algebraic-geometry/resources/Bryden R Cais.pdf`, so no duplicate cards or resource entry are created. The inventory's `9 problems` count treated solution headings as standalone queue problems.

- [x] [ist_ca_2015.pdf](assets/attachments/ist_ca_2015_extracted.md) (395L, 25 problems) — Sameer Chavan — complex-analysis — 2015 — disposition 2026-09-14: deterministic MinerU Flash extraction is byte-identical to the retained extraction and identifies *Problems in Complex Analysis*, a nine-section problem compilation rather than UNL topology material. All twenty-five explicit `Problem x.y` positions are represented in source order by `SRC-CHAVAN-COMPLEX-PROBLEMS-2015`: twenty-four source-local cards plus exact reuse of `E-TJ3WM` for Problem 8.7. Theorem, corollary, proof, and remark prose between those headings is retained as source context rather than manufactured into cards. Concrete extraction defects are recorded in provenance. The existing complex-analysis resource link remains the public reference route.

- [x] [Lie Groups and Sympl.pdf](assets/attachments/Lie_Groups_and_Sympl_extracted.md) (5525L, reference/course notes) — Robert L. Bryant — Lie groups / symplectic geometry — 1991 lectures; revised 2018 — disposition 2026-09-14: deterministic MinerU Flash extraction assembled verbatim from successful 20-page ranges through pages 161–180 identifies Bryant's nine-lecture *An Introduction to Lie Groups and Symplectic Geometry* from the 1991 Regional Geometry Institute in Park City.
  The notes are an expository course text; Exercise Sets 2–9 are integrated into the lecture sequence rather than a standalone problem bank. The inventory's `117 problems`, `UNL`, `alg-geom`, and truncated `July 19` labels were stale heuristic metadata.
  Added a substantive annotated entry to `wiki/topology/resources/books-notes.md` covering symmetry and differential equations, Lie groups and actions, conservation laws, symplectic manifolds, reduction, and the Gromov school; no exercise cards were manufactured. The raw Flash baseline's single NUL-byte defect is recorded in provenance rather than silently normalized.

- [x] [Li_-_INTRODUCTION_TO_ALGEBRAIC_TOPOLOGY.pdf](assets/attachments/Li_-_INTRODUCTION_TO_ALGEBRAIC_TOPOLOGY_extracted.md) (4036L, reference/course notes) — Si Li — algebraic topology — Tsinghua University, Spring 2018 — disposition 2026-09-14: fresh deterministic MinerU Flash extraction identifies *Introduction to Algebraic Topology*, a 28-section expository course text running from categories and the fundamental groupoid through coverings, homotopy groups, CW complexes, homology/cohomology, duality, spectral sequences, obstruction theory, Hurewicz, and the Eilenberg–Steenrod axioms.
  The fresh extraction contains no exercise/problem/homework headings; its only two uses of the word “problem” are ordinary expository prose. The inventory's `58 problems` and `alg-geom` labels were stale extraction heuristics.
  Enriched the existing topology resource entry with the source's actual course provenance and mathematical scope; no problem cards were manufactured.

- [ ] [more_calculus_from_test2.pdf](assets/attachments/more_calculus_from_test2_extracted.md) (162L, GRE Mathematics Test Form GR8767 calculus selection) — calculus / GRE mathematics — **BLOCKED 2026-09-14: deterministic MinerU Flash split extraction succeeded for pages 1–40 and identifies selected calculus questions from Form GR8767 followed by its answer-key/percentage worksheet, but a complete source-faithful card set cannot be recovered from the deterministic output.
  Several statements lose figures, question numbers, option labels, or essential formula glyphs (including the derivative-graph question, Questions 28–30's shared semicircle figure, and Question 41's graph choices). A pages 41–60 request returned MinerU `[-30003]` after the answer-key material; no fallback OCR/parser/model-vision path was used.
  Fresh extraction/provenance are retained and the existing resource entry is source-identified. The inventory's `20 problems` and `algebra` labels were stale heuristics.**

- [x] [Neil_Fall_2019_Solutions.pdf](assets/attachments/extracted/Neil_Fall_2019_Solutions.md) (83L, 5 problems) — real-analysis — August 2019 — disposition 2026-09-09: exact byte duplicate of `Fall_2019_SOLUTIONS.pdf`; the shared UGA Fall 2019 exam is already complete as `SRC-UGA-RA-FALL-2019`.

- [x] [Neil_Spring_2019_Solutions.pdf](assets/attachments/extracted/Neil_Spring_2019_Solutions.md) (325L, 5 problems) — UGA — real-analysis — Spring 2019 — disposition 2026-09-09: solution packet for the five-problem UGA Spring 2019 Real Analysis exam already complete as `SRC-UGA-RA-SPRING-2019`; byte-identical to `Spring 2019 with Solutions.pdf` (SHA-256 `3027e272d654a113b0cb15745bc0a4edb127fa36a6b91b9f4d772af84c0bb2e9`). As a solution writeup it is not added as collection provenance.

- [x] [Probability_Review.pdf](assets/attachments/extracted/Probability_Review.md) (582L, 0 problems) — real-analysis **OCR: image placeholders** — disposition 2026-09-09: Stanford CS229 probability review notes by Arian Maleki and Tom Do; expository reference material, not an exam or problem collection.
  No collection/card ingest required.

- [x] [qual18wintersol.pdf](assets/attachments/qual18wintersol_extracted.md) (61L, 10 problems) — algebra — Winter 2018 — disposition 2026-09-14: already ingested in `3a7a8b373` as complete collection `SRC-ALG-QUAL-WINTER-2018`, grounded in deterministic MinerU Flash v0.5.9. All ten source positions are represented in source order by five Part I true/false cards and five Part II longer-problem cards; the worked answers remain source provenance rather than imported solutions. The one identified symmetric-square extraction defect in Part II Problem 5 is recorded in provenance and on the source-checked card.

- [x] [QualProblemsHomotopy.pdf](assets/attachments/QualProblemsHomotopy_extracted.md) (32L, 11 posed items) — topology — disposition 2026-09-14: fresh deterministic MinerU Flash v0.5.9 extraction is byte-identical to the retained extraction and identifies *Topology Qual Workshop Day 6: Homotopy & Retractions*.
  Reconciled all 11 source positions in source order into `SRC-TOP-WORKSHOP`: five exact canonical reuses (`P-TOP-WORKSHOP-HR-W1`, `P-TOP-WORKSHOP-HR-W2`, `P-TOPSU15C`, `P-5AXU3`, `P-TOP-WORKSHOP-HR-05`) plus six source-local cards under `legacy-qual-problems-homotopy/`.
  MinerU's dropped-arrow and malformed-presentation defects are recorded in provenance; no fallback extraction path was used. The inventory's `0 problems` and `alg-geom` labels were stale heuristics.

- [ ] [Qual_Review_Selection_of_Hatcher_Problems_-_Unknown.pdf](assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md) (178L, 107 Hatcher references + 16 practice problems) — topology — **BLOCKED 2026-09-14: fresh deterministic MinerU Flash v0.5.9 extraction is byte-identical to the retained Markdown. The review sheet now has collection `SRC-QUAL-REVIEW-HATCHER`: 106 current Hatcher exercise selections reuse canonical `SRC-TEXT-HAT02` cards, while the sheet's §2.2 Exercise 34 reference is recorded but has no current card because Hatcher's errata withdrew that exercise; §2.2 Exercise 43(a) is represented by whole-exercise card `E-HAT-2.2-43` with the part-(a)-only selection documented.
  Thirteen of the sixteen additional practice problems are source-local cards. Practice problem 4 has an unresolved `S^4`/four-coordinate inconsistency in the deterministic text, and problems 6–7 depend on a figure emitted only as an image placeholder, so no repaired statements were invented. The inventory's `alg-geom` label was stale.**

- [ ] [s04.pdf](assets/attachments/extracted/s04.md) (89L, 3 problems) — applied-algebra

- [ ] [s05.pdf](assets/attachments/extracted/s05.md) (57L, 0 problems) — complex-analysis

- [ ] [Sequence_Series_(Neil_Lyall_2019).pdf](assets/attachments/extracted/Sequence_Series_(Neil_Lyall_2019).md) (650L, 67 problems) — UNL — applied-algebra — September 2020

- [x] [solution1.pdf](assets/attachments/extracted/solution1.md) (791L, 1 problems) — Harvard Math 21b — applied-algebra — Spring 2018 Practice Final 1 with solutions — disposition 2026-09-14: ingested as `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-1`, with all 14 top-level source problems represented by source-local cards. The Harvard Math 21b Spring 2018 resource page establishes course provenance. Problems 2, 3, and 11 depend on source images not recovered in the extraction, while Problem 14’s 124×124 display is represented by the scalar-matrix structure identified explicitly in the packet’s own worked solution. The inventory’s `1 problems` count was stale heuristic metadata.

- [x] [solution3.pdf](assets/attachments/extracted/solution3.md) (631L, 0 problems) — Harvard Math 21b — applied-algebra — Spring 2018 Practice Final 3 with solutions — disposition 2026-09-14: ingested as `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-3`, with all 14 top-level source problems represented by source-local cards. The Harvard Math 21b Spring 2018 resource page establishes course provenance. OCR loses headings for Problems 2, 4, 6, 9, and 12; Problem 3’s phase-portrait table and Problem 9(c)’s determinant matrix are damaged; Problem 14’s all-9s matrix is represented by the source-backed 10×10 structure identified in its worked solution. The inventory’s `0 problems` and OCR-derived labels were stale heuristic metadata.

- [x] [solution4.pdf](assets/attachments/extracted/solution4.md) (693L, 0 problems) — Harvard Math 21b — applied-algebra — Spring 2018 Practice Final 4 with solutions — disposition 2026-09-14: ingested as `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4`, with all 14 top-level source problems represented by source-local cards. The Harvard Math 21b Spring 2018 resource page establishes course provenance. Problem 1’s twentieth true-or-false statement is unrecovered, Problem 3’s matrix/portrait tables are damaged, Problem 9(c)’s eight-queens display conflicts with its own text/solution, and Problem 14’s 40×40 display is represented from the structural form identified by the packet’s own worked solution rather than the corrupt entrywise OCR. The inventory’s `0 problems` and OCR-derived labels were stale heuristic metadata.

- [x] [solution5.pdf](assets/attachments/extracted/solution5.md) (695L, 0 problems) — Harvard Math 21b — applied-algebra — Spring 2018 Practice Final 5 with solutions — disposition 2026-09-14: ingested as `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-5`, with all 14 top-level source problems represented by source-local cards. The Harvard Math 21b Spring 2018 resource page establishes course provenance. OCR loses headings for Problems 2, 3, 7, and 13, and Problem 3’s phase-portrait table is incomplete; those source conditions are explicit rather than reconstructed. The inventory’s `0 problems`, `UNL`, and OCR-derived labels were stale heuristic metadata.

- [x] [solution7.pdf](assets/attachments/extracted/solution7.md) (616L, 0 problems) — Harvard Math 21b — applied-algebra — Spring 2018 Practice Final 7 with solutions — disposition 2026-09-14: ingested as `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-7`, with all 14 top-level source problems represented by source-local cards. The Harvard Math 21b Spring 2018 resource page establishes course provenance. Problem 1 contains an internally inconsistent matrix-rank statement, while Problems 2 and 3 depend on graph/table material not fully recoverable from the retained extraction; those source defects are explicit rather than silently repaired. The inventory’s `0 problems` and OCR-derived labels were stale heuristic metadata.

- [x] [solution8.pdf](assets/attachments/extracted/solution8.md) (518L, 0 problems) — Harvard Math 21b — applied-algebra — Spring 2018 Practice Final 8 with solutions — disposition 2026-09-14: ingested as `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-8`, with all 14 top-level source problems represented by source-local cards. The Harvard Math 21b Spring 2018 resource page establishes course provenance. Problem 2’s source graph choices are unrecovered, and OCR-lost headings for Problems 2, 8, and 14 are accounted for by their complete statements and the fourteen-problem score table. The inventory’s `0 problems`, `diff-geom`, and OCR-derived labels were stale heuristic metadata.

- [x] [solution9.pdf](assets/attachments/extracted/solution9.md) (700L, 0 problems) — Harvard Math 21b — applied-algebra — Spring 2018 Practice Final 9 with solutions — disposition 2026-09-14: ingested as `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-9`, with all 14 top-level source problems represented by source-local cards. The Harvard Math 21b Spring 2018 resource page establishes the course provenance. Problem 2’s graph/phase-portrait choices and Problem 9’s displayed 36×36 matrix are unrecovered in the retained extraction and are recorded explicitly rather than reconstructed. The inventory’s `0 problems` and OCR-derived labels were stale heuristic metadata.

- [x] [solution.pdf](assets/attachments/extracted/solution.md) (723L, 0 problems) — Harvard Math 21b — applied-algebra — Spring 2018 final with solutions — disposition 2026-09-14: ingested as `SRC-HARVARD-MATH21B-SPRING-2018-FINAL`, with all 13 top-level final-exam problems represented by source-local cards. The existing Harvard Math 21b Spring 2018 resource page and Practice Final 6 collection establish the course provenance. One true-or-false item in Problem 1 and figure-dependent choices in Problems 2, 7, and 11 are unrecovered in the retained extraction and are recorded explicitly rather than reconstructed. The inventory’s `0 problems`, `UNL`, and OCR-derived labels were stale heuristic metadata.

- [x] [Spring 2019 with Solutions.pdf](assets/attachments/extracted/Spring 2019 with Solutions.md) (325L, 5 problems) — UGA — real-analysis — Spring 2019 — disposition 2026-09-09: exact byte duplicate of `Neil_Spring_2019_Solutions.pdf`; its five exam problems are already represented in `SRC-UGA-RA-SPRING-2019`, and the solution packet is not collection provenance.

- [x] [Spring79.pdf](assets/attachments/extracted/Spring79.md) (136L, 8 problems) — Berkeley — prelim — Spring 1979 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-SPRING-1979`, with all 20 source-order problems represented by 19 new source-local cards plus exact canonical reuse of `P-BERK97S-08` for Problem 11. Problem 8’s matrix-size glyph and Problem 13’s initial-condition right-hand side are unrecovered in every retained extraction and are recorded explicitly rather than reconstructed. The inventory’s `8 problems`, `algebra`, and truncated `Spring 19` labels were stale heuristic metadata.

- [x] [Spring93.pdf](assets/attachments/extracted/Spring93.md) (79L, 2 problems) — Berkeley — prelim — Spring 1993 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-SPRING-1993`, with all 18 source-order problems represented by source-local cards. Problem 5 is preserved with its literal homogeneous-boundary wording rather than an inferred nonzero-solution qualifier, and Problem 9's corrupted strip-coordinate glyph is explicitly unrecovered. The inventory's `2 problems`, `applied-algebra`, and truncated `Spring 19` labels were stale heuristic metadata.

- [x] [Spring99.pdf](assets/attachments/extracted/Spring99.md) (66L, 12 problems) — Berkeley — prelim — Spring 1999 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-SPRING-1999`, with all 18 source-order problems represented by source-local cards. Problem 8's displayed polynomial matrix loses its third row in every retained extraction; that source gap is explicit on `P-BKS99-08` rather than reconstructed. The inventory's `12 problems`, `complex-analysis`, and truncated `Spring 19` labels were stale heuristic metadata.

- [x] [squal1.pdf](assets/attachments/extracted/squal1.md) (25L, 8 problems) — topology — undated qualifying exam — disposition 2026-09-14: ingested as neutral collection `SRC-TOP-SQUAL1`, with all eight source-order problems represented by source-local cards. Neither the retained extraction nor the original qual-wiki resource page identifies an institution or date, so none was inferred.

- [x] [squal2.pdf](assets/attachments/extracted/squal2.md) (22L, 8 problems) — topology — undated qualifying exam — disposition 2026-09-14: ingested as neutral collection `SRC-TOP-SQUAL2`, with all eight source positions represented by six new source-local cards plus exact canonical reuse of `P-T07A2` for Section A Problem 4 and `P-OMOPR` for Section B Problem 6. Neither the retained extraction nor the original qual-wiki resource page identifies an institution or date, so none was inferred.

- [x] [Summer83.pdf](assets/attachments/extracted/Summer83.md) (103L, 2 problems) — Berkeley — prelim — Summer 1983 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-SUMMER-1983`, with all 20 source-order problems represented by 17 new source-local cards plus exact canonical reuse of `P-BKS84-1` for Problem 7, `P-BKF18-3B` for Problem 12, and `P-BKF96-14` for Problem 15. The inventory's `2 problems`, `applied-algebra`, and truncated `Summer 19` labels were stale heuristic metadata.

- [x] [Summer85.pdf](assets/attachments/extracted/Summer85.md) (117L, 7 problems) — Berkeley — prelim — Summer 1985 — disposition 2026-09-14: ingested as `SRC-BERKELEY-PRELIM-SUMMER-1985`, with all 20 source-order problems represented by 18 new source-local cards plus exact canonical reuse of `P-BKF89-13` for Problem 12 and `P-BKF83-2` for Problem 14. The inventory's `7 problems`, `applied-algebra`, and truncated `Summer 19` labels were stale heuristic metadata.

- [x] [Symplectic Geometry.pdf](assets/attachments/extracted/Symplectic Geometry.md) (1992L, 2 problems) — J.J. Duistermaat — symplectic geometry — Utrecht Spring School 2004 — reference/course notes — disposition 2026-09-14: treated as Duistermaat's expository spring-school lecture notes rather than a standalone problem source. The four chapters cover symplectic linear algebra, symplectic manifolds and reduction, Hamiltonian systems and Poisson geometry, and Hamilton–Jacobi theory, each with an exercise section. Added a substantive annotated entry to `wiki/topology/resources/books-notes.md`; no cards were manufactured from the heuristic `2 problems` count.

- [x] [Tevelev_-_GRADUATE_ALGEBRA_NUMBERS_EQUATIONS_SYMMETRIES.pdf](assets/attachments/extracted/Tevelev_-_GRADUATE_ALGEBRA_NUMBERS_EQUATIONS_SYMMETRIES.md) (4968L, 14 problems) — algebra — reference/course text — disposition 2026-09-14: treated as Tevelev's graduate-algebra notes rather than a standalone problem source. The document is organized as exposition on field extensions and Galois theory, radicals and cyclotomic fields, quadratic reciprocity, affine algebraic geometry, localization, and finite-group representations, with exercise sections and sample midterms embedded in the text. Enriched its existing entry in `wiki/algebra/resources/books-notes.md` with that mathematical scope; no cards were manufactured from the heuristic `14 problems` count.

- [x] [topology_2005-2003.pdf](assets/attachments/extracted/topology_2005-2003.md) (342L, 22 problems) — Wesleyan — topology — qualifying-exam compilation — disposition 2026-09-14: reconciled as canonical Wesleyan topology collections for August 2005, August 2004, and June 2003, with 30 primary top-level source positions represented by 28 source-local cards and two exact canonical reuses. The retained compilation also appends duplicate source copies of 2013 Part II (4 positions), the full 2006 exam (16 positions), and the 2003 exam again (10 positions), for 60 top-level appearances total; those duplicates are routed through the existing 2013/2006 collections and the same 2003 collection, with this PDF added as supplemental provenance where needed. OCR/source gaps remain explicit on affected cards rather than reconstructed. The inventory's `22 problems` and `alg-geom` labels were stale heuristic metadata.

- [x] [topology_2006-2014.pdf](assets/attachments/extracted/topology_2006-2014.md) (700L, 54 problems) — Wesleyan — topology — qualifying-exam compilation — disposition 2026-09-14: reconciled as nine canonical Wesleyan topology exam collections for 2006–2014, with all 82 top-level source positions represented. Seventy-five source-local cards were added and seven exact repeated statements reuse canonical cards. Diagram-dependent extraction gaps and source-sensitive text are explicit on the affected cards rather than reconstructed. The inventory's `54 problems` and `alg-geom` labels were stale heuristic metadata.

- [x] [Topology_Prelim_Answers_-_Unknown.pdf](assets/attachments/extracted/Topology_Prelim_Answers_-_Unknown.md) (3064L, 0 problems) — Malone–Housley — topology — worked answer compilation — disposition 2026-09-14: reconciled as `SRC-MALONE-HOUSLEY-TOPOLOGY-PRELIM-ANSWERS-2007`, with all 75 numbered source positions represented across Math 6520 Final Exam 2007, January 2007, Math 6510 Final Exam, August 2006, January 2006, embedded August 2005, and January 2005. The collection uses 72 canonical cards with three exact repeated appearances. January 2006 Problem 9 and January 2005 Problems 3 and 8 are truncated in the retained extraction, while January 2005 Problems 9 and 10 contain no statement text; those gaps are explicitly unrecovered rather than reconstructed. The inventory's `0 problems` and `diff-geom` labels were stale heuristic metadata.

- [x] [UCSD_Topology_Qual_Problems_2020-05-29.pdf](assets/attachments/extracted/UCSD_Topology_Qual_Problems_2020-05-29.md) (320L, 120 problems) — UCSD — topology — compilation — disposition 2026-09-13: reconciled as the byte-identical retained compiled source for `SRC-UCSD-TOP-JUSTIN`, which contains all 92 canonical problem positions. Added this PDF directly to collection provenance and corrected the extraction ledger: the four Van Kampen entries that are image/placeholders in the compilation were restored from Roberts’ official `UCSD_290_F14_sheet3.pdf`, already owned by the collection. No duplicate problem cards were created.

- [x] [Usher DG Notes.pdf](assets/attachments/extracted/Usher DG Notes.md) (3986L, 9 problems) — Mike Usher — Math 8210 Differential Geometry — Fall 2011 — reference/course notes — disposition 2026-09-13: treated as semester-long smooth-manifold lecture notes rather than a standalone problem source. The embedded exercises are subordinate to the exposition. Added a substantive annotated local-resource entry to `wiki/topology/resources/books-notes.md` covering tangent/vector-field formalisms, partitions of unity, bundles, differential forms, submanifolds and tubular neighborhoods, flows, Lie derivatives, Cartan's formula, and Moser's method; no exercise cards were manufactured.

- [x] [Won_-_Complex_Analysis_Qual_Sheet.pdf](assets/attachments/extracted/Won_-_Complex_Analysis_Qual_Sheet.md) (683L, 99 problems) — complex-analysis — reference sheet — disposition 2026-09-13: treated as Robert Won's expository complex-analysis qualifying-exam review sheet, not a posed problem source. The inventory's `99 problems` are numbered facts, observations, and theorem statements. Enriched its existing entry in `wiki/complex-analysis/resources/books-notes.md` with the sheet's actual organization and mathematical scope; no problem cards were manufactured.

## Preliminary exams (47)

- [x] [871-872June_2007_852-871.pdf](assets/attachments/extracted/871-872June_2007_852-871.md) (35L, 0 problems) — UNL — qualifying exam — June 2007 — disposition 2026-09-13: ingested as `SRC-UNL-QUAL-852-871-JUNE-2007`, with all 9 source positions represented in order. Five Section-A graph-theory/combinatorics cards were added; Section B reuses exact canonical topology cards `P-T07A1` through `P-T07A4` from the separately retained UNL June 2007 topology paper. The inventory's `0 problems` and `algebra` labels were stale heuristic metadata.

- [x] [calculating_galois_from_polynomial.pdf](assets/attachments/extracted/calculating_galois_from_polynomial.md) (255L, 22 problems) — Galois theory — reference notes — disposition 2026-09-13: treated as expository computational review notes rather than a problem source. The inventory's `22 problems` are worked examples embedded in the exposition, not a posed problem bank. Added a substantive annotated local-resource entry to `wiki/algebra/resources/fields.md` covering the notes' cubic-discriminant, prime-degree, cyclotomic, and finite-field Frobenius methods; the retained PDF remains the linked source.

- [x] [Fall00.pdf](assets/attachments/extracted/Fall00.md) (56L, 0 problems) — Berkeley — prelim — Fall 2000 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-2000`, with all 18 numbered problems represented in source order. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `0 problems` and `complex-analysis` labels were stale heuristic metadata for a mixed preliminary exam.

- [x] [Fall79.pdf](assets/attachments/extracted/Fall79.md) (117L, 12 problems) — Berkeley — prelim — Fall 1979 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1979`, with all 20 source positions represented in order. Thirteen source-local cards were added; Problems 1, 3, 13, 14, 15, 16, and 19 reuse exact canonical cards `P-BKF89-16`, `P-BKF91-1`, `P-BKF80-17`, `P-BERK81S-20`, `P-JHUSP01CAA`, `P-BERK85S-12`, and `P-BKF87-14`. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `12 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Fall80.pdf](assets/attachments/extracted/Fall80.md) (145L, 11 problems) — Berkeley — prelim — Fall 1980 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1980`, with all 20 source positions represented in order. Eighteen source-local cards were added; Problem 2 reuses `P-BKF92-1` and Problem 19 reuses `P-BKS10-1A`. Problem 9 retains an explicit extraction gap in the matrix-norm notation rather than guessing the missing typographic detail. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `11 problems` and `applied-algebra` labels were stale heuristic metadata.

- [x] [Fall83.pdf](assets/attachments/extracted/Fall83.md) (153L, 6 problems) — Berkeley — prelim — Fall 1983 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1983`, with all 20 source positions represented in order. Sixteen source-local cards were added; Problem 5 reuses `P-BERK96S-16`, Problem 14 reuses `E-AMD-HO6G56UF`, Problem 17 reuses `P-OVRL2`, and Problem 19 reuses `P-AA27R`. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `6 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Fall87.pdf](assets/attachments/extracted/Fall87.md) (105L, 2 problems) — Berkeley — prelim — Fall 1987 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1987`, with all 20 source positions represented in order. Eighteen source-local cards were added; Problem 13 reuses `P-BKF93-2` and Problem 19 reuses `P-BKS19-3B`. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `2 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Fall89.pdf](assets/attachments/extracted/Fall89.md) (78L, 0 problems) — Berkeley — prelim — Fall 1989 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1989`, with all 18 numbered problems represented in source order. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `0 problems` and `applied-algebra` labels were stale heuristic metadata.

- [x] [Fall91.pdf](assets/attachments/extracted/Fall91.md) (107L, 7 problems) — Berkeley — prelim — Fall 1991 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1991`, with all 18 numbered problems represented in source order. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `7 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Fall92.pdf](assets/attachments/extracted/Fall92.md) (111L, 5 problems) — Berkeley — prelim — Fall 1992 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1992`, with all 18 source positions represented in order. Seventeen source-local cards were added and Problem 16 reuses the exact Spring 1980 card `P-BKS80-16`. Problem 6 preserves an explicit extraction gap in the metric-comparison hypothesis rather than guessing the missing relation. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `5 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Fall93.pdf](assets/attachments/extracted/Fall93.md) (91L, 4 problems) — Berkeley — prelim — Fall 1993 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1993`, with all 18 numbered problems represented in source order. Problem 12 retains an explicit dependency on the contour omitted from the retained extraction; no curve was guessed. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `4 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Fall96.pdf](assets/attachments/extracted/Fall96.md) (123L, 4 problems) — Berkeley — prelim — Fall 1996 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1996`, with all 18 source positions represented in order. Sixteen source-local cards were added; Problem 12 reuses `P-BKS84-7` and Problem 18 reuses `P-BERK80S-11`. Problems 8 and 15 preserve explicit extraction gaps rather than guessed source data. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `4 problems` and `complex-analysis` labels were stale heuristic metadata.

- [x] [Fall98.pdf](assets/attachments/extracted/Fall98.md) (69L, 6 problems) — Berkeley — prelim — Fall 1998 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1998`, with all 18 numbered problems represented in source order. Seventeen source-local cards were added and Problem 17 reuses the exact canonical card `P-BJDIE` for the order of `GL_n(F_q)`. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `6 problems` and `applied-algebra` labels were stale heuristic metadata.

- [x] [Fall99.pdf](assets/attachments/extracted/Fall99.md) (64L, 0 problems) — Berkeley — prelim — Fall 1999 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-FALL-1999`, with all 18 numbered problems represented in source order. Sixteen source-local cards were added; Problem 10 reuses `P-BKF07-7B` and Problem 11 reuses `E-AMD-HO6G56UF`. The existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `0 problems` and `applied-algebra` labels were stale heuristic metadata.

- [x] [grad_prelim_Fall08.pdf](assets/attachments/extracted/grad_prelim_Fall08.md) (47L, 8 problems) — UGA — prelim — Fall 2008 — disposition 2026-09-13: ingested as `SRC-UGA-PRELIM-FALL-2008`, with all 8 source positions represented in order: 7 new cards plus exact reuse of `P-UGAP13F-06` for Problem 3. Problem 4 retains an explicit source gap because the displayed matrix is malformed in the retained extraction and repository history provides no independent recovery; no entries were guessed. The `grad_prelim_*` attachment lineage is the repository's UGA first-year preliminary-exam series.

- [x] [grad_prelim_Fall09.pdf](assets/attachments/extracted/grad_prelim_Fall09.md) (53L, 0 problems) — UGA — prelim — Fall 2009 — disposition 2026-09-13: ingested as `SRC-UGA-PRELIM-FALL-2009`, with all 8 top-level numbered problems represented in source order. The `grad_prelim_*` attachment lineage is the repository's UGA first-year preliminary-exam series. The inventory's `0 problems` and `no metadata` labels were stale heuristic metadata.

- [x] [grad_prelim_Fall11.pdf](assets/attachments/extracted/grad_prelim_Fall11.md) (29L, 9 problems) — UGA — prelim — Fall 2011 — disposition 2026-09-13: ingested as `SRC-UGA-PRELIM-FALL-2011`, with all 9 numbered problems represented in source order. The `grad_prelim_*` attachment lineage is the repository's UGA first-year preliminary-exam series.

- [x] [grad_prelim_Fall13.pdf](assets/attachments/extracted/grad_prelim_Fall13.md) (41L, 9 problems) — UGA — prelim — Fall 2013 — disposition 2026-09-13: ingested as `SRC-UGA-PRELIM-FALL-2013`, with all 9 numbered problems represented in source order. The `grad_prelim_*` attachment lineage is the repository's UGA first-year preliminary-exam series. The inventory's `complex-analysis` label was stale heuristic metadata for a mixed preliminary exam.

- [x] [grad_prelim_Spring08.pdf](assets/attachments/extracted/grad_prelim_Spring08.md) (37L, 8 problems) — UGA — prelim — Spring 2008 — disposition 2026-09-13: ingested as `SRC-UGA-PRELIM-SPRING-2008`, with all 8 numbered problems represented in source order. The retained extraction drops several symbols in Problems 1, 4, and 6; those cards record the uniquely forced reconstruction explicitly rather than silently normalizing the extraction. The `grad_prelim_*` attachment lineage is the repository's UGA first-year preliminary-exam series. The inventory's `algebra` label was stale heuristic metadata for a mixed preliminary exam.

- [x] [grad_prelim_Spring09.pdf](assets/attachments/extracted/grad_prelim_Spring09.md) (42L, 8 problems) — UGA — prelim — Spring 2009 — disposition 2026-09-13: ingested as `SRC-UGA-PRELIM-SPRING-2009`, with all 8 numbered problems represented in source order. The `grad_prelim_*` attachment lineage is the repository's UGA first-year preliminary-exam series; this missing Spring 2009 sitting is now represented with the retained PDF as provenance. The inventory's `algebra` label was stale heuristic metadata for a mixed preliminary exam.

- [x] [sample_exam.pdf](assets/attachments/extracted/sample_exam.md) (21L, 9 problems) — UGA — prelim — disposition 2026-09-13: reconciled the source-audited UGA sample graduate preliminary exam into the existing canonical `SRC-PRELIM-ART-A2355I` collection. All 9 source problems are represented in order: 7 new source-local cards plus exact existing cards `P-VAWOC` (Problem 4) and `P-HUKW5` (Problem 6). The retained PDF is now collection provenance; the prior collection had only those two appearances and no provenance.

- [x] [Spring00.pdf](assets/attachments/extracted/Spring00.md) (96L, 4 problems) — Berkeley — prelim — Spring 2000 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-SPRING-2000`, with all 18 numbered problems represented in source order. Seventeen source-local cards were added and Problem 4 reuses the exact canonical appearance `P-BERK89S-16`. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `4 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Spring01.pdf](assets/attachments/extracted/Spring01.md) (65L, 5 problems) — Berkeley — prelim — Spring 2001 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-SPRING-2001`, with all 18 numbered problems represented in source order. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `5 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Spring77.pdf](assets/attachments/extracted/Spring77.md) (157L, 17 problems) — Berkeley — prelim — Spring 1977 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-SPRING-1977`, with all 20 numbered problems represented in source order. Problem 3 remains mathematically complete despite the retained source printing a missing-PostScript message for its illustration, because the regular-polygon construction and chord lengths are specified textually. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `17 problems` and `applied-algebra` labels were stale heuristic metadata.

- [x] [Spring78.pdf](assets/attachments/extracted/Spring78.md) (135L, 14 problems) — Berkeley — prelim — Spring 1978 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-SPRING-1978`, with all 20 numbered problems represented in source order. Seventeen source-local cards were added; Problem 3 reuses `P-EMCA9`, Problem 4 reuses `P-BERK97S-12`, and Problem 9 reuses `P-PRELIM82S-01`. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `14 problems` and `complex-analysis` labels were stale heuristic metadata.

- [x] [Spring80.pdf](assets/attachments/extracted/Spring80.md) (153L, 13 problems) — Berkeley — prelim — Spring 1980 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-SPRING-1980`, with all 20 numbered problems represented in source order. Problem 9 preserves an explicit source gap because the retained extraction loses part of its displayed 2-by-2 matrix, and no missing entry was guessed. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `13 problems` count was stale heuristic metadata.

- [x] [Spring81.pdf](assets/attachments/extracted/Spring81.md) (167L, 17 problems) — Berkeley — prelim — Spring 1981 — disposition 2026-09-13: ingested as `SRC-BERKELEY-PRELIM-SPRING-1981`, with all 20 numbered problems represented in source order. Problem 11 retains an explicit dependency on the contour figure referenced by the exam because the retained markdown extraction omits that figure; no contour was guessed. Problem 9 records the extraction's undefined `a,b,c` symbols and the source-forced eigenvalue-sum interpretation explicitly. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `17 problems` and `topology` labels were stale heuristic metadata.

- [x] [Spring82.pdf](assets/attachments/extracted/Spring82.md) (95L, 0 problems) — Berkeley — prelim — Spring 1982 — disposition 2026-09-13: ingested from the retained PDF as `SRC-BERKELEY-PRELIM-SPRING-1982`, with all 20 numbered problems represented in source order. The retained `Spring82.md` extraction is materially wrong for Problems 2–9 and was not used for those statements; the PDF page was read directly instead. Problem 15 was also checked directly as a 2-by-2 matrix count over a field with p elements. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `0 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Spring83.pdf](assets/attachments/extracted/Spring83.md) (135L, 3 problems) — Berkeley — prelim — Spring 1983 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1983`, with Problems 1–20 represented in source order. Problem 4 is retained with an explicit audit note because the source PDF itself contains the message `../Fig/Pr/Sp83-4.ps not found` instead of the triangular-network diagram required by the problem; no reconstruction was guessed. Problem 18 was verified directly as a 3-by-3 matrix count over `F_7`. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `3 problems` and `complex-analysis` labels were stale heuristic metadata.

- [x] [Spring84.pdf](assets/attachments/extracted/Spring84.md) (102L, 4 problems) — Berkeley — prelim — Spring 1984 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1984`. Eighteen source-local cards represent Problems 1–8, 10, and 12–20; Problem 9 reuses canonical card `P-BERK87S-09`, and Problem 11 reuses canonical card `P-BKF81-18`. The Spring 1984 source uses the established `P-BKS84-*` ID family to avoid collision with the existing Summer 1984 `P-BERK84S-*` cards. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `4 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Spring85.pdf](assets/attachments/extracted/Spring85.md) (113L, 3 problems) — Berkeley — prelim — Spring 1985 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1985`, with Problems 1–20 represented in source order. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `3 problems` and `applied-algebra` labels were stale heuristic metadata.

- [x] [Spring86.pdf](assets/attachments/extracted/Spring86.md) (119L, 7 problems) — Berkeley — prelim — Spring 1986 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1986`. Seventeen source-local cards represent Problems 1–12, 15–18, and 20; Problem 13 reuses canonical card `P-UCLAB06S-10`, Problem 14 reuses `P-BERK96S-02`, and Problem 19 reuses `E-AMD-UXMX7R25`. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `7 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Spring87.pdf](assets/attachments/extracted/Spring87.md) (105L, 5 problems) — Berkeley — prelim — Spring 1987 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1987`. Eighteen source-local cards represent Problems 1–14, 16–17, and 19–20; Problem 15 reuses canonical card `P-8CA31`, and Problem 18 reuses canonical card `E-AMD-HO6G56UF`. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `5 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Spring89.pdf](assets/attachments/extracted/Spring89.md) (108L, 6 problems) — Berkeley — prelim — Spring 1989 — disposition 2026-09-13: identified from the retained PDF as an 18-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1989`, with Problems 1–18 represented in source order. Problem 17's garbled ideal conclusion was checked directly against the PDF page. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `6 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Spring90.pdf](assets/attachments/extracted/Spring90.md) (101L, 0 problems) — Berkeley — prelim — Spring 1990 — disposition 2026-09-13: identified from the retained PDF as an 18-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1990`, with Problems 1–18 represented in source order. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `0 problems` and `complex-analysis` labels were stale heuristic metadata.

- [x] [Spring91.pdf](assets/attachments/extracted/Spring91.md) (128L, 4 problems) — Berkeley — prelim — Spring 1991 — disposition 2026-09-13: identified from the retained PDF as an 18-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1991`. Seventeen source-local cards represent Problems 1 and 3–18; Problem 2 reuses canonical card `P-BERK79S-07`, the identical exponential-integral-entire statement from Summer 1979. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `4 problems` and `applied-algebra` labels were stale heuristic metadata.

- [x] [Spring92.pdf](assets/attachments/extracted/Spring92.md) (73L, 2 problems) — Berkeley — prelim — Spring 1992 — disposition 2026-09-13: identified from the retained PDF as an 18-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1992`. Seventeen source-local cards represent Problems 2–18; Problem 1 is the verbatim subgroup problem already canonical as `P-BERK77S-14`. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `2 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Spring95.pdf](assets/attachments/extracted/Spring95.md) (87L, 4 problems) — Berkeley — prelim — Spring 1995 — disposition 2026-09-13: identified from the retained PDF as an 18-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1995`. Sixteen source-local cards represent Problems 1–15 and 17; Problem 16 reuses canonical card `P-PRELIM82S-03`, and Problem 18 reuses canonical card `P-3A7RU`. OCR-sensitive matrix size in Problem 2 and the coefficient in Problem 14 were checked directly against the PDF pages. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `4 problems` and `applied-algebra` labels were stale heuristic metadata.

- [x] [Spring96.pdf](assets/attachments/extracted/Spring96.md) (101L, 0 problems) — Berkeley — prelim — Spring 1996 — disposition 2026-09-13: identified from the retained PDF as an 18-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1996`, with Problems 1–18 represented in source order. OCR-sensitive limits in Problem 11 and the matrix hypotheses in Problem 15 were checked directly against the PDF pages. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `0 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Spring97.pdf](assets/attachments/extracted/Spring97.md) (79L, 4 problems) — Berkeley — prelim — Spring 1997 — disposition 2026-09-13: identified from the retained PDF as an 18-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1997`, with Problems 1–18 represented in source order. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `4 problems` and `topology` labels were stale heuristic metadata.

- [x] [Spring98.pdf](assets/attachments/extracted/Spring98.md) (77L, 0 problems) — Berkeley — prelim — Spring 1998 — disposition 2026-09-13: identified from the retained PDF as an 18-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SPRING-1998`, with Problems 1–18 represented in source order. The damaged matrix entry in Problem 9 was verified directly against the PDF page. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `0 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Summer77.pdf](assets/attachments/extracted/Summer77.md) (111L, 8 problems) — Berkeley — prelim — Summer 1977 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SUMMER-1977`, with Problems 1–20 represented in source order. OCR-sensitive details in Problems 8, 9, and 20 were checked directly against the PDF pages. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `8 problems` and `complex-analysis` labels were stale heuristic metadata.

- [x] [Summer78.pdf](assets/attachments/extracted/Summer78.md) (173L, 26 problems) — Berkeley — prelim — Summer 1978 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SUMMER-1978`, with Problems 1–20 represented in source order. Problem 9 is preserved with an audit note because its nearest-point assertions are false for arbitrary metric spaces as printed; Problem 11 records the source's impossible n=0 strict coefficient inequality and states the coherent n>=1 condition. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `26 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Summer79.pdf](assets/attachments/extracted/Summer79.md) (137L, 8 problems) — Berkeley — prelim — Summer 1979 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SUMMER-1979`, with Problems 1–20 represented in source order. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `8 problems` and `algebra` labels were stale heuristic metadata.

- [x] [Summer81.pdf](assets/attachments/extracted/Summer81.md) (131L, 14 problems) — Berkeley — prelim — Summer 1981 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SUMMER-1981`. Nineteen source-local cards represent Problems 1–14 and 16–20; Problem 15 is the exact statement later repeated as Summer 1982 Problem 19 and reuses canonical card `P-PRELIM82S-19`. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `14 problems` and `topology` labels were stale heuristic metadata.

- [x] [Summer82.pdf](assets/attachments/extracted/Summer82.md) (145L, 9 problems) — Berkeley — prelim — Summer 1982 — disposition 2026-09-13: identified from the retained PDF as a 20-problem preliminary examination and ingested as `SRC-BERKELEY-PRELIM-SUMMER-1982`, with Problems 1–20 represented in source order. The PDF itself omits the institution name; the existing Berkeley prelim resource page supplies the Berkeley attribution. The inventory's `9 problems` and `complex-analysis` labels were stale heuristic metadata.

- [ ] [syllabus.pdf](assets/attachments/extracted/syllabus.md) (29L, 0 problems) — applied-algebra

## UCLA basic exams (41)

- [ ] [Auroux_-_Math_131_Introduction_to_Topology.pdf](assets/attachments/extracted/Auroux_-_Math_131_Introduction_to_Topology.md) (3661L, 48 problems) — UNL — alg-geom

- [ ] [basic-01F.pdf](assets/attachments/extracted/basic-01F.md) (51L, 10 problems) — UCLA — applied-algebra **OCR: image placeholders**

- [ ] [basic-02F.pdf](assets/attachments/extracted/basic-02F.md) (65L, 10 problems) — applied-algebra **OCR: image placeholders**

- [ ] [basic-02S.pdf](assets/attachments/extracted/basic-02S.md) (51L, 11 problems) — applied-algebra **OCR: image placeholders**

- [ ] [basic-02W.pdf](assets/attachments/extracted/basic-02W.md) (91L, 11 problems) — UCLA — applied-algebra **OCR: image placeholders**

- [ ] [basic-03F.pdf](assets/attachments/extracted/basic-03F.md) (103L, 0 problems) — UCLA — calculus — FALL 2003 **OCR: image placeholders**

- [ ] [basic-03S.pdf](assets/attachments/extracted/basic-03S.md) (55L, 10 problems) — UCLA — applied-algebra — May 2003

- [ ] [basic-04F.pdf](assets/attachments/extracted/basic-04F.md) (55L, 4 problems) — UCLA — Fall 2004

- [ ] [basic-04S.pdf](assets/attachments/extracted/basic-04S.md) (83L, 10 problems) — UCLA — applied-algebra

- [ ] [basic-05F.pdf](assets/attachments/extracted/basic-05F.md) (73L, 10 problems) — UCLA

- [ ] [basic-05S.pdf](assets/attachments/extracted/basic-05S.md) (131L, 12 problems) — topology

- [ ] [basic-06W.pdf](assets/attachments/extracted/basic-06W.md) (55L, 0 problems) — UCLA — applied-algebra — WINTER 2006

- [ ] [basic-07F.pdf](assets/attachments/extracted/basic-07F.md) (113L, 12 problems) — no metadata

- [x] [basic-07S.pdf](assets/attachments/extracted/basic-07S.md) (123L, 12 problems) — UCLA — prelim — Spring 2007 — disposition 2026-09-13: ingested as `SRC-UCLA-BASIC-SPRING-2007` with twelve source-order problem cards `P-UCLAB07S-01` through `P-UCLAB07S-12`; the retained PDF is collection provenance.

- [x] [basic-08F.pdf](assets/attachments/extracted/basic-08F.md) (83L, 0 problems) — UCLA — Fall 08 — disposition 2026-09-13: identified from the retained PDF and checked extraction as the UCLA Basic Examination, Fall 2008; ingested as `SRC-UCLA-BASIC-FALL-2008` with twelve source-order problem cards `P-UCLAB08F-01` through `P-UCLAB08F-12`. The inventory `0 problems` count was a false negative.

- [x] [basic-08S.pdf](assets/attachments/extracted/basic-08S.md) (109L, 11 problems) — no metadata — disposition 2026-09-13: identified from the retained resource link and checked extraction as the UCLA Basic Examination, Spring 2008; ingested as `SRC-UCLA-BASIC-SPRING-2008` with twelve source-order problem cards `P-UCLAB08S-01` through `P-UCLAB08S-12`. The inventory count of 11 was stale.

- [x] [basic-09F.pdf](assets/attachments/extracted/basic-09F.md) (87L, 12 problems) — UCLA — applied-algebra — Fall 2009 — disposition 2026-09-13: identified from the retained extraction as the UCLA Basic Exam, Fall 2009; ingested as `SRC-UCLA-BASIC-FALL-2009` with twelve source-order problem cards `P-UCLAB09F-01` through `P-UCLAB09F-12`. The source is a mixed Basic Examination, so the canonical collection is classified `prelim`.

- [x] [basic-09S.pdf](assets/attachments/extracted/basic-09S.md) (122L, 0 problems) — UCLA — algebra — Spring 2009 — disposition 2026-09-13: UCLA Basic Examination Spring 2009 ingested as `SRC-UCLA-BASIC-SPRING-2009`; all 12 numbered exam problems are represented in source order by `P-UCLAB09S-01` through `P-UCLAB09S-12`. The inventory count of 0 was a false negative, and the mixed Basic Examination is classified as `prelim` rather than algebra alone.

- [x] [basic-10F.pdf](assets/attachments/extracted/basic-10F.md) (105L, 12 problems) — UCLA — calculus — Fall 2010 — disposition 2026-09-13: UCLA Basic Examination Fall 2010 ingested as `SRC-UCLA-BASIC-FALL-2010`; all 12 numbered exam problems are represented in source order by `P-UCLAB10F-01` through `P-UCLAB10F-12`. Problem 4 was source-checked against the official UCLA PDF to repair the extraction’s `[0,1]` OCR corruption, and the mixed exam is classified as `prelim` rather than calculus alone.

- [x] [basic-10S.pdf](assets/attachments/extracted/basic-10S.md) (65L, 0 problems) — UCLA — applied-algebra — SPRING 2010 — disposition 2026-09-13: identified from the PDF as the UCLA Basic Examination, Spring 2010, and ingested as `SRC-UCLA-BASIC-SPRING-2010`; all 12 numbered problems are represented in source order by `P-UCLAB10S-01` through `P-UCLAB10S-12`. The inventory count of 0 was a false negative.

- [x] [basic-11F.pdf](assets/attachments/extracted/basic-11F.md) (93L, 2 problems) — UCLA — Fall 2011 — disposition 2026-09-13: identified from the PDF as the UCLA Basic Examination, Fall 2011, and ingested as `SRC-UCLA-BASIC-FALL-2011`; all 12 numbered problems are represented in source order by `P-UCLAB11F-01` through `P-UCLAB11F-12`. The inventory count of 2 was a stale extraction heuristic.

- [x] [basic-11S.pdf](assets/attachments/extracted/basic-11S.md) (99L, 20 problems) — UCLA — algebra — Spring 2011 — disposition 2026-09-13: UCLA Basic Examination Spring 2011 ingested as `SRC-UCLA-BASIC-SPRING-2011`; all twelve numbered exam problems are represented in source order by `P-UCLAB11S-01` through `P-UCLAB11S-12`. The inventory’s `20 problems` count split subparts/list items rather than the exam’s numbered problem units, and the source is classified as the mixed `prelim` Basic Examination rather than algebra alone.

- [ ] [basic-12S.pdf](assets/attachments/extracted/basic-12S.md) (75L, 0 problems) — UCLA — WINTER 2012

- [x] [basic-13F.pdf](assets/attachments/extracted/basic-13F.md) (75L, 12 problems) — UCLA — applied-algebra — Fall 2013 — disposition 2026-09-13: identified from the retained PDF as the UCLA Basic Examination, Fall 2013; already canonical as `SRC-UCLA-BASIC-FALL-2013`, whose provenance is this PDF and whose twelve source-order cards `P-UCLAB13F-01` through `P-UCLAB13F-12` match Problems 1–12.

- [x] [basic-13S.pdf](assets/attachments/extracted/basic-13S.md) (101L, 12 problems) — UCLA — alg-geom — Spring 2013 — disposition 2026-09-13: identified from the retained PDF as the UCLA Basic Examination, Spring 2013; already canonical as `SRC-UCLA-BASIC-SPRING-2013`, whose provenance is this PDF and whose twelve source-order cards `P-UCLAB13S-01` through `P-UCLAB13S-12` match Problems 1–12.

- [x] [basic-14F.pdf](assets/attachments/extracted/basic-14F.md) (61L, 0 problems) — UCLA — FALL 2014 — disposition 2026-09-13: identified from the retained PDF as the UCLA Basic Examination, Fall 2014; already canonical as `SRC-UCLA-BASIC-FALL-2014`, whose provenance is this PDF and whose twelve source-order cards `P-UCLAB14F-01` through `P-UCLAB14F-12` match Problems 1–12. The inventory `0 problems` count was a false negative.

- [ ] [basic-14S.pdf](assets/attachments/extracted/basic-14S.md) (107L, 12 problems) — UCLA — applied-algebra — Spring 2014

- [ ] [basic-15F.pdf](assets/attachments/extracted/basic-15F.md) (107L, 0 problems) — UCLA — calculus — FALL 2015

- [ ] [basic-15S.pdf](assets/attachments/extracted/basic-15S.md) (97L, 0 problems) — UCLA — algebra — SPRING 2015

- [ ] [basic-16S.pdf](assets/attachments/extracted/basic-16S.md) (105L, 0 problems) — UCLA — algebra — SPRING 2016

- [ ] [basic-17F.pdf](assets/attachments/extracted/basic-17F.md) (93L, 0 problems) — UCLA — applied-algebra — FALL 2017

- [ ] [basic-17S.pdf](assets/attachments/extracted/basic-17S.md) (97L, 0 problems) — UCLA — algebra — SPRING 2017

- [ ] [basic-18F.pdf](assets/attachments/extracted/basic-18F.md) (109L, 0 problems) — UCLA — FALL 2018

- [ ] [basic-18S.pdf](assets/attachments/extracted/basic-18S.md) (79L, 0 problems) — UCLA — prelim — Spring 2018 — reclassified 2026-09-09: UCLA Basic Exam, a mixed prelim source rather than a Real Analysis collection.

- [x] [DiffGeomNotes.pdf](assets/attachments/extracted/DiffGeomNotes.md) (6584L, 52 problems) — UNL — alg-geom — disposition 2026-09-13: the retained 2017 *Introduction to Differential Geometry: Lecture Notes for MAT367* are already canonical as `SRC-MAT367-DIFFGEOM-2017`, marked complete with 35 source-checked exercise/subpart cards `E-MAT367-01` through `E-MAT367-35` in source chapter order. The queue’s `52 problems` and `UNL` labels came from the old inventory heuristic; the PDF itself supplies neither that semantic count nor an institution. Intake is reconciled to the canonical collection, and the first exercise now carries a checked solution.

- [ ] [From Stein to Weinstein and Back.pdf](assets/attachments/extracted/From Stein to Weinstein and Back.md) (19152L, 24 problems) — UNL — alg-geom — Spring 19

- [x] [McMullen_-_Advanced_Complex_Analysis.pdf](assets/attachments/extracted/McMullen_-_Advanced_Complex_Analysis.md) (5772L, 260 problems) — Harvard — complex-analysis — 2017 — disposition 2026-09-13: C. McMullen's *Advanced Complex Analysis*, Harvard Math 213a course notes dated December 4, 2017, are complete as `SRC-HARVARD-MATH213A-2017`. The source has 156 authored exercise appearances across its opening six review exercises, three embedded exercises, and Sections 1.8, 2.5, 3.4, 4.4, and 5.5; all are represented in source order, with exact repeated problems reused rather than duplicated. The inventory's `260 problems`, `UNL`, and `alg-geom` labels were stale heuristic metadata.

- [x] [Mike Symplectic Topology Notes.pdf](assets/attachments/extracted/Mike Symplectic Topology Notes.md) (5751L, 18 problems) — UGA — alg-geom — SPRING 2019 — disposition 2026-09-13: Mike Usher’s UGA Math 8230 Symplectic Topology notes, Spring 2019, ingested as `SRC-UGA-MATH8230-SPRING-2019`. The collection retains the PDF as provenance and contains all 17 actual numbered exercise headings in source order; the inventory count of 18 included a later prose cross-reference to Exercise 4.5.

- [x] [Real_Analysis_Course_Notes.pdf](assets/attachments/extracted/Real_Analysis_Course_Notes.md) (3741L, 17 problems) — UNL — diff-geom — disposition 2026-09-10: expository Real Analysis course notes rather than an exam sitting; already linked from `wiki/real-analysis/resources/books-notes.md`, so no duplicate collection or problem-card intake is warranted.

- [x] [UCLA_Basic_Exam_Prelim.pdf](assets/attachments/extracted/UCLA_Basic_Exam_Prelim.md) (79L, 0 problems) — UCLA — prelim — Spring 2018 — disposition 2026-09-09: exact byte duplicate of `basic-18S.pdf` (SHA-256 `3ae97a051d30af40f6c497c68a1ebfad8ed56872cd471f4aa68c3b1ac8e19769`); ingest only the canonical `basic-18S.pdf` source.

- [ ] [UCLA_Basic_Exam_Topics.pdf](assets/attachments/extracted/UCLA_Basic_Exam_Topics.md) (59L, 18 problems) — UCLA — prelim

## Exams with solutions (39)

- [ ] [Algebra_Solutions 1.pdf](assets/attachments/extracted/Algebra_Solutions 1.md) (9243L, 16 problems) — UNL — alg-geom

- [ ] [Algebra_Solutions.pdf](assets/attachments/extracted/Algebra_Solutions.md) (9243L, 16 problems) — UNL — alg-geom

- [x] [Chernov_-_Selected_Problems_in_Real_Analysis.pdf](assets/attachments/extracted/Chernov_-_Selected_Problems_in_Real_Analysis.md) (3451L, 13 problems) — applied-algebra — May 2011 — disposition 2026-09-10: Chernov's solved Real Analysis problem collection, not a single exam sitting; already linked from `wiki/real-analysis/resources/solutions.md`, so retain it as a solutions resource rather than manufacturing an exam collection.

- [x] [complex_prelim.pdf](assets/attachments/extracted/complex_prelim.md) (1159L, 14 problems) — applied-algebra — Fall 2011 — disposition 2026-09-13: Cihan Bahran’s 2013 University of Minnesota complex-analysis prelim solution compilation is already canonical as `SRC-UMN-COMPLEX-PRELIM-BAHRAN-2013`. The collection retains this PDF as provenance and represents all 33 source-selected problems in its seven technique sections; the inventory count of 14 was only an extraction heuristic. The collection also records the packet’s repeated Fall 2009 Problem 5 and combined exam labels without manufacturing duplicate cards.

- [ ] [Complex_Qual_Notes.pdf](assets/attachments/extracted/Complex_Qual_Notes.md) (741L, 0 problems) — complex-analysis

- [x] [f05solution.pdf](assets/attachments/extracted/f05solution.md) (320L, 0 problems) — applied-algebra — FALL 2005 — disposition 2026-09-13: identified as the UC Berkeley Graduate Preliminary Examination, Fall 2005, solution packet; already canonical as `SRC-BERKELEY-PRELIM-FALL-2005`, whose provenance is this PDF and whose 18 cards represent Problems 1A–9A and 1B–9B. The inventory `0 problems` count was a false negative.

- [x] [f07solution.pdf](assets/attachments/extracted/f07solution.md) (231L, 0 problems) — complex-analysis — FALL 2007 — disposition 2026-09-13: identified as the UC Berkeley Graduate Preliminary Examination, Fall 2007, solution packet; already canonical as `SRC-BERKELEY-PRELIM-FALL-2007`, whose provenance is this PDF and whose 18 cards represent Problems 1A–9A and 1B–9B. The inventory `0 problems` count was a false negative.

- [x] [Fall_2014_Solutions.pdf](assets/attachments/extracted/Fall_2014_Solutions.md) (319L, 8 problems) — Berkeley — applied-algebra — disposition 2026-09-13: solution packet for the UC Berkeley Graduate Preliminary Examination, Fall 2014; already canonical as `SRC-BERKELEY-PRELIM-FALL-2014`, which retains both exam and solution PDFs as provenance and contains all 18 source-order problems 1A–9A and 1B–9B.

- [x] [fall-2018-prelim.pdf](assets/attachments/extracted/fall-2018-prelim.md) (315L, 18 problems) — Berkeley — prelim — disposition 2026-09-11: ingested as `SRC-BERKELEY-PRELIM-FALL-2018`; the Fall 2018 two-part Graduate Preliminary Examination contains 18 problems across calculus, real analysis, complex analysis, linear algebra, and abstract algebra, represented in paper order by `P-BKF18-1A` through `P-BKF18-9B`.

- [x] [Fall77.pdf](assets/attachments/extracted/Fall77.md) (132L, 20 problems) — Berkeley — prelim — Fall 1977 — disposition 2026-09-11: ingested as `SRC-BERKELEY-PRELIM-FALL-1977`; all 20 problems are represented in source order by `P-BKF77-1` through `P-BKF77-20`.

- [x] [Fall81.pdf](assets/attachments/extracted/Fall81.md) (193L, 20 problems) — Berkeley — prelim — Fall 1981 — disposition 2026-09-11: ingested as `SRC-BERKELEY-PRELIM-FALL-1981`; all 20 problems are represented in source order by `P-BKF81-1` through `P-BKF81-20`.

- [x] [Fall82.pdf](assets/attachments/extracted/Fall82.md) (126L, 20 problems) — Berkeley — prelim — Fall 1982 — disposition 2026-09-11: ingested as `SRC-BERKELEY-PRELIM-FALL-1982`; all 20 problems are represented in source order by `P-BKF82-1` through `P-BKF82-20`.

- [x] [Fall94.pdf](assets/attachments/extracted/Fall94.md) (121L, 18 problems) — Berkeley — prelim — Fall 1994 — disposition 2026-09-11: ingested as `SRC-BERKELEY-PRELIM-FALL-1994`; all 18 problems are represented in source order by `P-BKF94-1` through `P-BKF94-18`.

- [x] [Ma_-_A_NOTE_FOR_REAL_ANALYSIS_QUALIFYING_EXAM_IN_TAMU.pdf](assets/attachments/extracted/Ma_-_A_NOTE_FOR_REAL_ANALYSIS_QUALIFYING_EXAM_IN_TAMU.md) (2116L, 19 problems) — TAMU — applied-algebra — January 2017 — disposition 2026-09-10: Xin Ma's derivative solution notes for TAMU Real Analysis qualifying exams, not an original exam source; already linked from `wiki/real-analysis/resources/solutions.md`, so no duplicate collection is warranted.

- [x] [my-solutions-to-old-analysis-quals.pdf](assets/attachments/extracted/my-solutions-to-old-analysis-quals.md) (1788L, 0 problems) — UCSD — applied-algebra — December 2017 — disposition 2026-09-10: Jacob S. Townson's derivative solutions to University of Louisville analysis quals, not an original exam paper; already linked from `wiki/real-analysis/resources/solutions.md`, so retain it as a solutions resource.

- [x] [prelimsolutions_0.pdf](assets/attachments/extracted/prelimsolutions_0.md) (280L, 18 problems) — Berkeley — prelim — Spring 2021 — disposition 2026-09-11: official two-part online Graduate Preliminary Examination with solutions; ingested as `SRC-BERKELEY-PRELIM-SPRING-2021`, with all 18 problem statements represented in source order by `P-BKS21-1A` through `P-BKS21-9B`.

- [x] [prelimsolutions.pdf](assets/attachments/extracted/prelimsolutions.md) (355L, 18 problems) — Berkeley — prelim — Fall 2020 — disposition 2026-09-11: official two-part online Graduate Preliminary Examination with solutions; ingested as `SRC-BERKELEY-PRELIM-FALL-2020`, with all 18 problem statements represented in source order by `P-BKF20-1A` through `P-BKF20-9B`.

- [x] [prolrevqual.pdf](assets/attachments/extracted/prolrevqual.md) (4289L, 0 problems) — University of Arizona — geometry/topology — disposition 2026-09-11: John Kerl's derivative solution compendium for old University of Arizona geometry/topology qualifying exams, not an original exam source; already linked from `wiki/topology/resources/solutions.md`, so retain it as a solutions resource rather than manufacturing a collection.

- [x] [qf13sol.pdf](assets/attachments/extracted/qf13sol.md) (1073L, 20 problems) — Fall 2013 qualifying-exam solutions — disposition 2026-09-11: derivative solution compendium covering Qualifying Exams I, II, and III rather than an original exam paper; already linked from `wiki/archives/solution-compendia.md`, so retain it as a solutions resource and do not manufacture duplicate collections.

- [x] [Real_solutions.pdf](assets/attachments/extracted/Real_solutions.md) (6265L, 15 problems) — TAMU — applied-algebra — August 29 — disposition 2026-09-11: exact byte duplicate of `Texas_Solns.pdf` (SHA-256 `77623034b4c2c3903dffc0fe2e816a9e5d10fe94018cb1dbf6d40e183f6c899c`). Kari Eifler's TAMU Real Analysis qualifying-exam solutions are already represented as a solutions resource; the canonical resource link points to `Texas_Solns.pdf`, so no duplicate collection or resource entry is needed.

- [x] [s03.pdf](assets/attachments/extracted/s03.md) (99L, 18 problems) — Berkeley — prelim — Spring 2003 — disposition 2026-09-11: mixed two-part preliminary exam ingested as `SRC-BERKELEY-PRELIM-SPRING-2003`; all 18 problem statements are represented in source order by `P-BKS03-1A` through `P-BKS03-9B`.

- [x] [s07solution.pdf](assets/attachments/extracted/s07solution.md) (309L, 18 problems) — Berkeley — prelim solutions — Spring 2007 — disposition 2026-09-11: derivative solution edition of the separately vendored original exam `s07.pdf`; already linked from `wiki/prelim/problems/berkeley-prelims.md`, so retain it as a solutions resource and perform card intake from the original exam entry instead.

- [x] [s08solution.pdf](assets/attachments/extracted/s08solution.md) (275L, 0 problems) — applied-algebra — SPRING 2008 **OCR: image placeholders** — disposition 2026-09-13: identified as the UC Berkeley Graduate Preliminary Examination, Spring 2008, solution packet; already canonical as `SRC-BERKELEY-PRELIM-SPRING-2008`. The collection uses this PDF as provenance and contains all 18 source-order problems 1A–9A and 1B–9B. The inventory `0 problems` count was a false negative.

- [x] [s10solutions.pdf](assets/attachments/extracted/s10solutions.md) (179L, 0 problems) — applied-algebra — spring 2010 — disposition 2026-09-13: identified from the retained packet as the UC Berkeley Graduate Preliminary Examination, Spring 2010, with solutions; already canonical as `SRC-BERKELEY-PRELIM-SPRING-2010`. The collection uses this PDF as provenance and contains all 18 source-order problems 1A–9A and 1B–9B. The inventory `0 problems` count was a false negative.

- [x] [Sp13_Exam.pdf](assets/attachments/extracted/Sp13_Exam.md) (305L, 18 problems) — Berkeley — prelim — Spring 2013 — disposition 2026-09-12: UC Berkeley Spring 2013 Graduate Preliminary Examination ingested as `SRC-BERKELEY-PRELIM-SPRING-2013`; all 18 problems `1A`–`9B` are represented in exam order as `P-BKS13-1A` through `P-BKS13-9B`. The prior count of eleven came from lost extraction headings.

- [ ] [Sp14_Exam.pdf](assets/attachments/extracted/Sp14_Exam.md) (255L, 8 problems) — Berkeley — applied-algebra

- [ ] [Sp14_Solutions.pdf](assets/attachments/extracted/Sp14_Solutions.md) (337L, 8 problems) — Berkeley — applied-algebra

- [x] [Sp15_Exam.pdf](assets/attachments/extracted/Sp15_Exam.md) (329L, 8 problems) — Berkeley — complex-analysis — disposition 2026-09-13: identified from the retained PDF as the UC Berkeley Graduate Preliminary Examination, Spring 2015, and ingested as `SRC-BERKELEY-PRELIM-SPRING-2015`. The source contains 18 problems, Part A 1A–9A followed by Part B 1B–9B; fifteen are source-local cards and Problems 4A, 4B, and 5B reuse canonical cards `P-BKF20-5A`, `P-3A7RU`, and `P-BKS09-3A`. The inventory count of 8 was incomplete.

- [x] [Sp15_Solutions.pdf](assets/attachments/extracted/Sp15_Solutions.md) (435L, 8 problems) — Berkeley — alg-geom — disposition 2026-09-13: companion solution packet for the complete `SRC-BERKELEY-PRELIM-SPRING-2015` collection. It states and solves the same 18 Part A/B problems as the exam PDF and is retained as provenance beside that paper; no duplicate solution collection or problem cards are created.

- [x] [Spring_2019_prelim.pdf](assets/attachments/extracted/Spring_2019_prelim.md) (313L, 8 problems) — Berkeley — applied-algebra — disposition 2026-09-13: reconciled to `SRC-BERKELEY-PRELIM-SPRING-2019`, which contains all 18 source-order Part A/B problems and records this exam PDF as provenance.

- [x] [Spring_2019_prelim_solutions.pdf](assets/attachments/extracted/Spring_2019_prelim_solutions.md) (385L, 8 problems) — Berkeley — applied-algebra — disposition 2026-09-13: solution packet for the same complete `SRC-BERKELEY-PRELIM-SPRING-2019` collection; retained there as provenance beside the exam PDF, with no duplicate cards created.

- [x] [Spring88.pdf](assets/attachments/extracted/Spring88.md) (83L, 2 problems) — UNL — algebra — Spring 19 — disposition 2026-09-13: identified from the PDF as the UC Berkeley Spring 1988 Preliminary Exam and ingested as `SRC-BERKELEY-PRELIM-SPRING-1988`, with all twenty Problems 1–20 represented in source order by `P-BKS88-1` through `P-BKS88-20`. The inventory metadata/count were stale: the source is Berkeley prelim material and contains 20 numbered problems, not 2.

- [x] [Spring94.pdf](assets/attachments/extracted/Spring94.md) (89L, 7 problems) — algebra — Spring 19 — disposition 2026-09-13: already complete as `SRC-BERKELEY-PRELIM-SPRING-1994`; the collection records the vendored PDF as provenance and contains all 18 source-order problems, each source-checked against the Berkeley Spring 1994 exam. The inventory count of 7 problems is a stale extraction heuristic; the source has Problems 1–18.

- [x] [Study_Guide_for_Algebra.pdf](assets/attachments/extracted/Study_Guide_for_Algebra.md) (919L, 11 problems) — UNL — algebra — January 2012 — disposition 2026-09-13: identified from the PDF itself as the Amherst College Department of Mathematics and Statistics **Study Guide for Algebra**, September 2016. The inventory metadata and `11 problems` count were stale: the guide contains 31 numbered old-exam examples with worked proofs. Ingested as `SRC-AMHERST-ALGEBRA-STUDY-GUIDE-2016`, with source-order cards `P-AMH-ALG-SG16-01` through `P-AMH-ALG-SG16-31` grouped by the guide's group/permutation/ring/polynomial sections.

- [x] [Summer80.pdf](assets/attachments/extracted/Summer80.md) (163L, 13 problems) — complex-analysis — Summer 19 — disposition 2026-09-12: Berkeley Preliminary Exam, Summer 1980, ingested as `SRC-BERKELEY-PRELIM-SUMMER-1980` with twenty source-order cards `P-BERK80S-01` through `P-BERK80S-20`. The inventory count of 13 was incomplete; the PDF explicitly contains Problems 1–20. OCR-sensitive matrix equations in Problems 2 and 14 are preserved/checked against rendered PDF source pages.

- [x] [Summer84.pdf](assets/attachments/extracted/Summer84.md) (149L, 6 problems) — algebra — Summer 19 — disposition 2026-09-12: Berkeley Preliminary Exam, Summer 1984, ingested as `SRC-BERKELEY-PRELIM-SUMMER-1984` with twenty source-order cards `P-BERK84S-01` through `P-BERK84S-20`. The inventory count of 6 was a false negative: the PDF explicitly contains Problems 1–20; PDF text-layer checks repaired the OCR of Problem 13 (`2×2`, not `Q×Q`) and restored Problem 20 as the final real-line integral.

- [x] [Texas_Solns.pdf](assets/attachments/extracted/Texas_Solns.md) (6265L, 15 problems) — TAMU — applied-algebra — August 29 — disposition 2026-09-11: canonical retained copy of Kari Eifler's *Solutions to Texas A&M's Real Analysis Qual Courses*. It is already linked from `wiki/real-analysis/resources/solutions.md`; this derivative solutions packet is not an original exam sitting, so intake stops at the existing resource representation rather than creating a duplicate qualifying-exam collection.

- [x] [TopologySept19solutions.pdf](assets/attachments/extracted/TopologySept19solutions.md) (255L, 0 problems) — diff-geom — FALL 2019 **OCR: image placeholders** — disposition 2026-09-12: University of Oregon Fall 2019 Topology Qualifying Exam solution packet, ingested as `SRC-UO-TOP-FALL-2019` with ten source-order problem cards `P-UOT19-01` through `P-UOT19-10`; the inventory `0 problems` count was a false negative caused by the solution-packet extraction layout.
  Diagram-dependent prompts retain rendered source pages.

- [x] [UCLA_Solutions.pdf](assets/attachments/extracted/UCLA_Solutions.md) (11367L, 13 problems) — UCLA — applied-algebra — January 25 — disposition 2026-09-13: UCLA Analysis Qualifying Exam Solutions compendium (updated January 25, 2019), covering twenty sittings from Spring 2009 through Fall 2018. Existing corpus collections already represented Spring 2009 through Spring 2014. Intake completed the remaining nine sittings as `SRC-UCLA-RA-FALL-2014`, `SRC-UCLA-RA-SPRING-2015`, `SRC-UCLA-RA-FALL-2015`, `SRC-UCLA-RA-SPRING-2016`, `SRC-UCLA-RA-FALL-2016`, `SRC-UCLA-RA-SPRING-2017`, `SRC-UCLA-RA-FALL-2017`, `SRC-UCLA-RA-SPRING-2018`, and `SRC-UCLA-RA-FALL-2018`, with twelve source-order problem cards in each.
  Official UCLA exam PDFs were used to source-check seven text-bearing sittings; Fall 2014 and Fall 2015 are image-only and were transcribed from the retained compendium.
  The inventory count `13 problems` counted OCR headings rather than the compendium contents and was not a source count.

## Final exams (1)

- [x] [Spring2020Final.pdf](assets/attachments/extracted/Spring2020Final.md) (47L, 6 problems) — UNL — complex-analysis — Spring 2020 — disposition 2026-09-12: the queue institution label was incorrect; the source is UGA MATH 8150 Spring 2020 Final Exam (Jingzhi Tie), ingested as `SRC-UGA-MATH8150-SPRING-2020-FINAL`. Five source-local cards represent Problems 1–3 and 5–6; Problem 4 exactly reuses canonical `P-XKOQR` from UGA Fall 2019.

## Midterm exams (4)

- [x] [Group_Theory_(No_Solns).pdf](assets/attachments/extracted/Group_Theory_(No_Solns).md) (87L, 20 problems) — algebra — disposition 2026-09-12: ingested as complete `SRC-MA553-MIDTERM-I-SAMPLE-PROBLEMS`; all 20 source problems are represented in order, with Problem 13 reusing canonical `P-ALGFINAL11-01` and the remaining 19 represented by `P-MA553-MID1-*` cards.

- [x] [MATH871-Exam-Review-Sheets.pdf](assets/attachments/extracted/MATH871-Exam-Review-Sheets.md) (265L, 1 problems) — UNL — topology — Fall 2013 — disposition 2026-09-12: UNL Math 871 Fall 2013 exam-review sheets listing vocabulary, theorem statements, study tasks, and references to textbook/problem-set exercises rather than presenting a standalone authored problem collection.
  Already retained at `wiki/topology/resources/books-notes.md`; reference-only intake stops there, with no duplicate cards manufactured.

- [x] [Real_Analysis_Review_Midterm.pdf](assets/attachments/extracted/Real_Analysis_Review_Midterm.md) (163L, 0 problems) — diff-geom — disposition 2026-09-10: MAT 320 practice midterm/review sheet with solutions rather than a qualifying-exam sitting; already linked from `wiki/prelim/resources/references.md`, so no qual collection is appropriate.

- [x] [Spring2020Midterm.pdf](assets/attachments/extracted/Spring2020Midterm.md) (45L, 6 problems) — UGA — complex-analysis — Spring 2020 — disposition 2026-09-12: UGA MATH 8150 Spring 2020 Midterm ingested as `SRC-UGA-MATH8150-SPRING-2020-MIDTERM` with all six source-order problems.
  Problems 1, 2, and 6 reuse canonical corpus cards; Problems 3–5 are source-local cards `P-UGA8150S20-MID-03` through `P-UGA8150S20-MID-05`. The resource-page label was corrected from Spring 2021 to Spring 2020.

## Practice exams (2)

- [x] [calculus_practice_test3.pdf](assets/attachments/extracted/calculus_practice_test3.md) (151L, 9 problems) — no metadata **OCR: image placeholders** — disposition 2026-09-12: undergraduate calculus multiple-choice practice material, already retained at `wiki/prelim/resources/problems.md`. The prior Queue-E audit (`queues/E-batch-03.md`) explicitly classifies it as “not a collection candidate,” and `queues/E-corrections.md` records numerous scanner gaps/unreadable stems.
  Reference-only intake therefore stops at the existing resource representation; no qualifying-exam collection or cards are manufactured.

- [x] [multivariable_calculus.pdf](assets/attachments/extracted/multivariable_calculus.md) (127L, 6 problems) — no metadata **OCR: image placeholders** — disposition 2026-09-12: undergraduate multivariable-calculus multiple-choice practice material with an answer key, already retained as “Multivariable-calculus practice” on `wiki/prelim/resources/solutions.md`. This is reference/practice material rather than a qualifying-exam source, so intake stops at the existing resource representation; no qual cards manufactured.

## Exam or problem set (1)

- [x] [871-872January_2006_852-871.pdf](assets/attachments/extracted/871-872January_2006_852-871.md) (39L, 0 problems) — topology — disposition 2026-09-12: UNL Mathematics Qualifying Exam 852/970, January 2006, ingested as `SRC-UNL-QUAL-852-970-JANUARY-2006`. The inventory zero was a false negative: the paper has ten questions.
  Section A is represented by new cards `P-UNL852970-06A1` through `P-UNL852970-06A5`; Section B is verbatim the first five questions of `SRC-TOP-UNL-2006Q1` and reuses `P-T06Q1-1` through `P-T06Q1-5`.

## Workshop materials (6)

- [x] [day_1_compactness.pdf](assets/attachments/extracted/day_1_compactness.md) (31L, 9 problems) — topology — June 2011 — disposition 2026-09-12: already reconciled in `SRC-TOP-WORKSHOP` as `Revised packet — Compactness`. Its three warm-ups and nine numbered problems are represented in source order by the twelve listed workshop/canonical cards; the PDF is already collection provenance.

- [x] [day_2_connected_path_connnected.pdf](assets/attachments/extracted/day_2_connected_path_connnected.md) (31L, 10 problems) — topology — June 2004 — disposition 2026-09-12: already reconciled in `SRC-TOP-WORKSHOP` as `Revised packet — Connectedness and path connectedness`. Its two warm-ups and ten numbered problems are represented in source order by the twelve listed workshop/canonical cards; the PDF is already collection provenance.

- [x] [day_4_homotopy_retractions.pdf](assets/attachments/extracted/day_4_homotopy_retractions.md) (39L, 8 problems) — topology — June 2014 — disposition 2026-09-12: already reconciled in `SRC-TOP-WORKSHOP` as the `Revised packet — Homotopy and retractions` section.
  Its two warm-ups and eight numbered problems are represented in source order by the ten listed workshop/canonical cards; the vendored PDF is already collection provenance.

- [x] [day_5_fundamental_group.pdf](assets/attachments/extracted/day_5_fundamental_group.md) (33L, 9 problems) — topology — June 2005 **OCR: image placeholders** — disposition 2026-09-12: already reconciled in `SRC-TOP-WORKSHOP` as the `Revised packet — Fundamental group` section.
  The three warm-ups, seven numbered problems, and two covering-space bonus problems are represented in source order by the twelve listed workshop/canonical cards; the vendored PDF is already collection provenance.

- [x] [day_6_covering_spaces.pdf](assets/attachments/extracted/day_6_covering_spaces.md) (31L, 11 problems) — topology — June 2005 — disposition 2026-09-12: already reconciled in `SRC-TOP-WORKSHOP` as the `Revised packet — Covering spaces` section.
  Its two warm-ups and eleven numbered problems are represented one-for-one in source order by the thirteen listed workshop/canonical cards, and the vendored PDF is already collection provenance; no duplicate cards needed.

- [x] [day_7_homology.pdf](assets/attachments/extracted/day_7_homology.md) (29L, 10 problems) — topology — June 2005 — disposition 2026-09-12: already reconciled in `SRC-TOP-WORKSHOP` as the `Revised packet — Homology` section.
  Its two warm-ups and ten numbered problems are represented in source order by the twelve listed workshop/canonical cards, and the vendored PDF is already collection provenance; no duplicate cards needed.

## Problem sets (14)

- [x] [basic-06S.pdf](assets/attachments/extracted/basic-06S.md) (71L, 0 problems) — no metadata — disposition 2026-09-12: UCLA Basic Examination Spring 2006, already ingested completely as `SRC-UCLA-BASIC-SPRING-2006`; all ten source problems are represented in order by `P-UCLAB06S-01` through `P-UCLAB06S-10`.

- [x] [basic-16F.pdf](assets/attachments/extracted/basic-16F.md) (100L, 0 problems) — no metadata — disposition 2026-09-12: UCLA Basic Examination Fall 2016, already ingested completely as `SRC-UCLA-BASIC-FALL-2016`; all twelve source problems are represented in order by `P-UCLAB16F-01` through `P-UCLAB16F-12`.

- [x] [Chapter3-notes1.pdf](assets/attachments/extracted/Chapter3-notes1.md) (35L, 0 problems) — no metadata — disposition 2026-09-12: reference-only 2015 notes on convergent sequences, subsequences, and subsequential limits in metric spaces.
  Repository intake notes classify this as reference notes rather than a collection candidate; the existing real-analysis resource link has been annotated and no problem cards manufactured.

- [x] [Collection_of_Analysis_Theorems.pdf](assets/attachments/extracted/Collection_of_Analysis_Theorems.md) (669L, 29 problems) — topology — disposition 2026-09-12: reference-only Joshua Ruiter *Theorems: Real Analysis* notes (March 2018). The inventory problem count is a false positive from numbered theorem statements; repository intake notes classify this as reference notes, not a collection candidate.
  Added to `vocabularies/references.bib` as `Ruiter18AnalysisTheorems` and to the real-analysis books/notes resource page; no problem cards manufactured.

- [x] [F15_Solutions.pdf](assets/attachments/extracted/F15_Solutions.md) (191L, 0 problems) — complex-analysis — disposition 2026-09-12: already reconciled with `SRC-BERKELEY-PRELIM-FALL-2015`, whose provenance includes both `F15_Exam.pdf` and this solution packet.
  The paired exam confirms the complete 18-problem sequence 1A–9A and 1B–9B, exactly matching the collection cards.

- [x] [Folland Clipped Questions.pdf](assets/attachments/extracted/Folland Clipped Questions.md) (858L, 79 problems) — real-analysis **OCR: image placeholders** — disposition 2026-09-09: exact byte duplicate of `Folland_Clipped_Questions.pdf` (SHA-256 `e775d4915cbacc566da3d2731cc938692f9f57a45a2dc262cb8a5041ba95ec10`). The resource page already links the underscore-named copy, so no second collection or resource entry is warranted.

- [x] [Folland_Clipped_Questions.pdf](assets/attachments/extracted/Folland_Clipped_Questions.md) (858L, 79 problems) — real-analysis **OCR: image placeholders** — disposition 2026-09-09: canonical retained copy for the byte-identical pair with `Folland Clipped Questions.pdf`; already linked from `wiki/real-analysis/resources/problems.md`. This is a clipped textbook-exercise resource rather than an exam sitting, so intake stops at the existing resource link rather than manufacturing a qualifying-exam collection.

- [x] [Nori_Galois_Theory_Problems.pdf](assets/attachments/extracted/Nori_Galois_Theory_Problems.md) (225L, 0 problems) — algebra — disposition 2026-09-12: already ingested completely as `SRC-NORI-GALOIS-THEORY-PROBLEMS`. A direct recount finds 42 numbered source problems across Sections 2–7 and exactly the same 42 collection entries, with no missing or extra IDs.

- [x] [Problems_in_Algebraic_Topology_-_Unknown.pdf](assets/attachments/extracted/Problems_in_Algebraic_Topology_-_Unknown.md) (123L, 0 problems) — alg-geom — disposition 2026-09-12: identified as Laurentiu Maxim’s *Problems in Algebraic Topology* and already ingested completely as `SRC-MAXIM-PROBLEMS-ALGEBRAIC-TOPOLOGY`. The source contains 52 numbered problems across six sections, and `just list-cards` reports exactly 52 source-checked collection entries.

- [x] [Giant_List_of_Problems.pdf](assets/attachments/extracted/Giant_List_of_Problems.md) (509L, 0 problems) — real-analysis — October 2012 — disposition 2026-09-09: canonical copy of the byte-identical pair with `PrincetonQuestions.pdf` (SHA-256 `9ef5c3fee6a62b2eb412ef4af6f0b40619821f25e0e0144702a2ba7b0f39d0c7`). This is a topic-organized Real Analysis question/reference bank rather than an exam sitting, and it is already linked from `wiki/real-analysis/resources/problems.md`; intake stops at that existing resource representation rather than manufacturing a qualifying-exam collection.

- [x] [Math_872_-*Section_1*-*Spring_2014*-_Problem_sets_page.pdf](assets/attachments/extracted/Math_872_-_Section_1_-_Spring_2014_-_Problem_sets_page.md) (253L, 0 problems) — topology — Spring 2014 — disposition 2026-09-12: already ingested completely as `SRC-UNL-MATH872-SPRING-2014-PROBLEM-SETS`. A direct source-label recount finds 52 distinct assignments (`6.A.1` through `12.B.3`, including PP.1–PP.5), exactly matching the 52 source-order collection entries.

- [x] [Measure_Theory_Qual_Problems.pdf](assets/attachments/extracted/Measure_Theory_Qual_Problems.md) (681L, 49 problems) — real-analysis **OCR: image placeholders** — disposition 2026-09-09: mixed-source Measure Theory question bank, not a single qualifying-exam sitting.
  Its introduction states that problems are drawn from Stein--Shakarchi and Carothers as well as CUNY Graduate Center qualifying exams, with color coding distinguishing textbook-only questions from questions seen on quals; that visual provenance is not faithfully retained by the markdown extraction.
  The canonical PDF is already linked from `wiki/real-analysis/resources/problems.md`, so intake stops at the existing resource representation rather than creating cards with false or erased source attribution.

- [x] [PrincetonQuestions.pdf](assets/attachments/extracted/PrincetonQuestions.md) (509L, 0 problems) — real-analysis — October 2012 — exact byte duplicate of `Giant_List_of_Problems.pdf` (same SHA-256); do not create a second collection

- [x] [Ring_Theory_Qual_Problems.pdf](assets/attachments/extracted/Ring_Theory_Qual_Problems.md) (539L, 141 problems) — algebra — August 29 — disposition 2026-09-12: reconciled with `SRC-KENT-STATE-RING-THEORY-QUAL-2017`, which contains all 141 source-order ring-theory qualifying-exam problems.

## Homework assignments (53)

- [x] [603_11.pdf](assets/attachments/extracted/603_11.md) (217L, 0 problems) — UNL — applied-algebra — disposition 2026-09-12: exact byte duplicate of `Algebra_HW_11_Solns.pdf` (SHA-256 `a1a7fe73b51ba280adb4cd185a7f0234dbbb3bf7da7e8675a9a68281b13ac6b9`); no duplicate collection needed.

- [x] [8150-hw1.pdf](assets/attachments/extracted/8150-hw1.md) (81L, 10 problems) — UGA — complex-analysis — disposition 2026-09-12: reconciled with `SRC-UGA-MATH8150-SPRING-2021-HW1`, containing all ten source-order complex-analysis homework problems.

- [x] [8150-hw2.pdf](assets/attachments/extracted/8150-hw2.md) (77L, 12 problems) — UGA — complex-analysis — disposition 2026-09-12: reconciled with `SRC-UGA-MATH8150-SPRING-2021-HW2`, containing all twelve source-order complex-analysis homework problems.

- [x] [8150-hw3.pdf](assets/attachments/extracted/8150-hw3.md) (83L, 11 problems) — UGA — complex-analysis — disposition 2026-09-12: reconciled with `SRC-UGA-MATH8150-SPRING-2021-HW3`, containing all eleven source-order complex-analysis homework problems.

- [x] [871-872June_2004_852-871.pdf](assets/attachments/extracted/871-872June_2004_852-871.md) (51L, 0 problems) — topology — disposition 2026-09-12: reconciled with `SRC-UNL-QUAL-JUNE-2004-970-852`; direct intake contains ten source-order qualifying-exam problems, correcting the inventory zero.

- [x] [Adam Syllabus.pdf](assets/attachments/extracted/Adam Syllabus.md) (58L, 0 problems) — UGA — diff-geom — Fall 2018 — disposition 2026-09-12: reference-only Adam Saltz UGA Math 8210 Topology of Manifolds Fall 2018 syllabus; it describes course objectives, texts, and homework policy but contains no authored exercises.
  Added to `vocabularies/references.bib` as `Saltz18Math8210Syllabus`; no cards manufactured.

- [x] [AG Exam Problems.pdf](assets/attachments/extracted/AG Exam Problems.md) (67L, 6 problems) — UNL — alg-geom — August 2015 — disposition 2026-09-12: reconciled with `SRC-AG-EXAM-PROBLEMS-2015`, containing all six source-order algebraic-geometry exam problems.

- [x] [Algebra_HW_11_Solns.pdf](assets/attachments/extracted/Algebra_HW_11_Solns.md) (217L, 0 problems) — UNL — applied-algebra — disposition 2026-09-12: reconciled with `SRC-SHONKWILER-ALGEBRA-HW11`, containing all six source-order homework problems represented by this solution packet.

- [x] [Algebra_HW_4_Solns.pdf](assets/attachments/extracted/Algebra_HW_4_Solns.md) (351L, 0 problems) — algebra — disposition 2026-09-12: reconciled with `SRC-SHONKWILER-ALGEBRA-HW4`, containing all seven source-order homework problems represented by this solution packet.

- [x] [Algebra_Notes.pdf](assets/attachments/extracted/Algebra_Notes.md) (972L, 74 problems) — algebra — disposition 2026-09-12: reference-only Kari Eifler algebra qualifying-exam definitions/theorems notes dated August 9, 2017. Added to `vocabularies/references.bib` as `Eifler17AlgebraQualNotes`; numbered definitions and propositions are not manufactured into problem cards.

- [x] [analysis_notes_eamonqg.pdf](assets/attachments/extracted/analysis_notes_eamonqg.md) (1041L, 0 problems) — applied-algebra — disposition 2026-09-12: reference-only Eamon Quinlan analysis review notes dated April 24, 2018. Added to `vocabularies/references.bib` as `Quinlan18AnalysisNotes`; no authored problem collection is present.

- [x] [Cambridge Examples Sheets.pdf](assets/attachments/extracted/Cambridge Examples Sheets.md) (321L, 33 problems) — applied-algebra — disposition 2026-09-12: reconciled with `SRC-CAMBRIDGE-COMPLEX-METHODS-LENT-2016`, which contains 39 source-order examples-sheet problems; the inventory count of 33 was incomplete.

- [x] [Ch6Sltns.pdf](assets/attachments/extracted/Ch6Sltns.md) (98L, 0 problems) — algebra — disposition 2026-09-12: reference-only Chapter 6 solution outlines for Gallian’s *Contemporary Abstract Algebra*, covering selected isomorphism and automorphism exercises.
  Retained as worked-reference enrichment on the group-theory resource page and now indexed in `wiki/archives/solution-compendia.md`; no collection or duplicate problem cards manufactured.

- [x] [ComplexAnalysisNotes.pdf](assets/attachments/extracted/ComplexAnalysisNotes.md) (128L, 0 problems) — topology — disposition 2026-09-12: reference-only James Broomfield *Complex Analysis Theorems and Results* summary.
  Added to `vocabularies/references.bib` as `Broomfield15ComplexAnalysisSummary`; theorem statements are not manufactured into cards.

- [x] [Complex_Analysis_Prelim_Review.pdf](assets/attachments/extracted/Complex_Analysis_Prelim_Review.md) (41L, 0 problems) — Princeton — complex-analysis — disposition 2026-09-12: reference-only Robert Varley *Study Guide for Complex Analysis Exam* topic/reference outline.
  Added to `vocabularies/references.bib` as `Varley14ComplexPrelimReview`; no problem cards manufactured.

- [x] [Eur_ComplexAnalysis_Notes (1).pdf](assets/attachments/extracted/Eur_ComplexAnalysis_Notes (1).md) (783L, 0 problems) — UNL — diff-geom — disposition 2026-09-12: reference-only Christopher Eur complex-analysis review notes following Stein--Shakarchi and Ahlfors, with selected textbook exercise solutions.
  Added to `vocabularies/references.bib` as `Eur15ComplexAnalysisNotes`; no duplicate textbook-exercise cards manufactured.

- [x] [f03solution.pdf](assets/attachments/extracted/f03solution.md) (407L, 0 problems) — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2003`; the solution packet is retained as provenance for all 18 Part A/B problems.

- [x] [f06solution.pdf](assets/attachments/extracted/f06solution.md) (342L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2006`; the solution packet is retained as provenance for all 18 Part A/B problems.

- [x] [f08solutions.pdf](assets/attachments/extracted/f08solutions.md) (191L, 0 problems) — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2008`; all 18 Part A/B problems are represented and the solution packet is retained as provenance.

- [x] [f10solutions.pdf](assets/attachments/extracted/f10solutions.md) (282L, 0 problems) — UNL — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2010`; all 18 Part A/B problems are represented and the solution packet is retained as provenance.

- [x] [f11solutions.pdf](assets/attachments/extracted/f11solutions.md) (206L, 2 problems) — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2011`; all 18 Part A/B problems are represented and the solution packet is retained as provenance.

- [x] [F12_Solutions.pdf](assets/attachments/extracted/F12_Solutions.md) (244L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2012`; all 18 Part A/B problems are represented and this companion solution packet is provenance.

- [x] [F13_Solutions.pdf](assets/attachments/extracted/F13_Solutions.md) (384L, 15 problems) — Berkeley — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2013`; all 18 Part A/B problems are represented and this companion solution packet is provenance.

- [x] [F16_Solutions.pdf](assets/attachments/extracted/F16_Solutions.md) (509L, 8 problems) — Berkeley — applied-algebra — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2016`; all 18 Part A/B problems are represented and this companion solution packet is provenance.

- [x] [Folland_Real_Analysis_Solns.pdf](assets/attachments/extracted/Folland_Real_Analysis_Solns.md) (3921L, 9 problems) — UNL — applied-algebra — January 20 — disposition 2026-09-10: Jonathan Mostovoy's partial solutions to Folland, a reference/solutions resource rather than an exam; already linked from `wiki/real-analysis/resources/solutions.md`. This PDF is byte-identical to `Mostovoy_-_Partial_Solutions_to_Follands_Real_Analysis_Part.pdf` (SHA-256 `bc7ed6db9fbdbbd5f9a73a67b3c40f4f92fcb7ed26878c9bb7657149b266dc61`), so no duplicate collection is needed.

- [x] [Galois_Group_Practice 1.pdf](assets/attachments/extracted/Galois_Group_Practice 1.md) (147L, 10 problems) — algebra — Summer 2016 — disposition 2026-09-12: exact byte duplicate of `Galois_Group_Practice.pdf` (SHA-256 `a4a5d76264a18227769ce63520fc05459f05a7a7f606b18e625596ccc942864f`); no duplicate collection needed.

- [x] [Galois_Group_Practice.pdf](assets/attachments/extracted/Galois_Group_Practice.md) (147L, 10 problems) — algebra — Summer 2016 — disposition 2026-09-12: reconciled with `SRC-MATH113-SUMMER-2016-HW7`, containing all ten source-order Galois-theory problems.

- [x] [Gompf Contact Topology.pdf](assets/attachments/extracted/Gompf Contact Topology.md) (1994L, 34 problems) — Harvard — diff-geom — Fall 2017 — disposition 2026-09-12: reconciled with complete `SRC-UT-M392C-CONTACT-TOPOLOGY-FALL-2017`. Direct source reading finds nine unique explicit `Exercise x.y` statements, exactly matching the nine collection cards; the inventory count of 34 came from numbered expository prose rather than authored exercises.

- [x] [Handle Attaching in Symplectic Top.pdf](assets/attachments/extracted/Handle Attaching in Symplectic Top.md) (2296L, 4 problems) — UNL — diff-geom — disposition 2026-09-12: Alexander Fauck, *Handle Attaching in Symplectic Topology — A Second Glance* (August 2, 2016), is research/reference literature giving a corrected proof of invariance of symplectic homology under subcritical handle attachment, not an exercise source.
  Added to `vocabularies/references.bib` as `Fauck16HandleAttaching`; no cards manufactured.

- [x] [hmwk3x.pdf](assets/attachments/extracted/hmwk3x.md) (117L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with `SRC-MATH655-HW3-2003`, which contains the five source-order homework problems represented by this packet.

- [x] [HW1.pdf](assets/attachments/extracted/HW1.md) (89L, 0 problems) — diff-geom — disposition 2026-09-12: reconciled with `SRC-UGA-MATH8210-FALL-2018-HW1`; direct source intake contains six exercises, all represented in source order.

- [x] [HW2.pdf](assets/attachments/extracted/HW2.md) (41L, 0 problems) — diff-geom — disposition 2026-09-12: reconciled with `SRC-UGA-MATH8210-FALL-2018-HW2`; direct source intake contains seven exercises, all represented in source order.

- [x] [HW3.pdf](assets/attachments/extracted/HW3.md) (49L, 5 problems) — diff-geom — disposition 2026-09-12: reconciled with `SRC-UGA-MATH8210-FALL-2018-HW3`; the collection contains all six source-order problems, correcting the inventory count of five.

- [x] [HW4.pdf](assets/attachments/extracted/HW4.md) (51L, 5 problems) — diff-geom — disposition 2026-09-12: reconciled with `SRC-UGA-MATH8210-FALL-2018-HW4`; all five source-order problems are represented.
  The retained file is dated November 4, 2018 and internally repeats the heading “Homework 3”, a source quirk already recorded by the collection.

- [x] [Lefschetz Fibrations.pdf](assets/attachments/extracted/Lefschetz Fibrations.md) (1597L, 0 problems) — UNL — alg-geom — July 2015 — disposition 2026-09-12: Emmanuel Giroux and John Pardon, *Existence of Lefschetz fibrations on Stein and Weinstein domains* (2015, revised 2016), is research/reference literature rather than an authored exercise source.
  Intake stops at reference enrichment; no problem cards are manufactured.

- [x] [math6338_hw8.pdf](assets/attachments/extracted/math6338_hw8.md) (299L, 7 problems) — real-analysis — disposition 2026-09-09: ingested as `SRC-MATH6338-HW8`; all seven Fourier-analysis homework problems are represented by source-checked, reviewed solution cards `P-M6338H8-1` through `P-M6338H8-7`.

- [x] [midpracsol.pdf](assets/attachments/extracted/midpracsol.md) (87L, 14 problems) — complex-analysis — disposition 2026-09-12: practice-solution notes already retained at `wiki/real-analysis/resources/solutions.md`; this is solution/reference material rather than primary problem provenance, so intake stops at the existing resource representation instead of creating duplicate cards.

- [x] [Mostovoy_-_Partial_Solutions_to_Follands_Real_Analysis_Part.pdf](assets/attachments/extracted/Mostovoy_-_Partial_Solutions_to_Follands_Real_Analysis_Part.md) (3921L, 9 problems) — UNL — applied-algebra — January 20 — disposition 2026-09-10: exact byte duplicate of `Folland_Real_Analysis_Solns.pdf` (SHA-256 `bc7ed6db9fbdbbd5f9a73a67b3c40f4f92fcb7ed26878c9bb7657149b266dc61`); already linked as a Real Analysis solutions resource, so do not create a second representation.

- [x] [problemsets.pdf](assets/attachments/extracted/problemsets.md) (160L, 0 problems) — topology — Fall 2013 — disposition 2026-09-12: S. Hermiller's UNL Math 871 Fall 2013 problem-set packet ingested as `SRC-UNL-MATH871-FALL-2013-PROBLEM-SETS`. Direct source reading finds 69 assigned problem references across PS1–PS11, not zero; 23 source-local cards plus canonical Munkres/Hatcher cards give 70 card appearances because PS3.1 and PS7.3 split across reusable and local subproblems.
  The packet names `PS9.1` as due but contains no statement or locator, so no missing mathematics is invented.

- [x] [Questions_from_Tie.pdf](assets/attachments/extracted/Questions_from_Tie.md) (749L, 126 problems) — complex-analysis — Fall 2009 — disposition 2026-09-12: D. Zack Garza's 2020 compilation of selected complex-analysis questions spanning multiple exam terms is maintainer-authored enrichment, not external collection provenance.
  It remains a resource at `wiki/complex-analysis/resources/problems.md`; no duplicate collection is manufactured, and it is removed from the Fall 2016 UGA exam provenance in favor of that collection's official DOCX.

- [x] [s05solution.pdf](assets/attachments/extracted/s05solution.md) (249L, 0 problems) — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-SPRING-2005`, containing all 18 Part A/B prelim problems; this solution packet is retained as provenance.

- [x] [s09solutions.pdf](assets/attachments/extracted/s09solutions.md) (241L, 18 problems) — Berkeley — prelim — Spring 2009 — disposition 2026-09-12: full UC Berkeley Spring 2009 preliminary-exam solution packet, ingested as `SRC-BERKELEY-PRELIM-SPRING-2009` with all 18 source-order problems `P-BKS09-1A` through `P-BKS09-9B`. The old count of six came from merged extraction headings.

- [x] [s11solutions.pdf](assets/attachments/extracted/s11solutions.md) (196L, 18 problems) — Berkeley — prelim — Spring 2011 — disposition 2026-09-12: full UC Berkeley Spring 2011 preliminary-exam solution packet, ingested as `SRC-BERKELEY-PRELIM-SPRING-2011` with all 18 source-order problems `P-BKS11-1A` through `P-BKS11-9B`. The prior zero count came from OCR/extraction heading loss.

- [x] [s12solutions.pdf](assets/attachments/extracted/s12solutions.md) (227L, 18 problems) — Berkeley — prelim — Spring 2012 — disposition 2026-09-12: full UC Berkeley Spring 2012 preliminary-exam solution packet, ingested as `SRC-BERKELEY-PRELIM-SPRING-2012` with all 18 source-order problems `P-BKS12-1A` through `P-BKS12-9B`. The prior zero count came from OCR/extraction heading loss.

- [x] [Schilling_-_Acknowledgement._I_am_grateful_for_the_help_of_Dr..pdf](assets/attachments/extracted/Schilling_-_Acknowledgement._I_am_grateful_for_the_help_of_Dr..md) (21267L, 53 problems) — UNL — applied-algebra — May 2017 — disposition 2026-09-12: canonical retained copy of René L. Schilling’s *Measures, Integrals & Martingales* (2nd ed.)
  solution manual; exact byte duplicate of `solutions-mims-2ed.pdf`. This is textbook solution/reference material already linked from `wiki/real-analysis/resources/solutions.md`, so intake stops at the existing reference representation rather than manufacturing qualifying-exam cards.

- [x] [Series_Problems_.pdf](assets/attachments/extracted/Series_Problems_.md) (566L, 12 problems) — real-analysis — disposition 2026-09-12: source inspection identifies an unattributed “Solutions to Assignment-2” packet on sequences and series.
  Ingested as `SRC-SEQUENCES-SERIES-ASSIGNMENT-2` with the twelve top-level cards `P-SERIES-A2-01` through `P-SERIES-A2-12`; the prior count of 22 came from multipart subquestions.
  No institution or assignment date is printed in the source, so neither is invented.

- [x] [solhwg.pdf](assets/attachments/extracted/solhwg.md) (177L, 12 problems) — applied-algebra — disposition 2026-09-12: Math 114 Galois-theory homework solution packet dated April 4, 2006, ingested as `SRC-MATH114-GALOIS-HOMEWORK-2006`. Problem sets 8 and 9 contribute six source-order problems each, represented as `P-M114-8-01` through `P-M114-8-06` and `P-M114-9-01` through `P-M114-9-06`; source-supplied worked solutions remain external provenance rather than duplicate local solution sections.

- [x] [solutions-mims-2ed.pdf](assets/attachments/extracted/solutions-mims-2ed.md) (21267L, 53 problems) — UNL — applied-algebra — May 2017 — disposition 2026-09-12: René L. Schilling, *Measures, Integrals & Martingales* (2nd ed.)
  solution manual, corrected July 2019; byte-identical to `Schilling_-_Acknowledgement._I_am_grateful_for_the_help_of_Dr..pdf` (SHA-256 `703be127b8cc7dbdf0903d1addb98941f183393e61c60423b356119b06f65081`). It is already retained on the real-analysis solutions resource page, so no duplicate card collection is manufactured.

- [x] [Sp13_Solutions.pdf](assets/attachments/extracted/Sp13_Solutions.md) (273L, 18 problems) — Berkeley — prelim — Spring 2013 — disposition 2026-09-12: companion solution packet for `SRC-BERKELEY-PRELIM-SPRING-2013`, retained as collection provenance.
  It contains worked solutions for the same 18 source problems; intake cards the statements once rather than creating a duplicate solution collection.
  The prior count of three came from lost extraction headings.

- [x] [Sp17_Exam_0.pdf](assets/attachments/extracted/Sp17_Exam_0.md) (317L, 8 problems) — Berkeley — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-SPRING-2017` and added as primary exam provenance beside the solution packet.
  Direct text-layer comparison confirms the same 18 statements `1A`–`9B` in both PDFs; the inventory count of eight was incomplete and the document is the full multi-subject Berkeley prelim, not only complex analysis.

- [x] [Sp17_Solutions.pdf](assets/attachments/extracted/Sp17_Solutions.md) (583L, 8 problems) — UNL — complex-analysis — disposition 2026-09-12: identified from the PDF itself as the University of California, Berkeley Spring 2017 preliminary examination solution packet, not a UNL complex-analysis source.
  Ingested as `SRC-BERKELEY-PRELIM-SPRING-2017` with all 18 problems `P-BKS17-1A` through `P-BKS17-9B` in exam order; the inventory count of eight was incomplete.
  This entry records the solution PDF as provenance; source-provided worked solutions were not copied into local `.solution` sections during intake.

- [x] [Tate_Galois_Theory_Problems.pdf](assets/attachments/extracted/Tate_Galois_Theory_Problems.md) (361L, 0 problems) — Harvard — algebra — October 22, 1985 **OCR: image placeholders** — disposition 2026-09-12: J. Tate’s Harvard Algebra 250(a) Fall 1985 homework compilation ingested as `SRC-HARVARD-TATE-ALGEBRA-250A-1985`. Direct PDF inspection finds 36 authored problems across five dated sheets, the two-part `X^7-7X+3` challenge, and nine prime-ideal exercises; the Newton-formula/discriminant pages are expository reference material and were not manufactured into cards.
  The 36 source-order cards are grouped by those seven source sections as `P-TATE85-*`; the inventory count of zero was a false negative.

- [x] [Week5_solns.pdf](assets/attachments/extracted/Week5_solns.md) (570L, 4 problems) — complex-analysis **OCR: image placeholders** — disposition 2026-09-12: Christian Parkinson’s 2020 Week 5 Abstract Algebra & Complex Analysis GRE-prep packet, ingested as `SRC-PRELIM-PRACTICE-WEEK5-2020` with all 35 numbered prompts in source order as `P-PRACT20-W5-01` through `P-PRACT20-W5-35`. The inventory count of four was a false negative.
  The PDF remains provenance for its worked solutions; they were not copied into local `.solution` sections because the packet contains demonstrably incorrect supplied answers (for example Problem 4 calls $x\mapsto -x$ a homomorphism $U_4\to U_4$, and Problem 28 drops the minus sign in the contour integral).

## Solution writeups (33)

- [x] [AG Solutions (1).pdf](assets/attachments/extracted/AG Solutions (1).md) (5121L, 0 problems) — no metadata **OCR: binary/encoding garbage, possible encoding issues** — disposition 2026-09-12: reference-only archival algebraic-geometry solution notes.
  The 24-page PDF has no identifying author/date metadata and its embedded text layer is control-character/encoding garbage, so no reliable problem extraction is possible without inventing content.
  Retained on the solution-compendia resource page and added to `vocabularies/references.bib` as `AGSolutionsArchive`; no cards manufactured.

- [x] [Algebra_Final_Solns 1.pdf](assets/attachments/extracted/Algebra_Final_Solns 1.md) (116L, 14 problems) — algebra — disposition 2026-09-12: exact byte duplicate of `Algebra_Final_Solns.pdf` (SHA-256 `75d9773517a214758c59c3b4c5e274ff27f6e2b17b1415fc1a0f962e4fb60aa2`); no duplicate collection needed.

- [x] [Algebra_Final_Solns.pdf](assets/attachments/extracted/Algebra_Final_Solns.md) (116L, 14 problems) — algebra — disposition 2026-09-12: reconciled with `SRC-MATH504-FINAL-AUTUMN-2003`, which retains this solution packet as provenance for the seven source-order final-exam problems.

- [x] [basic-12F.pdf](assets/attachments/extracted/basic-12F.md) (53L, 0 problems) — UCLA — disposition 2026-09-12: already ingested as `SRC-UCLA-BASIC-FALL-2012`; all twelve source problems are represented in order by `P-UCLAB12-01` through `P-UCLAB12-12`, with the vendored PDF recorded as collection provenance.

- [x] [Ch10PtASltns.pdf](assets/attachments/extracted/Ch10PtASltns.md) (51L, 0 problems) — algebra — disposition 2026-09-12: reconciled with `SRC-CH10A-HOMOMORPHISM-SOLUTION-OUTLINES`, containing the seven selected Chapter 10 Part A exercises represented by this solution-outline packet.

- [x] [Ch10Sltns.pdf](assets/attachments/extracted/Ch10Sltns.md) (105L, 4 problems) — alg-geom — disposition 2026-09-12: reconciled with `SRC-CH10-HOMOMORPHISM-SOLUTION-OUTLINES`, containing eighteen selected Chapter 10 exercises represented by this packet.

- [x] [Ch12Sltns.pdf](assets/attachments/extracted/Ch12Sltns.md) (69L, 3 problems) — algebra — disposition 2026-09-12: reconciled with `SRC-CH12-RING-SOLUTION-OUTLINES`, containing seventeen selected Chapter 12 ring-theory exercises.

- [x] [Ch14Sltns.pdf](assets/attachments/extracted/Ch14Sltns.md) (99L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with `SRC-CH14-IDEAL-SOLUTION-OUTLINES`, containing fifteen selected Chapter 14 ideal-theory exercises.

- [x] [Ch15Sltns.pdf](assets/attachments/extracted/Ch15Sltns.md) (73L, 0 problems) — algebra — disposition 2026-09-12: reconciled with `SRC-CH15-RING-HOMOMORPHISM-SOLUTION-OUTLINES`, containing thirteen selected Chapter 15 exercises.

- [x] [Ch16Sltns.pdf](assets/attachments/extracted/Ch16Sltns.md) (61L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with `SRC-CH16-POLYNOMIAL-RING-SOLUTION-OUTLINES`, containing fourteen selected Chapter 16 exercises.

- [x] [Ch17Sltns.pdf](assets/attachments/extracted/Ch17Sltns.md) (61L, 0 problems) — algebra — disposition 2026-09-12: reconciled with `SRC-CH17-POLYNOMIAL-SOLUTION-OUTLINES`, containing twelve selected Chapter 17 exercises.

- [x] [Ch8Sltns.pdf](assets/attachments/extracted/Ch8Sltns.md) (127L, 1 problems) — algebra — disposition 2026-09-12: reconciled with `SRC-CH8-DIRECT-PRODUCT-SOLUTION-OUTLINES`, containing twenty-five selected Chapter 8 exercises.

- [x] [ExerciseSet8f06a.pdf](assets/attachments/extracted/ExerciseSet8f06a.md) (173L, 6 problems) — algebra — disposition 2026-09-12: reconciled with `SRC-MATH7200-EXERCISE-SET-8-FALL-2006`, which contains all six source-order exercises.

- [x] [f03.pdf](assets/attachments/extracted/f03.md) (103L, 0 problems) — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2003`, containing all 18 Part A/B prelim problems in source order.

- [x] [f09solutions.pdf](assets/attachments/extracted/f09solutions.md) (300L, 0 problems) — UNL — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2009`, containing all 18 Part A/B prelim problems; the vendored solution packet is retained as provenance.

- [x] [F12_Exam.pdf](assets/attachments/extracted/F12_Exam.md) (238L, 8 problems) — Berkeley — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2012`, containing all 18 Part A/B prelim problems in source order.

- [x] [F13_Exam.pdf](assets/attachments/extracted/F13_Exam.md) (268L, 15 problems) — Berkeley — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2013`, containing all 18 Part A/B prelim problems in source order.

- [x] [F15_Exam.pdf](assets/attachments/extracted/F15_Exam.md) (317L, 8 problems) — Berkeley — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2015`, containing all 18 Part A/B prelim problems in source order.

- [x] [F16_Exam.pdf](assets/attachments/extracted/F16_Exam.md) (337L, 8 problems) — Berkeley — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2016`, containing all 18 Part A/B prelim problems in source order.

- [x] [Fall_2014_Exam.pdf](assets/attachments/extracted/Fall_2014_Exam.md) (321L, 8 problems) — Berkeley — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2014`, containing all 18 Part A/B prelim problems in source order.

- [x] [fall-2018-prelim_solutions.pdf](assets/attachments/extracted/fall-2018-prelim_solutions.md) (289L, 0 problems) — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-FALL-2018`, containing all 18 Part A/B prelim problems; the vendored solution packet is retained as provenance.

- [x] [final2011-solns.pdf](assets/attachments/extracted/final2011-solns.md) (122L, 5 problems) — algebra — disposition 2026-09-12: reconciled with complete `SRC-ALGEBRA-FINAL-2011-SOLUTIONS`, containing all five source-order problems.

- [x] [Point_Set_Topology_Midterm_with_Solns_-_Unknown.pdf](assets/attachments/extracted/Point_Set_Topology_Midterm_with_Solns_-_Unknown.md) (55L, 6 problems) — topology — disposition 2026-09-12: reconciled with complete `SRC-POINT-SET-TOPOLOGY-MIDTERM`, containing all six source-order problems.

- [x] [s06.pdf](assets/attachments/extracted/s06.md) (81L, 0 problems) — complex-analysis — disposition 2026-09-12: reconciled with complete `SRC-BERKELEY-PRELIM-SPRING-2006`, containing all 18 Part A/B prelim problems in source order.

- [x] [s07.pdf](assets/attachments/extracted/s07.md) (101L, 0 problems) — prelim — reclassified 2026-09-09: mixed preliminary exam spanning analysis, algebra, complex analysis, ODEs, and linear algebra.
  — disposition 2026-09-12: reconciled with complete `SRC-BERKELEY-PRELIM-SPRING-2007`, containing all 18 mixed-subject Part A/B prelim problems in source order.

- [x] [Sample_Comp_Fa03Alg.pdf](assets/attachments/extracted/Sample_Comp_Fa03Alg.md) (51L, 5 problems) — applied-algebra — disposition 2026-09-12: reconciled with `SRC-ALGEBRA-COMP-FALL-2003`, containing all five source-order sample comprehensive-exam problems.

- [x] [Sp16_Exam.pdf](assets/attachments/extracted/Sp16_Exam.md) (335L, 8 problems) — Berkeley — complex-analysis — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-SPRING-2016`, containing all 18 Part A/B prelim problems in source order.

- [x] [Sp16_Solutions.pdf](assets/attachments/extracted/Sp16_Solutions.md) (415L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with `SRC-BERKELEY-PRELIM-SPRING-2016`; the solution packet is retained as provenance for the same 18 source-order problems.

- [x] [Week1_solns.pdf](assets/attachments/extracted/Week1_solns.md) (257L, 0 problems) — complex-analysis — disposition 2026-09-12: reconciled with `SRC-PRELIM-CALCULUS-I-WEEK1`; direct numbering in the source runs 1--28 and the collection contains exactly 28 source-order cards.

- [x] [Week2_solns.pdf](assets/attachments/extracted/Week2_solns.md) (440L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with `SRC-PRELIM-CALCULUS-II-WEEK2`; direct numbering in the source runs 1--23 and the collection contains exactly 23 source-order cards.

- [x] [Week3_solns.pdf](assets/attachments/extracted/Week3_solns.md) (362L, 0 problems) — complex-analysis **OCR: image placeholders** — disposition 2026-09-12: reconciled with `SRC-PRELIM-PRACTICE-WEEK3-2020`; direct numbering in the source runs 1--28 and the collection contains exactly 28 source-order cards.

- [x] [Week4_solns.pdf](assets/attachments/extracted/Week4_solns.md) (474L, 0 problems) — UNL — applied-algebra **OCR: image placeholders** — disposition 2026-09-12: reconciled with `SRC-PRELIM-PRACTICE-WEEK4-2020`; direct numbering in the source runs 1--26 and the collection contains exactly 26 source-order cards.

- [x] [Week6_solns.pdf](assets/attachments/extracted/Week6_solns.md) (501L, 0 problems) — UNL — topology **OCR: image placeholders** — disposition 2026-09-12: reconciled with `SRC-PRELIM-PRACTICE-WEEK6-2020`; direct numbering in the source runs 1--27 and the collection contains exactly 27 source-order cards.

## Solution manuals (3)

- [x] [chapter-1.pdf](assets/attachments/extracted/chapter-1.md) (87L, 16 problems) — no metadata — disposition 2026-09-12: reconciled with complete `SRC-GRE-MATH-CH1-REVIEW`, which represents all 25 numbered Chapter 1 review questions in source order.

- [x] [s03solution.pdf](assets/attachments/extracted/s03solution.md) (231L, 0 problems) — complex-analysis — disposition 2026-09-12: reconciled with complete `SRC-BERKELEY-PRELIM-SPRING-2003`; the vendored solution packet is provenance for all 18 Part A/B problems in source order.

- [x] [s06solution.pdf](assets/attachments/extracted/s06solution.md) (409L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with complete `SRC-BERKELEY-PRELIM-SPRING-2006`; the vendored solution packet is provenance for all 18 Part A/B problems in source order.

## Lecture notes (4)

- [x] [140A_Exam_Review.pdf](assets/attachments/extracted/140A_Exam_Review.md) (97L, 0 problems) — complex-analysis — disposition 2026-09-12: reference-only Todd Kemp Math 140A Exam 2 key-facts review (lim sup/inf, complex numbers, series, metric spaces), not a problem source.
  Retained on the prelim reference page and added to `vocabularies/references.bib` as `Kemp16Math140AExam2Review`; no cards manufactured.

- [x] [8.1.2 Further Examples (1).pdf](assets/attachments/extracted/8.1.2 Further Examples (1).md) (136L, 4 problems) — UGA — complex-analysis — March 30 **OCR: image placeholders** — disposition 2026-09-12: reference-only Jingzhi Tie UGA Math 8150 Spring 2020 lecture deck of worked conformal-mapping examples, not an exercise source despite the inventory count.
  Retained on the complex-analysis resource page and added to `vocabularies/references.bib` as `Tie20ConformalExamples`; no cards manufactured.

- [x] [Math_872_-*Section_1*-*Spring_2014*-_(Active)_Table_of_Contents.pdf](assets/attachments/extracted/Math_872_-_Section_1_-_Spring_2014_-_(Active)_Table_of_Contents.md) (351L, 0 problems) — topology — Spring 2014 — disposition 2026-09-12: reference-only Spring 2014 UNL Math 872 Algebraic Topology course contents/theorem outline, not a problem source.
  Retained on the topology resource page and added to `vocabularies/references.bib` as `Hermiller14Math872`; no cards manufactured.

- [x] [Perutz_-*2008*-_ALGEBRAIC_TOPOLOGY_I_FALL_2008.pdf](assets/attachments/extracted/Perutz_-_2008_-_ALGEBRAIC_TOPOLOGY_I_FALL_2008.md) (3929L, 58 problems) — topology — Fall 2008 — disposition 2026-09-12: reconciled to complete `SRC-PERUTZ-ALGEBRAIC-TOPOLOGY-I-2008`. Direct source typography contains 89 explicit exercises, not the inventory count of 58. A duplicate partial Chapters 1–4 intake was collapsed into the canonical collection by retaining its richer source-checked transcriptions for those 17 exercises; the canonical collection now contains all 89 exercises in source order.

## Textbook/theorem notes (16)

- [x] [8.2.3 Normal family.pdf](assets/attachments/extracted/8.2.3 Normal family.md) (159L, 0 problems) — UGA — complex-analysis — March 30 **OCR: image placeholders** — disposition 2026-09-12: reference-only UGA Math 8150 lecture notes by Jingzhi Tie on normal families, Montel’s theorem, Arzelà–Ascoli, and Hurwitz (Spring 2020), not an exercise source.
  Retained on the complex-analysis resource page and added to `vocabularies/references.bib` as `Tie20Montel`; no problem cards manufactured.

- [x] [8.3 Riemann Mapping Theorem (1).pdf](assets/attachments/extracted/8.3 Riemann Mapping Theorem (1).md) (233L, 0 problems) — UGA — complex-analysis — March 30 **OCR: image placeholders** — disposition 2026-09-12: reference-only UGA Math 8150 lecture notes by Jingzhi Tie on the Riemann mapping theorem (Spring 2020), not an exercise source.
  Retained on the complex-analysis resource page and added to `vocabularies/references.bib` as `Tie20RMT`; no problem cards manufactured.

- [x] [871-872January_2006_850-871.pdf](assets/attachments/extracted/871-872January_2006_850-871.md) (53L, 0 problems) — topology — disposition 2026-09-12: already ingested as `SRC-UNL-QUAL-850-871-JANUARY-2006`; its five Section A questions are local cards `P-UNL850871-06A1` through `P-UNL850871-06A5`, and the five Section B topology questions reuse canonical cards from the separately retained January 2006 UNL topology paper.
  All ten source questions are represented in source order.

- [x] [Ch11Sltns.pdf](assets/attachments/extracted/Ch11Sltns.md) (61L, 11 problems) — algebra — disposition 2026-09-12: reconciled with complete `SRC-CH11-ABELIAN-GROUP-SOLUTION-OUTLINES`, containing ten selected finite-abelian-group exercises represented by this packet.

- [x] [Ch13Sltns.pdf](assets/attachments/extracted/Ch13Sltns.md) (73L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with complete `SRC-CH13-RING-SOLUTION-OUTLINES`, containing the fourteen selected ring-theory exercises represented by this solution-outline packet.

- [x] [Ch20Sltns.pdf](assets/attachments/extracted/Ch20Sltns.md) (41L, 0 problems) — algebra — disposition 2026-09-12: reconciled with complete `SRC-CH20-FIELD-SOLUTION-OUTLINES`, containing the nine selected field-theory exercises represented by this solution-outline packet.

- [x] [Ch7Sltns.pdf](assets/attachments/extracted/Ch7Sltns.md) (133L, 0 problems) — algebra **OCR: image placeholders** — disposition 2026-09-12: reconciled with complete `SRC-CH7-GROUP-SOLUTION-OUTLINES`, which preserves 21 selected source exercises/solution outlines in source order.

- [x] [f04solution.pdf](assets/attachments/extracted/f04solution.md) (327L, 0 problems) — applied-algebra — disposition 2026-09-12: reconciled with complete `SRC-BERKELEY-PRELIM-FALL-2004`; the vendored solution packet is provenance for the 18 source-order Part A/B cards `P-BKF04-1A` through `P-BKF04-9B`.

- [x] [Folland_Solutions.pdf](assets/attachments/extracted/Folland_Solutions.md) (9097L, 131 problems) — real-analysis — disposition 2026-09-09: exact byte duplicate of `Le_-_MEASURE_and_INTEGRATION_Problems_with_Solutions.pdf` (SHA-256 `45cc7ffaf7ba4e7a3c41884817409e2728764bcce8a651979df4bb74cdccbc97`). The migration ledger already identifies the Le-named file as the retained native source, and the Real Analysis solutions resource page links this material; no duplicate collection is needed.

- [x] [Le_-_MEASURE_and_INTEGRATION_Problems_with_Solutions.pdf](assets/attachments/extracted/Le_-_MEASURE_and_INTEGRATION_Problems_with_Solutions.md) (9097L, 131 problems) — real-analysis — disposition 2026-09-09: canonical retained copy for the byte-identical pair with `Folland_Solutions.pdf`. This is Le's *Measure and Integration: Problems with Solutions*, a reference/problem-solutions resource rather than an exam paper; it remains a resource source and does not require a qualifying-exam collection.

- [x] [math185f09-hw7sol.pdf](assets/attachments/extracted/math185f09-hw7sol.md) (307L, 4 problems) — complex-analysis — FALL 2009 — disposition 2026-09-12: already ingested as `SRC-BERKELEY-MATH185-FALL-2009-PSET7`; all four numbered problems are represented in source order as `P-BK185F09-7-01` through `P-BK185F09-7-04` with the vendored solution packet retained as provenance.

- [x] [Neil_Spring_2018_Solutions.pdf](assets/attachments/extracted/Neil_Spring_2018_Solutions.md) (8L, 3 problems) — complex-analysis — disposition 2026-09-12: exact byte duplicate of `Spring2018_SOLUTIONS.pdf` (SHA-256 `0247c09295120c5594a5d27648f5381fdb744bf3e6f1dbe7a7b74dfd79a29ae9`); the five handwritten solutions match the five problems already represented in `SRC-UGA-RA-SPRING-2018`, so the packet is retained as enrichment rather than duplicate provenance or cards.

- [x] [Real_Named_Theorems.pdf](assets/attachments/extracted/Real_Named_Theorems.md) (287L, 13 problems) — real-analysis — July 10 **OCR: image placeholders** — disposition 2026-09-09: Kari Eifler's *Real Variables Named Theorems* is theorem/reference notes (definitions, theorem statements, and convergence-summary material), not an exam or problem collection.
  It is already linked from `wiki/real-analysis/resources/books-notes.md`; intake therefore stops at that reference resource.

- [x] [s04solution.pdf](assets/attachments/extracted/s04solution.md) (333L, 3 problems) — applied-algebra — disposition 2026-09-12: companion solutions for the UC Berkeley Spring 2004 Preliminary Examination, ingested together with the exam as `SRC-BERKELEY-PRELIM-SPRING-2004`. The source has 18 exam problems (Part A 1–9 and Part B 1–9), all represented in paper order with the retained solution packet source-checked and reviewed.

- [x] [solns7.pdf](assets/attachments/extracted/solns7.md) (203L, 5 problems) — algebra — disposition 2026-09-12: St Andrews MT5824 Topics in Groups Problem Sheet VII on nilpotent groups, ingested as `SRC-STANDREWS-MT5824-PSET7-2010`. The retained packet contains six numbered problems, not the inventory count of five; all six are represented in source order by `P-MT5824-7-01` through `P-MT5824-7-06`, with the packet solutions source-checked and reviewed.

- [x] [Spring2018_SOLUTIONS.pdf](assets/attachments/extracted/Spring2018_SOLUTIONS.md) (8L, 3 problems) — complex-analysis — disposition 2026-09-12: handwritten solution packet for the five-problem UGA Spring 2018 Real Analysis exam already complete as `SRC-UGA-RA-SPRING-2018`; byte-identical to `Neil_Spring_2018_Solutions.pdf` (SHA-256 `0247c09295120c5594a5d27648f5381fdb744bf3e6f1dbe7a7b74dfd79a29ae9`). No duplicate collection or cards are created.

## Review sheets (14)

- [x] [ALGEBRA_REVIEW1.pdf](assets/attachments/extracted/ALGEBRA_REVIEW1.md) (144L, 8 problems) — algebra **OCR: image placeholders** — disposition 2026-09-11: Alessandra Pantano’s 2011 algebra review packet ingested as `SRC-ALGEBRA-REVIEW-PANTANO-2011`. The inventory count of eight is a false negative: the source explicitly groups 6 questions from test 3, 6 from test 2, and 7 from test 1, for 19 total.
  They are represented in source order as `P-ALGPAN11-01` through `P-ALGPAN11-19`; source crops are retained for all questions, including prompts/choices lost by OCR.

- [x] [chapter-3.pdf](assets/attachments/extracted/chapter-3.md) (178L, 13 problems) — algebra **OCR: image placeholders** — disposition 2026-09-11: `Cracking the GRE Mathematics Subject Test` Chapter 3 multivariable/vector-calculus review ingested as `SRC-GRE-MATH-CH3-REVIEW`. Direct inspection of the six-page scan and extraction finds 30 numbered review questions, not the inventory count of 13; all 30 are represented in source order as `P-GRECH3-01` through `P-GRECH3-30`. Scanned source pages are preserved on Questions 1–3, 10, and 30 where diagrams or answer choices are image-dependent/OCR-damaged.

- [x] [chapter-4.pdf](assets/attachments/extracted/chapter-4.md) (212L, 5 problems) — calculus **OCR: image placeholders** — disposition 2026-09-12: already ingested as `SRC-GRE-MATH-CH4-REVIEW`, with all sixteen numbered Chapter 4 review questions represented in source order by `P-GRECH4-01` through `P-GRECH4-16`. The collection records the scan-loss in Question 2 and the missing slope-field figures in Question 4 rather than guessing unrecoverable source text.

- [x] [chapter-5.pdf](assets/attachments/extracted/chapter-5.md) (245L, 5 problems) — no metadata **OCR: image placeholders** — disposition 2026-09-12: reconciled with existing `SRC-GRE-MATH-CH5-REVIEW`.

- [x] [chapter-6.pdf](assets/attachments/extracted/chapter-6.md) (65L, 9 problems) — applied-algebra — disposition 2026-09-12: reconciled with existing `SRC-GRE-MATH-CH6-REVIEW`. The retained Chapter 6 review source contains 20 numbered group/ring/number-theory questions, all represented in source order by `P-GRECH6-01` through `P-GRECH6-20`; the inventory count of nine was incomplete.
  Earlier two-pass OCR repair is recorded in `queues/E-corrections.md`, including the surviving scan gaps in Questions 17, 18, and 20. No duplicate cards were created; the collection is now marked complete.

- [x] [linear_algebra_from_test2.pdf](assets/attachments/extracted/linear_algebra_from_test2.md) (17L, 3 problems) — applied-algebra — disposition 2026-09-12: reconciled with existing `SRC-LINEAR-ALGEBRA-TEST2-REVIEW`. The preserved extraction contains eight numbered multiple-choice linear-algebra questions (10, 48, 15, 38, 35, 32, 52, 53), all already represented in source order by the collection; the inventory count of three was incomplete.
  The PDF has no usable text layer, so source checks are explicitly against the retained PDF extraction.
  All eight cards are source-checked and the collection is marked complete.

- [x] [Master_10_27_2018.pdf](assets/attachments/extracted/Master_10_27_2018.md) (2786L, 4 problems) — UNL — applied-algebra — disposition 2026-09-12: reference-only broad mathematics/GRE compendium (41 pages, created October 27, 2018) covering formulas, definitions, theorem summaries, and worked examples across algebra, geometry, analysis, probability, topology, and related subjects.
  The scanner's four “problems” are incidental examples rather than an authored exercise set, and no UNL affiliation is evidenced in the document.
  It is now retained explicitly on `wiki/prelim/resources/references.md`; no problem cards are manufactured.

- [x] [Math_871_-_Table_of_Contents.pdf](assets/attachments/extracted/Math_871_-_Table_of_Contents.md) (407L, 0 problems) — diff-geom — disposition 2026-09-12: reference-only Math 871 course table of contents covering topology definitions, constructions, invariants, and theorem statements rather than an authored exercise source.
  It is retained and now explicitly annotated on `wiki/topology/resources/books-notes.md`; intake stops at reference enrichment and no problem cards are manufactured.

- [x] [Review1.pdf](assets/attachments/extracted/Review1.md) (77L, 11 problems) — algebra — disposition 2026-09-12: reconciled with existing `SRC-ALGEBRA-TEST-REVIEW-1`. All seven open-ended questions and four true/sometimes/false questions are already represented in source order by `P-ALGREV1-01` through `P-ALGREV1-11`; every card is source-checked, solved, and reviewed.
  The collection is now marked complete; the surrounding review-topic bullets remain reference material rather than separate problem cards.

- [x] [Separation_defintions.pdf](assets/attachments/extracted/Separation_defintions.md) (29L, 0 problems) — topology — disposition 2026-09-12: reconciled with existing `SRC-TOPOLOGY-SEPARATION-COUNTABILITY-REVIEW`. The PDF is a one-page definitions/review sheet whose only explicit proof tasks are the regularity and normality closure-neighborhood criteria; those are already represented in source order by `P-SEPDEF-01` and `P-SEPDEF-02`. Both cards are now source-checked and the collection is marked complete; the definitions/examples remain reference material rather than being manufactured into additional problem cards.

- [x] [solution6.pdf](assets/attachments/extracted/solution6.md) (795L, 0 problems) — applied-algebra **OCR: image placeholders** — disposition 2026-09-11: Harvard Math 21b Spring 2018 Practice Final 6 (May 8, 2018), ingested as `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-6` with 14 source-order problem cards `P-HM21B18-PF6-01` through `P-HM21B18-PF6-14`. The inventory `0 problems` count was a false negative caused by the extraction layout; the PDF score table and headings explicitly contain Problems 1–14. Image-dependent prompts are preserved from source pages.
  The source-provided Problem 8 solution is not imported because it gives incorrect eigenvalues for its displayed matrix; the issue is recorded in `COMPLAINTS.md`.

- [x] [fields.pdf](assets/attachments/extracted/fields.md) (177L, 8 selected qual problems) — algebra — Fall 2007 — Disposition 2026-09-03: `SRC-UCSD-ALG-REVIEW-FIELDS`; review-sheet provenance retained and matching exam problems reuse canonical cards.

- [x] [groups.pdf](assets/attachments/extracted/groups.md) (231L, 7 selected qual problems) — algebra — Spring 2008 — Disposition 2026-09-03: `SRC-UCSD-ALG-REVIEW-GROUPS`; review-sheet provenance retained and matching exam problems reuse canonical cards.

- [x] [ringsandmodules.pdf](assets/attachments/extracted/ringsandmodules.md) (151L, 8 selected qual problems) — algebra — Spring 2007 — Disposition 2026-09-03: `SRC-UCSD-ALG-REVIEW-RINGS-MODULES`; exact matches reuse canonical cards and the modified scalar-extension item has one explicit `variant-of` card.

## OCR issues (44 files)

- 8.1.2 Further Examples (1).md: image placeholders

- 8.2.3 Normal family.md: image placeholders

- 8.3 Riemann Mapping Theorem (1).md: image placeholders

- AG Solutions (1).md: binary/encoding garbage, possible encoding issues

- ALGEBRA_REVIEW1.md: image placeholders

- analysis_2003-2007.md: MinerU hallucination notes

- basic-01F.md: image placeholders

- basic-02F.md: image placeholders

- basic-02S.md: image placeholders

- basic-02W.md: image placeholders

- basic-03F.md: image placeholders

- calculus_practice_test3.md: image placeholders

- Ch7Sltns.md: image placeholders

- chapter-2.md: image placeholders

- chapter-3.md: image placeholders

- chapter-4.md: image placeholders

- chapter-5.md: image placeholders

- Chapter-7.md: image placeholders

- Conrad_-_SOME_EXAMPLES_OF_THE_GALOIS_CORRESPONDENCE.md: image placeholders

- day_5_fundamental_group.md: image placeholders

- Folland Clipped Questions.md: image placeholders

- Folland_Clipped_Questions.md: image placeholders

- Measure_Theory_Qual_Problems.md: image placeholders

- multivariable_calculus.md: image placeholders

- Probability_Review.md: image placeholders

- Qual_Review_Selection_of_Hatcher_Problems_-_Unknown.md: image placeholders

- Real_Named_Theorems.md: image placeholders

- s08solution.md: image placeholders

- solution3.md: image placeholders

- solution4.md: image placeholders

- solution5.md: image placeholders

- solution6.md: image placeholders

- solution7.md: image placeholders

- solution8.md: image placeholders

- solution9.md: image placeholders

- solution.md: image placeholders

- Tate_Galois_Theory_Problems.md: image placeholders

- topology_2005-2003.md: image placeholders

- TopologySept19solutions.md: image placeholders

- UCSD_Topology_Qual_Problems_2020-05-29.md: image placeholders

- Week3_solns.md: image placeholders

- Week4_solns.md: image placeholders

- Week5_solns.md: image placeholders

- Week6_solns.md: image placeholders

## Summary

| Type | Count |
| --- | ---: |
| Qualifying exams | 86 |
| Preliminary exams | 47 |
| UCLA basic exams | 41 |
| Exams with solutions | 39 |
| Final exams | 1 |
| Midterm exams | 4 |
| Practice exams | 2 |
| Exam or problem set | 1 |
| Workshop materials | 6 |
| Problem sets | 9 |
| Homework assignments | 53 |
| Solution writeups | 33 |
| Solution manuals | 3 |
| Lecture notes | 2 |
| Textbook/theorem notes | 16 |
| Review sheets | 11 |
| **Total** | **354** |
