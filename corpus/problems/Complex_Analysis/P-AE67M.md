---
schema: qual/card@1
id: P-AE67M
kind: problem
title: Uniform convergence of $\sum\abs{a_n'}$ on compacta from that of $\sum\abs{a_n}$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Cauchy Estimates
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $a_n(z)$ be an analytic sequence in a domain $D$ such that $\displaystyle \sum_{n=0}^\infty \abs{a_n(z)}$ converges uniformly on bounded and closed sub-regions of $D$.
Show that $\displaystyle \sum_{n=0}^\infty \abs{a'_n(z)}$ converges uniformly on bounded and closed sub-regions of $D$.
:::

::: {.solution}
Let $K\subset D$ be compact.
Choose $\rho>0$ so that $K_\rho\coloneqq\theset{w\suchthat \operatorname{dist}(w,K)\le\rho}$ is contained in $D$; $K_\rho$ is compact.

::: pf

::: {.pf-step #cauchy}
For $z\in K$ and every $n$, $\abs{a_n'(z)} \le \frac{1}{2\pi\rho^2}\int_{\abs{w-z}=\rho}\abs{a_n(w)}\,\abs{dw}$.

::: pf-proof
The closed disk $\abs{w-z}\le\rho$ lies in $K_\rho\subset D$, and Cauchy's formula gives $a_n'(z)=\frac{1}{2\pi i}\int_{\abs{w-z}=\rho}\frac{a_n(w)}{(w-z)^2}\,dw$.
:::

:::

::: pf-step
$\sum_n\abs{a_n'}$ converges uniformly on $K$.

::: pf-proof
For $N\le N'$ and $z\in K$, step [](#cauchy){.pf-ref} gives
$$
\sum_{n=N}^{N'}\abs{a_n'(z)} \le \frac{1}{\rho}\sup_{w\in K_\rho}\sum_{n=N}^{N'}\abs{a_n(w)},
$$
since the circle has length $2\pi\rho$ and lies in $K_\rho$.
By hypothesis $\sum\abs{a_n}$ converges uniformly on $K_\rho$, so the right side tends to $0$ as $N,N'\to\infty$.
Thus $\sum\abs{a_n'}$ is uniformly Cauchy on $K$, hence uniformly convergent there.
:::

:::

:::

:::
