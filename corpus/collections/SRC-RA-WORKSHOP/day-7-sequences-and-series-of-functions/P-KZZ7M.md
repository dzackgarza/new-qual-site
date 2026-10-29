---
schema: qual/card@1
id: P-KZZ7M
kind: problem
title: $\lim_{n\to\infty}\int_{1/n}^1 f_n=\int_0^1 f$ for uniform limits of continuous
  functions on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Suppose $f_n:[0,1]\to\RR$ are continuous functions converging uniformly to $f:[0,1]\to\RR$.
Either prove that $\displaystyle\lim_{n\to\infty}\int_{1/n}^1 f_n(x)\,dx=\int_0^1 f(x)\,dx$ or give a counterexample.
:::

::: {.solution}

The statement is true.

::: pf

::: {.pf-step #s2}

$\int_{1/n}^1 (f_n - f) \to 0$.

::: pf-proof

Uniform convergence $f_n \to f$ means $\norm{f_n - f}_\infty \to 0$, and the interval $[1/n,1]$ has length at most $1$, so $\abs{\int_{1/n}^1 (f_n - f)} \le \norm{f_n - f}_\infty \to 0$.

:::

:::

::: {.pf-step #s3}

$\int_{1/n}^1 f \to \int_0^1 f$.

::: pf-proof

$f$ is continuous on $[0,1]$, as a uniform limit of continuous functions, hence bounded: $\abs{f} \le M$. Then $\abs{\int_0^{1/n} f} \le M/n \to 0$, so $\int_{1/n}^1 f = \int_0^1 f - \int_0^{1/n} f \to \int_0^1 f$.

:::

:::

::: pf-step

$\lim_{n\to\infty}\int_{1/n}^1 f_n(x)\,dx = \int_0^1 f(x)\,dx$.

::: pf-proof

Write $\int_{1/n}^1 f_n = \int_{1/n}^1 f + \int_{1/n}^1 (f_n - f)$. The first term tends to $\int_0^1 f$ by step [](#s3){.pf-ref}, and the second tends to $0$ by step [](#s2){.pf-ref}.

:::

:::

:::

:::
