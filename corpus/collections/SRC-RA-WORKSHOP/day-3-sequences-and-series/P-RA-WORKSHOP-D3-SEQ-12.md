---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-12
kind: problem
title: A bounded positive multiplier preserves convergence of a positive series
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Sequences of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(January 2012 #1a) Let $\{a_n\}$, $\{b_n\}$ be bounded sequences of positive real numbers.
If $\sum b_n$ is convergent, show that $\sum a_nb_n$ is also convergent.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There exists $M>0$ such that $0\leq a_nb_n\leq Mb_n$ for every $n$.

::: pf-proof

Boundedness of the positive sequence $(a_n)$ supplies $M>0$ with $a_n\leq M$ for all $n$. Multiply this inequality by the positive number $b_n$.

:::

:::

::: pf-step

The series $\sum_n a_nb_n$ converges.

::: pf-proof

For every $N$, step [](#s1){.pf-ref} yields
$$
0\leq\sum_{n=1}^N a_nb_n\leq M\sum_{n=1}^N b_n.
$$
The right-hand partial sums are bounded because $\sum_n b_n$ converges. The left-hand partial sums are nondecreasing and bounded, hence converge in $\RR$.

:::

:::

:::

:::
