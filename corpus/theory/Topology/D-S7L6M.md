---
schema: qual/card@1
id: D-S7L6M
kind: definition
title: Left exact, right exact, and exact functors
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Category Theory
relations: []
review: draft
---

::: {.definition}
Let $T\colon\mathcal A\to\mathcal B$ be an additive covariant functor between abelian categories, such as categories of modules.
The functor $T$ is \dfn{right exact} if for every short [[D-BJYH3|exact sequence]] $0\to A\mapsvia{f}B\mapsvia{g}C\to0$ in $\mathcal A$ the sequence
$$
T(A)\mapsvia{T(f)}T(B)\mapsvia{T(g)}T(C)\to0
$$
is exact, and \dfn{left exact} if for every such sequence
$$
0\to T(A)\mapsvia{T(f)}T(B)\mapsvia{T(g)}T(C)
$$
is exact.
It is \dfn{exact} if it is both left and right exact, that is, if it takes every short exact sequence to a short exact sequence.
:::

::: {.example}
For a commutative ring $R$ and an $R$-module $N$, the functor $-\otimes_RN$ on $R$-modules is right exact [@DF04, sec. 10.5], and so is $N\otimes_R-$.
:::
