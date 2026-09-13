---
schema: qual/card@1
id: E-PER08-8.1
kind: problem
title: Perutz Algebraic Topology I Exercise 8.1
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
Think of $S^2$ as a tetrahedron, i.e. a $\Delta$-complex with four $2$-simplices, six $1$-simplices and four $0$-simplices.
Show that for this structure
\[
H_0^{\mathrm{simp}}(S^2)=\mathbb Z,\qquad
H_1^{\mathrm{simp}}(S^2)=0,\qquad
H_2^{\mathrm{simp}}(S^2)=\mathbb Z,\qquad
H_{>2}^{\mathrm{simp}}(S^2)=0.
\]
:::

::: {.solution}
Let the tetrahedron have vertices $v_0,v_1,v_2,v_3$, oriented edges $e_{ij}=[v_i,v_j]$ for $i<j$, and oriented faces $F_{ijk}=[v_i,v_j,v_k]$ for $i<j<k$.
Then
\[
C_2\cong\mathbb Z^4,\qquad C_1\cong\mathbb Z^6,\qquad C_0\cong\mathbb Z^4,
\]
and there are no higher chains.

<1>1. $H_0\cong\mathbb Z$.
::: {.proof}
The $1$-skeleton is connected, so $\operatorname{coker}\partial_1\cong\mathbb Z$.
:::

<1>2. $H_2\cong\mathbb Z$.
::: {.proof}
The oriented sum of the four faces with boundary orientations,
\[
F_{123}-F_{023}+F_{013}-F_{012},
\]
has zero boundary.
Conversely, if $\sum a_{ijk}F_{ijk}$ has zero boundary, comparing the coefficient of each edge forces all four coefficients to be determined by one integer with exactly these signs.
Thus $\ker\partial_2\cong\mathbb Z$.
Since $C_3=0$, this is $H_2$.
:::

<1>3. $H_1=0$.
::: {.proof}
$\operatorname{rank}\partial_1=3$ because the connected graph has four vertices.
Hence $\operatorname{rank}\ker\partial_1=6-3=3$.
From <1>2, $\operatorname{rank}\partial_2=4-1=3$.
Each triangular $1$-cycle is visibly the boundary of its face, and such triangle cycles generate the cycle group of the complete graph on four vertices.
Thus $\ker\partial_1=\operatorname{im}\partial_2$.
:::

Therefore
\[
H_0^{\rm simp}(S^2)=\mathbb Z,\quad H_1^{\rm simp}(S^2)=0,\quad H_2^{\rm simp}(S^2)=\mathbb Z,
\]
and $H_i^{\rm simp}=0$ for $i>2$.
:::
