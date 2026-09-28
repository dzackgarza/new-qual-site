---
schema: qual/card@1
id: D-6BTFJ
kind: definition
title: Transposition presentation of the symmetric group
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Group Presentations
relations: []
review: draft
---

::: {.definition}
Let $n\geq 2$.
The \dfn{symmetric group} $S_n$ is the group with [[D-V6UJ7|presentation]]
$$
S_n \coloneqq \gens{ \sigma_1, \ldots, \sigma_{n-1} \st \sigma_i^2 \ (1\leq i\leq n-1),\ \sigma_i\sigma_j\sigma_i^{-1}\sigma_j^{-1} \ (\abs{i-j}\geq 2),\ \sigma_i \sigma_{i+1} \sigma_i \sigma_{i+1}^{-1} \sigma_i^{-1} \sigma_{i+1}^{-1} \ (1\leq i\leq n-2) }.
$$
:::

::: {.remark}
Sending $\sigma_i$ to the transposition $(i, i+1)$ identifies this group with the group of bijections of $\theset{1, \ldots, n}$.
:::
