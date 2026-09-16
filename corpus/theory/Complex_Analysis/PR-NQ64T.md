---
schema: qual/card@1
id: PR-NQ64T
kind: proposition
title: Radius of convergence by the root test
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
relations: []
review: draft
---

::: {.proposition}
Let $(c_k)_{k\ge0}$ be complex numbers, and define $R\in[0,\infty]$ by
$$
\frac1R\coloneqq\limsup_{k\to\infty}\abs{c_k}^{1/k},
$$
with the conventions $1/0=\infty$ and $1/\infty=0$.
Then the power series $f(z)=\sum_{k\ge0}c_kz^k$ converges absolutely for $\abs{z}<R$, uniformly on every closed disc $\abs{z}\le r$ with $r<R$, and diverges for $\abs{z}>R$.
So $R$ is the radius of convergence of the series.

Moreover $f$ is [[D-E7A5W|holomorphic]] on $D_R\coloneqq\ts{z\st\abs{z}<R}$, and it can be differentiated term by term:
$$
f'(z)=\sum_{k\ge1}kc_kz^{k-1},\qquad \abs{z}<R,
$$
where the differentiated series has the same radius of convergence $R$.
:::
