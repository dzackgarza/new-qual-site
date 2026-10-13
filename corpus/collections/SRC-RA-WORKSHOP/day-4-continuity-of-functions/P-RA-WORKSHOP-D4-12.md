---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-12
kind: problem
title: A sequential liminf condition implies continuity at a point
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(January 2012 #1b) Let $y\in\mathbb R$ and $f:\mathbb R\to\mathbb R$ be given.
Suppose that for every sequence $\{x_n\}$ we have
$$
\liminf_{n\to\infty}|f(x_n)-f(y)|\le
\liminf_{n\to\infty}|x_n-y|.
$$
Prove that $f$ is continuous at $y$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $f$ is discontinuous at $y$, there exist $\varepsilon>0$ and a sequence $x_n\to y$ such that $|f(x_n)-f(y)|\geq\varepsilon$ for every $n$.

::: pf-proof

Negating continuity at $y$ gives $\varepsilon>0$ such that, for every $\delta>0$, there is an $x\in\mathbb R$ with $|x-y|<\delta$ but $|f(x)-f(y)|\geq\varepsilon$. For each $n\geq1$, take $\delta=1/n$ and select the corresponding $x_n$. Then $|x_n-y|<1/n$, so $x_n\to y$.

:::

:::

::: {.pf-step #s2}

The sequence of step [](#s1){.pf-ref} violates the assumed lower-limit inequality.

::: pf-proof

Since $|f(x_n)-f(y)|\geq\varepsilon$ for all $n$,
\[
\liminf_{n\to\infty}|f(x_n)-f(y)|\geq\varepsilon>0.
\]
On the other hand, $x_n\to y$ gives $\liminf_{n\to\infty}|x_n-y|=0$. This contradicts the hypothesis applied to the sequence $(x_n)$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} rule out discontinuity at $y$. Hence $f$ is continuous at $y$.

:::

:::

:::
