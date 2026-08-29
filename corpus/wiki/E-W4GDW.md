---
schema: qual/card@1
id: E-W4GDW
kind: exercise
title: A conformal map from $\HH$ onto $\{-\pi/2<\Re w<\pi/2,\,\Im w>0\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Trigonometry
relations: []
review: draft
---

:::{.problem}
Find the conformal map that takes the upper half-plane conformally onto the half-strip 
\[
\ts{w=x+iy \st -\pi/2 < x < \pi/2,\, y>0}
.\]
:::

:::{.solution}
It's well known that $z\mapsto \sin(z)$ sends $-\pi/2<\Re(z) < \pi/2$ with $\Im(z) > 0$ to $\HH$:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-31_23-37-00.png)

So take $z\mapsto \arcsin(z)$.

:::



