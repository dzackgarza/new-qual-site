---
schema: qual/card@1
id: E-ZWNTH
kind: problem
title: Convergence of $\sum \sin(n)/n$ by summation by parts
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

:::

:::
