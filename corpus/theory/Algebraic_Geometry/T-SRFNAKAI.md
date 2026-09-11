---
schema: qual/card@1
id: T-SRFNAKAI
kind: theorem
title: The Nakai--Moishezon criterion on a surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ample Divisors
  - Intersection Theory
  - Surfaces
relations:
- kind: uses
  target: D-SRFINT
review: draft
prompts:
- When is a divisor on a surface ample?
- State the Nakai--Moishezon criterion.
---

::: {.theorem}
A divisor $D$ on a smooth projective surface $X$ is ample if and only if
\[
D^2 > 0 \quad\text{and}\quad D \cdot C > 0 \text{ for every irreducible curve } C \subseteq X .
\]
:::

::: {.remark}
This is the surface analogue of "ample means positive degree" on a curve, and the two conditions are exactly the two dimensions of subvariety: positivity against every curve, and positivity against the surface itself.

Both are needed.
On the blowup of $\PP^2$ at a point, $D = \pi^*H$ has $D^2 = 1 > 0$ but $D \cdot E = 0$ on the exceptional curve, so it is not ample — it is only the pullback of an ample class, and it contracts $E$.
Conversely a class can meet every curve positively on a surface while failing $D^2 > 0$, which is why the first condition is not implied by the second.

The criterion is purely numerical, so ampleness on a surface depends only on the class in $\NS(X)$.
That is what lets one draw the ample cone inside $\NS(X) \otimes \RR$ and use the Hodge index theorem to describe it.
:::
