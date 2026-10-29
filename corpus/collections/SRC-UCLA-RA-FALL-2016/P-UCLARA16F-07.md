---
schema: qual/card@1
id: P-UCLARA16F-07
kind: problem
title: Reproducing kernel of the Bergman space of the disk
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $H$ be the space of holomorphic functions $f$ on the unit disk $D=\{z\in\CC:|z|<1\}$ such that
$$
\int_D |f(z)|^2\,dA(z)<\infty.
$$
Here integration is with respect to Lebesgue measure $A$ on $D$.
The vector space $H$ is a Hilbert space if equipped with the inner product
$$
\langle f,g\rangle=\int_D f(z)\overline{g(z)}\,dA(z)
$$
for $f,g\in H$.
Fix $z_0\in D$ and define $L_{z_0}(f)=f(z_0)$ for $f\in H$.

(a) Show that $L_{z_0}:H\to\CC$ is a bounded linear functional on $H$.

(b) Find an explicit function $g_{z_0}\in H$ such that
$$
L_{z_0}(f)=f(z_0)=\langle f,g_{z_0}\rangle
$$
for all $f\in H$.
:::

::: {.solution}

## Part (a)

Fix
$$
z_0\in D.
$$
Choose
$$
r=\frac{1-|z_0|}{2}>0.
$$
Then
$$
\overline{D(z_0,r)}\subset D.
$$

::: pf

::: pf-step

For every $f\in H$,
$$
|f(z_0)|^2
\le
\frac1{\pi r^2}
\int_{D(z_0,r)}
|f(z)|^2\,dA(z).
$$


::: pf-proof

The function $|f|^2$ is subharmonic. Apply the subharmonic mean-value inequality on the disk $D(z_0,r)$.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
|f(z_0)|^2
\le
\frac1{\pi r^2}
\|f\|_H^2.
$$


::: pf-proof

The integral over $D(z_0,r)$ is bounded above by the integral over the whole unit disk $D$.

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\boxed{
|L_{z_0}(f)|
\le
\frac1{\sqrt\pi\,r}\,
\|f\|_H}.
$$


::: pf-proof

Take square roots in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Thus $L_{z_0}$ is bounded.


::: pf-proof

Step [](#s1-3){.pf-ref} gives a finite operator-norm bound.

:::

:::

::: {.pf-step #s1-5}

The functional $L_{z_0}$ is linear.


::: pf-proof

For scalars $a,b$ and functions $f,g\in H$,
$$
L_{z_0}(af+bg)
=
af(z_0)+bg(z_0)
=
aL_{z_0}(f)+bL_{z_0}(g).
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
L_{z_0}:H\to\CC
\text{ is a bounded linear functional}.}
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

For integers $m,n\ge0$,
$$
\boxed{
\int_D
z^n\overline z^{\,m}\,dA(z)
=
\begin{cases}
0,&n\ne m,\\[4pt]
\dfrac{\pi}{n+1},&n=m.
\end{cases}}
$$


::: pf-proof

Use polar coordinates
$$
z=re^{i\theta},
\qquad
dA=r\,dr\,d\theta.
$$
Then
$$
z^n\overline z^{\,m}
=
r^{n+m}e^{i(n-m)\theta}.
$$
Thus
$$
\int_0^{2\pi}e^{i(n-m)\theta}\,d\theta
=
0
$$
if $n\ne m$, while for $n=m$,
$$
\int_D|z|^{2n}\,dA
=
2\pi\int_0^1r^{2n+1}\,dr
=
\frac{\pi}{n+1}.
$$

:::

:::

::: {.pf-step #s1-8}

Consequently,
$$
\boxed{
\|f\|_H^2
=
\pi
\sum_{n=0}^{\infty}
\frac{|a_n|^2}{n+1}}.
$$


::: pf-proof

For $0<\rho<1$, uniform convergence of the Taylor series on $|z|\le\rho$ and step [](#s1-7){.pf-ref} give
$$
\int_{|z|<\rho}|f(z)|^2\,dA
=
\pi
\sum_{n=0}^{\infty}
\frac{|a_n|^2}{n+1}
\rho^{2n+2}.
$$
Let $\rho\uparrow1$. The left-hand side increases to $\|f\|_H^2$, while the right-hand side increases termwise to the displayed series. Apply monotone convergence to the nonnegative sums.

:::

:::

::: {.pf-step #s1-9}

The power-series expansion is
$$
\boxed{
g_{z_0}(z)
=
\frac1\pi
\sum_{n=0}^{\infty}
(n+1)\overline{z_0}^{\,n}z^n}.
$$


::: pf-proof

For
$$
|w|<1,
$$
differentiate the geometric series:
$$
\frac1{1-w}
=
\sum_{n=0}^{\infty}w^n.
$$
This gives
$$
\frac1{(1-w)^2}
=
\sum_{n=0}^{\infty}(n+1)w^n.
$$
Set
$$
w=\overline{z_0}z.
$$
Since $|z_0|<1$ and $|z|<1$, one has $|w|<1$.

:::

:::

::: {.pf-step #s1-10}

The function $g_{z_0}$ belongs to $H$.


::: pf-proof

Its Taylor coefficients are
$$
b_n
=
\frac{n+1}{\pi}\overline{z_0}^{\,n}.
$$
Using step [](#s1-8){.pf-ref},
$$
\begin{aligned}
\|g_{z_0}\|_H^2
&=
\pi
\sum_{n=0}^{\infty}
\frac{|b_n|^2}{n+1}\\
&=
\frac1\pi
\sum_{n=0}^{\infty}
(n+1)|z_0|^{2n}.
\end{aligned}
$$
Since $|z_0|<1$,
$$
\sum_{n=0}^{\infty}
(n+1)|z_0|^{2n}
=
\frac1{(1-|z_0|^2)^2}
<
\infty.
$$
Thus $g_{z_0}\in H$.

:::

:::

::: {.pf-step #s1-11}

One has
$$
\boxed{
\langle f,g_{z_0}\rangle
=
\sum_{n=0}^{\infty}
a_n z_0^n}.
$$


::: pf-proof

By steps [](#s1-7){.pf-ref} through [](#s1-9){.pf-ref},
$$
\begin{aligned}
\langle f,g_{z_0}\rangle
&=
\int_D
\left(
\sum_{n\ge0}a_nz^n
\right)
\overline{
\left(
\frac1\pi
\sum_{m\ge0}(m+1)\overline{z_0}^{\,m}z^m
\right)
}
\,dA\\
&=
\frac1\pi
\sum_{n,m\ge0}
a_n(m+1)z_0^m
\int_D
z^n\overline z^{\,m}\,dA.
\end{aligned}
$$
Orthogonality from step [](#s1-7){.pf-ref} kills all terms except $n=m$, and the surviving factor is
$$
\frac1\pi
a_n(n+1)z_0^n
\frac{\pi}{n+1}
=
a_nz_0^n.
$$
The series converges absolutely by Cauchy--Schwarz with the coefficient norm from step [](#s1-8){.pf-ref} and the finite norm from step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Since
$$
f(z_0)
=
\sum_{n=0}^{\infty}
a_n z_0^n,
$$
one obtains
$$
\boxed{
f(z_0)
=
\langle f,g_{z_0}\rangle}.
$$


::: pf-proof

The Taylor series of an entire-on-the-disk holomorphic function converges to $f$ at every $z_0\in D$. Combine this with step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Therefore the reproducing vector is
$$
\boxed{
g_{z_0}(z)
=
\frac1{\pi(1-\overline{z_0}z)^2}}.
$$


::: pf-proof

Step [](#s1-10){.pf-ref} shows this function belongs to $H$, and step [](#s1-12){.pf-ref} proves the reproducing identity.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves part (a), and step [](#s1-13){.pf-ref} proves part (b).

:::

:::

:::
