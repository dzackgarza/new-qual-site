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
Let $(f_n)$ and $f$ be holomorphic on $\DD$. Prove that the following are
equivalent:
(a) $f_n\to f$ uniformly on compact subsets of $\DD$;
(b) for every $0<r<1$,
\[
\int_{|z|=r}|f_n(z)-f(z)|\,|dz|\longrightarrow0.
\]
:::

::: {.solution}
If $f_n\to f$ uniformly on compact sets, then on $|z|=r$,
\[
\int_{|z|=r}|f_n-f|\,|dz|
\le2\pi r\sup_{|z|=r}|f_n-f|\to0.
\]
Conversely, fix $0<\rho<1$ and choose $r$ with $\rho<r<1$. Cauchy's
formula applied to $f_n-f$ gives, for $|z|\le\rho$,
\[
|f_n(z)-f(z)|
\le\frac1{2\pi(r-\rho)}
\int_{|\zeta|=r}|f_n(\zeta)-f(\zeta)|\,|d\zeta|.
\]
The right side tends to zero, uniformly for $|z|\le\rho$. Every compact
subset of $\DD$ lies in such a disk, proving (a).
:::