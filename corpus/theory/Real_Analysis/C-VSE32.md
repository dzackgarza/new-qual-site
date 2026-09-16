---
schema: qual/card@1
id: C-VSE32
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
Let $(X,d)$ be a metric space, let $f_n\colon X\to\CC$ be [[D-AEAAD|continuous]] for every $n\geq 1$, and let $F\colon X\to\CC$.
If
$$
\norm{\sum_{n=1}^N f_n - F}_\infty \coloneqq \sup_{x\in X}\abs{\sum_{n=1}^N f_n(x) - F(x)} \xrightarrow{N\to\infty} 0,
$$
then $F$ is continuous.
:::

::: {.proof}
The partial sums $S_N\coloneqq\sum_{n=1}^N f_n$ are continuous and [[D-YZC3C|converge uniformly]] to $F$.
Fix $x_0\in X$ and $\varepsilon>0$, choose $N$ with $\norm{S_N-F}_\infty<\varepsilon/3$, and choose $\delta>0$ with $\abs{S_N(x)-S_N(x_0)}<\varepsilon/3$ whenever $d(x,x_0)<\delta$.
For such $x$, the triangle inequality gives $\abs{F(x)-F(x_0)}<\varepsilon$.
:::
