---
schema: qual/card@1
id: PR-PELLF
kind: proposition
title: Logarithm from the upper half-disc to a half-strip
slogan: 'The principal logarithm sends the upper half-disc to the half-strip $\Re w<0$, $0<\Im w<\pi$.'
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
F\colon\theset{z\st\abs{z}<1,\ \Im z>0}\to\theset{w\st\Re w<0,\ 0<\Im w<\pi},\qquad F(z)=\Log z,
$$
is a [[D-TM4TE|biholomorphism]], with inverse $w\mapsto e^w$.
:::

::: {.example}
Since $\Log(re^{i\theta})=\ln r+i\theta$, with $\ln r$ ranging over $(-\infty,0)$ or $(0,\infty)$ and $\theta$ over $(0,\pi)$ or $(-\pi,0)$, $\Log$ maps

- $\theset{\abs{z}<1,\ \Im z>0}$ onto the half-strip $\theset{\Re w<0,\ 0<\Im w<\pi}$ in the second quadrant,
- $\theset{\abs{z}<1,\ \Im z<0}$ onto the half-strip $\theset{\Re w<0,\ -\pi<\Im w<0}$ in the third quadrant,
- $\theset{\abs{z}>1,\ \Im z>0}$ onto the half-strip $\theset{\Re w>0,\ 0<\Im w<\pi}$ in the first quadrant,
- $\theset{\abs{z}>1,\ \Im z<0}$ onto the half-strip $\theset{\Re w>0,\ -\pi<\Im w<0}$ in the fourth quadrant.
:::

::: {.remark}
On the boundary of the upper half-disc, the segment $(0,1)$ maps onto $(-\infty,0)$, the semicircle $\theset{e^{i\theta}\st0<\theta<\pi}$ maps onto the segment from $0$ to $i\pi$, and the segment $(-1,0)$ maps onto the line $\theset{t+i\pi\st t<0}$.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_17-56-47.png)
:::
