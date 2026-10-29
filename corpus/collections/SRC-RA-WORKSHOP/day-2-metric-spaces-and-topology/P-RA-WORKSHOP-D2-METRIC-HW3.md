---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-HW3
kind: problem
title: Uncountability of the set of binary sequences
classification:
  areas:
  - real-analysis
  topics:
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Is the set of all sequences $x_1,x_2,\ldots$ with $x_i\in\{0,1\}$ for $i=1,2,\ldots$ countable?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

No map $f:\NN\to\{0,1\}^{\NN}$ is surjective.

::: pf-proof

Write $f(n)=(x^{(n)}_k)_{k\geq1}$ and set $y=(1-x^{(n)}_n)_{n\geq1}$. Each $x^{(n)}_n$ belongs to $\{0,1\}$, so the coordinate $y_n=1-x^{(n)}_n$ also belongs to $\{0,1\}$, and $y\in\{0,1\}^{\NN}$. Moreover $y_n\ne x^{(n)}_n$, hence $y\ne f(n)$ for every $n\in\NN$, and $y$ is not in the image of $f$.

:::

:::

::: pf-qed

A nonempty set is countable exactly when it is the image of a map from $\NN$. The set $\{0,1\}^{\NN}$ is nonempty, so by step [](#s1){.pf-ref} it is not countable: $\boxed{\text{the set of binary sequences is uncountable}}$.

:::

:::

:::
