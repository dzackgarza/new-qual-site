---
schema: qual/card@1
id: PR-74KHY
kind: proposition
title: Three points determine a Möbius transformation
slogan: 'A Möbius transformation is uniquely determined by the images of three distinct points.'
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
Let $z_1, z_2, z_3\in\CC$ be distinct.
The [[D-FRVBV|Möbius transformation]]
$$
T(z) \coloneqq { (z-z_1) (z_2-z_3) \over (z-z_3) (z_2 - z_1)}
$$
satisfies $T(z_1)=0$, $T(z_2)=1$, and $T(z_3)=\infty$, and it is the unique Möbius transformation with these values.
It is denoted $(z; z_1, z_2, z_3)$.

Consequently, for distinct $w_1,w_2,w_3\in\CC$, the map
$$
S\coloneqq(\,\cdot\,; w_1, w_2, w_3)\inv \circ (\,\cdot\,; z_1,z_2, z_3)
$$
is the unique Möbius transformation with $S(z_j)=w_j$ for $j=1,2,3$.
:::

::: {.proof}
Substituting $z_1$, $z_2$, $z_3$ into $T$ gives $0$, $1$, $\infty$.
If $T'$ is another Möbius transformation with the same values, then $R\coloneqq T'\circ T\inv$ fixes $0$, $1$, and $\infty$.
Fixing $\infty$ forces $R(z)=az+b$; fixing $0$ forces $b=0$; fixing $1$ forces $a=1$; so $R=\id$ and $T'=T$.
The map $S$ is a composite of Möbius transformations, and it sends $z_1,z_2,z_3$ to $0,1,\infty$ and then to $w_1,w_2,w_3$.
If $S'$ is another Möbius transformation with $S'(z_j)=w_j$ for $j=1,2,3$, then $(\,\cdot\,;w_1,w_2,w_3)\circ S'\circ(\,\cdot\,;z_1,z_2,z_3)\inv$ fixes $0$, $1$, and $\infty$, so it is the identity by the same argument, and $S'=S$.
:::

::: {.remark}
In [@Ahl79, Chapter 3, Section 3.2, Definition 12], the cross ratio $(z_1,z_2,z_3,z_4)$ has four arguments: it is the image of $z_1$ under the Möbius transformation carrying $z_2, z_3, z_4$ to $1, 0, \infty$.
In that notation, $(z;z_1,z_2,z_3)=(z,z_2,z_1,z_3)$.
:::
