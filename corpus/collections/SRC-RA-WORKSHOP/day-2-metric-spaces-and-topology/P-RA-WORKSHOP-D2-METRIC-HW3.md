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

Assume that the set $\{0,1\}^{\mathbb N}$ is countable, and choose a surjection $f:\mathbb N\to\{0,1\}^{\mathbb N}$.

::: pf-proof

The set is nonempty. Under the assumed countability it admits an enumeration, with repetitions permitted. Write $f(n)=(x^{(n)}_k)_{k\geq1}$.

:::

:::

::: {.pf-step #s2}

The sequence $y=(1-x^{(n)}_n)_{n\geq1}$ belongs to $\{0,1\}^{\mathbb N}$ but is unequal to $f(n)$ for every $n\in\mathbb N$.

::: pf-proof

Each $x^{(n)}_n$ belongs to $\{0,1\}$, so the coordinate $y_n=1-x^{(n)}_n$ also belongs to $\{0,1\}$. Moreover $y_n\ne x^{(n)}_n$, hence $y\ne f(n)$ for every $n$. This contradicts surjectivity of $f$ in step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

The contradiction between steps [](#s1){.pf-ref} and [](#s2){.pf-ref} proves that the set of binary sequences is uncountable.

:::

:::

:::
