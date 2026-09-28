---
schema: qual/card@1
id: PR-4X6G2
kind: proposition
title: Poincaré duality for closed manifolds
slogan: 'On a closed orientable manifold, cap product with the fundamental class exchanges degree $k$ cohomology with degree $n-k$ homology.'
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
---

::: {.proposition}
Let $M$ be a closed orientable $n$-manifold and $R$ a commutative ring; for example $R = \ZZ$ or $R$ a field.
Then cap product with the fundamental class gives isomorphisms
$$
H^{k}(M; R) \xrightarrow{\ \sim\ } H_{n-k}(M; R)
$$
for all $k$ [@Hat02].
:::

::: {.remark}
For $n\geq 1$, the orientable manifold $\RR^n$ is not closed, and $H^0(\RR^n;\ZZ)\cong\ZZ$ while $H_n(\RR^n;\ZZ) = 0$.
The closed manifold $\RP^2$ is not orientable, and $H^0(\RP^2;\ZZ)\cong\ZZ$ while $H_2(\RP^2;\ZZ) = 0$.
For a field $F$ of characteristic $2$, every closed manifold is $F$-orientable, so the duality holds for all closed manifolds with $\ZZ/2$ coefficients.
:::
