---
schema: qual/card@1
id: P-PRECALC2-23
kind: problem
title: Convergence of $\int_0^\infty\frac{dx}{1+x^4\sin^2x}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Decide whether the following integral converges: $\int _ { 0 } ^ { \infty } { \frac { d x } { 1 + x ^ { 4 } \sin ^ { 2 } ( x ) } }$
:::

Let
\[
f(x)
=
\frac1{1+x^4\sin^2x}.
\]

::: pf

::: pf-step

The integral over the initial interval
\[
[0,\pi/2]
\]
is finite.


::: pf-proof

The function \(f\) is continuous on the compact interval
\[
[0,\pi/2],
\]
and
\[
0<f(x)\le1.
\]
Hence its integral there is finite.

:::

:::

::: pf-step

For every real \(u\) with
\[
|u|\le\frac{\pi}{2},
\]
one has
\[
\boxed{
|\sin u|
\ge
\frac{2}{\pi}|u|}.
\]


::: pf-proof

On
\[
[0,\pi/2],
\]
the function \(\sin u\) is concave, so it lies above the chord joining
\[
(0,0)
\qquad\text{and}\qquad
(\pi/2,1).
\]
Thus
\[
\sin u
\ge
\frac{2u}{\pi}
\]
for \(0\le u\le\pi/2\). Oddness of \(\sin\) gives the absolute-value form.

:::

:::

::: pf-step

For each integer \(n\ge1\), define
\[
I_n
=
\left[
n\pi-\frac{\pi}{2},
n\pi+\frac{\pi}{2}
\right].
\]


::: pf-proof

These intervals cover
\[
[\pi/2,\infty)
\]
and each contains exactly one zero \(n\pi\) of \(\sin x\).

:::

:::

::: pf-step

If
\[
x=n\pi+u\in I_n,
\]
then
\[
|u|\le\frac{\pi}{2}
\]
and
\[
\boxed{
|\sin x|
=
|\sin u|}.
\]


::: pf-proof

Since \(n\in\mathbb Z\),
\[
\sin(n\pi+u)
=
(-1)^n\sin u.
\]
Taking absolute values gives the result.

:::

:::

::: pf-step

For \(x\in I_n\),
\[
\boxed{
x
\ge
\left(n-\frac12\right)\pi}.
\]


::: pf-proof

The left endpoint of \(I_n\) is
\[
n\pi-\frac{\pi}{2}
=
\left(n-\frac12\right)\pi.
\]

:::

:::

::: pf-step

Combining steps <1>2, <1>4, and <1>5,
\[
x^4\sin^2x
\ge
4\pi^2
\left(n-\frac12\right)^4
u^2.
\]


::: pf-proof

From step <1>5,
\[
x^4
\ge
\pi^4\left(n-\frac12\right)^4.
\]
From steps <1>2 and <1>4,
\[
\sin^2x
=
\sin^2u
\ge
\frac{4u^2}{\pi^2}.
\]
Multiply the inequalities.

:::

:::

::: pf-step

Hence
\[
\int_{I_n}f(x)\,dx
\le
\int_{-\pi/2}^{\pi/2}
\frac{du}
{1+
4\pi^2(n-\frac12)^4u^2}.
\]


::: pf-proof

Use the substitution
\[
x=n\pi+u
\]
and the denominator bound from step <1>6.

:::

:::

::: pf-step

Extending the domain of integration,
\[
\int_{I_n}f(x)\,dx
\le
\int_{-\infty}^{\infty}
\frac{du}
{1+
4\pi^2(n-\frac12)^4u^2}.
\]


::: pf-proof

The integrand is nonnegative.

:::

:::

::: pf-step

For every \(A>0\),
\[
\boxed{
\int_{-\infty}^{\infty}
\frac{du}{1+A^2u^2}
=
\frac{\pi}{A}}.
\]


::: pf-proof

Set
\[
v=Au.
\]
Then
\[
du=\frac{dv}{A},
\]
so
\[
\int_{-\infty}^{\infty}
\frac{du}{1+A^2u^2}
=
\frac1A
\int_{-\infty}^{\infty}
\frac{dv}{1+v^2}
=
\frac{\pi}{A}.
\]

:::

:::

::: pf-step

Applying step <1>9 with
\[
A
=
2\pi\left(n-\frac12\right)^2,
\]
one gets
\[
\boxed{
\int_{I_n}f(x)\,dx
\le
\frac1{2(n-\frac12)^2}}.
\]


::: pf-proof

The denominator in step <1>8 is
\[
1+A^2u^2
\]
for the displayed \(A\). Then
\[
\frac{\pi}{A}
=
\frac{\pi}
{2\pi(n-\frac12)^2}
=
\frac1{2(n-\frac12)^2}.
\]

:::

:::

::: pf-step

The series
\[
\sum_{n=1}^{\infty}
\frac1{2(n-\frac12)^2}
\]
converges.


::: pf-proof

For \(n\ge1\),
\[
n-\frac12
\ge
\frac n2.
\]
Hence
\[
\frac1{2(n-\frac12)^2}
\le
\frac2{n^2}.
\]
Compare with the convergent \(p\)-series
\[
\sum\frac1{n^2}.
\]

:::

:::

::: pf-step

Therefore
\[
\int_{\pi/2}^{\infty}
f(x)\,dx
\]
converges.


::: pf-proof

By step <1>3,
\[
[\pi/2,\infty)
=
\bigcup_{n=1}^{\infty}I_n
\]
up to shared endpoints. Since \(f\ge0\),
\[
\int_{\pi/2}^{\infty}f(x)\,dx
=
\sum_{n=1}^{\infty}
\int_{I_n}f(x)\,dx.
\]
Steps <1>10--<1>11 give a convergent majorant for this series.

:::

:::

::: pf-step

Hence
\[
\boxed{
\int_0^\infty
\frac{dx}{1+x^4\sin^2x}
\text{ converges}}.
\]


::: pf-proof

The integral over \([0,\pi/2]\) is finite by step <1>1, and the tail
converges by step <1>12.

:::

:::

::: pf-qed

Step <1>13 is the required convergence decision.

:::

:::
