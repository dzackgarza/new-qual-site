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
Let $H$ be the space of holomorphic functions $f$ on the unit disk $D=\{z\in\mathbb C:|z|<1\}$ such that
\[
\int_D |f(z)|^2\,dA(z)<\infty.
\]
Here integration is with respect to Lebesgue measure $A$ on $D$.
The vector space $H$ is a Hilbert space if equipped with the inner product
\[
\langle f,g\rangle=\int_D f(z)\overline{g(z)}\,dA(z)
\]
for $f,g\in H$.
Fix $z_0\in D$ and define $L_{z_0}(f)=f(z_0)$ for $f\in H$.

(a) Show that $L_{z_0}:H\to\mathbb C$ is a bounded linear functional on $H$.

(b) Find an explicit function $g_{z_0}\in H$ such that
\[
L_{z_0}(f)=f(z_0)=\langle f,g_{z_0}\rangle
\]
for all $f\in H$.
:::

::: {.solution}
## Part (a)

Fix
\[
z_0\in D.
\]
Choose
\[
r=\frac{1-|z_0|}{2}>0.
\]
Then
\[
\overline{D(z_0,r)}\subset D.
\]

<1>1. For every \(f\in H\),
\[
|f(z_0)|^2
\le
\frac1{\pi r^2}
\int_{D(z_0,r)}
|f(z)|^2\,dA(z).
\]

::: {.proof}
The function \(|f|^2\) is subharmonic. Apply the subharmonic mean-value inequality on the disk \(D(z_0,r)\).
:::

<1>2. Therefore
\[
|f(z_0)|^2
\le
\frac1{\pi r^2}
\|f\|_H^2.
\]

::: {.proof}
The integral over \(D(z_0,r)\) is bounded above by the integral over the whole unit disk \(D\).
:::

<1>3. Hence
\[
\boxed{
|L_{z_0}(f)|
\le
\frac1{\sqrt\pi\,r}\,
\|f\|_H}.
\]

::: {.proof}
Take square roots in step <1>2.
:::

<1>4. Thus \(L_{z_0}\) is bounded.

::: {.proof}
Step <1>3 gives a finite operator-norm bound.
:::

<1>5. The functional \(L_{z_0}\) is linear.

::: {.proof}
For scalars \(a,b\) and functions \(f,g\in H\),
\[
L_{z_0}(af+bg)
=
af(z_0)+bg(z_0)
=
aL_{z_0}(f)+bL_{z_0}(g).
\]
:::

<1>6. Therefore
\[
\boxed{
L_{z_0}:H\to\mathbb C
\text{ is a bounded linear functional}.}
\]

::: {.proof}
Combine steps <1>4--<1>5.
:::

## Part (b)

Let
\[
f(z)
=
\sum_{n=0}^{\infty}a_n z^n
\]
be the Taylor expansion of \(f\) at \(0\).

<1>7. For integers \(m,n\ge0\),
\[
\boxed{
\int_D
z^n\overline z^{\,m}\,dA(z)
=
\begin{cases}
0,&n\ne m,\\[4pt]
\dfrac{\pi}{n+1},&n=m.
\end{cases}}
\]

::: {.proof}
Use polar coordinates
\[
z=re^{i\theta},
\qquad
dA=r\,dr\,d\theta.
\]
Then
\[
z^n\overline z^{\,m}
=
r^{n+m}e^{i(n-m)\theta}.
\]
Thus
\[
\int_0^{2\pi}e^{i(n-m)\theta}\,d\theta
=
0
\]
if \(n\ne m\), while for \(n=m\),
\[
\int_D|z|^{2n}\,dA
=
2\pi\int_0^1r^{2n+1}\,dr
=
\frac{\pi}{n+1}.
\]
:::

<1>8. Consequently,
\[
\boxed{
\|f\|_H^2
=
\pi
\sum_{n=0}^{\infty}
\frac{|a_n|^2}{n+1}}.
\]

::: {.proof}
For \(0<\rho<1\), uniform convergence of the Taylor series on \(|z|\le\rho\) and step <1>7 give
\[
\int_{|z|<\rho}|f(z)|^2\,dA
=
\pi
\sum_{n=0}^{\infty}
\frac{|a_n|^2}{n+1}
\rho^{2n+2}.
\]
Let \(\rho\uparrow1\). The left-hand side increases to \(\|f\|_H^2\), while the right-hand side increases termwise to the displayed series. Apply monotone convergence to the nonnegative sums.
:::

Define
\[
\boxed{
g_{z_0}(z)
=
\frac1{\pi(1-\overline{z_0}z)^2}}.
\]

<1>9. The power-series expansion is
\[
\boxed{
g_{z_0}(z)
=
\frac1\pi
\sum_{n=0}^{\infty}
(n+1)\overline{z_0}^{\,n}z^n}.
\]

::: {.proof}
For
\[
|w|<1,
\]
differentiate the geometric series:
\[
\frac1{1-w}
=
\sum_{n=0}^{\infty}w^n.
\]
This gives
\[
\frac1{(1-w)^2}
=
\sum_{n=0}^{\infty}(n+1)w^n.
\]
Set
\[
w=\overline{z_0}z.
\]
Since \(|z_0|<1\) and \(|z|<1\), one has \(|w|<1\).
:::

<1>10. The function \(g_{z_0}\) belongs to \(H\).

::: {.proof}
Its Taylor coefficients are
\[
b_n
=
\frac{n+1}{\pi}\overline{z_0}^{\,n}.
\]
Using step <1>8,
\[
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
\]
Since \(|z_0|<1\),
\[
\sum_{n=0}^{\infty}
(n+1)|z_0|^{2n}
=
\frac1{(1-|z_0|^2)^2}
<
\infty.
\]
Thus \(g_{z_0}\in H\).
:::

<1>11. One has
\[
\boxed{
\langle f,g_{z_0}\rangle
=
\sum_{n=0}^{\infty}
a_n z_0^n}.
\]

::: {.proof}
By steps <1>7--<1>9,
\[
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
\]
Orthogonality from step <1>7 kills all terms except \(n=m\), and the surviving factor is
\[
\frac1\pi
a_n(n+1)z_0^n
\frac{\pi}{n+1}
=
a_nz_0^n.
\]
The series converges absolutely by Cauchy--Schwarz with the coefficient norm from step <1>8 and the finite norm from step <1>10.
:::

<1>12. Since
\[
f(z_0)
=
\sum_{n=0}^{\infty}
a_n z_0^n,
\]
one obtains
\[
\boxed{
f(z_0)
=
\langle f,g_{z_0}\rangle}.
\]

::: {.proof}
The Taylor series of an entire-on-the-disk holomorphic function converges to \(f\) at every \(z_0\in D\). Combine this with step <1>11.
:::

<1>13. Therefore the reproducing vector is
\[
\boxed{
g_{z_0}(z)
=
\frac1{\pi(1-\overline{z_0}z)^2}}.
\]

::: {.proof}
Step <1>10 shows this function belongs to \(H\), and step <1>12 proves the reproducing identity.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>6 proves part (a), and step <1>13 proves part (b).
:::
:::
