---
schema: qual/card@1
id: E-HAT-2.2-39
kind: exercise
title: Relative Mayer–Vietoris sequences for CW pairs from algebraic lemma
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - CW Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Use the preceding exercise to derive relative Mayer–Vietoris sequences for CW pairs $(X, Y) = (A \cup B, C \cup D)$ with $A = B$ or $C = D$.

::: {.solution}
<1>1. The preceding exercise (E-HAT-2.2-38) gives: from a commutative diagram with exact rows and every third vertical map an isomorphism, one obtains a long exact sequence $$\cdots \to E_{n+1} \to B_n \to C_n \oplus D_n \to E_n \to B_{n-1} \to \cdots.$$ Proof: the algebraic lemma.

<1>2. For a CW pair $(X, Y) = (A \cup B, C \cup D)$, the Mayer–Vietoris sequences for the pairs $(A, B)$ and $(C, D)$ fit into a commutative diagram with exact rows.
Proof: the Mayer–Vietoris sequence is natural, so the inclusion maps $C \hookrightarrow A$ and $D \hookrightarrow B$ induce a commutative diagram of the two Mayer–Vietoris sequences.

<1>3. Case $A = B$: then $X = A$ and $Y = C \cup D$, and the diagram has $H_n(A) = H_n(B)$ with the identity map (an isomorphism) on every third term.
Proof: when $A = B$, the two "halves" coincide, so the vertical maps on the $A$-terms are identities.

<1>4. Applying the algebraic lemma (<1>1) yields the relative Mayer–Vietoris sequence $$\cdots \to H_{n+1}(X, Y) \to H_n(A \cap B) \to H_n(A) \oplus H_n(B) \to H_n(X, Y) \to \cdots$$ (equivalently, the long exact sequence of the pair $(X, Y)$). Proof: <1>1 and <1>3.

<1>5. Case $C = D$: similarly, the vertical maps on the $C$-terms are identities, and the lemma yields the relative Mayer–Vietoris sequence for the pair.
Proof: the same argument with $C = D$.

<1>6. Q.E.D. Proof: <1>4 and <1>5.
:::
