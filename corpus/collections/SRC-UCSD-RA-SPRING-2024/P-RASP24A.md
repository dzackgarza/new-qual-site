---
schema: qual/card@1
id: P-RASP24A
kind: problem
title: "Borel measurable function defined by series over rationals"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UCSD Spring 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\{r_n\}_{n=1}^{\infty}$ be a sequence with $r_n \in [0,1]$ and define the function
$$
f(x) := \sum_{r_n < x} \frac{1}{2^n}.
$$
Show that $f$ is Borel measurable, find all its points of discontinuity, and find $\int_0^1 f(x)\,dx$.
:::

::: solution
<1>1. Prove Borel measurability.
::: proof
For each $n$,
\[
\mathbf 1_{(r_n,\infty)}(x)
=
\begin{cases}
1,&r_n<x,\\
0,&r_n\ge x.
\end{cases}
\]
Hence
\[
f(x)=\sum_{n=1}^\infty 2^{-n}\mathbf 1_{(r_n,\infty)}(x).
\]
Each summand is Borel measurable, and the partial sums increase pointwise to $f$. Therefore $f$ is Borel measurable.
:::

<1>2. Determine the discontinuity set.
::: proof
Fix $a\in\mathbb R$. Since the series is absolutely and uniformly bounded by
\[
\sum_{n=1}^\infty2^{-n}=1,
\]
we may compute the one-sided limits term by term. The left limit is
\[
f(a-)=\sum_{r_n<a}2^{-n}=f(a),
\]
while the right limit is
\[
f(a+)=\sum_{r_n\le a}2^{-n}.
\]
Thus the jump at $a$ is
\[
f(a+)-f(a)=\sum_{n:r_n=a}2^{-n}.
\]
This quantity is positive exactly when $a=r_n$ for at least one $n$. Therefore the set of discontinuities is precisely
\[
\boxed{\{r_n:n\ge1\}},
\]
where repetitions are ignored.
:::

<1>3. Compute the integral.
::: proof
The summands are nonnegative, so Tonelli's theorem gives
\[
\begin{aligned}
\int_0^1 f(x)\,dx
&=\sum_{n=1}^\infty 2^{-n}
\int_0^1\mathbf 1_{(r_n,\infty)}(x)\,dx\\
&=\sum_{n=1}^\infty 2^{-n}(1-r_n).
\end{aligned}
\]
Hence
\[
\boxed{\int_0^1 f(x)\,dx
=\sum_{n=1}^\infty\frac{1-r_n}{2^n}.}
\]
:::
:::
