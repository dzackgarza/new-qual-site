---
schema: qual/card@1
id: P-DFDX4
kind: problem
title: Power series $\sum a_n x^n$ and $\sum b_n x^n$ with radii of convergence $R_1$
  and $R_2$
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let the power series series $\sum_{n=0}^\infty a_nx^n$ and $\sum_{n=0}^\infty b_nx^n$ have radii of convergence $R_1$ and $R_2$, respectively.
:::
::: {.solution}

::: pf

::: pf-step

Cauchy–Hadamard formula: the radius of convergence of $\sum a_n x^n$ is $R = 1/\limsup_{n \to \infty} |a_n|^{1/n}$ (with $1/0 = \infty$, $1/\infty = 0$).

::: pf-proof

By the root test, since $\limsup |a_n x^n|^{1/n} = |x| \limsup |a_n|^{1/n}$, the series converges absolutely when $|x| < R$ and diverges when $|x| > R$, because then its terms do not tend to $0$.

:::

:::

::: pf-step

If $R_1 \neq R_2$, the radius of convergence of $\sum (a_n + b_n) x^n$ is $\min\{R_1, R_2\}$, and in general it is at least $\min\{R_1, R_2\}$. See [[P-E4WZN]].

:::

::: pf-step

The radius of convergence of $\sum a_n b_n x^n$ is at least $R_1 R_2$. See [[P-FYGQ6]].

:::

:::

:::
