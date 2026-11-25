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
The ordinary double point $\{xy-zw=0\}\subseteq\CC^4$ is the affine toric variety $U_\sigma$ of $\sigma=\Cone(e_1,e_2,e_1+e_3,e_2+e_3)$ [Cox--Little--Schenck, *Toric Varieties*, Example 11.2.12], and it is terminal by the lattice-point criterion of [*ibid.*, Proposition 11.4.12(b)(i)]: $\Pi_\sigma=\operatorname{Conv}(0,e_1,e_2,e_1+e_3,e_2+e_3)$ lies in $\inner{m_0}{u}\le1$ for $m_0=e_1+e_2$, a nonzero lattice point has $\inner{m_0}{u}=1$ and so lies in the facet, which is the unit square with vertices $(1,0)$, $(0,0)$, $(1,1)$, $(0,1)$ in the coordinates $(u_1,u_3)$ on that plane. Terminality forces every exceptional divisor of every proper birational morphism from a smooth variety to have positive discrepancy [*ibid.*, Definition 11.4.9(a) and the paragraph following it], so a crepant resolution of a terminal singularity has no exceptional divisor and is necessarily small; and here one exists, the refinement $\Sigma_1$ giving a crepant $X_{\Sigma_1}\to U_\sigma$ [*ibid.*, Example 11.2.6] whose exceptional locus is a $\PP^1$ [*ibid.*, Example 11.1.12].
Small is not the same as trivial, and the resolution is not unique: this singularity has two crepant small resolutions, each an isomorphism away from the vertex with a $\PP^1$ over it, and they are not isomorphic over it, the birational map between them being the Atiyah flop ([[FE-207WC]], [@Vak25, Exercise 22.4.N and Remark 22.4.11]); so a terminal singularity may carry non-isomorphic crepant small resolutions.
:::
