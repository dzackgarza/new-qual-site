---
schema: qual/card@1
id: E-ORJPT
kind: problem
title: Convergence of $\prod_{n\in\ZZ}(1+a_n)$ when $\{a_n\}\in\ell_1(\ZZ)$
classification:
  areas:
  - complex-analysis
  topics:
  - Weierstrass Factorization
  - Convergence Tests
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "Show that the product of (1 + a_n) over n in Z is < infinity"; for complex a_n an inequality is meaningless, so the statement asks that the product converge.'
---

::: {.exercise}
Show that $\prod_{n\in \ZZ} (1 + a_n)$ converges if $\theset{a_n} \in \ell_1(\ZZ)$.
:::

::: {.solution}

Here $\prod_{n\in\ZZ}(1+a_n)$ converges if the partial products $P_N \coloneqq \prod_{\abs{n}\leq N}(1+a_n)$ converge as $N\to\infty$, and $\log$ is the principal branch on $\abs{w-1}<1$.

::: pf

::: {.pf-step #tail}
There is an $N_0$ with $\abs{a_n}\leq 1/2$ for all $\abs{n}>N_0$.

::: pf-proof
$\sum_{n\in\ZZ}\abs{a_n}<\infty$, so $a_n\to0$ as $\abs{n}\to\infty$.
:::

:::

::: {.pf-step #log-bound}
For $\abs{w}\leq 1/2$, $\abs{\log(1+w)}\leq 2\abs{w}$.

::: pf-proof
$\abs{\log(1+w)} = \abs{\sum_{j\geq1}\frac{(-1)^{j+1}w^j}{j}}\leq \abs{w}\sum_{j\geq0}2^{-j} = 2\abs{w}$.
:::

:::

::: pf-step
The product converges, and its value is $0$ only if some factor $1+a_n$ is $0$.

::: pf-proof
By steps [](#tail){.pf-ref} and [](#log-bound){.pf-ref}, $\sum_{\abs{n}>N_0}\abs{\log(1+a_n)}\leq 2\sum_{n}\abs{a_n}<\infty$, so the symmetric partial sums $S_N \coloneqq \sum_{N_0<\abs{n}\leq N}\log(1+a_n)$ converge to some $S\in\CC$.
For $N>N_0$, $P_N = \prod_{\abs{n}\leq N_0}(1+a_n)\cdot e^{S_N}$, which converges to $\prod_{\abs{n}\leq N_0}(1+a_n)\cdot e^{S}$ by continuity of $\exp$.
Since $e^S\neq0$, this limit is $0$ only if one of the finitely many factors $1+a_n$ with $\abs{n}\leq N_0$ vanishes.
:::

:::

:::

:::
