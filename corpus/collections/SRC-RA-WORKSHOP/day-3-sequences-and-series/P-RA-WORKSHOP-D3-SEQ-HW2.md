---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW2
kind: problem
title: A limit point is the limit of a sequence from the set
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
  - Sequences of Numbers
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
If $X$ is a metric space, $E\subset X$, and $x$ is a limit point of $E$, then there exists a sequence $\{x_n\}\subset E$ which converges to $x$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every positive integer $n$, there exists $x_n\in E\setminus\{x\}$ with $d(x_n,x)<1/n$.

::: pf-proof

As $x$ is a limit point of $E$, every punctured neighborhood of $x$ intersects $E$. Apply this condition to the open ball $B(x,1/n)$, and choose such a point for each $n$.

:::

:::

::: {.pf-step #s2}

The sequence $(x_n)_{n\geq1}$ converges to $x$.

::: pf-proof

Given $\varepsilon>0$, choose $N\geq1$ such that $1/N<\varepsilon$. For every $n\geq N$, step [](#s1){.pf-ref} yields
\[
d(x_n,x)<\frac1n\leq\frac1N<\varepsilon.
\]
This is the definition of convergence in a metric space.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} constructs a sequence in $E$, and step [](#s2){.pf-ref} establishes its convergence to $x$.

:::

:::

:::
