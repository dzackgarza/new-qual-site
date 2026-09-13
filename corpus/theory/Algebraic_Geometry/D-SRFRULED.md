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
A surface $X$ is **ruled** over a curve $C$ if it is birational to $C \times \PP^1$; it is **geometrically ruled** if there is a morphism $X \to C$ whose every fibre is $\PP^1$, equivalently $X = \PP(\mathcal{E})$ for a rank-two bundle $\mathcal{E}$ on $C$.
$X$ is **rational** if it is birational to $\PP^2$.
:::

::: {.example title="Hirzebruch surfaces"}
$\FF_n = \PP(\OO_{\PP^1} \oplus \OO_{\PP^1}(n))$ is the geometrically ruled surface over $\PP^1$ with a section $C_0$ satisfying $C_0^2 = -n$.
$\FF_0 = \PP^1 \times \PP^1$ and $\FF_1 = \Bl_p \PP^2$.
The minimal rational surfaces are exactly $\PP^2$ and $\FF_n$ for $n \neq 1$.
:::

::: {.theorem title="Castelnuovo's rationality criterion"}
A surface over $\CC$ is rational if and only if $q = 0$ and $P_2 = h^0(2K) = 0$.
:::

::: {.remark}
$\FF_1$ is not minimal precisely because its negative section is a $(-1)$-curve, which contracts back to $\PP^2$; that is the concrete reason the minimal model of a rational surface is not unique.

The rationality criterion is worth stating carefully, because the naive guess — $p_g = q = 0$ — is false: the Enriques surfaces have $p_g = q = 0$ and are not rational, and $P_2 = 1$ detects them.

Ruled surfaces and rational surfaces are the $\kappa = -\infty$ part of the classification, and the invariant that identifies them is the vanishing of all plurigenera.
:::
