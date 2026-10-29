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
Prove the following.

(a) A monotone increasing (resp. decreasing) sequence of real numbers converges if and only if it is bounded above (resp. below).

(b) If $\sum_{k=1}^{\infty}a_k$ converges, then $\lim_{k\to\infty}a_k=0$.

(c) If $a_1\geq a_2\geq\cdots\geq0$, then $\sum_{n=1}^{\infty}a_n$ converges if and only if $\sum_{k=1}^{\infty}2^k a_{2^k}$ converges.
:::

::: {.solution}
For a series $\sum_{n=1}^{\infty}a_n$, write $S_N=\sum_{n=1}^{N}a_n$.

::: pf

::: {.pf-step #s1}

(a) A nondecreasing real sequence $(s_n)$ converges if and only if it is bounded above, and then $s_n\to\sup_n s_n$; likewise a nonincreasing sequence converges if and only if it is bounded below, and then $s_n\to\inf_n s_n$.

::: pf-proof

Every convergent real sequence is bounded. Conversely, let $(s_n)$ be nondecreasing and bounded above, and let $s=\sup_n s_n$, which exists by completeness of $\RR$. Given $\varepsilon>0$, there is $N$ with $s_N>s-\varepsilon$, and then $s-\varepsilon<s_N\leq s_n\leq s$ for all $n\geq N$, so $s_n\to s$. The nonincreasing case follows by applying this to $(-s_n)$.

:::

:::

::: pf-step

(b) If $\sum_n a_n$ converges, then $a_n\to0$.

::: pf-proof

Writing $S_N\to S$, one has $a_n=S_n-S_{n-1}\to S-S=0$ for $n\geq2$. Therefore a series whose terms do not tend to zero diverges.

:::

:::

::: pf-step

(c) If $(a_n)$ is nonincreasing and nonnegative, then
$$
\sum_{n=1}^{\infty}a_n\text{ converges}
\quad\Longleftrightarrow\quad
\sum_{k=1}^{\infty}2^k a_{2^k}\text{ converges}.
$$

::: pf-proof

For each $k\geq0$, monotonicity gives
$$
2^k a_{2^{k+1}}\leq
\sum_{n=2^k}^{2^{k+1}-1}a_n
\leq 2^k a_{2^k}.
$$
These blocks partition the positive integers, so summing for $0\leq k<m$ yields
$$
\frac12\sum_{j=1}^{m}2^j a_{2^j}
\leq S_{2^m-1}
\leq a_1+\sum_{k=1}^{m-1}2^k a_{2^k}.
$$
Both series have nonnegative terms, so their partial sums are nondecreasing, and by step [](#s1){.pf-ref} each converges exactly when its partial sums are bounded above. If the original series converges, the left inequality bounds the partial sums of the condensed series by $2\sup_N S_N$. Conversely, if the condensed series converges, the right inequality bounds $S_{2^m-1}$ independently of $m$; since $(S_N)$ is nondecreasing, every $S_N$ is bounded by some such $S_{2^m-1}$. Hence the two series converge or diverge together.

:::

:::

:::

:::
