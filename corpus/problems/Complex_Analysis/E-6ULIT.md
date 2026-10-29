---
schema: qual/card@1
id: E-6ULIT
kind: problem
title: Uniform limits preserve continuity and uniform continuity; pointwise limits
  need not
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Continuity
  - Uniform Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.exercise}
Show that a uniform limit of continuous functions is continuous, and a uniform limit of uniformly continuous functions is uniformly continuous.
Show that this is not true if uniform convergence is weakened to pointwise convergence.

:::

::: {.solution}
Let $f_n$ and $f$ be functions on a metric space $(X,d)$ with $\norm{f_n - f}_\infty\to 0$, and fix $\varepsilon>0$ and $n$ with $\norm{f-f_n}_\infty<\varepsilon/3$.

::: pf

::: {.pf-step #triangle}
For all $z,w\in X$, $\abs{f(z)-f(w)}<2\varepsilon/3+\abs{f_n(z)-f_n(w)}$.

::: pf-proof
By the triangle inequality,
$$
\abs{f(z) - f(w)} \leq \abs{f(z) - f_n(z)} + \abs{f_n(z) - f_n(w)} + \abs{f_n(w) - f(w)}
\leq 2\norm{f-f_n}_\infty+\abs{f_n(z) - f_n(w)}.
$$
:::

:::

::: pf-step
If each $f_n$ is continuous, then $f$ is continuous.

::: pf-proof
Fix $z$.
Since $f_n$ is continuous at $z$, there is $\delta>0$ with $\abs{f_n(z)-f_n(w)}<\varepsilon/3$ for $d(z,w)<\delta$, and then $\abs{f(z)-f(w)}<\varepsilon$ by step [](#triangle){.pf-ref}.
:::

:::

::: pf-step
If each $f_n$ is uniformly continuous, then $f$ is uniformly continuous.

::: pf-proof
There is $\delta>0$ with $\abs{f_n(z)-f_n(w)}<\varepsilon/3$ for all $z,w$ with $d(z,w)<\delta$, and then $\abs{f(z)-f(w)}<\varepsilon$ for all such $z,w$ by step [](#triangle){.pf-ref}.
The single index $n$ serves every point because the convergence is uniform; pointwise convergence gives an index depending on the point.
:::

:::

::: pf-step
Under pointwise convergence both conclusions fail.

::: pf-proof
On $[0,1]$, the uniformly continuous functions $f_n(x) \coloneqq x^n$ converge pointwise to the indicator function of $\theset{1}$, which is not continuous, hence not uniformly continuous.
:::

:::

:::

:::
