---
schema: qual/card@1
id: PR-TQDIL
kind: proposition
title: Exponential map from a vertical half-strip to a half-disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
The map
$$
F\colon\ts{z\st\abs{\Re z}<\tfrac\pi2,\ \Im z>0}\to\ts{w\st\abs{w}<1,\ \Re w>0},\qquad F(z)=e^{iz},
$$
is a [[D-TM4TE|biholomorphism]] from the vertical half-strip onto the right half-disc, with inverse $w\mapsto-i\Log w$, where $\Log$ is the [[D-4CSPM|principal branch]] of the logarithm.
:::

::: {.proof}
For $z=x+iy$, $e^{iz}=e^{-y}e^{ix}$.
As $y$ ranges over $(0,\infty)$ the modulus $e^{-y}$ ranges bijectively over $(0,1)$, and as $x$ ranges over $(-\pi/2,\pi/2)$ the argument $x$ ranges over the arguments of points with positive real part.
So $F$ is a bijection onto the right half-disc.
For such $w=\rho e^{ix}$, $-i\Log w=-i(\ln\rho+ix)=x-i\ln\rho=x+iy$ with $y=-\ln\rho$, which is the holomorphic inverse.
:::
