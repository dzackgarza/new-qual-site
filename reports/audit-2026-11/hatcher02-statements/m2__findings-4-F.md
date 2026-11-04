# findings-4-F — SRC-TEXT-HAT02 §4.F (Spectra and Homology Theories)

Cards in section: **3** (E-HAT-4.F-1 … 3). Book exercise block: AT.txt **line 22600**
("Exercises"), statements at **22601–22615**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.F-1 | **statement matches** (AT 22601–22603). | unread |
| E-HAT-4.F-2 | **statement differs** — bracketed hint dropped (defect 1). | unread |
| E-HAT-4.F-3 | **statement matches** (AT 22612–22615); the book's lim→ with mapping telescopes is rendered `\operatorname{hocolim}`, same content. | unread |

## Defects

1. **E-HAT-4.F-2: bracketed hint dropped.** Book, AT **22610–22611**: "… these maps eventually become
   isomorphisms. [Use induction on the number of cells of X and the five-lemma.]" The card ends at
   "isomorphisms." The hint is the whole proof strategy; without it the statement is a different
   (harder) problem.

## Census
3 cards; 1 differs. All 3 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.F-1 — proof correct.** Direct limit ⇒ wedge: finite subcomplexes of a wedge are
  contained in finite sub-wedges, where the finite wedge axiom holds, and the filtered colimit of the
  finite-wedge decompositions is the direct sum. Converse for countable X: the telescope T ≃ X, the
  even/odd cover with Mayer–Vietoris and the wedge axiom gives ⊕ →^{1−s_*} ⊕ → h̃_n(T) → …, and
  1 − s_* on a direct sum is injective by inspecting the *first* nonzero coordinate (so coker = colim).
  This is exactly the exercise's content.
- **E-HAT-4.F-2 — proof correct**, and it is the book's own prescribed route (AT 22610–22611: "[Use
  induction on the number of cells of X and the five-lemma.]"). Base case is Freudenthal with
  connectivity of Σ^rY growing in r; the step uses the Puppe sequences of S^{q−1} → A → X → S^q and
  the five lemma, and ⟨Σ^rX, Σ^rY⟩ is a group for r large enough.
- **E-HAT-4.F-3 — proof correct.** π_j(hocolim) = colim π_j for a telescope (compactness of S^j,
  finite telescopes deformation retract on their last stage), and π_j(ΩZ_n) = π_{j+1}(Z_n), so both
  sides are colim_n π_{j+1}(Z_n) and κ_* is the identity on it.
