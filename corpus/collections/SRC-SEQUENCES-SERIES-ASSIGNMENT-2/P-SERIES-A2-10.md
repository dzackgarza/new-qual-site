---
schema: qual/card@1
id: P-SERIES-A2-10
kind: problem
title: Divergence when $na_n\to\ell\ne0$ and convergence of $\sum a_n^p$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Show that if $a_n>0$ and
\[
\lim_{n\to\infty}n a_n=\ell\ne0,
\]
then $\sum a_n$ diverges.

(b) Given that $\sum a_n$ converges absolutely, show that $\sum a_n^p$ also converges whenever $p>1$. Give a counterexample when $\sum a_n$ only converges conditionally.
:::

## Part (a)

Assume
\[
a_n>0
\]
and
\[
na_n\to\ell\ne0.
\]

::: pf

::: pf-step

Since every \(na_n>0\), the limit satisfies
\[
\boxed{\ell>0}.
\]


::: pf-proof

A limit of positive numbers is nonnegative. Since the limit is assumed
nonzero, it must be positive.

:::

:::

::: pf-step

Choose
\[
\varepsilon=\frac{\ell}{2}>0.
\]
Then there exists \(N\) such that for all \(n\ge N\),
\[
|na_n-\ell|<\frac{\ell}{2}.
\]


::: pf-proof

Apply the definition of convergence to the sequence \(na_n\to\ell\).

:::

:::

::: pf-step

Hence, for \(n\ge N\),
\[
na_n>\frac{\ell}{2}.
\]


::: pf-proof

From step <1>2,
\[
na_n
>
\ell-\frac{\ell}{2}
=
\frac{\ell}{2}.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
a_n>\frac{\ell}{2n}}
\]
for every \(n\ge N\).


::: pf-proof

Divide step <1>3 by the positive integer \(n\).

:::

:::

::: pf-step

The comparison series
\[
\sum_{n=N}^{\infty}
\frac{\ell}{2n}
\]
diverges.


::: pf-proof

It is the positive constant \(\ell/2\) times the harmonic series.

:::

:::

::: pf-step

Hence
\[
\boxed{
\sum_{n=1}^{\infty}a_n
\text{ diverges}}.
\]


::: pf-proof

By steps <1>4--<1>5, the tail of \(\sum a_n\) dominates a divergent
nonnegative series.

:::

:::

::: pf-step

Absolute convergence implies
\[
\boxed{|a_n|\to0}.
\]


::: pf-proof

The terms of any convergent series must tend to zero. Apply this to the
nonnegative series \(\sum|a_n|\).

:::

:::

::: pf-step

Therefore there exists \(N\) such that
\[
\boxed{|a_n|<1}
\]
for every \(n\ge N\).


::: pf-proof

Apply step <1>7 with \(\varepsilon=1\).

:::

:::

::: pf-step

If
\[
p>1
\]
and \(n\ge N\), then
\[
\boxed{
|a_n|^p\le|a_n|}.
\]


::: pf-proof

For \(0\le x\le1\) and \(p>1\),
\[
x^p\le x.
\]
Apply this with \(x=|a_n|\).

:::

:::

::: pf-step

Hence
\[
\boxed{
\sum_{n=1}^{\infty}|a_n|^p
\text{ converges}}
\]
for every real \(p>1\).


::: pf-proof

The tail is bounded termwise by the convergent series
\[
\sum_{n=N}^{\infty}|a_n|
\]
using step <1>9. Finitely many initial terms do not affect convergence.

:::

:::

::: pf-step

In particular, whenever \(a_n^p\) is real-defined for every \(n\),
\[
\boxed{
\sum a_n^p
\text{ converges absolutely}}.
\]


::: pf-proof

Whenever the real power is defined,
\[
|a_n^p|=|a_n|^p.
\]
Apply step <1>10.

:::

:::

::: pf-step

Define
\[
\boxed{
a_n=\frac{(-1)^n}{\sqrt n}}.
\]


::: pf-proof

This will give the requested conditional-convergence counterexample.

:::

:::

::: pf-step

The series
\[
\sum_{n=1}^{\infty}a_n
=
\sum_{n=1}^{\infty}
\frac{(-1)^n}{\sqrt n}
\]
converges.


::: pf-proof

The positive sequence
\[
n^{-1/2}
\]
decreases to zero, so the alternating-series test applies.

:::

:::

::: pf-step

It does not converge absolutely.


::: pf-proof

\[
\sum|a_n|
=
\sum\frac1{\sqrt n},
\]
which is a divergent \(p\)-series with exponent \(1/2\le1\).

:::

:::

::: pf-step

Therefore
\[
\sum a_n
\]
converges conditionally.


::: pf-proof

Combine steps <1>13--<1>14.

:::

:::

::: pf-step

Take
\[
\boxed{p=2}.
\]
Then
\[
a_n^2=\frac1n.
\]


::: pf-proof

\[
\left(
\frac{(-1)^n}{\sqrt n}
\right)^2
=
\frac1n.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\sum a_n^2
=
\sum\frac1n
\text{ diverges}}.
\]


::: pf-proof

This is the harmonic series.

:::

:::

::: pf-step

Thus absolute convergence in part (b) is essential.


::: pf-proof

Steps <1>15--<1>17 give a conditionally convergent series whose square
series diverges.

:::

:::

::: pf-qed

Step <1>6 proves part (a); steps <1>10--<1>11 prove the power-series
conclusion under absolute convergence; and steps <1>12--<1>18 give the
counterexample.

:::

:::
