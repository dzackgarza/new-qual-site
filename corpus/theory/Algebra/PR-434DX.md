---
schema: qual/card@1
id: PR-434DX
kind: proposition
title: Formula for partitions
classification:
  areas:
  - algebra
  topics:
  - Partitions
  - Number Theory
relations: []
review: draft
---

:::{.proposition}
There is a recurrence relation
\[
P_k(n) = P_k(n-k) + P_{k-1}(n-1)
,\]
which follows from the fact that one can obtain a partition of $n$ with $k$ parts by either

- Taking a partition of $n-k$ into $k$ parts and adding 1 to each part, e.g. $[1,1,1,3] \mapsto [2,2,2,4]$
- Taking a partition of $n-1$ into $k-1$ parts and adding a new standalone part $1$, e.g. $[1,1,2,5] \mapsto [1,1,2,5,1]$.

Summing over $k$ yields the following, which can be recursed:
\[
P(n) 
&= \sum_{k=1}^n P_k(n-k) + P(n-1) \\
&= \sum_{k=1}^n P_k(n-k) + \sum_{k=1}^{n-1} P_k(n-1-k) + P(n-2) \\
&= \cdots
,\]
where $P_k(m) = 0$ for $k>m$ and $P_m(m) = 1$.
:::
