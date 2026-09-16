---
schema: qual/card@1
id: PR-L7LNZ
kind: proposition
title: Uniform limits commute with integrals on finite measure spaces
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Convergence of Integrals
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]] with $\mu(X)<\infty$.
If $f_n,f\in L^1(X,\mu)$ and $f_n\to f$ [[D-YZC3C|uniformly]] on $X$, then
$$
\abs{\int_X(f_n-f)\dmu}
\leq \mu(X)\sup_{x\in X}\abs{f_n(x)-f(x)} \convergesto{n\to\infty} 0,
$$
so $\int_X f_n\dmu\to\int_X f\dmu$.
:::

::: {.proof}
$$
\abs{\int_X(f_n-f)\dmu}
\leq \int_X\abs{f_n-f}\dmu
\leq \mu(X)\sup_{x\in X}\abs{f_n(x)-f(x)},
$$
and the right-hand side tends to $0$ by uniform convergence.
:::
