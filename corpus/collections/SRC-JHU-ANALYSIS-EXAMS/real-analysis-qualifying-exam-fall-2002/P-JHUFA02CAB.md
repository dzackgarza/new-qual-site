---
schema: qual/card@1
id: P-JHUFA02CAB
kind: problem
title: 'the limit $$ f ( x ) = \operatorname* { l i m } _ { n \to \i'
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Convergence
  - Interchange of Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the preserved JHU Fall 2002 Real Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

2. Let $f _ { 1 } ( x ) \leq f _ { 2 } ( x ) \leq . . . \leq f _ { n } ( x ) \leq . . .$ . on a set A,where the functions $f _ { n }$ are integrable and $\textstyle \int _ { A } f _ { n } ( x ) \ d x \leq M$ for some constant M. Show that the limit

$$
f ( x ) = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )
$$

exists and is finite almost everywhere on A and that

$$
\operatorname* { l i m } _ { n  \infty } \int _ { A } f _ { n } ( x ) \ d x = \int _ { A } f ( x ) \ d x \ .
$$

::: {.solution}
Set
\[
g_n:=f_n-f_1.
\]
Then each $g_n$ is measurable, nonnegative, and
\[
0=g_1\le g_2\le\cdots.
\]
Moreover
\[
\int_A g_n
=\int_A f_n-\int_A f_1
\le M-\int_A f_1<\infty.
\]

Let
\[
g(x):=\lim_{n\to\infty}g_n(x)\in[0,\infty].
\]
By the Monotone Convergence Theorem,
\[
\int_A g
=\lim_{n\to\infty}\int_A g_n
\le M-\int_A f_1<\infty.
\]
Hence $g(x)<\infty$ for almost every $x\in A$. Therefore
\[
f(x):=f_1(x)+g(x)
=\lim_{n\to\infty}f_n(x)
\]
exists and is finite almost everywhere.

Finally,
\[
\begin{aligned}
\lim_{n\to\infty}\int_A f_n
&=\int_A f_1+\lim_{n\to\infty}\int_A g_n\\
&=\int_A f_1+\int_A g\\
&=\int_A f.
\end{aligned}
\]
Thus the pointwise monotone limit is finite almost everywhere and the integrals converge to the integral of the limit.
:::
