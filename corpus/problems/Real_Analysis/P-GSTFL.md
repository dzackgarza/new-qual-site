---
schema: qual/card@1
id: P-GSTFL
kind: problem
title: Uniformly continuous functions preserve uniform convergence of sequences
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Uniform Continuity
relations: []
review: draft
---

::: {.problem}
Suppose $\theset{g_n}$ is a uniformly convergent sequence of functions from $\RR$ to $\RR$ and $f:\RR\to \RR$ is uniformly continuous.
Prove that the sequence $\theset{f\circ g_n}$ is uniformly convergent.
:::

::: {.solution}
Let $g_n\to g$ uniformly on $\RR$.

::: pf

::: {.pf-step #delta}
Fix $\varepsilon>0$. There is $\delta>0$ with $\abs{f(x)-f(y)}<\varepsilon$ whenever $\abs{x-y}<\delta$.

::: pf-proof
This is the uniform continuity of $f$.
:::

:::

::: {.pf-step #N}
There is $N$ with $\sup_{x\in\RR}\abs{g_n(x)-g(x)}<\delta$ for all $n\ge N$.

::: pf-proof
This is the uniform convergence of $g_n$ to $g$.
:::

:::

::: pf-step
$f\circ g_n\to f\circ g$ uniformly on $\RR$.

::: pf-proof
For $n\ge N$ and $x\in\RR$, step [](#N){.pf-ref} gives $\abs{g_n(x)-g(x)}<\delta$, so step [](#delta){.pf-ref} gives $\abs{f(g_n(x))-f(g(x))}<\varepsilon$. Hence $\sup_{x}\abs{f(g_n(x))-f(g(x))}\le\varepsilon$ for $n\ge N$.
:::

:::

:::

:::
