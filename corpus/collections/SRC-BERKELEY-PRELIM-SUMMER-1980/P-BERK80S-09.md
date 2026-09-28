---
schema: qual/card@1
id: P-BERK80S-09
kind: problem
title: Absolute and conditional convergence of a logarithmic power series
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 9 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the root-test regimes, the logarithmic p-series boundary, and the exact alternating-series condition at a=-1.
---

::: {.problem}
For each $( a , b , c ) \in \mathbb { R } ^ { 3 }$ , consider the series

$$
\sum _ { n = 3 } ^ { \infty } { \frac { a ^ { n } } { n ^ { b } ( \log n ) ^ { c } } } \cdotp
$$

Determine the values of $( a , b , c )$ for which the series

1. converges absolutely;

2. converges but not absolutely;

3. diverges.
:::


::: {.solution}
Write
\[
u_n=\frac{a^n}{n^b(\log n)^c}.
\]
Then the classification is as follows.

- The series converges **absolutely** if
  \[
  |a|<1,
  \]
  or if $|a|=1$ and
  \[
  b>1,
  \qquad\text{or}\qquad
  b=1\text{ and }c>1.
  \]
- It converges **conditionally** precisely when
  \[
  a=-1,
  \]
  the terms tend to zero, i.e.
  \[
  b>0\quad\text{or}\quad (b=0\text{ and }c>0),
  \]
  and the absolute-convergence condition above fails.
- It **diverges** in all remaining cases.

<1>1. If $|a|<1$, the series converges absolutely; if $|a|>1$, it diverges.
::: {.proof}
For the absolute values,
\[
|u_n|=\frac{|a|^n}{n^b(\log n)^c}.
\]
The $n$th root satisfies
\[
|u_n|^{1/n}
=|a|\,n^{-b/n}(\log n)^{-c/n}
\longrightarrow |a|.
\]
Thus the root test gives absolute convergence when $|a|<1$ and divergence when $|a|>1$. In the latter case, in particular, the terms do not tend to zero.
:::

<1>2. For $|a|=1$, absolute convergence is governed by
\[
\sum_{n=3}^\infty \frac1{n^b(\log n)^c},
\]
which converges exactly when $b>1$, or when $b=1$ and $c>1$.
::: {.proof}
If $b=1$, the integral test gives
\[
\int_3^\infty \frac{dx}{x(\log x)^c}.
\]
With $u=\log x$, this becomes
\[
\int_{\log 3}^\infty u^{-c}\,du,
\]
which converges exactly when $c>1$.

If $b>1$, then for $c\ge0$ the summand is eventually bounded by $n^{-b}$. If $c<0$, the standard estimate
\[
(\log n)^{|c|}=o(n^\varepsilon)
\]
for every $\varepsilon>0$ lets us choose $0<\varepsilon<b-1$ and bound the summand eventually by $n^{-(b-\varepsilon)}$, with exponent $>1$. Hence the series converges.

If $b<1$, choose $0<\varepsilon<1-b$. When $c>0$, the estimate $(\log n)^c=o(n^\varepsilon)$ gives, for large $n$,
\[
\frac1{n^b(\log n)^c}\ge \frac1{n^{b+\varepsilon}},
\]
and $b+\varepsilon<1$, so the series diverges. When $c\le0$, the summand is eventually at least a positive constant multiple of $n^{-b}$, which also diverges because $b<1$.
:::

<1>3. Conditional convergence can occur only for $a=-1$.
::: {.proof}
For real $a$ with $|a|=1$, the only possibilities are $a=1$ and $a=-1$.
If $a=1$, every term is positive, so convergence is the same as absolute convergence.

For $a=-1$, write
\[
d_n=\frac1{n^b(\log n)^c}>0.
\]
The alternating series
\[
\sum_{n=3}^\infty (-1)^n d_n
\]
converges whenever $d_n\to0$ and $d_n$ is eventually decreasing.
Now
\[
\log d_n=-b\log n-c\log\log n,
\]
so
\[
\frac{d}{dn}\log d_n
=-\frac1n\left(b+\frac{c}{\log n}\right).
\]
Thus $d_n$ is eventually decreasing whenever $b>0$, and also when $b=0,c>0$.
These are exactly the cases in which $d_n\to0$:
\[
b>0,
\qquad\text{or}\qquad
b=0,\ c>0.
\]
Hence the alternating series converges in exactly those cases. It is conditional precisely when, in addition, the absolute-convergence criterion of <1>2 fails.
:::

<1>4. The remaining parameter values give divergence.
::: {.proof}
The only cases not covered by absolute or conditional convergence are:

- $|a|>1$, already divergent by <1>1;
- $a=1$ with $b<1$, or $b=1,c\le1$, divergent by <1>2;
- $a=-1$ with $b<0$, or $b=0,c\le0$, for which $d_n\not\to0$.

In each case the series diverges.
:::
:::
