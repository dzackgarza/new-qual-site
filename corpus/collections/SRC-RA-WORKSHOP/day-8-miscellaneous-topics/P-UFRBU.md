---
schema: qual/card@1
id: P-UFRBU
kind: problem
title: A function with absolutely summable spikes on $[0,1]$ has bounded variation
classification:
  areas:
  - real-analysis
  topics:
  - Variation
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $\{a_n\}_{n=1}^\infty \subseteq \RR$ and a strictly increasing sequence $\{x_n\}_{n=1}^\infty \subseteq (0,1)$ be given.
Assume that $\sum_{n=1}^\infty a_n$ is absolutely convergent, and define $\alpha \colon [0,1] \to \RR$ by $$\alpha(x)\coloneqq \begin{cases} a_n &  x=x_n \\ 0 & \text{otherwise} \end{cases}.$$ Prove or disprove: $\alpha$ has bounded variation on $[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every partition $P=(0=t_0<\cdots<t_m=1)$ satisfies
$$
\sum_{j=1}^m\abs{\alpha(t_j)-\alpha(t_{j-1})}\leq2\sum_{n=1}^\infty\abs{a_n}.
$$

::: pf-proof

The triangle inequality bounds the partition sum by
$$
\abs{\alpha(t_0)}+2\sum_{j=1}^{m-1}\abs{\alpha(t_j)}+\abs{\alpha(t_m)}.
$$
Both endpoint values vanish because $x_n\in(0,1)$.
Each interior partition point with nonzero value is a distinct $x_n$, so the interior sum is at most $\sum_{n\geq1}\abs{a_n}$.

:::

:::

::: {.pf-step #s2}

For every $N\geq1$, a partition has variation sum at least $2\sum_{n=1}^N\abs{a_n}$.

::: pf-proof

There are points $y_0\in(0,x_1)$, $y_j\in(x_j,x_{j+1})$ for $1\leq j<N$, and $y_N\in(x_N,1)$, all distinct from every $x_n$, because the sequence is strictly increasing and its range is countable.
The partition
$$
0<y_0<x_1<y_1<\cdots<y_{N-1}<x_N<y_N<1
$$
has $\alpha(y_j)=0$ and $\alpha(x_j)=a_j$.
The two increments adjacent to each $x_j$ contribute $2\abs{a_j}$, while the remaining increments are nonnegative.

:::

:::

::: pf-step

$\boxed{\text{True}}$: $\alpha$ has bounded variation, with $V_{[0,1]}(\alpha)=2\sum_{n=1}^\infty\abs{a_n}<\infty$.

::: pf-proof

Step [](#s1){.pf-ref} gives the upper bound after taking the supremum over partitions.
Step [](#s2){.pf-ref} gives $V(\alpha)\geq2\sum_{n=1}^N\abs{a_n}$ for every $N$, and letting $N\to\infty$ gives the reverse bound.
Absolute convergence makes the common value finite.

:::

:::

:::

:::
