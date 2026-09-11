---
schema: qual/card@1
id: PR-DIVAMPCURVE
kind: proposition
title: Ampleness of a divisor on a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ample Divisors
  - Curves
  - Degree
relations:
- kind: uses
  target: D-DIVAMPLE
- kind: uses
  target: PR-Y5S7V
- kind: related-to
  target: T-D8TUX
review: draft
prompts:
- When is a divisor on a curve ample?
- What degree makes a divisor on a curve base-point free? Very ample?
---

::: {.proposition}
Let $D$ be a divisor on a smooth projective curve $X$ of genus $g$ over $k = \bar{k}$.

- $D$ is ample if and only if $\deg D > 0$.
- $\deg D \geq 2g$ implies $\abs{D}$ is base-point free.
- $\deg D \geq 2g+1$ implies $D$ is very ample.
:::

::: {.remark}
On a curve ampleness collapses to a single integer, and this is the cleanest place to see the ample-against-very-ample distinction: positivity of the degree is ample, but very ampleness needs the degree to clear a genus-dependent threshold.
Raising the degree past $2g+1$ is exactly what taking powers achieves, which is the definition of ample in this case.

The thresholds are what Riemann--Roch gives: once $\deg D > 2g-2$ the correction term vanishes and $h^0$ is computable, so the conditions for base points and for separation become arithmetic.
Both bounds are sharp on an elliptic curve, where $g = 1$ and degree $2$ gives the base-point-free double cover of $\PP^1$ while degree $3$ first embeds.
:::
