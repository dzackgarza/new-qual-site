---
schema: qual/card@1
id: P-YPGAW
kind: problem
title: '$L^1$ convergence gives an a.e.-convergent subsequence but not uniform convergence'
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the corresponding Fall 2012 JHU analysis qualifying-exam problem in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

5. For each natural number n, let $f _ { n } : [ 0 , 1 ] \to \mathbb { R }$ be a sequence of absolutely integrable functions, and let $f : [ 0 , 1 ] \to$ R be another absolutely integrable function such that

$$
\int _ { 0 } ^ { 1 } { \big | } f _ { n } ( x ) - f ( x ) { \big | } d x \to 0 , \qquad { \mathrm { a s } } \quad n \to \infty .
$$

(a) Show that there exists a subsequence $f _ { n _ { j } }$ of $f _ { n }$ which converges to $f$ pointwise almost everywhere.

(b) Give a counterexample to show that the assertion fails if ”pointwise almost everywhere” is replaced by ”uniformly”.

::: solution
<1>1. Choose a subsequence with summable $L^1$ errors.
::: proof
Since
\[
\|f_n-f\|_1\longrightarrow0,
\]
we may choose indices
\[
n_1<n_2<\cdots
\]
such that
\[
\|f_{n_j}-f\|_1<2^{-j}
\]
for every $j$.
:::

<1>2. Prove almost-everywhere convergence of that subsequence.
::: proof
By Tonelli's theorem,
\[
\begin{aligned}
\int_0^1\sum_{j=1}^\infty
|f_{n_j}(x)-f(x)|\,dx
&=\sum_{j=1}^\infty\|f_{n_j}-f\|_1\\
&<\sum_{j=1}^\infty2^{-j}<\infty.
\end{aligned}
\]
Hence
\[
\sum_{j=1}^\infty|f_{n_j}(x)-f(x)|<\infty
\]
for almost every $x$. Therefore
\[
|f_{n_j}(x)-f(x)|\longrightarrow0
\]
for almost every $x$, proving part (a).
:::

<1>3. Give a counterexample to uniform convergence.
::: proof
Let
\[
f_n=\mathbf1_{(0,1/n)},
\qquad
f=0.
\]
Then
\[
\|f_n-f\|_1=\frac1n\longrightarrow0.
\]
However,
\[
\|f_n-f\|_\infty=1
\]
for every $n$. The same is true for every subsequence, so no subsequence can converge uniformly to $f$.

Thus the almost-everywhere conclusion cannot be replaced by uniform convergence.
:::
:::
