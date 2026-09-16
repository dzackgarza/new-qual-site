---
schema: qual/card@1
id: D-TMME3
kind: definition
title: Alternating group
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
A permutation $\sigma\in S_n$ is \dfn{even} if $\sgn(\sigma) = 0$, where $\sgn\colon S_n\to\ZZ/2$ is the [[D-BZ3KD|sign homomorphism]].
The \dfn{alternating group} is the subgroup of even permutations of the [[D-6BTFJ|symmetric group]]:
$$
A_n \coloneqq \theset{\sigma \in S_n \suchthat \sgn(\sigma) = 0} = \ker(\sgn).
$$
:::

::: {.remark}
A cycle of length $\ell$ is a product of $\ell-1$ transpositions, so a permutation is even if and only if its disjoint cycle decomposition has an even number of cycles of even length.
:::
