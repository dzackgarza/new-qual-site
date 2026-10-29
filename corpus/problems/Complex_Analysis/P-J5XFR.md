---
schema: qual/card@1
id: P-J5XFR
kind: problem
title: Compact convergence of holomorphic $f_n$ on $\DD$ is equivalent to $L^1$ convergence on circles
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Let $(f_n)$ and $f$ be holomorphic on $\DD$. Prove that the following are equivalent:

(a) $f_n\to f$ uniformly on compact subsets of $\DD$;

(b) for every $0<r<1$,
$$
\int_{\abs{z}=r}\abs{f_n(z)-f(z)}\,\abs{dz}\longrightarrow0.
$$
:::

::: {.solution}
::: pf

::: pf-step
(a) implies (b).

::: pf-proof
The circle $\abs{z}=r$ is compact, so
$$
\int_{\abs{z}=r}\abs{f_n-f}\,\abs{dz} \le2\pi r\sup_{\abs{z}=r}\abs{f_n-f}\to0.
$$
:::

:::

::: pf-step
(b) implies (a).

::: pf-proof
Fix $0<\rho<r<1$.
Cauchy's integral formula for $f_n-f$ on $\abs{\zeta}=r$ gives, for $\abs{z}\le\rho$, since $\abs{\zeta - z} \geq r - \rho$,
$$
\abs{f_n(z)-f(z)} \le\frac1{2\pi(r-\rho)} \int_{\abs{\zeta}=r}\abs{f_n(\zeta)-f(\zeta)}\,\abs{d\zeta}.
$$
By (b) the right-hand side tends to $0$, and it does not depend on $z$, so $f_n \to f$ uniformly on $\abs{z}\le\rho$.
Every compact subset of $\DD$ lies in such a disc.
:::

:::

:::
:::
