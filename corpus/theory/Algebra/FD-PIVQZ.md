---
schema: qual/card@1
id: FD-PIVQZ
kind: definition
title: Even and odd permutations
prompts:
- What distinguishes an even permutation from an odd one?
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
---

::: {.definition}
Let $\varepsilon\colon S_n\to\theset{\pm1}$ be the sign homomorphism and $\sigma\in S_n$.
The permutation $\sigma$ is \dfn{even} if $\varepsilon(\sigma) = 1$ and \dfn{odd} if $\varepsilon(\sigma) = -1$.
:::

::: {.remark}
Since every permutation is a product of transpositions and each transposition has sign $-1$, a product of $t$ transpositions has sign $(-1)^t$.
So $\sigma$ is even if and only if it is a product of an even number of transpositions, and odd if and only if it is a product of an odd number of transpositions.
:::
