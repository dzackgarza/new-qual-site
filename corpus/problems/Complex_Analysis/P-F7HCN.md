---
schema: qual/card@1
id: P-F7HCN
kind: problem
title: Convergence of $\sum nz^n$, $\sum z^n/n^2$, and $\sum z^n/n$ on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Prove the following:

(a) $\sum_{n} nz^n$ does not converge at any point of $S^1$.

(b) $\sum_n {z^n \over n^2}$ converges at every point of $S^1$.

(c) $\sum_n {z^n \over n}$ converges at every point of $S^1$ except $z=1$.
:::

::: {.solution}
::: pf

::: pf-step
(a) For $\abs z = 1$, the series $\sum_n nz^n$ diverges.

::: pf-proof
$\abs{n z^n} = n \to \infty$, so the terms do not tend to $0$, and a series whose terms do not tend to $0$ diverges.
:::

:::

::: pf-step
(b) $\sum_n \frac{z^n}{n^2}$ converges absolutely at every point of $S^1$.

::: pf-proof
For $\abs z = 1$ we have $\abs{z^n/n^2} = 1/n^2$, and $\sum_n 1/n^2$ converges.
By the comparison test the series converges absolutely, hence converges.
:::

:::

::: pf-step
(c) $\sum_n \frac{z^n}{n}$ diverges at $z=1$ and converges at every $z\in S^1\setminus\theset{1}$.

::: pf-proof

::: pf-step
At $z = 1$ the series diverges.

::: pf-proof
It is the harmonic series.
:::

:::

::: {.pf-step #partial-sums-bounded}
For $z \in S^1 \setminus \theset{1}$, the partial sums $A_N \coloneqq \sum_{n=1}^{N} z^n$ are bounded.

::: pf-proof
By the geometric sum, $A_N = \frac{z - z^{N+1}}{1 - z}$, so $\abs{A_N} \leq \frac{2}{\abs{1 - z}}$ for every $N$.
:::

:::

::: pf-step
For $z \in S^1 \setminus \theset{1}$ the series converges.

::: pf-proof
Dirichlet's test states that $\sum a_n b_n$ converges if the partial sums of $\sum a_n$ are bounded and $b_n$ decreases to $0$.
Take $a_n = z^n$ and $b_n = 1/n$, and use step [](#partial-sums-bounded){.pf-ref}.
:::

:::

:::

:::

:::

:::
