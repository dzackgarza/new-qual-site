---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-15
kind: problem
title: Prove the monotone, nth-term, and Cauchy condensation theorems
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Sequences of Numbers
  - Convergence
relations: []
review: draft
---

::: {.problem title="?"}
Prove Theorems 2.1, 2.2, and 2.3.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Theorem 2.1 (Monotone Convergence Theorem for series).
Proof: let $a_n \ge 0$.
The partial sums $S_N = \sum_{n=1}^N a_n$ form an increasing sequence, so $S_N$ converges in $[0,\infty]$; the series converges iff $(S_N)$ is bounded above, and then the sum is $\sup_N S_N$.
(If $a_n \ge 0$ only eventually, ignore the initial terms.)
<1>2. Theorem 2.2 (nth-term test).
Proof: if $\sum a_n$ converges with partial sums $S_N \to S$, then $a_n = S_n - S_{n-1} \to S - S = 0$.
Hence if $a_n \not\to 0$ the series diverges.
(For series of real numbers; for a series of vectors the same holds via Cauchy: $a_n \to 0$ is necessary.)
<1>3. Theorem 2.3 (Cauchy condensation test).
Proof: assume $a_1 \ge a_2 \ge \cdots \ge 0$.
(⇒) If $\sum a_n$ converges, group terms between powers of $2$: \[\sum_{n=1}^{2^m - 1} a_n \ge a_1 + (a_2 + a_3) + \cdots + (a_{2^{m-1}} + \cdots + a_{2^m - 1}) \ge a_1 + \frac12\big(2a_2 + 4a_4 + \cdots + 2^{m-1}a_{2^{m-1}}\big),\] so the partial sums of $\sum 2^k a_{2^k}$ are bounded by $2\sum a_n < \infty$; hence $\sum 2^k a_{2^k}$ converges.
(⇐) If $\sum 2^k a_{2^k}$ converges, then grouping in the other direction: \[\sum_{n=2}^{2^m} a_n \le (a_2 + a_3) + (a_4 + \cdots + a_7) + \cdots + (a_{2^{m-1}} + \cdots + a_{2^m}) \le 2a_2 + 4a_4 + \cdots + 2^m a_{2^m},\] so the partial sums of $\sum a_n$ are bounded, hence $\sum a_n$ converges.
<1>4. Q.E.D.
:::
