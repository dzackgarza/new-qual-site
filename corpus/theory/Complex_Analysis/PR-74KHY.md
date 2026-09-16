---
schema: qual/card@1
id: PR-74KHY
kind: proposition
title: Three points determine a Möbius transformation
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
Ahlfors, *Complex Analysis*, ch. 3, §3.2 (The Cross Ratio), Definition 12.
Ahlfors normalizes with four arguments, $(z_1,z_2,z_3,z_4)$ being the image of $z_1$ under the map carrying $z_2, z_3, z_4$ to $1, 0, \infty$; the three-argument form above is that map with $z_2, z_3, z_4$ relabelled $z_2, z_1, z_3$.
:::
