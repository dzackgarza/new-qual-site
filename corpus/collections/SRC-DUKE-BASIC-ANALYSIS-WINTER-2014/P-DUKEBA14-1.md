---
schema: qual/card@1
id: P-DUKEBA14-1
kind: problem
title: Integral test for convergence of series
classification:
  areas: [real-analysis]
  topics: [Series, Improper Integrals]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part I, Problem 1 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
State and prove the integral test for convergence of series. You may assume the comparison test.
:::

::: solution
<1>1. State the test.
::: proof
Let $f:[1,\infty)\to[0,\infty)$ be decreasing. Then
\[
\sum_{n=1}^\infty f(n)
\]
converges if and only if the improper integral
\[
\int_1^\infty f(x)\,dx
\]
converges.
:::

<1>2. Compare each integral over a unit interval with neighboring terms.
::: proof
For $n\ge1$ and $x\in[n,n+1]$, monotonicity gives
\[
f(n+1)\le f(x)\le f(n).
\]
Hence
\[
f(n+1)\le \int_n^{n+1}f(x)\,dx\le f(n).
\]
Summing from $n=1$ to $N$ yields
\[
\sum_{n=2}^{N+1}f(n)
\le \int_1^{N+1}f(x)\,dx
\le \sum_{n=1}^{N}f(n).
\]
:::

<1>3. Deduce equivalence of convergence.
::: proof
If $\sum f(n)$ converges, the right inequality bounds the increasing partial integrals, so $\int_1^\infty f<\infty$.

Conversely, if $\int_1^\infty f<\infty$, the left inequality bounds the partial sums of $\sum_{n=2}^\infty f(n)$; adding the finite first term $f(1)$ gives convergence of $\sum_{n=1}^\infty f(n)$.
:::
:::
