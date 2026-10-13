---
schema: qual/card@1
id: P-UCLARA17F-07
kind: problem
title: Meromorphic function with zeros at $\mathbb Z$ and poles at $\mathbb Z+\frac13$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 7. Prove that there exists a meromorphic function $f$ on $\mathbb C$ with the following three properties:

1. $f(z)=0$ if and only if $z\in\mathbb Z$;
2. $f(z)=\infty$ if and only if $z-\frac13\in\mathbb Z$;
3. $|f(x+iy)|\le1$ for all $x\in\mathbb R$ and all $y\in\mathbb R$ with $|y|\ge1$.
:::

::: {.solution}
Define
\[
\boxed{
f(z)
=
\tanh(\pi)\,
\frac{\sin(\pi z)}
{\sin\!\left(\pi(z-\frac13)\right)}}.
\]

We verify the three required properties.

## Zeros

<1>1. The numerator vanishes exactly at
\[
\boxed{z\in\mathbb Z}.
\]

::: {.proof}
The zeros of \(\sin(\pi z)\) are exactly the integers.
:::

<1>2. For every \(n\in\mathbb Z\),
\[
\sin\!\left(
\pi\left(n-\frac13\right)
\right)
\ne0.
\]

::: {.proof}
One has
\[
n-\frac13\notin\mathbb Z.
\]
Since \(\sin(\pi w)=0\) exactly when \(w\in\mathbb Z\), the denominator is nonzero at \(z=n\).
:::

<1>3. Therefore
\[
\boxed{
f(z)=0
\iff
z\in\mathbb Z}.
\]

::: {.proof}
The prefactor \(\tanh\pi\) is nonzero, and step <1>2 shows no numerator zero is canceled by a denominator zero.
:::

## Poles

<1>4. The denominator vanishes exactly when
\[
\boxed{
z-\frac13\in\mathbb Z}.
\]

::: {.proof}
\[
\sin\!\left(
\pi(z-\tfrac13)
\right)=0
\]
if and only if
\[
z-\tfrac13\in\mathbb Z.
\]
:::

<1>5. If
\[
z=n+\frac13,
\qquad
n\in\mathbb Z,
\]
then the numerator is nonzero.

::: {.proof}
\[
\sin\!\left(
\pi\left(n+\frac13\right)
\right)
=
(-1)^n\sin\frac{\pi}{3}
=
(-1)^n\frac{\sqrt3}{2}
\ne0.
\]
:::

<1>6. Hence every point
\[
n+\frac13
\]
is a genuine simple pole of \(f\), and there are no other poles.

::: {.proof}
The zeros of the denominator are simple because
\[
\frac{d}{dz}
\sin\!\left(
\pi(z-\tfrac13)
\right)
=
\pi
\cos\!\left(
\pi(z-\tfrac13)
\right),
\]
which equals \(\pm\pi\) at those zeros. Step <1>5 prevents cancellation.
:::

<1>7. Therefore
\[
\boxed{
f(z)=\infty
\iff
z-\frac13\in\mathbb Z}.
\]

::: {.proof}
This is step <1>6.
:::

## Growth in the horizontal tails

Let
\[
z=x+iy.
\]

<1>8. One has
\[
\boxed{
|\sin(\pi z)|^2
=
\sin^2(\pi x)
+
\sinh^2(\pi y)}.
\]

::: {.proof}
Using
\[
\sin(a+ib)
=
\sin a\,\cosh b
+
i\cos a\,\sinh b,
\]
\[
\begin{aligned}
|\sin(a+ib)|^2
&=
\sin^2a\,\cosh^2b
+
\cos^2a\,\sinh^2b\\
&=
\sin^2a(1+\sinh^2b)
+
\cos^2a\,\sinh^2b\\
&=
\sin^2a+\sinh^2b.
\end{aligned}
\]
Set
\[
a=\pi x,
\qquad
b=\pi y.
\]
:::

<1>9. Likewise,
\[
\boxed{
\left|
\sin\!\left(
\pi(z-\tfrac13)
\right)
\right|^2
=
\sin^2\!\left(
\pi(x-\tfrac13)
\right)
+
\sinh^2(\pi y)}.
\]

::: {.proof}
Apply step <1>8 with \(x\) replaced by \(x-\tfrac13\).
:::

Assume now
\[
|y|\ge1.
\]

<1>10. The numerator satisfies
\[
|\sin(\pi z)|^2
\le
1+\sinh^2(\pi y).
\]

::: {.proof}
Since
\[
\sin^2(\pi x)\le1,
\]
apply step <1>8.
:::

<1>11. The denominator satisfies
\[
\left|
\sin\!\left(
\pi(z-\tfrac13)
\right)
\right|^2
\ge
\sinh^2(\pi y).
\]

::: {.proof}
The sine-squared term in step <1>9 is nonnegative.
:::

<1>12. Therefore
\[
\left|
\frac{\sin(\pi z)}
{\sin\!\left(\pi(z-\tfrac13)\right)}
\right|^2
\le
1+\frac1{\sinh^2(\pi y)}.
\]

::: {.proof}
Divide the upper bound in step <1>10 by the lower bound in step <1>11.
:::

<1>13. Since
\[
|y|\ge1,
\]
one has
\[
|\sinh(\pi y)|
\ge
\sinh\pi.
\]

::: {.proof}
The function \(|\sinh t|\) is increasing in \(|t|\) for \(|t|\ge0\).
:::

<1>14. Hence
\[
1+\frac1{\sinh^2(\pi y)}
\le
1+\frac1{\sinh^2\pi}
=
\coth^2\pi.
\]

::: {.proof}
The inequality uses step <1>13. The identity
\[
1+\operatorname{csch}^2\pi
=
\coth^2\pi
\]
is the hyperbolic identity
\[
\cosh^2\pi-\sinh^2\pi=1
\]
divided by \(\sinh^2\pi\).
:::

<1>15. Therefore
\[
\boxed{
\left|
\frac{\sin(\pi z)}
{\sin\!\left(\pi(z-\tfrac13)\right)}
\right|
\le
\coth\pi}.
\]

::: {.proof}
Take nonnegative square roots in steps <1>12--<1>14.
:::

<1>16. Multiplying by \(\tanh\pi\),
\[
\boxed{
|f(x+iy)|\le1}
\]
whenever
\[
|y|\ge1.
\]

::: {.proof}
By definition,
\[
|f(z)|
=
\tanh\pi
\left|
\frac{\sin(\pi z)}
{\sin\!\left(\pi(z-\tfrac13)\right)}
\right|.
\]
Use step <1>15 and
\[
\tanh\pi\cdot\coth\pi=1.
\]
:::

<1>17. Q.E.D.

::: {.proof}
Step <1>3 proves the zero set, step <1>7 proves the pole set, and step <1>16 proves the required bound.
:::
:::
