---
schema: qual/card@1
id: T-SRY2V
kind: theorem
title: "Holomorphic implies analytic"
classification:
  areas:
  - complex-analysis
  topics:
  - power-series
  - holomorphic-functions
  - cauchy-integral-formula
relations: []
review: draft
---

::: {.theorem title="Holomorphic implies analytic"}
Suppose $f$ is holomorphic on an open set $\Omega$, and let $D$ be a disc centred at $p$ whose closure is contained in $\Omega$.
Then $f$ has a power series expansion at $p$,
\[
f(z) = \sum_{k\geq 0} c_k (z-p)^k, \qquad c_k = {f^{(k)}(p) \over k!}
,\]
converging for all $z\in D$.
:::

::: {.remark}
Stein and Shakarchi, *Complex Analysis*, Ch. 2 Theorem 4.4.
The hypothesis is holomorphy, i.e. complex differentiability; the conclusion is analyticity, i.e. a local power series.
The two are therefore equivalent, which is why the words are used interchangeably, but this theorem is the direction that needs Cauchy's integral formula.
:::
