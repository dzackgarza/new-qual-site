---
schema: qual/card@1
id: E-EMISN
kind: problem
title: Power series are continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Continuity
  - Uniform Convergence
relations: []
review: draft
---

::: {.exercise}
Show that any power series is continuous on its domain of convergence.
:::

::: {.solution}
Let $f(z) = \lim_{N\to\infty} S_N(z)$ with $S_N(z)=\sum_{k\leq N} c_k (z-z_0)^k$, and let $R>0$ be the radius of convergence. The domain of convergence is the open disk $\abs{z-z_0}<R$, the interior of the set where the series converges.
For $0<r<R$, the series converges absolutely and uniformly on the closed disk $\abs{z-z_0}\le r$ (Weierstrass $M$-test with $M_k=\abs{c_k}r^k$, which is summable since $r<R$).
Each partial sum $S_N$ is a polynomial, hence continuous, so $f$ is continuous on $\abs{z-z_0}\le r$ by the uniform limit theorem.
Every point of the open disk $\abs{z-z_0}<R$ lies in such a closed disk, so $f$ is continuous on the open disk of convergence.
:::
