---
schema: qual/card@1
id: PR-ZCPDD
kind: proposition
title: Vanishing of homology and cohomology above the dimension
slogan: 'A closed $n$-manifold has no homology or integral cohomology above degree $n$.'
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Homology
  - Cohomology
relations: []
review: draft
---

::: {.proposition}
Let $M$ be a closed connected $n$-manifold.
Then $H_i(M;R) = 0$ for $i > n$ and every coefficient ring $R$ [@Hat02], and $H^i(M;\ZZ) = 0$ for $i>n$ by the universal coefficient theorem [@Hat02], since $H_n(M;\ZZ)$ is free.
:::

::: {.remark}
In degree $n$, $H^n(M;\ZZ)\cong\ZZ$ if $M$ is orientable and $H^n(M;\ZZ)\cong\ZZ/2$ otherwise, by the universal coefficient theorem applied to $H_n(M;\ZZ)$ and the torsion subgroup of $H_{n-1}(M;\ZZ)$ [@Hat02].
:::
