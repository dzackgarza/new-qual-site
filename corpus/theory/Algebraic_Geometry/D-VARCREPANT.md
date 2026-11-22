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
For a proper birational morphism $f \colon Y \to X$, write
$$
K_Y = f^* K_X + \sum_i a_i E_i
$$
over the $f$-exceptional prime divisors $E_i$; the numbers $a_i$ are the \dfn{discrepancies} of $f$.
The morphism $f$ is \dfn{crepant} if $K_Y = f^* K_X$ as $\QQ$-divisor classes, that is, every $f$-exceptional prime divisor has discrepancy $0$.
A \dfn{crepant resolution} is a crepant $f$ with $Y$ smooth.
:::

::: {.example}
The minimal resolution of an ADE surface singularity is crepant: its exceptional curves $E$ are smooth rational curves with $E^2 = -2$, so $K_Y \cdot E = 0$ for each, and $K_Y - f^* K_X$, supported on the exceptional curves, is zero because the intersection form on them is negative definite.
The blowup $f \colon Y \to X$ of a smooth point on a surface is not crepant: $K_Y = f^* K_X + E$.
The ordinary double point $\{xy-zw=0\}\subseteq\CC^4$ is terminal and has crepant small resolutions: terminality forces every exceptional divisor of every resolution to have positive discrepancy, so a crepant resolution of a terminal singularity has no exceptional divisor and is necessarily small, and such a resolution can exist [Cox--Little--Schenck, *Toric Varieties*, Proposition 11.4.12 and Example 11.4.13, and Exercise 11.4.13(a)].
Small is not the same as trivial, and the resolution is not unique: this singularity has two crepant small resolutions, each an isomorphism away from the vertex with a $\PP^1$ over it, and they are not isomorphic over it, the birational map between them being the Atiyah flop ([[FE-207WC]], [@Vak25, Exercise 22.4.N and Remark 22.4.11]); so a terminal singularity may carry non-isomorphic crepant small resolutions.
:::
