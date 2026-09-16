---
schema: qual/card@1
id: E-HAT-2.1-3
kind: problem
title: $\Delta$-complex structure on $\mathbb{RP}^n$ from $S^n$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Projective Spaces
  - Simplicial Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the boundary of the cross-polytope with vertices plus/minus coordinate vectors and descended its antipodal simplicial action.
---

::: {.problem}
Construct a $\Delta$-complex structure on $\mathbb{RP}^n$ as a quotient of a $\Delta$-complex structure on $S^n$ having vertices the two vectors of length 1 along each coordinate axis in $\mathbb{R}^{n+1}$.
:::

::: {.solution}
Let
\[
e_0,\dots,e_n
\]
be the standard basis of $\mathbb R^{n+1}$ and let
\[
C=\operatorname{conv}\{\pm e_0,\dots,\pm e_n\}
\]
be the $(n+1)$-dimensional cross-polytope.

<1>1. The boundary $\partial C$ is a simplicial complex with precisely the desired $2(n+1)$ vertices.
::: {.proof}
A facet of $C$ is obtained by choosing one vertex from each antipodal pair:
\[
[\varepsilon_0e_0,\dots,\varepsilon_ne_n],
\qquad
\varepsilon_i\in\{\pm1\}.
\]
All lower-dimensional faces are their faces.
Hence $\partial C$ is a simplicial $n$-sphere whose vertices are exactly the unit vectors in the positive and negative coordinate directions.
:::

<1>2. Radial projection gives a homeomorphism
\[
\partial C\cong S^n.
\]
::: {.proof}
The origin lies in the interior of the convex polytope $C$.
Every ray from the origin meets $\partial C$ in exactly one point.
Thus
\[
x\longmapsto \frac{x}{\|x\|}
\]
is a continuous bijection from compact $\partial C$ to Hausdorff $S^n$, hence a homeomorphism.
:::

<1>3. The antipodal map acts simplicially on this triangulation and has no fixed simplex.
::: {.proof}
It sends every vertex $e_i$ to $-e_i$ and every facet
\[
[\varepsilon_0e_0,\dots,\varepsilon_ne_n]
\]
to the opposite facet
\[
[-\varepsilon_0e_0,\dots,-\varepsilon_ne_n].
\]
No simplex contains both $e_i$ and $-e_i$, so no simplex is carried to itself pointwise or setwise by the antipodal map.
:::

<1>4. The quotient simplices give a $\Delta$-complex structure on
\[
S^n/(x\sim-x)=\mathbb{RP}^n.
\]
::: {.proof}
Pair each simplex of $\partial C$ with its antipodal simplex.
Since the antipodal action is simplicial and free, the quotient characteristic maps remain injective on simplex interiors and their face identifications are affine.
These are precisely the axioms of a $\Delta$-complex.
:::

<1>5. The vertices of the quotient are the $n+1$ antipodal pairs
\[
\{e_i,-e_i\},
\qquad 0\le i\le n.
\]
::: {.proof}
This is immediate from the quotient construction in <1>4.
Thus the required $\Delta$-complex on $\mathbb{RP}^n$ is obtained from the stated $S^n$ triangulation.
:::
:::
