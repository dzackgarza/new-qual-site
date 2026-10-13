---
schema: qual/card@1
id: P-UCLARA11F-07
kind: problem
title: A contour integral with a double pole
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
Compute
\[
\int_0^\infty \frac{\cos x}{(1+x^2)^2}\,dx.
\]
:::

::: {.solution}
Consider
\[
F(z)=\frac{e^{iz}}{(1+z^2)^2}
=
\frac{e^{iz}}{(z-i)^2(z+i)^2}.
\]

<1>1. Integrate \(F\) over the positively oriented contour consisting of
\[
[-R,R]
\]
and the upper semicircle
\[
\Gamma_R=\{Re^{i\theta}:0\le\theta\le\pi\}.
\]

::: {.proof}
This is the standard upper-half-plane contour for the exponential \(e^{iz}\), whose modulus decays there.
:::

<1>2. The only pole of \(F\) inside the contour is
\[
\boxed{z=i},
\]
and it is a double pole.

::: {.proof}
The denominator factors as
\[
(z-i)^2(z+i)^2.
\]
The pole at \(-i\) lies in the lower half-plane.
:::

<1>3. The residue at \(z=i\) is
\[
\operatorname{Res}_{z=i}F
=
\left.
\frac{d}{dz}
\left(
\frac{e^{iz}}{(z+i)^2}
\right)
\right|_{z=i}.
\]

::: {.proof}
For a double pole,
\[
\operatorname{Res}_{z=i}
\frac{h(z)}{(z-i)^2}
=
h'(i),
\]
with
\[
h(z)=\frac{e^{iz}}{(z+i)^2}.
\]
:::

<1>4. Differentiate:
\[
\frac{d}{dz}
\left(
\frac{e^{iz}}{(z+i)^2}
\right)
=
\frac{i e^{iz}}{(z+i)^2}
-
\frac{2e^{iz}}{(z+i)^3}.
\]

::: {.proof}
Apply the product rule to
\[
e^{iz}(z+i)^{-2}.
\]
:::

<1>5. At \(z=i\),
\[
e^{iz}=e^{-1}
\]
and
\[
z+i=2i.
\]

::: {.proof}
\[
e^{i\cdot i}=e^{-1}.
\]
:::

<1>6. Hence
\[
\begin{aligned}
\operatorname{Res}_{z=i}F
&=
\frac{i e^{-1}}{(2i)^2}
-
\frac{2e^{-1}}{(2i)^3}\\
&=
-\frac{i}{4e}
-\frac{i}{4e}\\
&=
\boxed{-\frac{i}{2e}}.
\end{aligned}
\]

::: {.proof}
Use
\[
(2i)^2=-4,
\qquad
(2i)^3=-8i.
\]
Then
\[
\frac{i}{-4}
=
-\frac i4,
\]
and
\[
-\frac{2}{-8i}
=
\frac1{4i}
=
-\frac i4.
\]
:::

<1>7. On the upper semicircle,
\[
|e^{iz}|
=
e^{-\operatorname{Im}z}
\le1.
\]

::: {.proof}
If
\[
z=x+iy
\]
with \(y\ge0\), then
\[
|e^{iz}|
=
|e^{ix-y}|
=
e^{-y}
\le1.
\]
:::

<1>8. For \(R>2\) and \(z\in\Gamma_R\),
\[
|1+z^2|
\ge
R^2-1.
\]

::: {.proof}
By the reverse triangle inequality,
\[
|1+z^2|
\ge
\bigl||z|^2-1\bigr|
=
R^2-1.
\]
:::

<1>9. Therefore
\[
\left|
\int_{\Gamma_R}F(z)\,dz
\right|
\le
\frac{\pi R}{(R^2-1)^2}
\longrightarrow0.
\]

::: {.proof}
The length of \(\Gamma_R\) is \(\pi R\). Combine steps <1>7--<1>8 with the \(ML\)-estimate.
:::

<1>10. By the residue theorem,
\[
\int_{-R}^{R}
\frac{e^{ix}}{(1+x^2)^2}\,dx
+
\int_{\Gamma_R}F(z)\,dz
=
2\pi i
\left(
-\frac{i}{2e}
\right).
\]

::: {.proof}
Use the residue from step <1>6.
:::

<1>11. Letting \(R\to\infty\),
\[
\boxed{
\int_{-\infty}^{\infty}
\frac{e^{ix}}{(1+x^2)^2}\,dx
=
\frac{\pi}{e}}.
\]

::: {.proof}
The semicircle term vanishes by step <1>9, and
\[
2\pi i
\left(
-\frac{i}{2e}
\right)
=
\frac{\pi}{e}.
\]
:::

<1>12. Taking real parts,
\[
\boxed{
\int_{-\infty}^{\infty}
\frac{\cos x}{(1+x^2)^2}\,dx
=
\frac{\pi}{e}}.
\]

::: {.proof}
The denominator is real on the real axis, so the real part of the integrand in step <1>11 is
\[
\frac{\cos x}{(1+x^2)^2}.
\]
:::

<1>13. The integrand in step <1>12 is even.

::: {.proof}
Both \(\cos x\) and \((1+x^2)^2\) are even functions.
:::

<1>14. Hence
\[
2
\int_0^\infty
\frac{\cos x}{(1+x^2)^2}\,dx
=
\frac{\pi}{e}.
\]

::: {.proof}
The integral over the whole real line of an even integrable function is twice the integral over \([0,\infty)\).
:::

<1>15. Therefore
\[
\boxed{
\int_0^\infty
\frac{\cos x}{(1+x^2)^2}\,dx
=
\frac{\pi}{2e}}.
\]

::: {.proof}
Divide step <1>14 by \(2\).
:::

<1>16. Q.E.D.

::: {.proof}
Step <1>15 is the requested value.
:::
:::
