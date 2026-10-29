---
schema: qual/card@1
id: E-ZWNTH
kind: problem
title: Series convergence on the circle by summation by parts
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
Use summation by parts to show that $\sum \sin(n)/n$ converges.
:::

::: {.exercise}
Show that

(a) $\sum kz^k$ diverges on $S^1$.

(b) $\sum k^{-2} z^k$ converges on $S^1$.

(c) $\sum \inverseof{k} z^k$ converges on $S^1\sm\theset{1}$ and diverges at $1$.
:::

::: {.solution}

Dirichlet's test, which is summation by parts, states: if $a_k$ decreases to $0$ and the partial sums of $\sum b_k$ are bounded, then $\sum a_kb_k$ converges.

::: pf

::: {.pf-step #geometric-bound}
For $\theta\in(0,2\pi)$ and every $m$, $\abs{\sum_{k=1}^m e^{ik\theta}}\leq \dfrac{2}{\abs{1-e^{i\theta}}}$.

::: pf-proof
Summing the geometric series, $\sum_{k=1}^m e^{ik\theta} = e^{i\theta}\dfrac{1-e^{im\theta}}{1-e^{i\theta}}$, and $\abs{1-e^{im\theta}}\leq 2$.
:::

:::

::: pf-step
$\sum \sin(n)/n$ converges.

::: pf-proof
Take $a_n=1/n$ and $b_n=\sin n = \Im e^{in}$.
By step [](#geometric-bound){.pf-ref} with $\theta=1$, the partial sums of $\sum b_n$ are bounded by $2/\abs{1-e^{i}}$, so Dirichlet's test applies.
:::

:::

::: pf-step
(a) $\sum kz^k$ diverges at every $z\in S^1$.

::: pf-proof
For $\abs{z}=1$, $\abs{kz^k}=k\not\to 0$, and the terms of a convergent series tend to $0$.
:::

:::

::: pf-step
(b) $\sum k^{-2} z^k$ converges at every $z\in S^1$.

::: pf-proof
For $\abs{z}=1$, $\sum \abs{k^{-2} z^k} = \sum k^{-2}$ converges by the $p$-test, and absolute convergence implies convergence.
:::

:::

::: pf-step
(c) $\sum \inverseof{k} z^k$ diverges at $z=1$ and converges at every $z\in S^1\sm\theset{1}$.

::: pf-proof
At $z=1$ the series is the harmonic series, which diverges.
For $z=e^{i\theta}$ with $\theta\in(0,2\pi)$, take $a_k=1/k$ and $b_k=e^{ik\theta}$; the partial sums of $\sum b_k$ are bounded by step [](#geometric-bound){.pf-ref}, so Dirichlet's test applies.
:::

:::

:::

:::
