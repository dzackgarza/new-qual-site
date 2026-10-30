---
schema: qual/card@1
id: P-OFKQJ
kind: problem
title: Uniform convergence of $\sum\abs{a_n}$ on compacta implies that of $\sum\abs{a_n'}$
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
Let $K\subset D$ be compact. A series of nonnegative functions converges uniformly on a set exactly when the supremum over the set of its tails $\sum_{n\ge N}$ tends to $0$ as $N\to\infty$.

::: pf

::: {.pf-step #thicken}
There is $\delta>0$ such that $K'\coloneqq\theset{w\suchthat \operatorname{dist}(w,K)\le\delta}$ is a compact subset of $D$.

::: pf-proof
If $D=\CC$ take $\delta=1$. Otherwise $\operatorname{dist}(K,\CC\setminus D)>0$ because $K$ is compact and $\CC\setminus D$ is closed and disjoint from $K$; take $\delta$ half of it. Then $K'$ is closed and bounded.
:::

:::

::: {.pf-step #pointwise}
For $z\in K$ and every $n$, $\abs{a_n'(z)}\le\frac{1}{2\pi\delta}\int_0^{2\pi}\abs{a_n(z+\delta e^{it})}\,dt$.

::: pf-proof
The closed disk of radius $\delta$ about $z$ lies in $K'\subset D$ by step [](#thicken){.pf-ref}. By the Cauchy integral formula for the derivative, $a_n'(z)=\frac{1}{2\pi i}\oint_{\abs{w-z}=\delta}\frac{a_n(w)}{(w-z)^2}\,dw$; parametrize $w=z+\delta e^{it}$ and bound the integrand.
:::

:::

::: pf-step
$\sum_n\abs{a_n'}$ converges uniformly on $K$.

::: pf-proof
Let $T_N(w)\coloneqq\sum_{n\ge N}\abs{a_n(w)}$. By hypothesis $\varepsilon_N\coloneqq\sup_{K'}T_N\to0$. For $z\in K$, summing step [](#pointwise){.pf-ref} over $n\ge N$ and exchanging sum and integral for nonnegative terms (monotone convergence),
$$
\sum_{n\ge N}\abs{a_n'(z)}\le\frac{1}{2\pi\delta}\int_0^{2\pi}T_N(z+\delta e^{it})\,dt\le\frac{\varepsilon_N}{\delta}.
$$
The bound is independent of $z\in K$ and tends to $0$.
:::

:::

:::
:::
