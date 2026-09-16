---
schema: qual/card@1
id: T-B7YTE
kind: theorem
title: Abel's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
relations: []
review: draft
---

::: {.theorem}
Let $(c_k)_{k\ge0}$ be complex numbers such that $\sum_{k\ge0}c_k$ converges.
Then $\sum_{k\ge0}c_kz^k$ converges for $\abs z<1$, and
$$
\lim_{r\to1^-}\sum_{k\ge0}c_kr^k=\sum_{k\ge0}c_k,
$$
where the limit is taken over real $r\in(0,1)$.
:::
