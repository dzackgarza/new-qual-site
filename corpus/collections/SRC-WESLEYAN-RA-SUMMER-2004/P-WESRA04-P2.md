---
schema: qual/card@1
id: P-WESRA04-P2
kind: problem
title: Total variation is lower semicontinuous under pointwise convergence
classification:
  areas: [real-analysis]
  topics: [Bounded Variation]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $(f_n)$ be a sequence of functions on $[a,b]$ converging pointwise to $f$.
If $T_a^b(h)$ denotes the total variation of $h$ on $[a,b]$, prove that
\[
T_a^b(f)\le \liminf_{n\to\infty}T_a^b(f_n).
\]
:::

::: {.solution}
Fix an arbitrary partition
\[
P:a=x_0<x_1<\cdots<x_m=b.
\]
Its variation sum is
\[
V_P(h)=\sum_{j=1}^m|h(x_j)-h(x_{j-1})|.
\]
Pointwise convergence at the finitely many partition points gives
\[
V_P(f_n)\longrightarrow V_P(f).
\]
For every $n$,
\[
V_P(f_n)\le T_a^b(f_n).
\]
Hence
\[
V_P(f)
=\lim_{n\to\infty}V_P(f_n)
\le \liminf_{n\to\infty}T_a^b(f_n).
\]
The right-hand side is independent of $P$.
Taking the supremum over all partitions yields
\[
T_a^b(f)
=\sup_P V_P(f)
\le \boxed{\liminf_{n\to\infty}T_a^b(f_n)}.
\]
:::
