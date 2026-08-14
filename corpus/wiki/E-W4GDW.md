---
schema: qual/card@1
id: E-W4GDW
kind: exercise
title: "Find the conformal map that takes the upper half-plane conformally ont\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - conformal-maps
  - trigonometry
relations: []
review: draft
---
:::{.problem title="?"}
Find the conformal map that takes the upper half-plane conformally onto the half-strip 
\[
\ts{w=x+iy \st -\pi/2 < x < \pi/2,\, y>0}
.\]
:::

:::{.solution}
It's well known that $z\mapsto \sin(z)$ sends $-\pi/2<\Re(z) < \pi/2$ with $\Im(z) > 0$ to $\HH$:

![](../../assets/30_Complex_Analysis/999_Quals/figures/2021-12-31_23-37-00.png)

So take $z\mapsto \arcsin(z)$.

:::



