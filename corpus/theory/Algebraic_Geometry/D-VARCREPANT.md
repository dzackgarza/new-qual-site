---
schema: qual/card@1
id: D-VARCREPANT
kind: definition
title: Crepant morphisms and crepant resolutions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Canonical Divisor
  - Resolution of Singularities
  - Discrepancy
relations:
- kind: related-to
  target: D-SRFADE
- kind: related-to
  target: FE-SRFBLOW
review: draft
prompts:
- What is a crepant map?
---

::: {.definition title="Crepant morphism"}
Let $X$ and $Y$ be normal varieties whose canonical divisors are $\QQ$-Cartier.
A proper birational morphism $f \colon Y \to X$ is \dfn{crepant} if $K_Y = f^* K_X$ as $\QQ$-divisor classes, that is, every $f$-exceptional prime divisor has discrepancy $0$.
A \dfn{crepant resolution} is a crepant $f$ with $Y$ smooth.
:::

::: {.example}
The minimal resolution of an ADE surface singularity is crepant: its exceptional curves $E$ are smooth rational curves with $E^2 = -2$, so $K_Y \cdot E = 0$ for each, and $K_Y - f^* K_X$, supported on the exceptional curves, is zero because the intersection form on them is negative definite.
The blowup $f \colon Y \to X$ of a smooth point on a surface is not crepant: $K_Y = f^* K_X + E$.
The quotient $\CC^4 / \{\pm 1\}$ has no crepant resolution, because its singularity is terminal: every exceptional divisor of every resolution has positive discrepancy.
:::
