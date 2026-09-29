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

:::: {.solution}
::: pf

::: pf-step
Prove the contrapositive: if $f$ is not continuous at $y$, the hypothesis fails.
:::

::: pf-step
Discontinuity gives a sequence violating the liminf condition.
Proof: suppose $f$ is discontinuous at $y$.
Then there is $\epsilon > 0$ and a sequence $x_n \to y$ with $|f(x_n) - f(y)| \ge \epsilon$ for all $n$ (take $x_n \in (y - 1/n, y + 1/n)$ with $|f(x_n) - f(y)| \ge \epsilon$, which exists since $f$ is not continuous at $y$).
:::

::: pf-step
Compare the two liminfs.
Proof: for this sequence, $\liminf_{n\to\infty}|x_n - y| = 0$ (as $x_n \to y$), while $\liminf_{n\to\infty}|f(x_n) - f(y)| \ge \epsilon > 0$.
Hence \[\liminf |f(x_n) - f(y)| \ge \epsilon > 0 = \liminf |x_n - y|,\] violating the hypothesis for this particular sequence.
:::

::: pf-qed
Proof: contrapositive established: hypothesis ⟹ $f$ continuous at $y$.
:::

:::
::::
