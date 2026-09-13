---
schema: qual/card@1
id: P-BERK84S-20
kind: problem
title: A real-line integral with x sin x over a quadratic denominator
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 20 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the upper-half-plane residue computation and the vanishing of the semicircular contribution.
---

::: {.problem}
Evaluate

$$
\int _ { - \infty } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + 4 x + 2 0 } } d x .
$$
:::


::: {.solution}
Consider
\[
F(z)=\frac{z e^{iz}}{z^2+4z+20}
=\frac{z e^{iz}}{(z+2)^2+16}.
\]
Its poles are $-2\pm4i$.

<1>1. On a large upper semicircle, the contour integral of $F$ tends to zero.
::: {.proof}
Let $C_R$ be the upper semicircle $z=Re^{i\theta}$, $0\le\theta\le\pi$, with $R$ large. Since the denominator is quadratic, there is a constant $K$ such that on $C_R$,
\[
\left|\frac{z}{z^2+4z+20}\right|\le\frac{K}{R}.
\]
Also
\[
|e^{iz}|=e^{-\operatorname{Im}z}=e^{-R\sin\theta}.
\]
Hence
\[
\left|\int_{C_R}F(z)\,dz\right|
\le K\int_0^\pi e^{-R\sin\theta}\,d\theta.
\]
Using $\sin\theta\ge 2\theta/\pi$ on $[0,\pi/2]$ and symmetry,
\[
\int_0^\pi e^{-R\sin\theta}\,d\theta
\le2\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta
\le\frac{\pi}{R}.
\]
Therefore the semicircular integral tends to $0$ as $R\to\infty$.
:::

<1>2. The real-line integral of $F$ equals the residue contribution from $z_0=-2+4i$.
::: {.proof}
By the residue theorem and <1>1,
\[
\int_{-\infty}^{\infty}\frac{x e^{ix}}{x^2+4x+20}\,dx
=2\pi i\operatorname{Res}_{z=-2+4i}F(z).
\]
Since $(z^2+4z+20)'=2z+4$,
\[
\operatorname{Res}_{z=z_0}F(z)
=\frac{z_0e^{iz_0}}{2z_0+4}
=\frac{(-2+4i)e^{i(-2+4i)}}{8i}.
\]
Thus
\[
J:=\int_{-\infty}^{\infty}\frac{x e^{ix}}{x^2+4x+20}\,dx
=\frac{\pi}{4}e^{-4}(-2+4i)e^{-2i}.
\]
:::

<1>3. Taking imaginary parts gives the required integral.
::: {.proof}
Because
\[
e^{-2i}=\cos2-i\sin2,
\]
one has
\[
(-2+4i)e^{-2i}
=(-2\cos2+4\sin2)+i(2\sin2+4\cos2).
\]
Therefore
\[
\operatorname{Im}J
=\frac{\pi}{4}e^{-4}(2\sin2+4\cos2)
=\pi e^{-4}\left(\cos2+\frac12\sin2\right).
\]
Since $\operatorname{Im}(x e^{ix})=x\sin x$,
\[
\boxed{\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+4x+20}\,dx
=\pi e^{-4}\left(\cos2+\frac12\sin2\right)}.
\]
:::
:::
