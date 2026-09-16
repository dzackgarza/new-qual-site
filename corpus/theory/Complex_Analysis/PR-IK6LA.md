---
schema: qual/card@1
id: PR-IK6LA
kind: proposition
title: Disc complement to slit plane
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
z &\mapsto z+ z\inv
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]].

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-12-10_17-47-48.png)
:::

::: {.proof}
For $w\in\CC$, the solutions of $F(z)=w$ are the roots of $z^2-wz+1=0$, whose product is $1$.
If $w\in[-2,2]$, the discriminant $w^2-4\le0$, so the roots are complex conjugates of product $1$ and both lie on the unit circle; hence $F$ maps $\abs{z}>1$ into $\CC\sm[-2,2]$.
If $w\notin[-2,2]$, no root lies on the unit circle, since $F(e^{i\theta})=2\cos\theta\in[-2,2]$, and the roots are distinct, since a double root would be $\pm1$ with $w=\pm2$; as their product is $1$, exactly one root satisfies $\abs{z}>1$.
So $F$ is a holomorphic bijection onto $\CC\sm[-2,2]$, and its inverse is holomorphic.
:::
