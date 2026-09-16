---
schema: qual/card@1
id: PR-SF23E
kind: proposition
title: Logarithm from the slit plane to a horizontal strip
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
F\colon\CC\sm(-\infty,0]\to\ts{w\st-\pi<\Im w<\pi},\qquad F(z)=\Log z,
$$
is a [[D-TM4TE|biholomorphism]], with inverse $w\mapsto e^w$.
It maps each circle $\ts{\abs{z}=R}$, with the point $-R$ removed, onto the vertical segment $\ts{\ln R+it\st-\pi<t<\pi}$, and each ray $\ts{re^{i\theta}\st r>0}$ with $-\pi<\theta<\pi$ onto the horizontal line $\ts{t+i\theta\st t\in\RR}$.
:::

::: {.proof}
For $z=re^{i\theta}$ with $r>0$ and $-\pi<\theta<\pi$, $\Log z=\ln r+i\theta$.
Since $r\mapsto\ln r$ is a bijection $(0,\infty)\to\RR$, $F$ is a bijection onto the strip, it maps $\ts{r=R}$ and $\ts{\theta=\text{const}}$ as stated, and $e^{\ln r+i\theta}=re^{i\theta}$ gives the holomorphic inverse.
:::

::: {.example}
The same computation shows that $w\mapsto e^w$ maps the strip $\ts{w\st\abs{\Im w}<\pi/2}$ biholomorphically onto the right half-plane $\ts{z\st\Re z>0}$.
:::

::: {.remark}
![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_19-56-51.png)
:::
