---
schema: qual/card@1
id: E-HAT-2.1-4
kind: problem
title: Simplicial homology of triangular parachute
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Wrote the simplicial chain complex with one vertex, three edges, and one 2-simplex; the single primitive boundary relation leaves H1 of rank two.
---

::: {.problem}
Compute the simplicial homology groups of the triangular parachute obtained from $\Delta^2$ by identifying its three vertices to a single point.
:::

::: {.solution}
Let $v$ be the common image of the three vertices.
Let
\[
a=[v_0,v_1],
\qquad
b=[v_0,v_2],
\qquad
c=[v_1,v_2]
\]
denote the three distinct $1$-simplices, and let
\[
\sigma=[v_0,v_1,v_2]
\]
be the unique $2$-simplex.

<1>1. The simplicial chain groups are
\[
C_2\cong\mathbb Z,
\qquad
C_1\cong\mathbb Z^3,
\qquad
C_0\cong\mathbb Z.
\]
::: {.proof}
There is one $2$-simplex, three $1$-simplices, and one vertex in the quotient $\Delta$-complex.
:::

<1>2. The first boundary map is zero:
\[
\partial_1=0.
\]
::: {.proof}
Every edge begins and ends at the same quotient vertex $v$, so
\[
\partial_1(a)=\partial_1(b)=\partial_1(c)=v-v=0.
\]
:::

<1>3. The second boundary map is
\[
\partial_2(\sigma)=a-b+c.
\]
::: {.proof}
The simplicial boundary formula gives
\[
\partial[v_0,v_1,v_2]
=[v_1,v_2]-[v_0,v_2]+[v_0,v_1]
=c-b+a.
\]
:::

<1>4. The map $\partial_2:\mathbb Z\to\mathbb Z^3$ is injective and its image is a primitive rank-one subgroup.
::: {.proof}
The vector of coefficients is
\[
(1,-1,1),
\]
which is nonzero and whose coordinates have greatest common divisor $1$.
Thus the map is injective and the quotient by its image is torsion-free of rank two.
:::

<1>5. Therefore
\[
\boxed{H_0\cong\mathbb Z,\qquad H_1\cong\mathbb Z^2,\qquad H_k=0\ (k\ge2).}
\]
::: {.proof}
Since $\partial_1=0$,
\[
H_0=C_0\cong\mathbb Z.
\]
Also
\[
H_1=\ker\partial_1/\operatorname{im}\partial_2
\cong
\mathbb Z^3/\langle(1,-1,1)\rangle
\cong\mathbb Z^2.
\]
Injectivity of $\partial_2$ gives $H_2=0$, and there are no higher simplices.
:::
:::
