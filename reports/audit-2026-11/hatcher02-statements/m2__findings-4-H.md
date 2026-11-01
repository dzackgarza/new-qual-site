# findings-4-H — SRC-TEXT-HAT02 §4.H (Eckmann–Hilton Duality)

Cards in section: **4** (E-HAT-4.H-1 … 4). Book exercise block: AT.txt **line 23110**
("Exercises"), statements at **23111–23121**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.H-1 | **statement differs** — bracketed hint dropped (defect 1). | unread |
| E-HAT-4.H-2 | **statement differs** — the words "as at the right" are dropped, and the pushout diagram itself is not in AT.txt; the card also writes $B\cup_f X$ where AT 23114–23116 prints "B ⊔f X" (defects 2, 3). | unread |
| E-HAT-4.H-3 | **statement differs** — bracketed remark dropped (defect 4). | unread |
| E-HAT-4.H-4 | **statement matches** (AT 23120–23121). | unread |

## Defects (most serious first)

1. **E-HAT-4.H-1: bracketed hint dropped.** Book, AT **23112–23113**: "… the map Y X →Y A obtained by
   restriction of functions is a fibration. [If A ֓ X is a cofibration, so is A× Y ֓ X × Y for any
   space Y .]" The hint is the key step (it transports the cofibration to the product).
2. **E-HAT-4.H-2: reference to the printed diagram dropped.** Book, AT **23114–23115**: "Consider a
   pushout diagram as at the right, where B ⊔f X is B with X attached along A via f ." The diagram is a
   figure; the extraction (AT 23114–23116) carries none of it, so the card's paraphrase is unwitnessed
   as to the actual square printed. The card also silently drops "as at the right".
3. **E-HAT-4.H-2: symbol changed.** AT **23114–23116** prints "B ⊔f X" (the extraction's glyph for the
   pushout/attaching notation, consistent throughout AT.txt — 279 occurrences); the card prints
   `$B\cup_f X$`. Hatcher's attaching notation is ∪_f, and the extraction's ⊔ is an artefact of the
   OCR, but the card and the witness in this repository disagree on the symbol.
4. **E-HAT-4.H-3: bracketed remark dropped.** AT **23118–23119**: "[This is dual to Proposition 0.19.]"

## Census
4 cards; 3 differ. All 4 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.H-1 — proof correct.** Adjointing the data (f_0, g) of the lifting problem gives
  F_0: Z×X → Y and G: Z×I×A → Y; the hint's content ("if A ↪ X is a cofibration, so is
  A×Y ↪ X×Y") is exactly what makes Z×A ↪ Z×X a cofibration, so the partially defined map on
  (Z×X×{0}) ∪ (Z×A×I) extends; adjoint back. Note the card proves the hint instead of just citing it.
- **E-HAT-4.H-2 — proof correct.** Given (u, H) on B, put u_X = uq and h_A = H(f×id); HEP for
  A ↪ X extends to H_X, and the pushout universal property (P×I is the pushout of B×I and X×I over
  A×I) gives H̃ agreeing on the overlap because H(f(a),t) = H_X(i(a),t). Hence B ↪ B ⊔_f X is a
  cofibration.
- **E-HAT-4.H-3 — proof correct.** Adjust the ordinary inverse g to a fiber-preserving g' by lifting
  p_2fg ≃ p_2; the lemma (fiber-preserving u ≃ id over a fibration has a left homotopy inverse over B)
  is proved by lifting the base homotopy and a two-parameter square, and then ℓ = ag satisfies
  ℓf ≃_B id, and applying the same construction to ℓ gives m with mℓ ≃_B id, whence
  fℓ ≃_B mℓ ≃_B id. Both fiber homotopies are produced, so f is a fiber homotopy equivalence.
- **E-HAT-4.H-4 — proof correct.** The dual of M(f_1,…,f_n) is defined as tuples (φ_σ) with
  φ_σ: σ → X_{max σ} subject to φ_σ|_τ = f_{max σ,max τ} ∘ φ_τ; the conditions are closed and
  consistent, n = 1 gives the mapping path space E_{f_1}, and the passage to ∇X for a complex of
  spaces over Δ-complex Γ reverses the maps. As a definition-exercise the answer is coherent and the
  n = 1 check pins the variance.
