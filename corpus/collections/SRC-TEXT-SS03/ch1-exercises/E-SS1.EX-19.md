---
schema: qual/card@1
id: E-SS1.EX-19
kind: problem
title: Convergence of $\sum kz^k$, $\sum z^k/k^2$, and $\sum z^k/k$ on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
  - Series of Functions
relations: []
review: draft
---

::: {.exercise}
Show that

1. $\sum kz^k$ diverges on $S^1$.

2. $\sum k^{-2} z^k$ converges on $S^1$.

3. $\sum \inverseof{k} z^k$ converges on $S^1\sm\ts{1}$ and diverges at $1$.
:::

::: {.solution}

::: pf

::: pf-step

(1) $\sum kz^k$ diverges at every $z\in S^1$.

::: pf-proof

The terms of a convergent series tend to $0$, but $\abs{kz^k} = k \to \infty$ for $\abs z=1$.

:::

:::

::: pf-step

(2) $\sum k^{-2} z^k$ converges at every $z\in S^1$.

::: pf-proof

For $\abs z=1$, $\sum \abs{k^{-2} z^k} = \sum k^{-2}$ converges by the $p$-test, and an absolutely convergent series converges.

:::

:::

::: pf-step

(3) $\sum k^{-1} z^k$ diverges at $z=1$ and converges at every $z\in S^1\setminus\{1\}$.

::: pf-proof

At $z=1$ the series is the harmonic series.
Otherwise $z = e^{i\theta}$ with $\theta \in (0, 2\pi)$.
The partial sums of $\sum e^{ik\theta}$ are bounded, since the geometric sum formula gives $$\abs{\sum_{k=0}^{m} e^{ik\theta}} = \abs{\frac{1 - e^{i(m+1)\theta}}{1 - e^{i\theta}}} \leq \frac{2}{\abs{1- e^{i\theta}}}$$ for every $m$, using $\abs{1 - e^{i(m+1)\theta}}\le2$.
The coefficients $1/k$ decrease monotonically to $0$, so Dirichlet's test gives convergence.

:::

:::

:::

:::
