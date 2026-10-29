---
schema: qual/card@1
id: P-YFBBW
kind: problem
title: A continuous $f:\RR\to\RR$ vanishing at $\pm\infty$ is uniformly continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
relations: []
review: draft
---

::: {.problem}
Suppose $f:\RR\to\RR$ is continuous and $\lim_{x\to \pm \infty} f(x) = 0$.
Prove that $f$ is uniformly continuous.
:::

::: {.solution}
Fix $\varepsilon>0$.

::: pf

::: {.pf-step #tail}
There is $M>0$ such that $\abs{f(x)-f(y)}<\varepsilon$ whenever $\abs{x},\abs{y}\ge M$.

::: pf-proof
Since $f(x)\to0$ as $x\to\pm\infty$, choose $M$ with $\abs{f(x)}<\varepsilon/2$ for $\abs{x}\ge M$; then $\abs{f(x)-f(y)}\le\abs{f(x)}+\abs{f(y)}<\varepsilon$.
:::

:::

::: {.pf-step #compact}
There is $\delta_0>0$ such that $\abs{f(x)-f(y)}<\varepsilon$ whenever $x,y\in[-M-1,M+1]$ and $\abs{x-y}<\delta_0$.

::: pf-proof
A continuous function on a compact interval is uniformly continuous.
:::

:::

::: pf-step
With $\delta=\min(\delta_0,1)$, $\abs{x-y}<\delta$ implies $\abs{f(x)-f(y)}<\varepsilon$.

::: pf-proof
If $x,y\in[-M-1,M+1]$, apply step [](#compact){.pf-ref}.
Otherwise one of them, say $x$, has $\abs{x}>M+1$, and then $\abs{y}>\abs{x}-1>M$; apply step [](#tail){.pf-ref}.
:::

:::

:::

:::
