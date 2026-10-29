---
schema: qual/card@1
id: P-CIWAP
kind: problem
title: Holomorphic functions on the disk expand as power series uniformly on compact
  subsets
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

::: {.problem}
Show that if $f$ is holomorphic on $\DD$ then $f$ has a power series expansion that converges uniformly on every compact $K\subset \DD$.
:::

::: {.solution}

Let $f(z)=\sum_{n=0}^\infty a_nz^n$ be the Taylor expansion of $f$ at $0$, which converges to $f$ on $\DD$.
Let $K\subset\DD$ be compact, $r\coloneqq\max_{z\in K}\abs{z}<1$, and fix $R$ with $r<R<1$.

::: pf

::: {.pf-step #cauchy}
$\abs{a_n}\le M_R/R^n$, where $M_R\coloneqq\max_{\abs{\zeta}=R}\abs{f(\zeta)}$.

::: pf-proof
This is Cauchy's estimate on the circle $\abs{\zeta}=R$.
:::

:::

::: pf-step
The series converges uniformly on $K$.

::: pf-proof
For $z\in K$, step [](#cauchy){.pf-ref} gives $\abs{a_nz^n}\le M_R(r/R)^n$, a summable geometric majorant, so the Weierstrass $M$-test applies.
:::

:::

:::

:::
