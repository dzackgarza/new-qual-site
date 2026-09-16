---
schema: qual/card@1
id: PR-PELLF
kind: proposition
title: Logarithm from the upper half-disc to a half-strip
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
relations: []
review: draft
---

::: {.proposition}
Let $\Log$ be the [[D-4CSPM|principal branch]] of the logarithm.
The map
$$
F\colon\ts{z\st\abs{z}<1,\ \Im z>0}\to\ts{w\st\Re w<0,\ 0<\Im w<\pi},\qquad F(z)=\Log z,
$$
is a [[D-TM4TE|biholomorphism]], with inverse $w\mapsto e^w$.
:::

::: {.proof}
For $z=re^{i\theta}$ with $0<r<1$ and $0<\theta<\pi$, $\Log z=\ln r+i\theta$ with $\ln r<0$.
Since $r\mapsto\ln r$ is a bijection $(0,1)\to(-\infty,0)$, $F$ is a bijection onto the half-strip, and $e^{\ln r+i\theta}=re^{i\theta}$ gives the inverse, which is holomorphic.
:::

::: {.example}
The same computation, with $\ln r$ ranging over $(-\infty,0)$ or $(0,\infty)$ and $\theta$ over $(0,\pi)$ or $(-\pi,0)$, shows that $\Log$ maps

- $\ts{\abs{z}<1,\ \Im z>0}$ onto the half-strip $\ts{\Re w<0,\ 0<\Im w<\pi}$ in the second quadrant,
- $\ts{\abs{z}<1,\ \Im z<0}$ onto the half-strip $\ts{\Re w<0,\ -\pi<\Im w<0}$ in the third quadrant,
- $\ts{\abs{z}>1,\ \Im z>0}$ onto the half-strip $\ts{\Re w>0,\ 0<\Im w<\pi}$ in the first quadrant,
- $\ts{\abs{z}>1,\ \Im z<0}$ onto the half-strip $\ts{\Re w>0,\ -\pi<\Im w<0}$ in the fourth quadrant.
:::

::: {.remark}
On the boundary of the upper half-disc, the segment $(0,1)$ maps onto $(-\infty,0)$, the semicircle $\ts{e^{i\theta}\st0<\theta<\pi}$ maps onto the segment from $0$ to $i\pi$, and the segment $(-1,0)$ maps onto the line $\ts{t+i\pi\st t<0}$.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_17-56-47.png)
:::
