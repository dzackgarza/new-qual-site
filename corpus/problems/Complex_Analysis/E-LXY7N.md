---
schema: qual/card@1
id: E-LXY7N
kind: problem
title: A non-equicontinuous sequence
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Counterexamples
  - Sequences of Functions
relations: []
review: draft
---

::: {.exercise}
Exhibit a sequence of functions that is not equicontinuous.
:::

::: {.solution}
::: pf

::: pf-step
The sequence $f_k(x)=x^k$ on $[0,1]$ is not equicontinuous at $x=1$.

::: pf-proof
Take $\varepsilon=\frac12$. For every $\delta>0$ choose $x_0\in(1-\delta,1)$. Since $x_0^k\to0$, for large $k$ we have $\abs{f_k(x_0)-f_k(1)}=1-x_0^k>\frac12$, although $\abs{x_0-1}<\delta$.
:::

:::

:::

:::
