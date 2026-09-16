---
schema: qual/card@1
id: PR-OTMIR
kind: proposition
title: Joukowski map from the upper half-disc to the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
Let $\DD\cap\HH=\ts{z\st\abs{z}<1,\ \Im z>0}$ be the upper half-disc and $\HH=\ts{w\st\Im w>0}$ the upper half-plane.
The map
$$
F\colon\DD\cap\HH\to\HH,\qquad F(z)=-\frac12\big(z+z^{-1}\big),
$$
is a [[D-TM4TE|biholomorphism]].
:::

::: {.proof}
For $z=re^{i\theta}$ with $0<r<1$ and $0<\theta<\pi$,
$$
F(z)=-\frac12\Big(r+\frac1r\Big)\cos\theta+\frac i2\Big(\frac1r-r\Big)\sin\theta,
$$
so $\Im F(z)>0$ and $F$ is a holomorphic map into $\HH$.
Given $w\in\HH$, the equation $F(z)=w$ is $z^2+2wz+1=0$.
Its two roots have product $1$, and neither lies on the unit circle or the real axis, because $F$ maps the unit circle into $[-1,1]$ and $\RR\sm\ts{0}$ into $\RR$.
So exactly one root $z$ satisfies $\abs{z}<1$, and it satisfies $\Im z>0$ because $\Im F(z)$ has the sign of $\sin\theta$ when $\abs{z}<1$.
Hence $F$ is bijective, and a bijective holomorphic map has a holomorphic inverse.
:::

::: {.remark}
The map $z\mapsto\frac12(z+z^{-1})$ is the Joukowski map; $F$ is its negative.
On the boundary of the half-disc, $F$ maps the upper unit semicircle onto $[-1,1]$, with $F(1)=-1$, $F(i)=0$, $F(-1)=1$, and it maps the segments $(0,1)$ and $(-1,0)$ onto $(-\infty,-1)$ and $(1,\infty)$ respectively.
The inverse is $F^{-1}(w)=-w+\sqrt{w^2-1}$, with the branch of the square root for which this value lies in $\DD$.
:::

::: {.remark}
It additionally maps $\DD^c\to \RR\sm[-1, 1]$.
A similar variant: $z\mapsto {1\over 2i}(z+z^{-1})$ sends the right half-plane to $\CC\sm\ts{t\in \RR \st \abs{t} \geq 1}$.
:::
