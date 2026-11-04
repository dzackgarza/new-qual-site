# findings-4-K — SRC-TEXT-HAT02 §4.K (The Dold–Thom Theorem)

Cards in section: **6** (E-HAT-4.K-1 … 6). Book exercise block: AT.txt **line 24094**
("Exercises"), statements at **24095–24121**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.K-1 | **statement matches** (AT 24095–24096). | unread |
| E-HAT-4.K-2 | **statement differs** — bracketed hint dropped (defect 1). | unread |
| E-HAT-4.K-3 | **statement matches** (AT 24102). | unread |
| E-HAT-4.K-4 | **statement matches** (AT 24104–24105). | unread |
| E-HAT-4.K-5 | **statement matches** (AT 24109–24118); the book's "non-pathconnected" is hyphenated in the card. | unread |
| E-HAT-4.K-6 | **statement matches** (AT 24119–24121). | unread |

## Defects

1. **E-HAT-4.K-2: bracketed hint dropped.** Book, AT **24099–24100**: "[Consider the cover of L by
   open stars of simplices and the cover of K by the preimages of these open stars.]" The hint is the
   only indication that a cover-based (nerve/Proposition 4G.2) argument is intended. Note the card also
   reproduces the book's own typo "contractible" correctly spelled; AT 24099 prints "contractible" with
   a line break, no issue.

## Census
6 cards; 1 differs. All 6 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.K-1 — proof correct.** Hypotheses as stated for Corollary 4K.2, restricted to
  subcomplexes; each f_J is a weak equivalence between CW complexes, hence (Whitehead) a homotopy
  equivalence; 4G.1 on the intersection diagrams plus the subcomplex-cover form of 4G.2 (Section 4.G
  exercise 4) give that f is a homotopy equivalence.
- **E-HAT-4.K-2 — proof correct.** Over the open-star covers, V_ρ (ρ spanned by the vertices) is
  contractible and U_ρ = f^{-1}(V_ρ) deformation retracts onto the contractible f^{-1}(x_ρ) — the
  barycentric-coordinate scaling is a legitimate retraction — so f: U_ρ → V_ρ is a weak equivalence
  and 4K.2 applies; simplicial complexes have CW type, so Whitehead upgrades to homotopy equivalence.
  The retraction is sketched rather than written out, but the construction given is the standard one.
- **E-HAT-4.K-3 — proof correct.** Monotone coordinates give a continuous bijection from the closed
  simplex-like region Q (compact) to SP_n(I) (Hausdorff), hence a homeomorphism, and
  (x) ↦ (y_0,…,y_n) = (x_1, x_2−x_1, …, 1−x_n) is an affine isomorphism onto Δ^n.
- **E-HAT-4.K-4 — proof correct.** Unoriented chords of S^1 ↔ (θ,s) with (θ,s) ~ (θ+π,−s), which is
  the Möbius band; |s| = 1 is the diagonal. The comparison with Example 4K.5 (n = 1: the unreduced
  suspension of RP^0 is an interval, and the mapping cone is the Möbius band) is consistent.
- **E-HAT-4.K-5 — proof correct in outline.** (i) ⇔ (ii) by comparing the exact sequences of
  (E,p^{-1}(b)) and (E_p,F_b); (iii) is the componentwise form. The extension of Lemma 4K.3 to
  non-path-connected bases is argued componentwise, with compactness handling (b). The five-lemma
  comparisons are invoked rather than written out, and the phrase "the corrected current hypothesis
  that every compact subset of B is contained in some B_n" is editorial residue in the statement of
  4K.3(b), but the mathematics is right.
- **E-HAT-4.K-6 — proof correct in outline.** Over a simplex p^{-1}(σ) is an iterated mapping
  cylinder, which collapses to X_{v_q}; fibers map to X_{v_q} by composites of edge maps, which are
  weak equivalences, so 4K.3(c) gives the quasifibration over each simplex and each face; the gluing
  over a finite subcomplex uses 4K.3(a) with collars; the passage to Γ uses 4K.3(b) and compactness.
