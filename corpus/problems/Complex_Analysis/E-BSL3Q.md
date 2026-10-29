---
schema: qual/card@1
id: E-BSL3Q
kind: problem
title: Power series of holomorphic functions on the disk converge uniformly on compacta
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Uniform Convergence
  - Holomorphic Functions
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is holomorphic on $\DD$ then $f$ has a power series expansion that converges uniformly on every compact $K\subset \DD$.
::: {.solution}
Since $f$ is holomorphic on $\DD$, its Taylor series $f(z)=\sum_{n\ge0}a_nz^n$ at $0$ converges to $f$ on $\DD$.
Let $K\subset\DD$ be compact and nonempty, let $r\coloneqq\max_{z\in K}\abs z<1$, choose $R$ with $r<R<1$, and let $M_R\coloneqq\max_{\abs\zeta=R}\abs{f(\zeta)}$.

::: pf

::: {.pf-step #bound}
$\abs{a_nz^n}\le M_R(r/R)^n$ for $z\in K$ and $n\ge0$.

::: pf-proof
Cauchy's estimate on the circle $\abs\zeta=R$ gives $\abs{a_n}\le M_R/R^n$, and $\abs z\le r$ on $K$.
:::

:::

::: pf-step
The Taylor series converges uniformly on $K$.

::: pf-proof
Since $r/R<1$, the geometric series $\sum_nM_R(r/R)^n$ converges, so the Weierstrass $M$-test applies by step [](#bound){.pf-ref}.
:::

:::

:::

:::
