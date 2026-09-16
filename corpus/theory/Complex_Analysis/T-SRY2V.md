---
schema: qual/card@1
id: T-SRY2V
kind: theorem
title: Holomorphic implies analytic
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Holomorphic Functions
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open, let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$, and let $D$ be an open disc centred at $p$ whose closure is contained in $\Omega$.
Then for every $z\in D$ the series below converges and
$$
f(z)=\sum_{k\geq0}c_k(z-p)^k,\qquad c_k=\frac{f^{(k)}(p)}{k!}.
$$
In particular, $f$ is [[D-V6UQJ|analytic]] at every point of $\Omega$.
:::

::: {.remark}
See [@SS03].
Conversely, a function analytic on $\Omega$ is holomorphic on $\Omega$, since a power series is complex differentiable inside its disc of convergence; so holomorphic and analytic functions on $\Omega$ coincide.
:::
