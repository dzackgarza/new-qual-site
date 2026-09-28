---
schema: qual/card@1
id: P-AE67M
kind: problem
title: Uniform convergence of $\sum|a_n'|$ on compacta from that of $\sum|a_n|$
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
Let $a_n(z)$ be an analytic sequence in a domain $D$ such that $\displaystyle \sum_{n=0}^\infty |a_n(z)|$ converges uniformly on bounded and closed sub-regions of $D$.
Show that $\displaystyle \sum_{n=0}^\infty |a'_n(z)|$ converges uniformly on bounded and closed sub-regions of $D$.
:::

::: {.solution}
Let $K\Subset D$ be compact. Choose $\rho>0$ so that the closed
$\rho$-neighborhood
\[
K_\rho=\{w:\operatorname{dist}(w,K)\le\rho\}
\]
is compactly contained in $D$. For $z\in K$, Cauchy's formula on
$|w-z|=\rho$ gives
\[
|a_n'(z)|
\le \frac1{2\pi\rho}
\int_{|w-z|=\rho}|a_n(w)|\,|dw|.
\]
Therefore for integers $N\le M$,
\[
\sum_{n=N}^M|a_n'(z)|
\le
\frac1{2\pi\rho}
\int_{|w-z|=\rho}
\sum_{n=N}^M|a_n(w)|\,|dw|.
\]
Since $\sum |a_n|$ converges uniformly on $K_\rho$, its tails are uniformly
small there. Hence
\[
\sup_{z\in K}\sum_{n=N}^M|a_n'(z)|\to0
\qquad(N,M\to\infty).
\]
Thus $\sum |a_n'|$ is uniformly Cauchy, hence uniformly convergent, on $K$.
Since $K\Subset D$ was arbitrary, the conclusion holds on every bounded
closed subregion compactly contained in $D$.
:::
