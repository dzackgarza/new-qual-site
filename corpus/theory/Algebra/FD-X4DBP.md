---
schema: qual/card@1
id: FD-X4DBP
kind: definition
title: Alternating group
prompts:
- What is the alternating group, as a kernel?
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
Let $n\geq 1$ and let $\sgn\colon S_n\to\theset{\pm1}$ be the sign homomorphism.
The \dfn{alternating group} is
$$
A_n\coloneqq\ker(\sgn)=\theset{\sigma\in S_n \st \sgn(\sigma)=1},
$$
the subgroup of [[FD-PIVQZ|even permutations]] of $S_n$.
:::
