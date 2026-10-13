---
schema: qual/card@1
id: D-BZ3KD
kind: definition
title: Sign homomorphism
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Homomorphisms
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$.
The \dfn{sign homomorphism} is the map
$$
\sgn\colon S_n \to \theset{\pm1}, \qquad \sigma \mapsto (-1)^k,
$$
where $\sigma = \tau_1 \cdots \tau_k$ is any expression of $\sigma$ as a product of $k\geq 0$ transpositions.
:::

::: {.proposition}
Let $n \geq 1$.
For $\sigma\in S_n$, all expressions of $\sigma$ as a product of transpositions have the same number of factors modulo $2$, so $\sgn$ is well defined. Moreover,
$$
\sgn(\sigma\rho)=\sgn(\sigma)\sgn(\rho),
$$
so $\sgn$ is a group homomorphism.
:::
