---
schema: qual/card@1
id: E-G55QF
kind: problem
title: Mapping $\DD^c \intersect \HH$ to $\HH$ via cross-ratios
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Find a conformal map from $\DD^c \intersect \HH$ to $\HH$ using cross-ratios.
:::

::: {.solution}
The unit circle and the real line both pass through $\pm1$, so a fractional linear transformation sending $-1\mapsto0$ and $1\mapsto\infty$ sends both to lines through $0$.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2022-01-02_19-52-53.png)

::: pf

::: {.pf-step #cross-ratio}
The cross-ratio $f(z)\coloneqq {z+1\over z-1}\cdot{i-1\over i+1} = i\,{z+1\over z-1}$, which sends $(i,-1,1)\mapsto(1,0,\infty)$, maps $\DD^c\intersect\HH$ conformally onto the first quadrant $\theset{w \st \Re w>0,\ \Im w>0}$.

::: pf-proof
The map $f$ is a fractional linear transformation with $f(i)=1$, $f(-1)=0$ and $f(1)=\infty$.
For real $x$ with $\abs x>1$, ${x+1\over x-1}>0$, so $f$ maps the boundary rays $(-\infty,-1)\union(1,\infty)$ into the positive imaginary axis.
The arc of the unit circle in $\HH$ passes through $-1$, $i$, $1$, so its image is a line through $0$ and $1$ ending at $\infty$, namely the positive real axis.
The region is connected with boundary mapped into the two half-axes, and $f(2i)={4+3i\over5}$ lies in the first quadrant, so the image is the first quadrant.
:::

:::

::: pf-step
The map $z\mapsto \boxed{\qty{i\,{z+1\over z-1}}^2}$ sends $\DD^c\intersect\HH$ conformally onto $\HH$.

::: pf-proof
By step [](#cross-ratio){.pf-ref} the first factor maps onto the first quadrant, and $w\mapsto w^2$ maps the first quadrant $0<\Arg w<\pi/2$ bijectively and conformally onto $0<\Arg w<\pi$, which is $\HH$.
:::

:::

:::

:::
