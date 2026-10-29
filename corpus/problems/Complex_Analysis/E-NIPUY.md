---
schema: qual/card@1
id: E-NIPUY
kind: problem
title: Uniform continuity of $x^{-n}$ near $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source claims that f(x)=x^{-n}, n in Z_{>=0}, is uniformly continuous on [0,infinity), which is false for n>=1. The previous statement reported that claim and asked where it fails; the statement now asks the question directly.
---

::: {.problem}
Let $n\in\ZZ_{\geq0}$ and $f(x)=x^{-n}$.
Determine for which $n$ the function $f$ is uniformly continuous on $[0,\infty)$, and for the remaining $n$ decide whether $f$ is uniformly continuous on $(0,\infty)$.
:::

::: {.solution}
::: pf

::: pf-step
For $n=0$, $f\equiv1$ is uniformly continuous on $[0,\infty)$.
:::

::: pf-step
For $n\ge1$, $f$ is not defined at $0$, and it is not uniformly continuous on $(0,\infty)$.

::: pf-proof
Take $x_k=\frac1k$ and $y_k=\frac1{k+1}$. Then $\abs{x_k-y_k}=\frac1{k(k+1)}\to0$, while $\abs{f(x_k)-f(y_k)}=(k+1)^n-k^n\ge1$ for every $k$.
:::

:::

:::

:::
