---
schema: qual/card@1
id: E-SS3.EX-6
kind: problem
title: "SS 3.6: The integral of 1/(1+x^2)^(n+1)"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
6. Show that

$$
\int_ {- \infty} ^ {\infty} \frac {d x}{(1 + x ^ {2}) ^ {n + 1}} = \frac {1 \cdot 3 \cdot 5 \cdots (2 n - 1)}{2 \cdot 4 \cdot 6 \cdots (2 n)} \cdot \pi .
$$
:::

::: {.solution}
For $m\ge1$, set
\[
J_m=\int_{-\infty}^{\infty}\frac{dx}{(1+x^2)^m}.
\]
We have $J_1=\pi$. For $m\ge2$, differentiate
\[
\frac{x}{(1+x^2)^{m-1}}.
\]
Since this function tends to $0$ at both ends,
\[
0=\int_{-\infty}^{\infty}\left[
\frac1{(1+x^2)^{m-1}}-
\frac{2(m-1)x^2}{(1+x^2)^m}
\right]dx.
\]
Using
\[
\frac{x^2}{(1+x^2)^m}
=\frac1{(1+x^2)^{m-1}}-\frac1{(1+x^2)^m},
\]
we get
\[
J_{m-1}=2(m-1)(J_{m-1}-J_m),
\]
so
\[
J_m=\frac{2m-3}{2m-2}J_{m-1}.
\]
Iterating from $J_1=\pi$ gives
\[
J_{n+1}
=\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}\,\pi.
\]
Hence
\[
\boxed{
\int_{-\infty}^{\infty}\frac{dx}{(1+x^2)^{n+1}}
=\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}\pi}.
\]
:::
