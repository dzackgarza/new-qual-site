---
schema: qual/card@1
id: E-C5QHZ
kind: problem
title: Uniformly bounded derivatives imply equicontinuity
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Normal Families
relations: []
review: draft
---

::: {.exercise}
Let $\mcf$ be a family of differentiable functions $f:[0,1]\to\CC$ such that
$$
\abs{f'(x)}\le M
$$
for every $f\in\mcf$ and every $x\in[0,1]$, for one constant $M$ independent of $f$.
Show that $\mcf$ is equicontinuous.
:::

::: {.hint}
Apply the mean value inequality.
:::

::: {.solution}

::: pf

::: {.pf-step #lipschitz}
For every $f\in\mcf$ and $x,y\in[0,1]$,
$$
\abs{f(x)-f(y)}\le M\abs{x-y}.
$$

::: pf-proof
This is the mean value inequality for a differentiable function on $[0,1]$ with $\abs{f'}\le M$.
:::

:::

::: pf-step
$\mcf$ is equicontinuous.

::: pf-proof
Let $\varepsilon>0$. If $M>0$, take $\delta=\varepsilon/M$; if $M=0$, take any $\delta>0$.
By step [](#lipschitz){.pf-ref}, $\abs{x-y}<\delta$ implies $\abs{f(x)-f(y)}<\varepsilon$ for every $f\in\mcf$.
The number $\delta$ does not depend on $f$, $x$, or $y$.
:::

:::

:::

:::
