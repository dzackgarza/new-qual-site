---
schema: qual/card@1
id: T-DB3DO
kind: theorem
title: Taylor expansion with holomorphic remainder
slogan: 'After truncating a Taylor series, the remainder still factors holomorphically by the next power of $z-z_0$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open, let $z_0\in\Omega$, let $f$ be [[D-V6UQJ|analytic]] on $\Omega$, and let $n\geq1$.
Then there is a function $R_n$ analytic on $\Omega$ such that for all $z\in\Omega$,
$$
f(z)=\sum_{k=0}^{n-1}\frac{f^{(k)}(z_0)}{k!}(z-z_0)^k+R_n(z)(z-z_0)^n.
$$
:::
