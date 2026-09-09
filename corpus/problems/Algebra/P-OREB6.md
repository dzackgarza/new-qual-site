---
schema: qual/card@1
id: P-OREB6
kind: problem
title: A permutation is odd iff it has an odd number of even-length cycles
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
---

::: problem
Show that a permutation is odd if and only if its disjoint-cycle decomposition contains an odd number of even-length cycles.
:::

::: {.solution}
An $m$-cycle has sign
\[
(-1)^{m-1},
\]
so it is odd exactly when $m$ is even.

Write a permutation as a product of disjoint cycles
\[
\sigma=c_1\cdots c_r.
\]
Then
\[
\operatorname{sgn}(\sigma)=\prod_{i=1}^r\operatorname{sgn}(c_i).
\]
Odd-length cycles contribute $+1$, while even-length cycles contribute $-1$. Hence
\[
\operatorname{sgn}(\sigma)=(-1)^e,
\]
where $e$ is the number of even-length cycles. Therefore $\sigma$ is odd exactly when $e$ is odd.
:::
