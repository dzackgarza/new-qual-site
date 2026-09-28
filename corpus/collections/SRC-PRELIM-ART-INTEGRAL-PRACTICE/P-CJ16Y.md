---
schema: qual/card@1
id: P-CJ16Y
kind: problem
title: Integrals of $\cos(x+\pi/4)\cos(x-\pi/4)$, $\sin(4x)\cos(3x)$, and $\cos x\cos
  2x\sin 3x$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Compute the following indefinite integrals:

1. \(\displaystyle \int \cos\!\left(x+\frac\pi4\right)\cos\!\left(x-\frac\pi4\right)\,dx\).
2. \(\displaystyle \int \sin(4x)\cos(3x)\,dx\).
3. \(\displaystyle \int 4\cos x\cos(2x)\sin(3x)\,dx\).
:::

::: {.solution}
<1>1. Use product-to-sum.
::: {.proof}
\[
\cos\!\left(x+\frac\pi4\right)\cos\!\left(x-\frac\pi4\right)
=\frac12\left(\cos(2x)+\cos\frac\pi2\right)
=\frac12\cos(2x).
\]
Hence
\[
\boxed{\int \cos\!\left(x+\frac\pi4\right)\cos\!\left(x-\frac\pi4\right)\,dx
=\frac14\sin(2x)+C.}
\]
:::

<1>2. Use product-to-sum again.
::: {.proof}
\[
\sin(4x)\cos(3x)=\frac12\bigl(\sin(7x)+\sin x\bigr).
\]
Therefore
\[
\boxed{\int \sin(4x)\cos(3x)\,dx
=-\frac1{14}\cos(7x)-\frac12\cos x+C.}
\]
:::

<1>3. Reduce the triple product.
::: {.proof}
Since
\[
2\cos x\cos(2x)=\cos(3x)+\cos x,
\]
we have
\[
\begin{aligned}
4\cos x\cos(2x)\sin(3x)
&=2\sin(3x)\bigl(\cos(3x)+\cos x\bigr)\\
&=\sin(6x)+\sin(4x)+\sin(2x).
\end{aligned}
\]
Thus
\[
\boxed{\int4\cos x\cos(2x)\sin(3x)\,dx
=-\frac16\cos(6x)-\frac14\cos(4x)-\frac12\cos(2x)+C.}
\]
:::
:::
