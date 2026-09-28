---
schema: qual/card@1
id: T-SRFADJ
kind: theorem
title: The adjunction formula on a surface
slogan: 'Adjunction turns genus into intersection theory: $2g(C)-2=C\cdot(C+K_X)$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Adjunction
  - Intersection Theory
  - Canonical Divisor
relations:
- kind: uses
  target: D-SRFINT
review: draft
prompts:
- State the adjunction formula.
- Derive the degree-genus formula for plane curves.
- What is the canonical divisor of $\PP^2$, and its self-intersection?
---

::: {.theorem}
Let $C$ be a smooth curve on a smooth projective surface $X$.
Then
\[
\omega_C = (\omega_X \otimes \OO_X(C))\vert_C , \qquad 2g(C) - 2 = C \cdot (C + K_X) .
\]
The same numerical formula computes the arithmetic genus of any curve on $X$.
:::

::: {.remark}
Adjunction converts genus calculations on surfaces into intersection-number calculations.

On $\PP^2$ it gives the degree-genus formula.
On $\PP^2$ one has $K = -3H$ and $H^2 = 1$, so $K^2 = 9$; for $C$ of degree $d$,
\[
2g-2 = C \cdot (C - 3H) = d^2 - 3d ,
\]
giving $g = \tfrac{1}{2}(d-1)(d-2)$.
On $\PP^1 \times \PP^1$, $K = (-2,-2)$ and the same computation gives $g = (a-1)(b-1)$ for a curve of type $(a,b)$.

In any dimension, for a smooth divisor $D$ on a smooth $X$, the sheaf-level form is $K_D = (K_X + D)\vert_D$.
:::
