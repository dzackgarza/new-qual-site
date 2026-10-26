---
schema: qual/card@1
id: P-UCLARA11F-09
kind: problem
title: L2 integrability removes a punctured-disc singularity
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Suppose $f$ is holomorphic on the punctured unit disc $\mathbb D^*=\mathbb D\setminus\{0\}$ and
\[
\int_{\mathbb D^*}|f(z)|^2\,dA(z)<\infty,
\]
where $dA$ is two-dimensional Lebesgue measure.
Show that $f$ extends holomorphically to the unit disc $\mathbb D$.
:::

Since \(f\) is holomorphic on the punctured disk, it has a Laurent expansion
\[
\boxed{
f(z)=\sum_{k=-\infty}^{\infty}a_k z^k}
\]
converging on
\[
0<|z|<1.
\]

::: pf

::: pf-step

Fix
\[
0<r<1.
\]
On the circle \(|z|=r\),
\[
f(re^{i\theta})
=
\sum_{k\in\mathbb Z}
a_k r^k e^{ik\theta}.
\]


::: pf-proof

Substitute
\[
z=re^{i\theta}
\]
into the Laurent series.

:::

:::

::: pf-step

The Laurent series converges uniformly on the circle \(|z|=r\).


::: pf-proof

Every compact subset of the annulus
\[
0<|z|<1
\]
lies in a smaller closed annulus on which the Laurent series converges uniformly. A fixed circle is compact.

:::

:::

::: pf-step

Therefore Parseval's identity gives
\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
|f(re^{i\theta})|^2\,d\theta
=
\sum_{k\in\mathbb Z}
|a_k|^2r^{2k}}.
\]


::: pf-proof

For fixed \(r\), the function
\[
\theta\mapsto f(re^{i\theta})
\]
has Fourier series with coefficients
\[
a_k r^k.
\]
Uniform convergence permits the usual Fourier/Parseval identity.

:::

:::

::: pf-step

In polar coordinates,
\[
\int_{\mathbb D^*}|f(z)|^2\,dA(z)
=
\int_0^1
\int_0^{2\pi}
|f(re^{i\theta})|^2
\,r\,d\theta\,dr.
\]


::: pf-proof

The planar area element is
\[
dA=r\,dr\,d\theta.
\]

:::

:::

::: pf-step

Using step <1>3,
\[
\int_{\mathbb D^*}|f|^2\,dA
=
2\pi
\int_0^1
\left(
\sum_{k\in\mathbb Z}|a_k|^2r^{2k}
\right)
r\,dr.
\]


::: pf-proof

Substitute the Parseval identity into step <1>4.

:::

:::

::: pf-step

Since all summands are nonnegative, Tonelli's theorem gives
\[
\boxed{
\int_{\mathbb D^*}|f|^2\,dA
=
2\pi
\sum_{k\in\mathbb Z}
|a_k|^2
\int_0^1
r^{2k+1}\,dr},
\]
where the right side may a priori be \(+\infty\).


::: pf-proof

Tonelli permits interchange of the sum and integral for nonnegative functions.

:::

:::

::: pf-step

If
\[
k=-1,
\]
then
\[
\int_0^1r^{2k+1}\,dr
=
\int_0^1\frac{dr}{r}
=
\infty.
\]


::: pf-proof

Substitute \(k=-1\).

:::

:::

::: pf-step

If
\[
k\le-2,
\]
then
\[
2k+1\le-3,
\]
so
\[
\int_0^1r^{2k+1}\,dr=\infty.
\]


::: pf-proof

For any exponent \(a\le-1\),
\[
\int_0^1r^a\,dr
\]
diverges at \(0\).

:::

:::

::: pf-step

Hence for every
\[
k<0,
\]
the finiteness assumption forces
\[
\boxed{a_k=0}.
\]


::: pf-proof

If some \(a_k\ne0\) with \(k<0\), then the corresponding nonnegative term in the sum in step <1>6 would be
\[
2\pi|a_k|^2\cdot\infty=\infty,
\]
forcing the whole \(L^2\)-integral to diverge.

:::

:::

::: pf-step

Therefore the Laurent expansion reduces to
\[
\boxed{
f(z)=\sum_{k=0}^{\infty}a_k z^k}
\]
for
\[
0<|z|<1.
\]


::: pf-proof

All negative-power coefficients vanish by step <1>9.

:::

:::

::: pf-step

The power series
\[
\sum_{k=0}^{\infty}a_k z^k
\]
converges on the whole unit disk.


::: pf-proof

It is the nonnegative part of the Laurent series whose outer radius of convergence is at least \(1\). Thus it converges for every \(|z|<1\), including \(z=0\).

:::

:::

::: pf-step

Define
\[
\boxed{
\widetilde f(z)
=
\sum_{k=0}^{\infty}a_k z^k}
\]
for
\[
|z|<1.
\]


::: pf-proof

The series is well-defined by step <1>11.

:::

:::

::: pf-step

The function \(\widetilde f\) is holomorphic on \(\mathbb D\).


::: pf-proof

A power series is holomorphic on its disk of convergence.

:::

:::

::: pf-step

On the punctured disk,
\[
\boxed{
\widetilde f=f}.
\]


::: pf-proof

For
\[
0<|z|<1,
\]
the defining power series for \(\widetilde f\) is exactly the Laurent series for \(f\) after the negative coefficients were shown to vanish in step <1>10.

:::

:::

::: pf-step

Therefore \(f\) extends holomorphically across \(0\).


::: pf-proof

The function \(\widetilde f\) from steps <1>12--<1>14 is a holomorphic extension to the whole disk.

:::

:::

::: pf-qed

Step <1>15 is the required conclusion.

:::

:::
