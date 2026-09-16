---
schema: qual/card@1
id: E-HAT-3.2-1
kind: problem
title: Cup product structure on closed orientable surfaces
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Assuming as known the cup product structure on the torus $S^1 \times S^1$, compute the cup product structure in $H^*(M_g)$ for $M_g$ the closed orientable surface of genus $g$ by using the quotient map from $M_g$ to a wedge sum of $g$ tori.
:::

::: {.solution}
Choose the standard symplectic basis
\[
a_1,b_1,\dots,a_g,b_g\in H^1(M_g;\mathbb Z)
\]
and let $u\in H^2(M_g;\mathbb Z)\cong\mathbb Z$ be the orientation class.

Let
\[
q:M_g\longrightarrow T_1\vee\cdots\vee T_g
\]
be the quotient map obtained by collapsing the separating circles between the $g$ handles. On $H^1$, $q^*$ identifies the two degree-one generators of $H^1(T_i)$ with $a_i,b_i$. If $u_i\in H^2(T_i)$ is the orientation class of the $i$th torus, then $q^*(u_i)=u$: restricting $q$ to the $i$th handle and collapsing its boundary has degree $1$ onto $T_i$.

On each torus, with the usual orientation,
\[
x_i\smile y_i=u_i,\qquad y_i\smile x_i=-u_i,
\qquad x_i^2=y_i^2=0.
\]
Products of classes supported on distinct wedge summands vanish. Naturality of the cup product therefore gives
\[
\boxed{a_i\smile b_j=\delta_{ij}u,\qquad
b_i\smile a_j=-\delta_{ij}u,}
\]
and
\[
\boxed{a_i\smile a_j=0,\qquad b_i\smile b_j=0}
\]
for all $i,j$. Since $H^k(M_g;\mathbb Z)=0$ for $k>2$, these relations, together with the unit in $H^0$, determine the whole ring.
:::
