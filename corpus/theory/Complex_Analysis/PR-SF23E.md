---
schema: qual/card@1
id: PR-SF23E
kind: proposition
title: Logarithm from the slit plane to a horizontal strip
slogan: 'The principal logarithm unwraps the slit plane into the strip $-\pi<\Im w<\pi$.'
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
F\colon\CC\sm(-\infty,0]\to\theset{w\st-\pi<\Im w<\pi},\qquad F(z)=\Log z,
$$
is a [[D-TM4TE|biholomorphism]], with inverse $w\mapsto e^w$.
It maps each circle $\theset{\abs{z}=R}$, with the point $-R$ removed, onto the vertical segment $\theset{\ln R+it\st-\pi<t<\pi}$, and each ray $\theset{re^{i\theta}\st r>0}$ with $-\pi<\theta<\pi$ onto the horizontal line $\theset{t+i\theta\st t\in\RR}$.

The map and its image strip are [@SS03, ch. 3, §6, The complex logarithm]: on the slit plane the principal branch is there $\log z=\log r+i\theta$ with $z=re^{i\theta}$ and $\abs\theta<\pi$, which is the $\Log$ above, and the two curve computations are that formula read on a circle and on a ray.
:::

::: {.example}
Since $e^{x+iy}=e^xe^{iy}$, the map $w\mapsto e^w$ maps the strip $\theset{w\st\abs{\Im w}<\pi/2}$ biholomorphically onto the right half-plane $\theset{z\st\Re z>0}$.
:::

::: {.remark}
![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_19-56-51.png)
:::
