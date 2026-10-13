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

::: {.solution}
## Part (a)

Assume
\[
a_n>0
\]
and
\[
na_n\to\ell\ne0.
\]

<1>1. Since every \(na_n>0\), the limit satisfies
\[
\boxed{\ell>0}.
\]

::: {.proof}
A limit of positive numbers is nonnegative. Since the limit is assumed
nonzero, it must be positive.
:::

<1>2. Choose
\[
\varepsilon=\frac{\ell}{2}>0.
\]
Then there exists \(N\) such that for all \(n\ge N\),
\[
|na_n-\ell|<\frac{\ell}{2}.
\]

::: {.proof}
Apply the definition of convergence to the sequence \(na_n\to\ell\).
:::

<1>3. Hence, for \(n\ge N\),
\[
na_n>\frac{\ell}{2}.
\]

::: {.proof}
From step <1>2,
\[
na_n
>
\ell-\frac{\ell}{2}
=
\frac{\ell}{2}.
\]
:::

<1>4. Therefore
\[
\boxed{
a_n>\frac{\ell}{2n}}
\]
for every \(n\ge N\).

::: {.proof}
Divide step <1>3 by the positive integer \(n\).
:::

<1>5. The comparison series
\[
\sum_{n=N}^{\infty}
\frac{\ell}{2n}
\]
diverges.

::: {.proof}
It is the positive constant \(\ell/2\) times the harmonic series.
:::

<1>6. Hence
\[
\boxed{
\sum_{n=1}^{\infty}a_n
\text{ diverges}}.
\]

::: {.proof}
By steps <1>4--<1>5, the tail of \(\sum a_n\) dominates a divergent
nonnegative series.
:::

## Part (b)

Assume now that
\[
\sum_{n=1}^{\infty}a_n
\]
converges absolutely, so
\[
\sum_{n=1}^{\infty}|a_n|<\infty.
\]

<1>7. Absolute convergence implies
\[
\boxed{|a_n|\to0}.
\]

::: {.proof}
The terms of any convergent series must tend to zero. Apply this to the
nonnegative series \(\sum|a_n|\).
:::

<1>8. Therefore there exists \(N\) such that
\[
\boxed{|a_n|<1}
\]
for every \(n\ge N\).

::: {.proof}
Apply step <1>7 with \(\varepsilon=1\).
:::

<1>9. If
\[
p>1
\]
and \(n\ge N\), then
\[
\boxed{
|a_n|^p\le|a_n|}.
\]

::: {.proof}
For \(0\le x\le1\) and \(p>1\),
\[
x^p\le x.
\]
Apply this with \(x=|a_n|\).
:::

<1>10. Hence
\[
\boxed{
\sum_{n=1}^{\infty}|a_n|^p
\text{ converges}}
\]
for every real \(p>1\).

::: {.proof}
The tail is bounded termwise by the convergent series
\[
\sum_{n=N}^{\infty}|a_n|
\]
using step <1>9. Finitely many initial terms do not affect convergence.
:::

<1>11. In particular, whenever \(a_n^p\) is real-defined for every \(n\),
\[
\boxed{
\sum a_n^p
\text{ converges absolutely}}.
\]

::: {.proof}
Whenever the real power is defined,
\[
|a_n^p|=|a_n|^p.
\]
Apply step <1>10.
:::

<1>12. Define
\[
\boxed{
a_n=\frac{(-1)^n}{\sqrt n}}.
\]

::: {.proof}
This will give the requested conditional-convergence counterexample.
:::

<1>13. The series
\[
\sum_{n=1}^{\infty}a_n
=
\sum_{n=1}^{\infty}
\frac{(-1)^n}{\sqrt n}
\]
converges.

::: {.proof}
The positive sequence
\[
n^{-1/2}
\]
decreases to zero, so the alternating-series test applies.
:::

<1>14. It does not converge absolutely.

::: {.proof}
\[
\sum|a_n|
=
\sum\frac1{\sqrt n},
\]
which is a divergent \(p\)-series with exponent \(1/2\le1\).
:::

<1>15. Therefore
\[
\sum a_n
\]
converges conditionally.

::: {.proof}
Combine steps <1>13--<1>14.
:::

<1>16. Take
\[
\boxed{p=2}.
\]
Then
\[
a_n^2=\frac1n.
\]

::: {.proof}
\[
\left(
\frac{(-1)^n}{\sqrt n}
\right)^2
=
\frac1n.
\]
:::

<1>17. Hence
\[
\boxed{
\sum a_n^2
=
\sum\frac1n
\text{ diverges}}.
\]

::: {.proof}
This is the harmonic series.
:::

<1>18. Thus absolute convergence in part (b) is essential.

::: {.proof}
Steps <1>15--<1>17 give a conditionally convergent series whose square
series diverges.
:::

<1>19. Q.E.D.

::: {.proof}
Step <1>6 proves part (a); steps <1>10--<1>11 prove the power-series
conclusion under absolute convergence; and steps <1>12--<1>18 give the
counterexample.
:::
:::
