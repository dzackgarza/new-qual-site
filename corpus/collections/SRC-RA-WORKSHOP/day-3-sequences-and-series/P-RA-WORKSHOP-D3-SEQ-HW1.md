---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW1
kind: problem
title: Uniqueness of the limit of a real sequence (warm-up)
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
---

::: {.problem}
For a real sequence $\{x_n\}$, if $\lim_{n\to\infty}x_n=x$ and $\lim_{n\to\infty}x_n=y$ then $x=y$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Suppose $x_n \to x$ and $x_n \to y$; show $x = y$.
Proof: given $\epsilon > 0$, there are $N_1, N_2$ with $|x_n - x| < \epsilon/2$ for $n \ge N_1$ and $|x_n - y| < \epsilon/2$ for $n \ge N_2$.
For $n \ge \max(N_1, N_2)$: \[|x - y| \le |x - x_n| + |x_n - y| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.\] Since $\epsilon > 0$ was arbitrary, $|x - y| = 0$, so $x = y$.
<1>2. Q.E.D.
:::
