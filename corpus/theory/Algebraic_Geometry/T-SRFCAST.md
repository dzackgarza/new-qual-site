---
schema: qual/card@1
id: T-SRFCAST
kind: theorem
title: Castelnuovo's contractibility criterion
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Minimal Models
  - Surfaces
relations:
- kind: uses
  target: FE-SRFBLOW
review: draft
prompts:
- State Castelnuovo's contractibility criterion.
- What is a $(-1)$-curve?
- What is a minimal surface?
- What is the minimal model program for surfaces?
---

::: {.theorem}
Let $X$ be a smooth projective surface and $E \subseteq X$ a curve with $E \cong \PP^1$ and $E^2 = -1$, a **$(-1)$-curve** or exceptional curve of the first kind.
Then there is a smooth projective surface $Y$ and a morphism $\pi \colon X \to Y$ realising $X$ as the blowup of $Y$ at a point, with $E$ the exceptional curve.
:::

::: {.remark}
This converts a numerical condition into a birational morphism, and it is what makes the minimal model program work in dimension two: contract $(-1)$-curves until none remain, and the result is a **minimal** surface.
Since each contraction raises $K^2$ by one and $\rho$ drops by one, the process terminates.

By adjunction, $E \cong \PP^1$ with $E^2 = -1$ is equivalent to $E^2 = -1$ and $K \cdot E = -1$, which is the form the criterion is usually applied in.

The natural follow-up is whether a surface has finitely many $(-1)$-curves, and the answer is no: $\Bl_n \PP^2$ for $n \geq 9$ has infinitely many.
The minimal model is then not unique in general — for rational surfaces one can reach both $\PP^2$ and the Hirzebruch surfaces — which is exactly the dimension-two failure that makes the classification of rational and ruled surfaces a separate theorem.
:::
