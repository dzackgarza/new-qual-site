---
schema: qual/card@1
id: E-ISFYB
kind: problem
title: A sequence with uniformly bounded derivatives on $[0,1]$ is equicontinuous
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Mean Value Theorem
  - Sequences of Functions
relations: []
review: draft
---

::: {.exercise}
Let $f_k:[0,1]\to\CC$ be differentiable and suppose
$$
\abs{f_k'(x)}\le M
$$
for every $k$ and every $x\in[0,1]$, where $M$ is independent of $k$.
Show that $\theset{f_k}$ is equicontinuous.
:::

::: {.hint}
Use the mean value theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #lipschitz}
$\abs{f_k(x)-f_k(y)}\le M\abs{x-y}$ for all $x,y\in[0,1]$ and all $k$.

::: pf-proof
This is the mean value inequality for the differentiable function $f_k$ with $\abs{f_k'}\le M$.
:::

:::

::: pf-step
$\theset{f_k}$ is equicontinuous.

::: pf-proof
Given $\varepsilon>0$, let $\delta\coloneqq\varepsilon/(M+1)$.
By step [](#lipschitz){.pf-ref}, $\abs{x-y}<\delta$ implies $\abs{f_k(x)-f_k(y)}\le M\delta<\varepsilon$ for every $k$.
:::

:::

:::

:::
