---
schema: qual/card@1
id: P-PRECALC2-13
kind: problem
title: Convergence of $\sum\frac{1}{\log(n!)}$ and $\sum\frac{1}{(\log n)^{\log n}}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Do the series $\sum _ { n = 2 } ^ { \infty } { \frac { 1 } { \log ( n ! ) } }$ and $\sum _ { n = 3 } ^ { \infty } { \frac { 1 } { \log ( n ) ^ { \log ( n ) } } }$ converge or diverge?
:::

Consider first
\[
\sum_{n=2}^{\infty}\frac1{\log(n!)}.
\]

::: pf

::: pf-step

For every \(n\ge2\),
\[
\boxed{n!\le n^n}.
\]


::: pf-proof

Each factor in
\[
n!=1\cdot2\cdots n
\]
is at most \(n\), so the product is at most the product of \(n\) copies of
\(n\).

:::

:::

::: pf-step

Therefore
\[
\boxed{\log(n!)\le n\log n}.
\]


::: pf-proof

The logarithm is increasing on \((0,\infty)\). Apply \(\log\) to step <1>1:
\[
\log(n^n)=n\log n.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\frac1{\log(n!)}
\ge
\frac1{n\log n}}.
\]


::: pf-proof

For \(n\ge2\), both denominators are positive. Taking reciprocals reverses
the inequality in step <1>2.

:::

:::

::: pf-step

The comparison series
\[
\sum_{n=2}^{\infty}
\frac1{n\log n}
\]
diverges.


::: pf-proof

By the integral test,
\[
\int_2^\infty
\frac{dx}{x\log x}
=
\left[
\log\log x
\right]_2^\infty
=
\infty.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\sum_{n=2}^{\infty}
\frac1{\log(n!)}
\text{ diverges}}.
\]


::: pf-proof

The terms are nonnegative, and step <1>3 bounds them below by the terms of
the divergent series in step <1>4.

:::

:::

::: pf-step

One has
\[
\boxed{
(\log n)^{\log n}
=
n^{\log\log n}}.
\]


::: pf-proof

Using \(a^b=e^{b\log a}\),
\[
(\log n)^{\log n}
=
e^{(\log n)(\log\log n)}.
\]
Also
\[
n^{\log\log n}
=
e^{(\log\log n)(\log n)}.
\]
The two expressions are equal.

:::

:::

::: pf-step

Hence
\[
\boxed{
\frac1{(\log n)^{\log n}}
=
\frac1{n^{\log\log n}}}.
\]


::: pf-proof

Take reciprocals in step <1>6.

:::

:::

::: pf-step

There exists \(N\) such that for every \(n\ge N\),
\[
\boxed{\log\log n\ge2}.
\]


::: pf-proof

Since
\[
\log\log n\longrightarrow\infty,
\]
it eventually exceeds \(2\). For example, any
\[
N\ge e^{e^2}
\]
works.

:::

:::

::: pf-step

Therefore, for all \(n\ge N\),
\[
\boxed{
\frac1{n^{\log\log n}}
\le
\frac1{n^2}}.
\]


::: pf-proof

By step <1>8,
\[
\log\log n\ge2.
\]
For \(n>1\), increasing the positive exponent increases \(n^\text{exponent}\),
so
\[
n^{\log\log n}\ge n^2.
\]
Take reciprocals.

:::

:::

::: pf-step

The series
\[
\sum_{n=N}^{\infty}
\frac1{n^2}
\]
converges.


::: pf-proof

This is a \(p\)-series with
\[
p=2>1.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\sum_{n=3}^{\infty}
\frac1{(\log n)^{\log n}}
\text{ converges}}.
\]


::: pf-proof

By steps <1>7 and <1>9, its tail is bounded above by the convergent series in
step <1>10. Finitely many initial terms do not affect convergence.

:::

:::

::: pf-qed

Step <1>5 gives divergence of the first series, and step <1>11 gives
convergence of the second.

:::

:::
