---
schema: qual/card@1
id: D-RA-WORKSHOP-D7-CONVERGENCE
kind: definition
title: Pointwise and uniform convergence of function sequences and series
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
  - Sequences of Functions
  - Series of Functions
relations: []
review: draft
---

::: {.definition}
Let $E$ be a set, and let $f_n\colon E\to\RR$ for $n\geq 1$ and $f\colon E\to\RR$ be functions.

1. $f_n\to f$ \dfn{pointwise} on $E$ if $\lim_{n\to\infty}f_n(x)=f(x)$ for each $x\in E$.

2. $f_n\to f$ \dfn{uniformly} on $E$ if for every $\varepsilon>0$ there exists $N\in\NN$ such that $\abs{f_n(x)-f(x)}<\varepsilon$ for all $n\geq N$ and all $x\in E$.

3. $\sum_{n=1}^{\infty}f_n=f$ \dfn{pointwise} on $E$ if the partial sums $\sum_{n=1}^{N}f_n$ converge pointwise to $f$ as $N\to\infty$.

4. $\sum_{n=1}^{\infty}f_n=f$ \dfn{uniformly} on $E$ if the partial sums $\sum_{n=1}^{N}f_n$ converge uniformly to $f$ as $N\to\infty$.
:::

::: {.remark}
With the supremum norm $\norm{g}_\infty\coloneqq\sup_{x\in E}\abs{g(x)}$ for $g\colon E\to\RR$, condition (2) holds if and only if $\norm{f_n-f}_\infty\to 0$.
:::
