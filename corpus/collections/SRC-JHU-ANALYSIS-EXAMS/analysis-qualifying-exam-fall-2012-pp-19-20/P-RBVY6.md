---
schema: qual/card@1
id: P-RBVY6
kind: problem
title: 'Residue computation of the Fourier transform of $\frac{1}{x^{2}+1}$'
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Analysis Qualifying Exam, Fall 2012, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
2. Let $\textstyle f ( x ) = { \frac { 1 } { x ^ { 2 } + 1 } }$ . Use residues to compute the Fourier transform

$$
{ \widehat { f } } ( t ) = \int _ { - \infty } ^ { + \infty } f ( x ) e ^ { - i t x } d x ~ .
$$
:::

::: {.solution}
Set
\[
F_t(z)=\frac{e^{-itz}}{z^2+1}.
\]
Its poles are simple, at $z=i$ and $z=-i$.

<1>1. The case $t>0$.
::: {.proof}
Close the contour by the lower semicircle of radius $R>1$, oriented clockwise. If $z=x+iy$ lies in the lower half-plane, then
\[
|e^{-itz}|=e^{ty}\le1.
\]
Hence on the semicircular arc,
\[
|F_t(z)|\le \frac1{R^2-1},
\]
so the arc integral has absolute value at most
\[
\frac{\pi R}{R^2-1}\longrightarrow0.
\]
The only enclosed pole is $z=-i$, and
\[
\operatorname{Res}_{z=-i}F_t(z)
=\frac{e^{-it(-i)}}{-2i}
=-\frac{e^{-t}}{2i}.
\]
Because the contour is clockwise, the residue theorem gives
\[
\int_{-\infty}^{\infty}\frac{e^{-itx}}{1+x^2}\,dx
=-2\pi i\left(-\frac{e^{-t}}{2i}\right)
=\pi e^{-t}.
\]
:::

<1>2. The case $t<0$.
::: {.proof}
Now close the contour by the upper semicircle. Since $t<0$ and $y\ge0$,
\[
|e^{-itz}|=e^{ty}\le1,
\]
so the same arc estimate makes the semicircle contribution tend to zero.
The enclosed pole is $z=i$, with residue
\[
\operatorname{Res}_{z=i}F_t(z)
=\frac{e^{-iti}}{2i}
=\frac{e^t}{2i}.
\]
Thus
\[
\int_{-\infty}^{\infty}\frac{e^{-itx}}{1+x^2}\,dx
=2\pi i\frac{e^t}{2i}
=\pi e^t.
\]
:::

<1>3. The case $t=0$ and the final formula.
::: {.proof}
At $t=0$,
\[
\widehat f(0)=\int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\pi.
\]
Combining the three cases,
\[
\boxed{\widehat f(t)=\pi e^{-|t|}}.
\]
:::
:::
