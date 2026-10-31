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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the chain groups and both boundary maps: the alternating sum gives $\partial_2\sigma=a-b+c$, so $H_2=0$, $H_1=\ZZ^2$ and $H_0=\ZZ$, matching the homotopy type of a wedge of two circles.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    The homology is certified in proofs/cards/DeltaComplexHomology.sage: the boundary matrices
    are fed to Sage's ChainComplex (which checks d^2 = 0) and the group read off homology(0..2)
    is (Z, Z^2, 0), as the card states. Identifying that complex with the space is the geometric
    step and rests on the book's description.

    Rerun on the supported Sage development image: Sage 11.0.beta5, Python 3.14.10, source
    HEAD b0cd7d86e2, all checks passing there.
---

::: {.problem}
Compute the simplicial homology groups of the triangular parachute obtained from $\Delta^2$ by identifying its three vertices to a single point.
:::

::: {.solution}
Let $v$ be the common image of the three vertices.
Let
$$
a=[v_0,v_1],
\qquad
b=[v_0,v_2],
\qquad
c=[v_1,v_2]
$$
denote the three distinct $1$-simplices, and let
$$
\sigma=[v_0,v_1,v_2]
$$
be the unique $2$-simplex.

::: pf

::: pf-step

The simplicial chain groups are
$$
C_2\cong\ZZ,
\qquad
C_1\cong\ZZ^3,
\qquad
C_0\cong\ZZ.
$$

::: pf-proof

There is one $2$-simplex, three $1$-simplices, and one vertex in the quotient $\Delta$-complex.

:::

:::

::: pf-step

The first boundary map is zero:
$$
\partial_1=0.
$$

::: pf-proof

Every edge begins and ends at the same quotient vertex $v$, so
$$
\partial_1(a)=\partial_1(b)=\partial_1(c)=v-v=0.
$$

:::

:::

::: pf-step

The second boundary map is
$$
\partial_2(\sigma)=a-b+c.
$$

::: pf-proof

The simplicial boundary formula gives
$$
\partial[v_0,v_1,v_2]
=[v_1,v_2]-[v_0,v_2]+[v_0,v_1]
=c-b+a.
$$

:::

:::

::: pf-step

The map $\partial_2:\ZZ\to\ZZ^3$ is injective and its image is a primitive rank-one subgroup.

::: pf-proof

The vector of coefficients is
$$
(1,-1,1),
$$
which is nonzero and whose coordinates have greatest common divisor $1$.
Thus the map is injective and the quotient by its image is torsion-free of rank two.

:::

:::

::: pf-step

Therefore
$$
\boxed{H_0\cong\ZZ,\qquad H_1\cong\ZZ^2,\qquad H_k=0\ (k\ge2).}
$$

::: pf-proof

Since $\partial_1=0$,
$$
H_0=C_0\cong\ZZ.
$$
Also
$$
H_1=\ker\partial_1/\operatorname{im}\partial_2
\cong
\ZZ^3/\langle(1,-1,1)\rangle
\cong\ZZ^2.
$$
Injectivity of $\partial_2$ gives $H_2=0$, and there are no higher simplices.

:::

:::

:::

:::
