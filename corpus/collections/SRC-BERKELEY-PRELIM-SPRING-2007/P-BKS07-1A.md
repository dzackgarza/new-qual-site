---
schema: qual/card@1
id: P-BKS07-1A
kind: problem
title: A sequence whose every subsequence has a subsequence tending to $0$ converges to $0$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Let $x_{1}, x_{2}, \ldots$ be an infinite sequence of real numbers such that every subsequence contains a subsequence converging to $0$. Must the original sequence converge?
:::

::: {.solution}

Yes. The sequence converges to $0$.

::: pf

::: {.pf-step #s1}

Suppose that $x_n\not\to0$. Then there is a subsequence $S$ of $(x_n)$ and an $\varepsilon>0$ with $\abs{s}>\varepsilon$ for every term $s$ of $S$.

::: pf-proof

By the negation of convergence to $0$, there is $\varepsilon>0$ with $\abs{x_n}>\varepsilon$ for infinitely many $n$. Let $S$ list these terms in order.

:::

:::

::: pf-qed

Every subsequence of the sequence $S$ of step [](#s1){.pf-ref} has all its terms of absolute value greater than $\varepsilon$, so it does not converge to $0$. This contradicts the hypothesis applied to $S$. Hence $x_n\to0$.

:::

:::

:::
