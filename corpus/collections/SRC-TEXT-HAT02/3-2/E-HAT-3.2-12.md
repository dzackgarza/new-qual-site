---
schema: qual/card@1
id: E-HAT-3.2-12
kind: problem
title: "Spaces with isomorphic cohomology but different homotopy type"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that the spaces $(S^1 \times \mathbb{CP}^\infty) / (S^1 \times \{x_0\})$ and $S^3 \times \mathbb{CP}^\infty$ have isomorphic cohomology rings with $\mathbb{Z}$ or any other coefficients.
[An exercise for §4.L is to show these two spaces are not homotopy equivalent.]
:::

::: {.solution}
Let $Y=\mathbb{CP}^\infty$ with basepoint $y_0$, and set
\[
Q=(S^1\times Y)/(S^1\times\{y_0\}).
\]
Reduced cohomology of $Q$ is relative cohomology:
\[
\widetilde H^*(Q;R)\cong H^*(S^1\times Y,S^1\times\{y_0\};R)
\]
for any coefficient ring $R$.

Write $u\in H^2(Y;R)$ for the standard generator and $s\in H^1(S^1;R)$. The relative Künneth theorem gives
\[
H^*(S^1\times Y,S^1\times\{y_0\};R)
\cong H^*(S^1;R)\otimes\widetilde H^*(Y;R).
\]
Thus, additively, the positive-degree classes are
\[
u^k\quad(k\ge1),\qquad s u^k\quad(k\ge1).
\]
The relative cross product is compatible with cup products, so
\[
u^i u^j=u^{i+j},\qquad
(su^i)u^j=su^{i+j},\qquad
(su^i)(su^j)=0
\]
because $s^2=0$. If
\[
v=su\in H^3(Q;R),
\]
then every odd class is $vu^{k-1}$ and $v^2=0$. Hence
\[
H^*(Q;R)\cong R[u,v]/(v^2),\qquad |u|=2,\ |v|=3.
\]

On the other hand
\[
H^*(S^3\times\mathbb{CP}^\infty;R)
\cong H^*(S^3;R)\otimes_R R[u]
\cong R[u,v]/(v^2),
\]
with the same degrees. Therefore the two spaces have isomorphic cohomology rings with $\mathbb Z$ coefficients and, by the same calculation, with arbitrary coefficients.
:::
