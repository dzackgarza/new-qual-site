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
Let $X$ be a smooth surface, separated and of finite type over an algebraically closed field $k$, and let $E \subseteq X$ be an integral curve that is proper over $k$.
There exist a smooth surface $Y$ over $k$, a point $p \in Y$ and a morphism $\sigma \colon X \to Y$ that is the blowup of $Y$ at $p$ with exceptional curve $E$ if and only if $E \cong \PP^1$ and $E^2 = -1$.
Such a curve is a \dfn{$(-1)$-curve}, or exceptional curve of the first kind.
If $X$ is projective, then $Y$ is projective [@Har10a, Theorem V.5.7].
:::

::: {.remark}
This converts a numerical condition into a birational morphism, and it is what makes the minimal model program work in dimension two: contract $(-1)$-curves until none remain, and the result is a **minimal** surface.
Since each contraction raises $K^2$ by one and $\rho$ drops by one, the process terminates.

By adjunction, $E \cong \PP^1$ with $E^2 = -1$ is equivalent to $E^2 = -1$ and $K \cdot E = -1$, which is the form the criterion is usually applied in.

A surface can have infinitely many $(-1)$-curves: the blowup of $\PP^2$ at $9$ points in general position, in the sense that no three of the points are collinear after any finite sequence of quadratic transformations centred at three of them, has infinitely many ([[P-AGH5415GENPOSITION]], part (e)), while for $r = 7$ and $r = 8$ points in general position there are exactly $56$ and $240$ (part (d)).
The minimal model is then not unique in general — for rational surfaces one can reach both $\PP^2$ and the Hirzebruch surfaces — which is exactly the dimension-two failure that makes the classification of rational and ruled surfaces a separate theorem.
:::
