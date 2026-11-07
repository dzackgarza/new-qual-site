---
schema: qual/card@1
id: E-HAT-2.2-21
kind: problem
title: Euler characteristic of union of subcomplexes
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 21; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the inclusion-exclusion: every cell of $X=A\cup B$ lies in $A$ or in $B$ and in both
    exactly when it is a cell of $A\cap B$, so the cell counts satisfy inclusion-exclusion
    degreewise and the alternating sum is linear; the remark's Mayer-Vietoris version for open
    covers with bounded finite-rank homology is correct, the alternating sum of dimensions in a
    bounded exact sequence being zero.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 21 as printed on p. 157. The inclusion-exclusion over cells is
    correct; it now cites p. 7 for subcomplexes and p. 146 for the definition of chi, and states
    that the cells of X are partitioned into those of A only, of B only, and of A cap B.
    What is not covered: the added remark on the open-cover Mayer-Vietoris version is a
    variation and is not part of the exercise; it is left as stated.
---

::: {.problem}
If a finite CW complex $X$ is the union of subcomplexes $A$ and $B$, show that $\chi(X) = \chi(A) + \chi(B) - \chi(A \cap B)$.
:::

::: {.solution}
Because $A$ and $B$ are subcomplexes of $X$, every open cell of $X=A\cup B$ lies in $A$ or in $B$, and it lies in both exactly when it is a cell of $A\cap B$. Here a subcomplex is a closed union of cells (p. 7), $A\cap B$ is again one, and the cells of a cell complex are disjoint (p. 5), so the cells of $X$ are partitioned into those of $A$ only, of $B$ only, and of $A\cap B$.

Let $c_i(Z)$ denote the number of $i$-cells of a finite CW complex $Z$. For each $i$, ordinary inclusion--exclusion for the finite sets of $i$-cells gives
$$
c_i(X)=c_i(A)+c_i(B)-c_i(A\cap B).
$$
Taking alternating sums, using the definition of $\chi$ for a finite CW complex as the alternating sum of the numbers of its cells (p. 146),
$$
\begin{aligned}
\chi(X)
&=\sum_i(-1)^i c_i(X)\\
&=\sum_i(-1)^i c_i(A)
 +\sum_i(-1)^i c_i(B)
 -\sum_i(-1)^i c_i(A\cap B)\\
&=\boxed{\chi(A)+\chi(B)-\chi(A\cap B)}.
\end{aligned}
$$
The sums are finite because the three complexes have finitely many cells.
:::

::: {.remark title="Variation"}
If $Z=U\cup V$ with $U,V$ open, the same formula
holds when the rational homology of
$Z,U,V,U\cap V$ has finite rank and vanishes
outside a bounded range. The Mayer--Vietoris
sequence is then a bounded long exact sequence
of finite-dimensional $\QQ$-vector spaces.
Its alternating sum of dimensions is zero,
which rearranges to
$$
\chi(Z)=\chi(U)+\chi(V)-\chi(U\cap V).
$$The inclusion--exclusion count agrees with Sam's §2.2 Exercise 21, printed p. 12. The cells in the union are those counted only by $c_i(A)$, only by $c_i(B)$, or those of $A\cap B$, since subcomplexes are closed unions of cells which are pairwise disjoint (Hatcher pp. 5, 7).


:::
