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

::: {.solution}
Let
\[
f(x)
=
\frac1{1+x^4\sin^2x}.
\]

<1>1. The integral over the initial interval
\[
[0,\pi/2]
\]
is finite.

::: {.proof}
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

<1>2. For every real \(u\) with
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

::: {.proof}
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

<1>3. For each integer \(n\ge1\), define
\[
I_n
=
\left[
n\pi-\frac{\pi}{2},
n\pi+\frac{\pi}{2}
\right].
\]

::: {.proof}
These intervals cover
\[
[\pi/2,\infty)
\]
and each contains exactly one zero \(n\pi\) of \(\sin x\).
:::

<1>4. If
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

::: {.proof}
Since \(n\in\mathbb Z\),
\[
\sin(n\pi+u)
=
(-1)^n\sin u.
\]
Taking absolute values gives the result.
:::

<1>5. For \(x\in I_n\),
\[
\boxed{
x
\ge
\left(n-\frac12\right)\pi}.
\]

::: {.proof}
The left endpoint of \(I_n\) is
\[
n\pi-\frac{\pi}{2}
=
\left(n-\frac12\right)\pi.
\]
:::

<1>6. Combining steps <1>2, <1>4, and <1>5,
\[
x^4\sin^2x
\ge
4\pi^2
\left(n-\frac12\right)^4
u^2.
\]

::: {.proof}
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

<1>7. Hence
\[
\int_{I_n}f(x)\,dx
\le
\int_{-\pi/2}^{\pi/2}
\frac{du}
{1+
4\pi^2(n-\frac12)^4u^2}.
\]

::: {.proof}
Use the substitution
\[
x=n\pi+u
\]
and the denominator bound from step <1>6.
:::

<1>8. Extending the domain of integration,
\[
\int_{I_n}f(x)\,dx
\le
\int_{-\infty}^{\infty}
\frac{du}
{1+
4\pi^2(n-\frac12)^4u^2}.
\]

::: {.proof}
The integrand is nonnegative.
:::

<1>9. For every \(A>0\),
\[
\boxed{
\int_{-\infty}^{\infty}
\frac{du}{1+A^2u^2}
=
\frac{\pi}{A}}.
\]

::: {.proof}
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

<1>10. Applying step <1>9 with
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

::: {.proof}
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

<1>11. The series
\[
\sum_{n=1}^{\infty}
\frac1{2(n-\frac12)^2}
\]
converges.

::: {.proof}
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

<1>12. Therefore
\[
\int_{\pi/2}^{\infty}
f(x)\,dx
\]
converges.

::: {.proof}
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

<1>13. Hence
\[
\boxed{
\int_0^\infty
\frac{dx}{1+x^4\sin^2x}
\text{ converges}}.
\]

::: {.proof}
The integral over \([0,\pi/2]\) is finite by step <1>1, and the tail
converges by step <1>12.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>13 is the required convergence decision.
:::
:::
