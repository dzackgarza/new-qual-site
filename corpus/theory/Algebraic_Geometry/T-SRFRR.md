---
schema: qual/card@1
id: T-SRFRR
kind: theorem
title: Riemann--Roch for surfaces
slogan: 'Surface Riemann--Roch turns Euler characteristic into intersection theory: $\chi(\OO_X(D))-\chi(\OO_X)=\tfrac12D\cdot(D-K_X)$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Surfaces
  - Intersection Theory
relations:
- kind: uses
  target: D-SRFINT
- kind: uses
  target: T-SRFADJ
review: draft
prompts:
- State Riemann--Roch for surfaces.
- What is Noether's formula?
- How do you show a divisor on a surface is effective?
---

::: {.theorem}
For a divisor $D$ on a smooth projective surface $X$,
\[
\chi(\OO_X(D)) = \chi(\OO_X) + \tfrac{1}{2} D \cdot (D - K_X) .
\]
:::

::: {.theorem title="Noether's formula"}
\[
\chi(\OO_X) = \tfrac{1}{12}\left( K_X^2 + c_2(X) \right) ,
\]
where $c_2(X)$ is the topological Euler characteristic over $\CC$.
:::

::: {.remark}
The surface formula parallels the curve formula, with $\deg D$ replaced by $\tfrac{1}{2}D\cdot(D-K)$ and $1-g$ replaced by $\chi(\OO_X)$; adjunction makes these substitutions consistent.

The typical use is not to compute $\chi$ but to force a section.
Serre duality gives $h^2(D) = h^0(K-D)$, so
\[
h^0(D) \geq \chi(\OO_X) + \tfrac{1}{2}D\cdot(D-K) ,
\]
and if in addition $h^0(K-D) = 0$ — for instance because $D \cdot H > K \cdot H$ for an ample $H$ — then $D^2$ large forces $D$ or $-D$ to be effective.
This inequality is a standard mechanism for proving that a divisor on a surface has sections and hence moves in a linear system.

Noether's formula is the constraint relating $K^2$ and the topology: on $\PP^2$, $K^2 = 9$ and $c_2 = 3$, and $\tfrac{1}{12}(9+3) = 1 = \chi(\OO)$.
:::
