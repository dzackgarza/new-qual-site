---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW2
kind: problem
title: A limit point is the limit of a sequence from the set (warm-up)
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

:::: {.solution}
<1>1. Use the definition of limit point.
Proof: $x$ is a limit point of $E$ means every neighborhood of $x$ contains a point of $E$ other than $x$.
In particular, for each $n \ge 1$, the ball $B(x, 1/n)$ contains a point $x_n \in E$ with $x_n \ne x$.
<1>2. The sequence $(x_n)$ converges to $x$.
Proof: for every $\epsilon > 0$ choose $N$ with $1/N < \epsilon$; then for $n \ge N$, $d(x_n, x) < 1/n \le 1/N < \epsilon$.
Hence $x_n \to x$.
<1>3. Q.E.D.
:::
