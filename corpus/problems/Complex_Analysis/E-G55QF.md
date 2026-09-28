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

::: {.exercise title="$\mathbb{D}^c \intersect \mathbb{H}$ to $\mathbb{H}$"}
Find a conformal map from $\DD^c \intersect \HH$ to $\HH$ using cross-ratios.

:::

::: {.solution}
The unit circle and the real line both pass through $\pm1$, so a fractional linear transformation sending $-1\to0$ and $1\to\infty$ sends both to lines through $0$. Take the cross-ratio sending $(i, -1, 1)\to (1,0,\infty)$:

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2022-01-02_19-52-53.png)

This is the cross-ratio
\[
f(z) = {z+1\over z-1} {i-1\over i+1}
.\]

The image of $\DD^c \intersect \HH$ is the 1st quadrant $\HH \intersect \Re(z) > 0$.
Send this to $\HH$ with $z\mapsto z^2$.
:::
