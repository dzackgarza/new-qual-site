---
schema: qual/card@1
id: E-OUBBQ
kind: problem
title: Uniform continuity of $x^n$
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
For $n\geq1$, show that $f(x)=x^n$ is uniformly continuous on any interval $[-M,M]$.
:::

::: {.solution}

::: pf

::: {.pf-step #lipschitz}
For $x,y\in[-M,M]$, $\abs{x^n-y^n}\leq nM^{n-1}\abs{x-y}$.

::: pf-proof
Factor and bound each of the $n$ terms by $M^{n-1}$:
$$
\abs{x^n-y^n}=\abs{x-y}\abs{\sum_{k=0}^{n-1}x^{n-1-k}y^k}\leq nM^{n-1}\abs{x-y}.
$$
:::

:::

::: pf-step
$f$ is uniformly continuous on $[-M,M]$.

::: pf-proof
If $M=0$ the interval is a point.
If $M>0$, given $\varepsilon>0$ take $\delta=\varepsilon/(nM^{n-1})$; by step [](#lipschitz){.pf-ref}, $\abs{x-y}<\delta$ implies $\abs{x^n-y^n}<\varepsilon$.
:::

:::

:::

:::
