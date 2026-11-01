# findings-4-G — SRC-TEXT-HAT02 §4.G (Gluing Constructions)

Cards in section: **4** (E-HAT-4.G-1 … 4). Book exercise block: AT.txt **line 22813**
("Exercises"), statements at **22815–22823**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.G-1 | **statement matches** (AT 22815–22817). | unread |
| E-HAT-4.G-2 | **statement matches** (AT 22818–22819). | unread |
| E-HAT-4.G-3 | **statement differs** — bracketed cross-reference dropped (defect 2). | unread |
| E-HAT-4.G-4 | **statement differs** — bracketed remark dropped (defect 1). | unread |

## Defects

1. **E-HAT-4.G-4: bracketed remark dropped.** Book, AT **22823**: "[CW complexes are paracompact; see
   [VBKT].]" The card gives the exercise with no indication of why the CW case holds.
2. **E-HAT-4.G-3: bracketed cross-reference dropped.** AT **22821**: "[See Lemma 2C.2.]"

## Census
4 cards; 2 differ. All 4 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT

- **E-HAT-4.G-1 — proof correct.** Successive deformation retractions M_n ↘ T_n, compatible in n,
  assemble on the union because the union is the colimit of the cofibrations M_n → M_{n+1}; the time-1
  map lands in ∪T_n and the telescope is fixed throughout.
- **E-HAT-4.G-2 — proof correct.** With all attaching maps homeomorphisms and Γ connected, all X_v,
  X_e are homeomorphic to one fiber F; over the interior of an edge p is X_e × (0,1) → (0,1); over the
  open star of a vertex, x ↦ f_{e,v}(x) identifies each half-edge product with X_v × [0,1/2), and the
  gluing at t = 0 is the identity. Local triviality over a basis of Γ gives a fiber bundle.
- **E-HAT-4.G-3 — proof correct.** st°(v_0) ∩ … ∩ st°(v_q) ≠ ∅ iff v_0,…,v_q span a simplex (a
  point of the interior of τ lies in st°(v) iff v is a vertex of τ), so the nerve is isomorphic to K.
  This is the answer Lemma 2C.2 is meant to suggest.
- **E-HAT-4.G-4 — proof correct in outline; one step asserted.** The diagram-of-intersections
  construction and the two reductions (p: ΔX_U → X a homotopy equivalence; then 4G.1 applied to the
  diagram of points) are the right ones and are what the exercise asks for. But "The homotopy gluing
  lemma therefore proves by cellular induction that p is a homotopy equivalence" is stated, not
  carried out: the card never verifies the induction (contractibility of the simplex of subcomplexes
  containing a given cell, compatibility on boundaries). The conclusion is true; the write-up leaves
  the induction to the reader.
