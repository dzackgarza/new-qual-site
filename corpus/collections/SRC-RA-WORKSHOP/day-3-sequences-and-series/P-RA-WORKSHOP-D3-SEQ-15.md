---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-15
kind: problem
title: Monotone convergence, the nth-term test, and Cauchy condensation
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Sequences of Numbers
  - Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove Theorems 2.1, 2.2, and 2.3.
:::

::: {.solution}
For a series $\sum_{n=1}^{\infty}a_n$, write $S_N=\sum_{n=1}^{N}a_n$.

<1>1. If $a_n\geq0$ for every $n$, then $\sum_n a_n$ converges if and only if $(S_N)$ is bounded above, and in that case its sum is $\sup_N S_N$.

::: {.proof}
Since $S_{N+1}-S_N=a_{N+1}\geq0$, the sequence $(S_N)$ is nondecreasing. If it is bounded above, completeness of $\mathbb R$ gives $S_N\to\sup_N S_N$. Conversely, every convergent real sequence is bounded. These implications prove the claimed equivalence and identify the sum.
:::

<1>2. If $\sum_n a_n$ converges, then $a_n\to0$.

::: {.proof}
Writing $S_N\to S$, one has $a_n=S_n-S_{n-1}\to S-S=0$ for $n\geq2$. Therefore a series whose terms do not tend to zero diverges.
:::

<1>3. If $(a_n)$ is nonincreasing and nonnegative, then
\[
\sum_{n=1}^{\infty}a_n\text{ converges}
\quad\Longleftrightarrow\quad
\sum_{k=0}^{\infty}2^k a_{2^k}\text{ converges}.
\]

::: {.proof}
For each $k\geq0$, monotonicity gives
\[
2^k a_{2^{k+1}}\leq
\sum_{n=2^k}^{2^{k+1}-1}a_n
\leq 2^k a_{2^k}.
\]
These blocks partition $\mathbb N_{\geq1}$, so summing for $0\leq k<m$ yields
\[
\frac12\sum_{j=1}^{m}2^j a_{2^j}
\leq S_{2^m-1}
\leq\sum_{k=0}^{m-1}2^k a_{2^k}.
\]
If the original series converges, its partial sums are bounded; the left inequality then bounds the partial sums of the condensed series (the omitted initial term $a_1$ is finite). Conversely, if the condensed series converges, the right inequality bounds $S_{2^m-1}$ independently of $m$. Since $(S_N)$ is nondecreasing, every $S_N$ is bounded by some such $S_{2^m-1}$ and hence by a common constant. Step <1>1 then establishes convergence of the original series. The same step establishes convergence of the condensed series from boundedness of its nonnegative partial sums.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 prove the three requested assertions.
:::
:::
