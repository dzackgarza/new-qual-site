---
schema: qual/card@1
id: P-P2W6W
kind: problem
title: A continuous function vanishing at $\pm\infty$ is uniformly continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Suppose $f: \RR \to \RR$ is continuous and $\lim_{x \to \pm \infty} f(x) = 0$.
Prove that $f$ is uniformly continuous on $\RR$.
:::

::: {.solution}
Fix $\varepsilon>0$.

::: pf

::: {.pf-step #tail}

There is $M>0$ such that $\abs{f(x)}<\varepsilon/2$ whenever $\abs{x}\ge M$.

::: pf-proof

This is the hypothesis $\lim_{x\to\pm\infty}f(x)=0$.

:::

:::

::: {.pf-step #compact}

There is $\delta_0>0$ such that $\abs{f(x)-f(y)}<\varepsilon$ whenever $x,y\in[-M-1,M+1]$ and $\abs{x-y}<\delta_0$.

::: pf-proof

By the Heine--Cantor theorem, $f$ is uniformly continuous on the compact interval $[-M-1,M+1]$.

:::

:::

::: pf-step

With $\delta\coloneqq\min\{1,\delta_0\}$, every $x,y\in\RR$ with $\abs{x-y}<\delta$ satisfy $\abs{f(x)-f(y)}<\varepsilon$; hence $f$ is uniformly continuous on $\RR$.

::: pf-proof

::: pf-step

If $x,y\in[-M-1,M+1]$, then $\abs{f(x)-f(y)}<\varepsilon$.

::: pf-proof

This is step [](#compact){.pf-ref}, since $\delta\le\delta_0$.

:::

:::

::: pf-step

If $x$ or $y$ lies outside $[-M-1,M+1]$, then $\abs{f(x)-f(y)}<\varepsilon$.

::: pf-proof

By symmetry suppose $\abs{x}>M+1$. Since $\abs{x-y}<1$, we have $\abs{y}>M$. Step [](#tail){.pf-ref} gives
$$
\abs{f(x)-f(y)}\le\abs{f(x)}+\abs{f(y)}<\varepsilon.
$$

:::

:::

:::

:::

:::

:::
