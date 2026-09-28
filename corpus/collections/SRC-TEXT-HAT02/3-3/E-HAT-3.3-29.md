---
schema: qual/card@1
id: E-HAT-3.3-29
kind: problem
title: "Retractions of surfaces onto graphs"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 29; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Use the preceding problem to show that if the closed orientable surface $M_g$ of genus $g$ retracts onto a graph $X \subset M_g$, then $H_1(X)$ has rank at most $g$.
Deduce an alternative proof of Exercise 13 from this, and construct a retraction of $M_g$ onto a wedge sum of $k$ circles for each $k \leq g$.
:::

::: {.solution}
Suppose $r:M_g\to X$ is a retraction onto a graph $X\subset M_g$, with inclusion $i:X\hookrightarrow M_g$. Then
\[
r\circ i=\operatorname{id}_X,
\]
so on cohomology over a field $F$,
\[
i^*r^*=\operatorname{id}_{H^1(X;F)}.
\]
Hence
\[
r^*:H^1(X;F)\hookrightarrow H^1(M_g;F)
\]
is injective.

Since $X$ is a graph, $H^2(X;F)=0$, so for all $u,v\in H^1(X;F)$,
\[
r^*u\smile r^*v=r^*(u\smile v)=0.
\]
Thus the image $V=r^*H^1(X;F)$ is an isotropic subspace for the nonsingular skew-symmetric cup-product pairing on the $2g$-dimensional vector space $H^1(M_g;F)$. By Exercise 28,
\[
\dim_F V\le g.
\]
Taking $F=\mathbb Q$ gives
\[
\boxed{\operatorname{rank}H_1(X)\le g.}
\]

For Exercise 13, a genus-$h$ surface with one boundary component deformation retracts onto a wedge of $2h$ circles. If there were a retraction $M_g\to M_h'$, composing it with this spine retraction would give a retraction of $M_g$ onto a graph of first-homology rank $2h$. Hence $2h\le g$, so no such retraction exists when $h>g/2$.

Finally use the standard CW structure on $M_g$ with one vertex, loops
\[
a_1,b_1,\ldots,a_g,b_g,
\]
and one $2$-cell attached by $\prod_i[a_i,b_i]$. For any $k\le g$, let $X_k$ be the wedge of the loops $a_1,\ldots,a_k$. Define a cellular map $M_g\to X_k$ that is the identity on these loops and sends every other $1$-cell to the vertex. The attaching word maps to the trivial loop, since each commutator has at least one factor sent to the vertex, so the map extends over the $2$-cell. It restricts to the identity on $X_k$, hence is a retraction.
:::
