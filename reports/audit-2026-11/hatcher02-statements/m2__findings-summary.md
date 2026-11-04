# SRC-TEXT-HAT02 — remaining unread cards: census, statement audit, proof audit

Auditor: m2. Witness for every book claim: line numbers of `tmp/hat/AT.txt` (the extraction's \f
form-feeds delimit pages; the printed page number is in each page's running head, so page→line is
recoverable, but 11 pages carry no number token in the extraction).

## Card census (unread slice)

| section | cards | of which unread |
|---|---|---|
| 3-d | 3 | 3 |
| 3-f | 9 | 9 |
| 3-h | 6 | 6 |
| 4-1 | 23 | 14 (exercises 1–9 already read) |
| 4-2 | 39 | 39 |
| 4-3 | 24 | 24 |
| 4-a | 5 | 5 |
| 4-b | 2 | 2 |
| 4-d | 10 | 10 |
| 4-f | 3 | 3 |
| 4-g | 4 | 4 |
| 4-h | 4 | 4 |
| 4-i | 3 | 3 |
| 4-k | 6 | 6 |
| 4-l | 5 | 5 |
| **total** | **146** | **137** |

There are no `4-c`, `4-e` or `4-j` directories (Hatcher §4.C, §4.E, §4.J have no exercises).
Book exercise blocks: §3.D 15093, §3.F 15973, §3.H 16834, §4.1 17817 (ex. 10 at 17861), §4.2 19319,
§4.3 20754, §4.A 21092, §4.B 21215, §4.D 22149, §4.F 22600, §4.G 22813, §4.H 23110, §4.I 23272,
§4.K 24094, §4.L 25802.

## What was actually done

* **Statement layer: all 137 unread cards**, card by card against the printed text. Per-card verdicts
  and book line quotes are in `findings-<section>.md` (15 files, one per section slice).
* **Proof layer: 40 cards read line by line** — all of §3.D (3), §3.F (1–3), §3.H (6), §4.A (1–3),
  §4.B (2), §4.F (3), §4.G (4), §4.H (4), §4.I (3), §4.K (6), §4.L (1–3).
  The remaining **97 proofs are marked unread**, not correct: §3.F 4–9 (6), §4.A-4, §4.A-5,
  §4.1 10–23 (14), §4.2 (39), §4.3 (24), §4.D (10), §4.L-4, §4.L-5.

## Defects, most serious first

**A. Statements that lost mathematical content (not paraphrase).**

1. **E-HAT-4.2-29** — a three-part exercise reduced to its opening sentence. AT 19436–19443 prints
   "… via the following steps:", then (a) with the hint "[Rechoose the generator of the Zm action on
   S 2n−1 .]" (19444–19449), (b) the construction of g with "degree k1 ··· kn + dm" and the hint
   "[Show first that a lift of g to the universal cover S 2n−1 has this degree.]" (19450–19457), and
   (c) with "[For πi with i > 1 , consider a lift of g to the universal cover.]" (19461–19466). All
   of it is gone from the card.
2. **E-HAT-4.2-28** — the argument the exercise asks the reader to fill in is deleted: AT 19430–19435
   (covering space S^n → M, building K(Zp×Zp,1) from M by one (n+1)-cell, the H^{n+1} contradiction,
   and "(The case n = 1 is more elementary.)").
3. **E-HAT-4.2-15** — the whole bracket at AT 19371–19377 is dropped, including the Poincaré-duality
   route, Corollary A.12, and the remark that the homeomorphism statement is the Poincaré conjecture.
4. **"iff" halved to "if"** in three places: **E-HAT-3.F-9(a)** (AT 16022 "… is divisible iff A is
   torsionfree"), **E-HAT-4.1-19** (AT 17896 "X ≃w Y iff X and Y have a common CW approximation"),
   **E-HAT-4.1-22** (AT 17907–17909 "… countably many cells iff πn (X) is countable for all n").
   In each the card states only one implication.
5. **E-HAT-4.A-2** — the final sentence of AT 21100–21101 is dropped: "In particular, if π is abelian
   then [X, K(π , 1)] = hX, K(π , 1)i = Hom(π1 (X), π ) ."
6. **E-HAT-4.I-2** — the closing sentence of AT 23281–23282 is dropped ("Thus to determine stable
   splittings of K(Zn , 1) it suffices to do the case that n is a prime power …"), which is the point
   of the exercise.
7. **E-HAT-4.2-5** — the definition of the mapping torus (AT 19331–19332, "the quotient space of
   (Sα2 ∨ Sβ2 )× I under the identifications (x, 0) ∼ (f (x), 1)") is dropped.
8. **E-HAT-4.D-6** — AT 22168–22169 "[When n > 1 there are examples where M is not homeomorphic to
   CPn .]" is the remark that makes the converse meaningful; dropped.

**B. Dropped bracketed hints, pointers and printed parentheticals (29 cards).** Each is book text
that the task requires to be preserved: 3.F-9 (the six-term sequence is printed as a *diagram*, AT
16014–16021, and the card prints an unwitnessed formula instead); 4.1-15(c) (AT 17886 "(Use Gaussian
elimination, for example.)"); 4.1-22 (AT 17908–17909); 4.2-12, 4.2-13, 4.2-14, 4.2-18, 4.2-22,
4.2-23, 4.2-24, 4.2-27, 4.2-32; 4.3-5, 4.3-9, 4.3-13, 4.3-14, 4.3-23; 4.A-4 (AT 21113); 4.B-2 (AT
21223); 4.D-5 (AT 22164), 4.D-9 (AT 22181–22182), 4.D-10 (AT 22184–22186); 4.F-2 (AT 22610–22611);
4.G-3 (AT 22821), 4.G-4 (AT 22823); 4.H-1 (AT 23112–23113), 4.H-3 (AT 23118–23119); 4.I-1 (AT
23274–23276), 4.I-3 (AT 23287–23288); 4.K-2 (AT 24099–24100); 4.L-3 (AT 25809–25810), 4.L-4 (AT
25811–25813).

**C. Smaller divergences.** 4.H-2 drops "as at the right" and writes `B\cup_f X` where the extraction
(consistent throughout, 279 occurrences) prints "B ⊔f X"; 4.1-13 adds an editorial gloss "(homotopy
extension property for CW pairs)" that is not book text; 3.F-1 "gluing"/"glueing", 3.K-4
"non-path-connected"/"non-pathconnected", 4.A-5 "2-dimensional"/"2 dimensional" are orthographic only.

**D. Proof defects (of the 37 proofs read).**

1. **E-HAT-3.H-5 — gap.** The asserted split injectivity of H̃^0(X̃−T_i) → H̃^0(X̃−T_{i+1}) is not
   justified and, under the canonical identification H^1(X̃,X̃−T_i) ≅ H̃^0(X̃−T_i), that map is
   "constant on descendants", which does not preserve the sum-zero condition, so it is not even a map
   of H̃^0. The conclusion (Z for g = 1, countable free for g > 1, AT 16847–16848) is true; the
   argument for countable rank is missing.
2. **E-HAT-3.D-3 — gap.** "The cellular complex of SO(5) is C^2⊗C^4" is asserted without proof and is
   then fed to Künneth. AT 15085–15089 states only that SO(n) has the same homology *groups* as
   V3,2 × V5,2 and that its cup product structure differs, so the substitution of the product's
   complex is unsupported. The resulting groups are in fact right (checked against AT 15080–15091),
   and the mod-2 exterior-algebra input is right, but `bd` generating H_10 is also asserted.
3. **E-HAT-4.G-4 — gap in rigour.** "The homotopy gluing lemma therefore proves by cellular induction
   that p is a homotopy equivalence" — the induction is never carried out.
4. **Outline-only (no error found, but terseness noted):** 4.K-5 (five-lemma comparisons invoked, and
   editorial residue "the corrected current hypothesis" in 4.K.3(b)), 4.K-6 (collar gluing invoked),
   3.D-1 (orientation transport presupposes path-independence before supplying it), 4.K-2
   (deformation retraction of U_ρ sketched).

Everything else read — 3.F-1, 3.F-2, 3.F-3, 3.H-1, 3.H-2, 3.H-3, 3.H-4, 3.H-6, 4.A-1, 4.A-2,
4.A-3, 4.B-1, 4.B-2, 4.F-1, 4.F-2, 4.F-3, 4.G-1, 4.G-2, 4.G-3, 4.H-1, 4.H-2, 4.H-3, 4.H-4, 4.I-1,
4.I-2, 4.I-3, 4.K-1, 4.K-3, 4.K-4, 4.L-1, 4.L-2, 4.L-3 — **proof correct**.

## Process observation

Every one of the 137 unread cards already carries `source-checked`, `solution-written` and
`solution-reviewed` events in its frontmatter, all authored `gpt-5.6-sol` (2026-09-09). For at least
41 cards the `source-checked` claim ("the stored statement matches") is false. The frontmatter audit
trail therefore cannot be used as evidence that a card has been read.
