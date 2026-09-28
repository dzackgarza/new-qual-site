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
---

::: {.problem}
If a finite CW complex $X$ is the union of subcomplexes $A$ and $B$, show that $\chi(X) = \chi(A) + \chi(B) - \chi(A \cap B)$.
:::

::: {.solution}
Because $A$ and $B$ are subcomplexes of $X$, every open cell of $X=A\cup B$ lies in $A$ or in $B$, and it lies in both exactly when it is a cell of $A\cap B$.

Let $c_i(Z)$ denote the number of $i$-cells of a finite CW complex $Z$. For each $i$, ordinary inclusion--exclusion for the finite sets of $i$-cells gives
\[
c_i(X)=c_i(A)+c_i(B)-c_i(A\cap B).
\]
Taking alternating sums,
\[
\begin{aligned}
\chi(X)
&=\sum_i(-1)^i c_i(X)\\
&=\sum_i(-1)^i c_i(A)
 +\sum_i(-1)^i c_i(B)
 -\sum_i(-1)^i c_i(A\cap B)\\
&=\boxed{\chi(A)+\chi(B)-\chi(A\cap B)}.
\end{aligned}
\]
:::
