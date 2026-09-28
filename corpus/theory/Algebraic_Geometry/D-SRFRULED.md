---
schema: qual/card@1
id: D-SRFRULED
kind: definition
title: Rational and ruled surfaces, and the Hirzebruch surfaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ruled Surfaces
  - Rational Surfaces
  - Minimal Models
relations:
- kind: uses
  target: T-SRFCAST
review: draft
prompts:
- What is a ruled surface?
- What are the minimal rational surfaces?
- Give a criterion for a surface to be rational.
---

::: {.definition}
A surface $X$ is \dfn{ruled} over a curve $C$ if it is birational to $C \times \PP^1$; it is \dfn{geometrically ruled} if there is a morphism $X \to C$ whose every fibre is $\PP^1$, equivalently $X = \PP(\mathcal{E})$ for a rank-two bundle $\mathcal{E}$ on $C$.
$X$ is \dfn{rational} if it is birational to $\PP^2$.
:::

::: {.example title="Hirzebruch surfaces"}
$\FF_n = \PP(\OO_{\PP^1} \oplus \OO_{\PP^1}(n))$ is the geometrically ruled surface over $\PP^1$ with a section $C_0$ satisfying $C_0^2 = -n$.
$\FF_0 = \PP^1 \times \PP^1$ and $\FF_1 = \Bl_p \PP^2$.
The minimal rational surfaces are exactly $\PP^2$ and $\FF_n$ for $n \neq 1$.
:::

::: {.theorem title="Castelnuovo's rationality criterion"}
A smooth projective surface over $\CC$ is rational if and only if $q = 0$ and $P_2 = h^0(2K) = 0$.
:::

::: {.remark}
The section $C_0$ of $\FF_1$ is a $(-1)$-curve, and contracting it gives $\PP^2$, so $\FF_1$ is not minimal.
The minimal rational surfaces $\PP^2$, $\FF_0$, $\FF_2$, $\FF_3,\ldots$ are pairwise non-isomorphic and birational to each other, so a rational surface has no unique minimal model.

The conditions $p_g=q=0$ do not imply rationality: Enriques surfaces satisfy them but have $P_2=1$, while Castelnuovo's criterion requires $q=P_2=0$.

A smooth projective surface over $\CC$ has Kodaira dimension $\kappa = -\infty$, that is, all plurigenera $P_m=h^0(mK)$ with $m\ge1$ vanish, if and only if it is ruled; rational surfaces are the surfaces ruled over $\PP^1$.
:::
