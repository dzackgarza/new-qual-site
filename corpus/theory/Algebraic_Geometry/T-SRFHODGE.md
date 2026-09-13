---
schema: qual/card@1
id: T-SRFHODGE
kind: theorem
title: The Hodge index theorem
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hodge Index Theorem
  - Intersection Theory
  - Neron-Severi Group
relations:
- kind: uses
  target: D-SRFNS
review: draft
prompts:
- State the Hodge index theorem.
- What is the signature of the intersection form on a surface?
---

::: {.theorem}
Let $X$ be a smooth projective surface and $H$ an ample divisor.
If $D \cdot H = 0$ and $D \not\equiv 0$, then $D^2 < 0$.
Equivalently, the intersection form on $\NS(X) \otimes \RR$ has signature $(1, \rho - 1)$.
:::

::: {.remark}
One plus direction, everything else negative: the ample cone supplies the single positive direction, and the orthogonal complement of an ample class is negative definite.
That is the whole content, and it is why $\NS$ of a surface is a hyperbolic lattice.

The practical consequences are the ones asked about.
If $D^2 > 0$ then $D \cdot H \neq 0$ for every ample $H$, so $D$ or $-D$ is on the positive side — combined with Riemann--Roch this is how one proves a divisor with $D^2 > 0$ and $D \cdot H > 0$ is effective for large multiples.
And the inequality $(D \cdot E)^2 \geq D^2 E^2$ for $D$ with $D^2 > 0$ is a signature statement, the reverse Cauchy--Schwarz that holds in a hyperbolic lattice.

Over $\CC$ this is the Hodge--Riemann bilinear relation on $H^{1,1}$ specialised to the algebraic classes, which is where the name comes from.
:::
