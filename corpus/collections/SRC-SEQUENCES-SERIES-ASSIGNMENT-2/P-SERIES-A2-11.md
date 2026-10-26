---
schema: qual/card@1
id: P-SERIES-A2-11
kind: problem
title: 'Convergent series: $\sum a_nb_n$, $\sum n^2a_n$ and $na_n\to0$'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
For each proposition, give a short proof if it is true and a counterexample if it is false.

(a) If $\sum a_n$ converges and the sequence $\{b_n\}$ also converges, then $\sum a_n b_n$ converges.

(b) If $\sum a_n$ converges conditionally, then $\sum n^2a_n$ diverges.

(c) If $\{a_n\}$ is decreasing and $\sum a_n$ converges, then
\[
\lim_{n\to\infty} n a_n=0.
\]
:::

## Part (a)

The proposition is false.

::: pf

::: pf-step

Define
\[
\boxed{
a_n=\frac{(-1)^n}{\sqrt n},
\qquad
b_n=\frac{(-1)^n}{\sqrt n}}.
\]


::: pf-proof

These sequences will give a counterexample.

:::

:::

::: pf-step

The series
\[
\sum_{n=1}^{\infty}a_n
\]
converges.


::: pf-proof

The positive sequence
\[
n^{-1/2}
\]
decreases to \(0\), so the alternating-series test applies.

:::

:::

::: pf-step

The sequence \((b_n)\) converges to \(0\).


::: pf-proof

\[
|b_n|=\frac1{\sqrt n}\to0.
\]

:::

:::

::: pf-step

But
\[
\boxed{
a_nb_n=\frac1n}.
\]


::: pf-proof

\[
\frac{(-1)^n}{\sqrt n}
\frac{(-1)^n}{\sqrt n}
=
\frac{(-1)^{2n}}{n}
=
\frac1n.
\]

:::

:::

::: pf-step

Therefore
\[
\sum_{n=1}^{\infty}a_nb_n
\]
diverges.


::: pf-proof

By step <1>4, this is the harmonic series.

:::

:::

::: pf-step

Hence proposition (a) is
\[
\boxed{\text{false}}.
\]


::: pf-proof

Steps <1>2--<1>5 satisfy the hypotheses but not the conclusion.

:::

:::

::: pf-step

Suppose, toward a contradiction, that
\[
\sum n^2a_n
\]
converges.


::: pf-proof

We will show this forces absolute convergence of \(\sum a_n\).

:::

:::

::: pf-step

Then
\[
\boxed{
n^2a_n\to0}.
\]


::: pf-proof

The terms of every convergent series tend to zero.

:::

:::

::: pf-step

Hence there exists \(N\) such that for every \(n\ge N\),
\[
\boxed{
|n^2a_n|<1}.
\]


::: pf-proof

Apply step <1>8 with \(\varepsilon=1\).

:::

:::

::: pf-step

Therefore, for \(n\ge N\),
\[
\boxed{
|a_n|<\frac1{n^2}}.
\]


::: pf-proof

Divide step <1>9 by the positive number \(n^2\).

:::

:::

::: pf-step

Hence
\[
\sum_{n=N}^{\infty}|a_n|
\]
converges.


::: pf-proof

By step <1>10, compare with the convergent \(p\)-series
\[
\sum_{n=N}^{\infty}\frac1{n^2}.
\]

:::

:::

::: pf-step

Thus
\[
\sum a_n
\]
would converge absolutely.


::: pf-proof

Adding finitely many initial absolute values does not affect convergence.
Apply step <1>11.

:::

:::

::: pf-step

This contradicts conditional convergence.


::: pf-proof

Conditional convergence means convergence without absolute convergence.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\sum n^2a_n
\text{ diverges}}.
\]


::: pf-proof

The assumption in step <1>7 led to a contradiction.

:::

:::

::: pf-step

One has
\[
\boxed{a_n\to0}.
\]


::: pf-proof

The terms of a convergent series tend to zero.

:::

:::

::: pf-step

Since \((a_n)\) is decreasing and tends to \(0\),
\[
\boxed{a_n\ge0}
\]
for every \(n\).


::: pf-proof

If some \(a_N<0\), then decreasingness would give
\[
a_n\le a_N<0
\]
for all \(n\ge N\), contradicting \(a_n\to0\).

:::

:::

::: pf-step

Let
\[
\varepsilon>0.
\]
By the Cauchy criterion for the convergent series \(\sum a_n\), there exists
\(N\) such that whenever \(q>p\ge N\),
\[
\boxed{
\sum_{k=p}^{q}a_k<\frac{\varepsilon}{2}}.
\]


::: pf-proof

All terms are nonnegative by step <1>16, so the absolute value in the Cauchy
criterion may be omitted.

:::

:::

::: pf-step

Let \(n>2N\) and set
\[
m=\left\lfloor\frac n2\right\rfloor.
\]
Then
\[
m\ge N.
\]


::: pf-proof

Since \(n>2N\),
\[
\frac n2>N.
\]
Taking the floor gives \(m\ge N\).

:::

:::

::: pf-step

Since the sequence is decreasing,
\[
a_k\ge a_n
\]
for every
\[
m\le k\le n.
\]


::: pf-proof

For \(k\le n\), decreasingness gives \(a_k\ge a_n\).

:::

:::

::: pf-step

Hence
\[
\sum_{k=m}^{n}a_k
\ge
(n-m+1)a_n.
\]


::: pf-proof

There are \(n-m+1\) terms, each at least \(a_n\) by step <1>19.

:::

:::

::: pf-step

One has
\[
n-m+1\ge\frac n2.
\]


::: pf-proof

Since
\[
m=\left\lfloor\frac n2\right\rfloor\le\frac n2,
\]
\[
n-m+1
\ge
n-\frac n2
=
\frac n2.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\sum_{k=m}^{n}a_k
\ge
\frac n2\,a_n}.
\]


::: pf-proof

Combine steps <1>20--<1>21 and use \(a_n\ge0\).

:::

:::

::: pf-step

By step <1>17,
\[
\sum_{k=m}^{n}a_k<\frac{\varepsilon}{2}.
\]


::: pf-proof

Step <1>18 gives \(m\ge N\), so the Cauchy tail estimate applies.

:::

:::

::: pf-step

Combining steps <1>22--<1>23,
\[
\frac n2\,a_n<\frac{\varepsilon}{2}.
\]


::: pf-proof

The same tail sum is bounded below and above by those two quantities.

:::

:::

::: pf-step

Hence
\[
\boxed{
na_n<\varepsilon}
\]
for every \(n>2N\).


::: pf-proof

Multiply step <1>24 by \(2\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
na_n\to0}.
\]


::: pf-proof

Step <1>25 is the \(\varepsilon\)-definition of convergence to \(0\).

:::

:::

::: pf-step

Thus the answers are:
\[
\boxed{
\text{(a) false,\qquad (b) true,\qquad (c) true}.}
\]


::: pf-proof

Use steps <1>6, <1>14, and <1>26.

:::

:::

::: pf-qed

Step <1>27 gives the required dispositions.

:::

:::
