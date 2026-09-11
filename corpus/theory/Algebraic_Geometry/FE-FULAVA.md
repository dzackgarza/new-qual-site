---
schema: qual/card@1
id: FE-FULAVA
kind: example
title: An ample divisor that is not very ample
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Ample Divisors
  - Polytopes
relations:
- kind: uses
  target: PR-TORPOS
- kind: uses
  target: D-FULNORMPOLY
- kind: uses
  target: T-FULDEG
review: draft
prompts:
- Exhibit an ample divisor that is not very ample.
- Why is dimension three the smallest place such an example can live?
---

::: {.example title="The polytope"}
In $M_\RR = \RR^3$ take
\[
P = \operatorname{Conv}\big( (0,0,0),\ (0,1,1),\ (1,0,1),\ (1,1,0) \big) ,
\]
a lattice $3$-simplex, and let $D = D_P$ be the corresponding divisor on $X_P$.
Since $P$ is a full-dimensional simplex, its normal fan has four maximal cones matched with the four vertices, so $\varphi_D$ is strictly convex and $D$ is ample.
:::

::: {.example title="Why it is not very ample"}
The only lattice points of $P$ are its four vertices.
At the vertex $v = (0,0,0)$ the edge vectors are
\[
(0,1,1), \quad (1,0,1), \quad (1,1,0) ,
\]
and
\[
\det \begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix} = 2 ,
\]
so they generate a sublattice of index $2$ in $M = \ZZ^3$.
The semigroup $\ts{m - v \st m \in P \intersect M}$ is therefore not saturated, which is exactly the clause very ampleness requires, and $D$ fails it.
:::

::: {.remark title="What the map does"}
The four lattice points give a morphism $X_P \to \PP^3$, and
\[
\deg X_P = 3! \cdot \vol(P) = 3! \cdot \tfrac{1}{3} = 2 ,
\]
so the map is finite of degree $2$ rather than an embedding: $X_P$ is a double cover of $\PP^3$ branched over the four coordinate hyperplanes.
Doubling repairs it, since $2P$ is normal and hence very ample.

Three things make this the example to remember.
It must be three-dimensional, because ample and very ample agree on complete toric surfaces.
It must be singular, because they also agree on smooth complete toric varieties.
And the obstruction is a single determinant, which is the same index computation that detects a quotient singularity at the corresponding fixed point.
:::
