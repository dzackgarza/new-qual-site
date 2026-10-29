---
schema: qual/card@1
id: P-UCLARA17F-07
kind: problem
title: Meromorphic function with zeros at $\ZZ$ and poles at $\ZZ+\frac13$
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
Problem 7. Prove that there exists a meromorphic function $f$ on $\CC$ with the following three properties:

1. $f(z)=0$ if and only if $z\in\ZZ$;
2. $f(z)=\infty$ if and only if $z-\frac13\in\ZZ$;
3. $|f(x+iy)|\le1$ for all $x\in\RR$ and all $y\in\RR$ with $|y|\ge1$.
:::

::: {.solution}

Define
$$
\boxed{
f(z)
=
\tanh(\pi)\,
\frac{\sin(\pi z)}
{\sin\!\left(\pi(z-\frac13)\right)}}.
$$

We verify the three required properties.

## Zeros

::: pf

::: pf-step

The numerator vanishes exactly at
$$
\boxed{z\in\ZZ}.
$$


::: pf-proof

The zeros of $\sin(\pi z)$ are exactly the integers.

:::

:::

::: {.pf-step #s1-2}

For every $n\in\ZZ$,
$$
\sin\!\left(
\pi\left(n-\frac13\right)
\right)
\ne0.
$$


::: pf-proof

One has
$$
n-\frac13\notin\ZZ.
$$
Since $\sin(\pi w)=0$ exactly when $w\in\ZZ$, the denominator is nonzero at $z=n$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
f(z)=0
\iff
z\in\ZZ}.
$$


::: pf-proof

The prefactor $\tanh\pi$ is nonzero, and step [](#s1-2){.pf-ref} shows no numerator zero is canceled by a denominator zero.

:::

:::

::: pf-step

The denominator vanishes exactly when
$$
\boxed{
z-\frac13\in\ZZ}.
$$


::: pf-proof

$$
\sin\!\left(
\pi(z-\tfrac13)
\right)=0
$$
if and only if
$$
z-\tfrac13\in\ZZ.
$$

:::

:::

::: {.pf-step #s1-5}

If
$$
z=n+\frac13,
\qquad
n\in\ZZ,
$$
then the numerator is nonzero.


::: pf-proof

$$
\sin\!\left(
\pi\left(n+\frac13\right)
\right)
=
(-1)^n\sin\frac{\pi}{3}
=
(-1)^n\frac{\sqrt3}{2}
\ne0.
$$

:::

:::

::: {.pf-step #s1-6}

Hence every point
$$
n+\frac13
$$
is a genuine simple pole of $f$, and there are no other poles.


::: pf-proof

The zeros of the denominator are simple because
$$
\frac{d}{dz}
\sin\!\left(
\pi(z-\tfrac13)
\right)
=
\pi
\cos\!\left(
\pi(z-\tfrac13)
\right),
$$
which equals $\pm\pi$ at those zeros. Step [](#s1-5){.pf-ref} prevents cancellation.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
f(z)=\infty
\iff
z-\frac13\in\ZZ}.
$$


::: pf-proof

This is step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

One has
$$
\boxed{
|\sin(\pi z)|^2
=
\sin^2(\pi x)
+
\sinh^2(\pi y)}.
$$


::: pf-proof

Using
$$
\sin(a+ib)
=
\sin a\,\cosh b
+
i\cos a\,\sinh b,
$$
$$
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
$$
Set
$$
a=\pi x,
\qquad
b=\pi y.
$$

:::

:::

::: {.pf-step #s1-9}

Likewise,
$$
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
$$


::: pf-proof

Apply step [](#s1-8){.pf-ref} with $x$ replaced by $x-\tfrac13$.

:::

:::

::: {.pf-step #s1-10}

The numerator satisfies
$$
|\sin(\pi z)|^2
\le
1+\sinh^2(\pi y).
$$


::: pf-proof

Since
$$
\sin^2(\pi x)\le1,
$$
apply step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

The denominator satisfies
$$
\left|
\sin\!\left(
\pi(z-\tfrac13)
\right)
\right|^2
\ge
\sinh^2(\pi y).
$$


::: pf-proof

The sine-squared term in step [](#s1-9){.pf-ref} is nonnegative.

:::

:::

::: {.pf-step #s1-12}

Therefore
$$
\left|
\frac{\sin(\pi z)}
{\sin\!\left(\pi(z-\tfrac13)\right)}
\right|^2
\le
1+\frac1{\sinh^2(\pi y)}.
$$


::: pf-proof

Divide the upper bound in step [](#s1-10){.pf-ref} by the lower bound in step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Since
$$
|y|\ge1,
$$
one has
$$
|\sinh(\pi y)|
\ge
\sinh\pi.
$$


::: pf-proof

The function $|\sinh t|$ is increasing in $|t|$ for $|t|\ge0$.

:::

:::

::: {.pf-step #s1-14}

Hence
$$
1+\frac1{\sinh^2(\pi y)}
\le
1+\frac1{\sinh^2\pi}
=
\coth^2\pi.
$$


::: pf-proof

The inequality uses step [](#s1-13){.pf-ref}. The identity
$$
1+\operatorname{csch}^2\pi
=
\coth^2\pi
$$
is the hyperbolic identity
$$
\cosh^2\pi-\sinh^2\pi=1
$$
divided by $\sinh^2\pi$.

:::

:::

::: {.pf-step #s1-15}

Therefore
$$
\boxed{
\left|
\frac{\sin(\pi z)}
{\sin\!\left(\pi(z-\tfrac13)\right)}
\right|
\le
\coth\pi}.
$$


::: pf-proof

Take nonnegative square roots in steps [](#s1-12){.pf-ref} through [](#s1-14){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

Multiplying by $\tanh\pi$,
$$
\boxed{
|f(x+iy)|\le1}
$$
whenever
$$
|y|\ge1.
$$


::: pf-proof

By definition,
$$
|f(z)|
=
\tanh\pi
\left|
\frac{\sin(\pi z)}
{\sin\!\left(\pi(z-\tfrac13)\right)}
\right|.
$$
Use step [](#s1-15){.pf-ref} and
$$
\tanh\pi\cdot\coth\pi=1.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the zero set, step [](#s1-7){.pf-ref} proves the pole set, and step [](#s1-16){.pf-ref} proves the required bound.

:::

:::

:::
