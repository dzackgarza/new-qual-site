---
schema: qual/card@1
id: P-FBY23
kind: problem
title: Cauchy integral formula for $\oint_\gamma z^2/(z-i)\,dz$ on a circle about
  $i$
classification:
  areas:
  - prelim
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
a. State the Cauchy integral formula and use it to evaluate the complex line integral: $\oint_\gamma z^2/(z-i)\, dz$, where $\gamma$ is a circle centered at $i$ and oriented counterclockwise.
b. Use a parametrization of the path $\gamma$ to express the line integral explicitly in terms of real integrals, with limits of integration.
[You do not have to evaluate these real integrals.]
:::

::: {.solution}
Cauchy's integral formula states that if $f$ is holomorphic on and inside a positively oriented simple closed contour $\gamma$, and $a$ lies inside $\gamma$, then
\[
\oint_\gamma \frac{f(z)}{z-a}\,dz=2\pi i\,f(a).
\]
Taking $f(z)=z^2$ and $a=i$ gives
\[
\oint_\gamma \frac{z^2}{z-i}\,dz
=2\pi i\,i^2
=-2\pi i.
\]

Let the circle have radius $R>0$. A counterclockwise parametrization is
\[
z(t)=i+Re^{it},\qquad 0\le t\le2\pi,
\]
with
\[
dz=iRe^{it}\,dt.
\]
Therefore
\[
\oint_\gamma \frac{z^2}{z-i}\,dz
=\int_0^{2\pi} i\bigl(i+Re^{it}\bigr)^2\,dt.
\]
Writing $e^{it}=\cos t+i\sin t$, this becomes
\[
\int_0^{2\pi}
\Bigl[-2R\cos t\,(1+R\sin t)
+i\bigl(R^2\cos^2t-(1+R\sin t)^2\bigr)\Bigr]dt,
\]
which is an explicit expression in real integrals with limits of integration.
:::
