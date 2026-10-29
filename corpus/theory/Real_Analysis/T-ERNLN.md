---
schema: qual/card@1
id: T-ERNLN
kind: theorem
title: Uniform limit theorem
slogan: 'Uniform convergence preserves continuity.'
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuity
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a topological space, and let $f_n\colon X\to\CC$ for $n\geq1$ and $f\colon X\to\CC$ be functions.
If each $f_n$ is [[D-AEAAD|continuous]] and $f_n\to f$ [[D-YZC3C|uniformly]] on $X$, then $f$ is continuous.
:::

::: {.proof}
Fix $x_0\in X$ and $\varepsilon>0$.
Choose $n$ with $\abs{f_n(x)-f(x)}<\varepsilon/3$ for all $x\in X$, and then a neighborhood $U$ of $x_0$ with $\abs{f_n(x)-f_n(x_0)}<\varepsilon/3$ for all $x\in U$.
For $x\in U$,
$$
\abs{f(x)-f(x_0)}\leq\abs{f(x)-f_n(x)}+\abs{f_n(x)-f_n(x_0)}+\abs{f_n(x_0)-f(x_0)}<\varepsilon .
$$
:::

::: {.remark title="Series"}
If each $f_n$ is continuous and the partial sums $S_N\coloneqq\sum_{n=1}^N f_n$ converge uniformly on $X$ to $f$, then $f$ is continuous: each $S_N$ is a finite sum of continuous functions, hence continuous, and the theorem applies to $(S_N)$.
:::
