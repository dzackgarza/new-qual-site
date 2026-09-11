---
schema: qual/card@1
id: D-TORQD
kind: definition
title: The polytope of a divisor, and its lattice points as sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Divisors
  - Polytopes
relations:
- kind: uses
  target: T-TORDIV
- kind: uses
  target: D-TORPOLY
review: draft
prompts:
- Given a torus-invariant divisor on a toric variety, what polytope does it determine?
- Compute the global sections of a line bundle on a toric variety.
---

::: {.definition}
For $D = \sum_{\rho} a_\rho D_\rho$ on $X_\Sigma$ put
\[
P_D = \ts{ m \in M_\RR \st \inp{m}{u_\rho} \geq -a_\rho \text{ for all } \rho \in \Sigma(1) } .
\]
:::

::: {.theorem title="Sections"}
\[
H^0\big( X_\Sigma, \OO(D) \big) = \bigoplus_{m \in P_D \intersect M} k \cdot \chi^m ,
\]
so $h^0(\OO(D))$ is a count of lattice points.
:::

::: {.remark}
The two constructions invert each other.
Starting from a polytope $P$ with facet presentation $\inp{m}{u_F} \geq -a_F$, the divisor $D_P = \sum_F a_F D_F$ on $X_P$ satisfies $P_{D_P} = P$.
Starting from a divisor, $P_D$ is the polytope whose normal fan is refined by $\Sigma$.

The case worth carrying is the anticanonical one.
Since $K_X = -\sum_\rho D_\rho$, the anticanonical divisor has $a_\rho = 1$ for every $\rho$ and
\[
P_{-K_X} = \ts{ m \in M_\RR \st \inp{m}{u_\rho} \geq -1 } ,
\]
which is exactly the polar dual of the convex hull of the ray generators.
For $X = X_P$ with $P$ reflexive this recovers $P_{-K_{X_P}} = P$.
:::
