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
<1>1. Prove the contrapositive: if $f$ is not continuous at $y$, the hypothesis fails.
<1>2. Discontinuity gives a sequence violating the liminf condition.
Proof: suppose $f$ is discontinuous at $y$.
Then there is $\epsilon > 0$ and a sequence $x_n \to y$ with $|f(x_n) - f(y)| \ge \epsilon$ for all $n$ (take $x_n \in (y - 1/n, y + 1/n)$ with $|f(x_n) - f(y)| \ge \epsilon$, which exists since $f$ is not continuous at $y$). <1>3. Compare the two liminfs.
Proof: for this sequence, $\liminf_{n\to\infty}|x_n - y| = 0$ (as $x_n \to y$), while $\liminf_{n\to\infty}|f(x_n) - f(y)| \ge \epsilon > 0$.
Hence \[\liminf |f(x_n) - f(y)| \ge \epsilon > 0 = \liminf |x_n - y|,\] violating the hypothesis for this particular sequence.
<1>4. Q.E.D. Proof: contrapositive established: hypothesis ⟹ $f$ continuous at $y$.
:::
