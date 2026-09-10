---
schema: qual/card@1
id: E-MUN-5-4
kind: problem
title: Bijections between finite and countable product spaces
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 4; restored part (f) to the printed map X^A -> X^B for A subset B.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $m, n \in \mathbb{Z}_{+}$ . Let $X \neq \varnothing$ .

(a) If $m \leq n$, find an injective map $f: X^m \to X^n$ .

(b) Find a bijective map $g: X^m \times X^n \to X^{m+n}$ .

(c) Find an injective map $h: X^n \to X^\omega$ .

(d) Find a bijective map $k: X^n \times X^\omega \to X^\omega$ .

(e) Find a bijective map $l: X^{\omega} \times X^{\omega} \to X^{\omega}$ .

(f) If $A \subset B$, find an injective map $m: X^A \to X^B$ .
:::

::: {.solution}
Choose once and for all a point \(x_0\in X\).

(a) If \(m\le n\), define
\[
f(x_1,\dots,x_m)
=(x_1,\dots,x_m,\underbrace{x_0,\dots,x_0}_{n-m}).
\]
The first \(m\) coordinates recover the input, so \(f\) is injective.

(b) Concatenation gives a bijection
\[
g:X^m\times X^n\longrightarrow X^{m+n},
\]
\[
g((x_1,\dots,x_m),(y_1,\dots,y_n))
=(x_1,\dots,x_m,y_1,\dots,y_n).
\]
Its inverse splits an \((m+n)\)-tuple after the \(m\)-th coordinate.

(c) Define
\[
h(x_1,\dots,x_n)
=(x_1,\dots,x_n,x_0,x_0,\dots).
\]
Again the first \(n\) coordinates recover the input, so \(h\) is injective.

(d) Define
\[
k((x_1,\dots,x_n),(y_1,y_2,\dots))
=(x_1,\dots,x_n,y_1,y_2,\dots).
\]
The inverse separates the first \(n\) coordinates from the infinite tail, so \(k\) is bijective.

(e) Interleave coordinates:
\[
l((x_1,x_2,\dots),(y_1,y_2,\dots))
=(x_1,y_1,x_2,y_2,\dots).
\]
Taking odd and even coordinates gives the inverse, hence \(l\) is bijective.

(f) Let \(A\subset B\). For \(u\in X^A\), define \(m(u)\in X^B\) by
\[
m(u)(b)=
\begin{cases}
u(b),&b\in A,\\
x_0,&b\in B-A.
\end{cases}
\]
If \(u\ne v\), they differ at some \(a\in A\), and then \(m(u)(a)\ne m(v)(a)\). Thus
\[
m:X^A\hookrightarrow X^B
\]
is injective.
:::
