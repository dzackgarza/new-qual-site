---
schema: qual/card@1
id: PR-IK6LA
kind: proposition
title: Disc complement to slit plane
slogan: 'The Joukowski map $z+z^{-1}$ sends the exterior unit disc biholomorphically onto the plane slit along $[-2,2]$.'
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
\begin{aligned}
F\colon \theset{z\in\CC : \abs{z}>1} &\to \CC\sm[-2, 2], \\
z &\mapsto z+ \inverseof{z}
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]].

This is the correspondence (15) of [@Ahl73, ch. 3, §4.2, A Survey of Elementary Mappings], where the region exterior to the segment $[-1,1]$ is mapped onto $\abs w<1$ by $z=\frac12(w+1/w)$, and the section notes that changing the sign of the square root gives the mapping onto $\abs w>1$. Doubling the scale, $z\mapsto z+1/z$ carries $\abs z>1$ onto the complement of $[-2,2]$, which is the card's statement.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-12-10_17-47-48.png)
:::
