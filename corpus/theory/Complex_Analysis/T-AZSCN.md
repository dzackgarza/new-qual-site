---
schema: qual/card@1
id: T-AZSCN
kind: theorem
title: Weierstrass M-test
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
---

::: {.theorem}
Let $\Omega$ be a set, let $f_n\colon\Omega\to\CC$ for $n\in\NN$, and suppose there are real numbers $M_n$ with
$$
\sup_{x\in\Omega}\abs{f_n(x)}\le M_n\quad\text{for all }n,\qquad\sum_{n\in\NN}M_n<\infty.
$$
Then $f(x)\coloneqq\sum_{n\in\NN}f_n(x)$ converges absolutely and [[D-YZC3C|uniformly]] on $\Omega$.
If moreover $\Omega$ is a topological space and every $f_n$ is continuous, then $f$ is continuous, by the uniform limit theorem.
:::

::: {.proof}
For each $x$, $\sum_n\abs{f_n(x)}\le\sum_nM_n<\infty$, so the series converges absolutely.
For $N\ge1$ and all $x\in\Omega$,
$$
\abs{f(x)-\sum_{n\le N}f_n(x)}\le\sum_{n>N}M_n,
$$
and the right side is independent of $x$ and tends to $0$ as $N\to\infty$.
:::
