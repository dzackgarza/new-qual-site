---
schema: qual/card@1
id: PR-NQ64T
kind: proposition
title: Radius of convergence by the root test
slogan: 'The radius of convergence $R$ of $\sum c_kz^k$ is given by $R^{-1}=\limsup\abs{c_k}^{1/k}$.'
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
Let $(c_k)_{k\ge0}$ be complex numbers, let $z_0\in\CC$, and define $R\in[0,\infty]$ by
$$
\frac1R\coloneqq\limsup_{k\to\infty}\abs{c_k}^{1/k},
$$
with the conventions $1/0=\infty$ and $1/\infty=0$.
Then the power series $f(z)=\sum_{k\ge0}c_k(z-z_0)^k$ converges absolutely for $\abs{z-z_0}<R$, uniformly on every closed disc $\abs{z-z_0}\le r$ with $r<R$, and diverges for $\abs{z-z_0}>R$.
So $R$ is the radius of convergence of the series.

Moreover $f$ is [[D-E7A5W|holomorphic]] on $\DD_R(z_0)\coloneqq\theset{z\st\abs{z-z_0}<R}$, and it can be differentiated term by term:
$$
f'(z)=\sum_{k\ge1}kc_k(z-z_0)^{k-1},\qquad \abs{z-z_0}<R,
$$
where the differentiated series has the same radius of convergence $R$.

The radius and its Hadamard formula are [@SS03, Theorem 2.5 of Chapter 1 (p. 15)], which states the absolute convergence, the divergence, and the formula, and termwise differentiation inside the disc is [@SS03, Corollary 2.7 (p. 18)].
The uniform convergence on closed discs and the equality of the differentiated series' radius are additions here, both consequences of the comparison test inside $\DD_R(z_0)$.
:::
