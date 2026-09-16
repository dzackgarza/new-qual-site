---
schema: qual/card@1
id: D-UI3FE
kind: definition
title: Lens space
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Covering Spaces
  - Group Actions
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $m\geq 2$, $n \geq 1$ and let $\ell_1, \ldots, \ell_n$ be integers coprime to $m$.
Let $\ZZ/m$ act on the unit sphere $S^{2n-1}\subseteq \CC^n$ with the generator acting by
$$
(z_1, \ldots, z_n) \mapsto \qty{ e^{2\pi i \ell_1/m} z_1, \ldots, e^{2\pi i \ell_n /m} z_n }
.$$
The \dfn{lens space} is the orbit space
$$
L_m(\ell_1, \ldots, \ell_n) \coloneqq S^{2n-1}/\qty{\ZZ/m}
$$
[@Hat02, Example 2.43, p. 144].
:::

::: {.remark}
The action is free, so $S^{2n-1}\to L_m(\ell_1,\ldots,\ell_n)$ is a covering space [@Hat02, Example 2.43, p. 144], and $L_m(\ell_1,\ldots,\ell_n)$ is a closed $(2n-1)$-manifold.
For $n\geq 2$ the sphere $S^{2n-1}$ is simply connected, so it is the universal cover and $\pi_1(L_m(\ell_1,\ldots,\ell_n)) \cong \ZZ/m$ [@Hat02, Proposition 1.40, p. 72].
For $m=2$ the lens space is $\RP^{2n-1}$.
:::
