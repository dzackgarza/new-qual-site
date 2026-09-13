---
schema: qual/card@1
id: P-AGXGATHVICLOSURE
kind: problem
title: $V(I(X))$ is the Zariski closure of an arbitrary subset of $\AA^n$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Topology
  - Closure
  - Nullstellensatz
relations: []
review: draft
---

::: problem
Let $X\subset \AA^n$ be an arbitrary subset and show that
\[
V(I(X)) = \bar{X}
.\]
:::

::: solution
$\bar{X} \subseteq V(I(X))$:
We have $X\subseteq V(I(X))$, and $V(J)$ is closed in the Zariski topology for any ideal $J \normal k[x_1, \cdots, x_{n}]$ by definition, so $V(I(X))$ is closed.
Thus
\[
X\subseteq V(I(X)) \text{ and } V(I(X))\text{ closed } \implies \bar{X} \subseteq V(I(X))
,\]
since $\bar{X}$ is the intersection of all closed sets containing $X$.

$V(I(X)) \subseteq \bar{X}$:
Noting that $V({-})$ and $I({-})$ are individually order-reversing, $V(I({-}))$ is order-*preserving*, so
\[
X\subseteq \bar{X} \implies V(I(X)) \subseteq V(I(\bar{X})) = \bar{X}
,\]
where the last equality uses part (i) of the Nullstellensatz: if $X$ is an affine variety, then $V(I(X)) = X$.
This applies because $\bar{X}$ is always closed, and the closed sets in the Zariski topology are precisely the affine varieties.
:::
