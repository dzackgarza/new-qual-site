---
schema: qual/card@1
id: C-3S4XS
kind: corollary
title: Uniform limits of series of continuous functions are continuous
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Continuity
relations: []
review: draft
---

::: {.corollary}
Let $(X,d)$ be a metric space and let $f_n\colon X\to\CC$ be [[D-AEAAD|continuous]] for every $n\geq 1$.
If the partial sums $S_N\coloneqq\sum_{n=1}^N f_n$ [[D-YZC3C|converge uniformly]] on $X$ to a function $f\colon X\to\CC$, then $f$ is continuous.
:::

::: {.proof}
Each $S_N$ is a finite sum of continuous functions, hence continuous.
Fix $x_0\in X$ and $\varepsilon>0$.
Choose $N$ with $\abs{S_N(x)-f(x)}<\varepsilon/3$ for all $x\in X$, and then $\delta>0$ with $\abs{S_N(x)-S_N(x_0)}<\varepsilon/3$ whenever $d(x,x_0)<\delta$.
For such $x$,
$$
\abs{f(x)-f(x_0)}\leq\abs{f(x)-S_N(x)}+\abs{S_N(x)-S_N(x_0)}+\abs{S_N(x_0)-f(x_0)}<\varepsilon.
$$
:::
