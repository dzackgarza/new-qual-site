---
schema: qual/card@1
id: D-EGHL6
kind: definition
title: Perfect pairing
classification:
  areas:
  - topology
  topics:
  - Modules
  - Linear Algebra
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring and $M$, $N$, $L$ $R$-modules.
A \dfn{pairing} of $M$ and $N$ with values in $L$ is an $R$-bilinear map $p\colon M\times N\to L$, equivalently an $R$-linear map $M\otimes_R N\to L$ on the [[D-DEFTENS|tensor product]].
The pairing $p$ is \dfn{perfect} if the $R$-linear map
$$
\phi\colon M\to\Hom_R(N, L),\qquad \phi(m)(n)\coloneqq p(m, n),
$$
is an isomorphism.
:::
