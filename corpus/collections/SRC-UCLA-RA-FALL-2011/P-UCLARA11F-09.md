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

::: {.solution}
Since \(f\) is holomorphic on the punctured disk, it has a Laurent expansion
\[
\boxed{
f(z)=\sum_{k=-\infty}^{\infty}a_k z^k}
\]
converging on
\[
0<|z|<1.
\]

<1>1. Fix
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

::: {.proof}
Substitute
\[
z=re^{i\theta}
\]
into the Laurent series.
:::

<1>2. The Laurent series converges uniformly on the circle \(|z|=r\).

::: {.proof}
Every compact subset of the annulus
\[
0<|z|<1
\]
lies in a smaller closed annulus on which the Laurent series converges uniformly. A fixed circle is compact.
:::

<1>3. Therefore Parseval's identity gives
\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
|f(re^{i\theta})|^2\,d\theta
=
\sum_{k\in\mathbb Z}
|a_k|^2r^{2k}}.
\]

::: {.proof}
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

<1>4. In polar coordinates,
\[
\int_{\mathbb D^*}|f(z)|^2\,dA(z)
=
\int_0^1
\int_0^{2\pi}
|f(re^{i\theta})|^2
\,r\,d\theta\,dr.
\]

::: {.proof}
The planar area element is
\[
dA=r\,dr\,d\theta.
\]
:::

<1>5. Using step <1>3,
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

::: {.proof}
Substitute the Parseval identity into step <1>4.
:::

<1>6. Since all summands are nonnegative, Tonelli's theorem gives
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

::: {.proof}
Tonelli permits interchange of the sum and integral for nonnegative functions.
:::

<1>7. If
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

::: {.proof}
Substitute \(k=-1\).
:::

<1>8. If
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

::: {.proof}
For any exponent \(a\le-1\),
\[
\int_0^1r^a\,dr
\]
diverges at \(0\).
:::

<1>9. Hence for every
\[
k<0,
\]
the finiteness assumption forces
\[
\boxed{a_k=0}.
\]

::: {.proof}
If some \(a_k\ne0\) with \(k<0\), then the corresponding nonnegative term in the sum in step <1>6 would be
\[
2\pi|a_k|^2\cdot\infty=\infty,
\]
forcing the whole \(L^2\)-integral to diverge.
:::

<1>10. Therefore the Laurent expansion reduces to
\[
\boxed{
f(z)=\sum_{k=0}^{\infty}a_k z^k}
\]
for
\[
0<|z|<1.
\]

::: {.proof}
All negative-power coefficients vanish by step <1>9.
:::

<1>11. The power series
\[
\sum_{k=0}^{\infty}a_k z^k
\]
converges on the whole unit disk.

::: {.proof}
It is the nonnegative part of the Laurent series whose outer radius of convergence is at least \(1\). Thus it converges for every \(|z|<1\), including \(z=0\).
:::

<1>12. Define
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

::: {.proof}
The series is well-defined by step <1>11.
:::

<1>13. The function \(\widetilde f\) is holomorphic on \(\mathbb D\).

::: {.proof}
A power series is holomorphic on its disk of convergence.
:::

<1>14. On the punctured disk,
\[
\boxed{
\widetilde f=f}.
\]

::: {.proof}
For
\[
0<|z|<1,
\]
the defining power series for \(\widetilde f\) is exactly the Laurent series for \(f\) after the negative coefficients were shown to vanish in step <1>10.
:::

<1>15. Therefore \(f\) extends holomorphically across \(0\).

::: {.proof}
The function \(\widetilde f\) from steps <1>12--<1>14 is a holomorphic extension to the whole disk.
:::

<1>16. Q.E.D.

::: {.proof}
Step <1>15 is the required conclusion.
:::
:::
