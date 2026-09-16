---
schema: qual/card@1
id: PR-TOK44
kind: proposition
title: Root test for power series
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
relations: []
review: draft
---

::: {.proposition}
Let $(a_n)_{n\ge0}$ be complex numbers, $z_0\in\CC$, and
$$
R\coloneqq\liminf_{n\to\infty}\abs{a_n}^{-1/n}=\frac{1}{\limsup_{n\to\infty}\abs{a_n}^{1/n}}\in[0,\infty],
$$
with the conventions $1/0=\infty$ and $1/\infty=0$.
Then the power series $\sum_{n\ge0}a_n(z-z_0)^n$

(a) converges absolutely on $\ts{z\st\abs{z-z_0}<R}$,

(b) converges uniformly on $\ts{z\st\abs{z-z_0}\le r}$ for every $r<R$, and

(c) diverges on $\ts{z\st\abs{z-z_0}>R}$.
:::
