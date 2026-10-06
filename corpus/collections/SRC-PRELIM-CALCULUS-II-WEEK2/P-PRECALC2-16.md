---
schema: qual/card@1
id: P-PRECALC2-16
kind: problem
title: Convergence of $\sum(1-\tanh n)$ and $\sum(\frac\pi2-\arctan n)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Decide whether the following series converge or diverge:

$$
( \mathrm { a } ) \sum _ { n = 1 } ^ { \infty } [ 1 - \operatorname { t a n h } ( n ) ] , \quad \quad ( \mathrm { b } ) \sum _ { n = 1 } ^ { \infty } \left( { \frac { \pi } { 2 } } - \arctan ( n ) \right) .
$$
:::

::: {.solution}
## Part (a)

<1>1. Using the exponential formula for \(\tanh\),
\[
\tanh n
=
\frac{e^n-e^{-n}}{e^n+e^{-n}}
=
\frac{e^{2n}-1}{e^{2n}+1}.
\]

::: {.proof}
Multiply numerator and denominator of
\[
\frac{e^n-e^{-n}}{e^n+e^{-n}}
\]
by \(e^n\).
:::

<1>2. Therefore
\[
\boxed{
1-\tanh n
=
\frac{2}{e^{2n}+1}}.
\]

::: {.proof}
\[
1-\frac{e^{2n}-1}{e^{2n}+1}
=
\frac{e^{2n}+1-e^{2n}+1}{e^{2n}+1}
=
\frac2{e^{2n}+1}.
\]
:::

<1>3. For every \(n\ge1\),
\[
0<
1-\tanh n
\le
2e^{-2n}.
\]

::: {.proof}
Since
\[
e^{2n}+1\ge e^{2n},
\]
step <1>2 gives
\[
\frac2{e^{2n}+1}
\le
\frac2{e^{2n}}
=
2e^{-2n}.
\]
:::

<1>4. The series
\[
\sum_{n=1}^{\infty}2e^{-2n}
\]
converges.

::: {.proof}
It is geometric with ratio
\[
e^{-2}<1.
\]
:::

<1>5. Hence
\[
\boxed{
\sum_{n=1}^{\infty}
(1-\tanh n)
\text{ converges}}.
\]

::: {.proof}
Apply the comparison test using steps <1>3--<1>4.
:::

## Part (b)

<1>6. For every \(n>0\),
\[
\boxed{
\frac{\pi}{2}-\arctan n
=
\arctan\frac1n}.
\]

::: {.proof}
For \(x>0\),
\[
\arctan x+\arctan\frac1x
=
\frac{\pi}{2}.
\]
This follows from the tangent addition formula, or geometrically from the
complementary acute angles in a right triangle with legs \(1,x\).
Set \(x=n\).
:::

<1>7. Let
\[
a_n
=
\arctan\frac1n.
\]
Then
\[
\frac{a_n}{1/n}
=
n\arctan\frac1n.
\]

::: {.proof}
This is direct algebra.
:::

<1>8. One has
\[
\boxed{
\lim_{n\to\infty}
n\arctan\frac1n
=
1}.
\]

::: {.proof}
Set
\[
x=\frac1n.
\]
Then \(x\to0^+\), and
\[
n\arctan\frac1n
=
\frac{\arctan x}{x}.
\]
Since \(\arctan x\) is differentiable at \(0\) with derivative \(1\),
\[
\lim_{x\to0}
\frac{\arctan x-\arctan0}{x-0}
=
1.
\]
:::

<1>9. Thus
\[
a_n
\]
is limit-comparable to
\[
\frac1n.
\]

::: {.proof}
Step <1>8 gives
\[
\lim_{n\to\infty}
\frac{a_n}{1/n}
=
1,
\]
a positive finite constant.
:::

<1>10. Therefore
\[
\boxed{
\sum_{n=1}^{\infty}
\left(
\frac{\pi}{2}-\arctan n
\right)
\text{ diverges}}.
\]

::: {.proof}
By step <1>6, the series is \(\sum a_n\). By step <1>9 and the limit
comparison test, it has the same convergence behavior as the harmonic series
\[
\sum_{n=1}^{\infty}\frac1n,
\]
which diverges.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>5 proves convergence in part (a), and step <1>10 proves divergence in
part (b).
:::
:::
