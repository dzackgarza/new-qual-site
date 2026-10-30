---
schema: qual/card@1
id: PR-7TLAS
kind: proposition
title: Vertical half-strip to right half-disc
slogan: 'The exponential turns a vertical half-strip into a half-disc by converting height to radius and horizontal position to angle.'
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
Let $S\coloneqq\theset{z\in\CC : -\pi/2<\Re z<\pi/2,\ \Im z>0}$ and $H\coloneqq\DD \intersect \theset{\Re(w) > 0}$.
Then
$$
\begin{aligned}
F\colon S &\to H, \\
z &\mapsto e^{iz}
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]] with inverse $w\mapsto -i\Log(w)$, where $\Log$ is the [[D-4CSPM|principal branch]] of the logarithm.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_18-22-45.png)
:::
