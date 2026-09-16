---
schema: qual/card@1
id: PR-QNDSD
kind: proposition
title: Power series are smooth on their disc of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $f(z)=\sum_{k\ge0}c_k(z-z_0)^k$ be a power series with radius of convergence $R>0$.
Then $f$ is [[D-E7A5W|holomorphic]] and infinitely differentiable on $D_R(z_0)$, its derivative is obtained by term-by-term differentiation,
$$
f'(z)=\sum_{k\ge1}kc_k(z-z_0)^{k-1},\qquad z\in D_R(z_0),
$$
where this series also has radius of convergence $R$, and the coefficients are
$$
c_k=\frac{f^{(k)}(z_0)}{k!},\qquad k\ge0.
$$
:::
