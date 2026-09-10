---
schema: qual/card@1
id: E-SS2.EX-3
kind: problem
title: "SS 2.3: Laplace transforms of sine and cosine via sector contours"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
3. Evaluate the integrals

$$
\int_ {0} ^ {\infty} e ^ {- a x} \cos b x d x \quad \text { and } \quad \int_ {0} ^ {\infty} e ^ {- a x} \sin b x d x, \quad a > 0
$$

by integrating $e ^ { - A z } , A = { \sqrt { a ^ { 2 } + b ^ { 2 } } }$ , over an appropriate sector with angle $\omega ,$ with cos $\omega = a / A$
:::

::: solution
Let
\[
A=\sqrt{a^2+b^2},
\qquad
\cos\omega=\frac aA,
\qquad
\sin\omega=\frac bA,
\]
with $|\omega|<\pi/2$ because $a>0$. Then
\[
Ae^{-i\omega}=a-ib.
\]
Integrate the entire function $e^{-Az}$ around the sector bounded by the positive real axis, the ray $\arg z=-\omega$, and a circular arc of radius $R$ joining them. Along every point of this arc the real part of $z$ is bounded below by a positive constant times $R$ away from the endpoints, and the usual sector estimate gives that the arc integral tends to $0$ as $R\to\infty$.

The two radial sides therefore give
\[
\int_0^\infty e^{-Ax}\,dx
=e^{-i\omega}\int_0^\infty e^{-Ae^{-i\omega}x}\,dx.
\]
Since the left side is $1/A$,
\[
\int_0^\infty e^{-(a-ib)x}\,dx
=\frac{e^{i\omega}}A
=\frac{a+ib}{a^2+b^2}.
\]
But
\[
e^{-(a-ib)x}=e^{-ax}(\cos bx+i\sin bx).
\]
Taking real and imaginary parts yields
\[
\boxed{\displaystyle
\int_0^\infty e^{-ax}\cos bx\,dx=\frac{a}{a^2+b^2}},
\qquad
\boxed{\displaystyle
\int_0^\infty e^{-ax}\sin bx\,dx=\frac{b}{a^2+b^2}}.
\]
:::
