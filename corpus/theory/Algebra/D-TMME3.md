---
schema: qual/card@1
id: D-TMME3
kind: definition
title: Alternating group
prompts:
- What is the alternating group, as a kernel?
- What distinguishes an even permutation from an odd one?
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Subgroups
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$.
A permutation $\sigma\in S_n$ is \dfn{even} if $\sgn(\sigma) = 1$, where $\sgn\colon S_n\to\theset{\pm1}$ is the [[D-BZ3KD|sign homomorphism]], and \dfn{odd} if $\sgn(\sigma) = -1$.
The \dfn{alternating group} is the subgroup of even permutations of the [[D-6BTFJ|symmetric group]]:
$$
A_n \coloneqq \theset{\sigma \in S_n \suchthat \sgn(\sigma) = 1} = \ker(\sgn).
$$
:::

::: {.remark}
Each transposition has sign $-1$, so a product of $t$ transpositions has sign $(-1)^t$.
Hence $\sigma$ is even if and only if it is a product of an even number of transpositions, and odd if and only if it is a product of an odd number of transpositions.
A cycle of length $\ell$ is a product of $\ell-1$ transpositions, so a permutation is even if and only if its disjoint cycle decomposition has an even number of cycles of even length.
:::
