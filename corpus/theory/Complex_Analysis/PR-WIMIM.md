---
schema: qual/card@1
id: PR-WIMIM
kind: proposition
title: Ratio test
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
Let $(a_k)_{k\ge0}$ be nonzero complex numbers such that $L\coloneqq\lim_{k\to\infty}\abs{\frac{a_{k+1}}{a_k}}$ exists in $[0,\infty]$.

- If $L<1$, then $\sum_k a_k$ converges absolutely.

- If $L>1$, then $\sum_k a_k$ diverges.

- If $L=1$, the test gives no information: $\sum_k 1/k$ diverges and $\sum_k 1/k^2$ converges, and both have $L=1$.

In particular, if $c_k\neq0$ and $\lim_k\abs{c_{k+1}/c_k}=\ell\in[0,\infty]$, applying the test to $a_k=c_kz^k$ shows that $\sum_kc_kz^k$ has radius of convergence $1/\ell$, with $1/0=\infty$ and $1/\infty=0$.
:::
