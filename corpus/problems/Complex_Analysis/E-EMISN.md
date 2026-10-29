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
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "on its domain of convergence", which can include boundary points of the disk of convergence where continuity is not the intended claim; the statement now names the open disk of convergence, as the solution reads it.'
---

::: {.exercise}
Show that any power series with positive radius of convergence is continuous on its open disk of convergence.
:::

::: {.solution}
Let $f(z)=\sum_{k\geq0}c_k(z-z_0)^k$ have radius of convergence $R\in(0,\infty]$, and let $S_N(z)=\sum_{k\leq N} c_k (z-z_0)^k$.

::: pf

::: {.pf-step #uniform}
For $0<r<R$, $S_N\to f$ uniformly on the closed disk $\abs{z-z_0}\le r$.

::: pf-proof
On this disk $\abs{c_k(z-z_0)^k}\le\abs{c_k}r^k$, and $\sum_k\abs{c_k}r^k$ converges because $r<R$. The Weierstrass $M$-test gives uniform convergence.
:::

:::

::: pf-step
$f$ is continuous on $\abs{z-z_0}<R$.

::: pf-proof
Each $S_N$ is a polynomial, hence continuous, so by step [](#uniform){.pf-ref} and the uniform limit theorem $f$ is continuous on $\abs{z-z_0}\le r$ for every $r<R$.
Every point of the open disk lies in the interior of such a closed disk.
:::

:::

:::

:::
