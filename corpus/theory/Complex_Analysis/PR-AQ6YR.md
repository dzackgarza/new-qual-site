---
schema: qual/card@1
id: PR-AQ6YR
kind: proposition
title: Cross-ratio construction of conformal maps
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
For $z_1\in\CC$ and distinct $z_2,z_3,z_4\in\CC$, write
$$
(z_1, z_2, z_3, z_4) \coloneqq {z_1 - z_3\over z_1-z_4}\cdot{z_2 - z_4 \over z_2 - z_3}.
$$

(a) For distinct $a,b,c\in\CC$, the map
$$
R(z) \coloneqq (z, a,b,c) = {z - b\over z-c}\cdot{a - c\over a - b}
$$
is a [[D-FRVBV|Möbius transformation]] with $R(a)=1$, $R(b)=0$, and $R(c)=\infty$.

(b) If one of $a,b,c$ is $\infty$, the factors containing it are deleted, and the resulting Möbius transformation has the same three values:
$$
(z,\infty,b,c)={z-b\over z-c},\qquad (z,a,\infty,c)={a-c\over z-c},\qquad (z,a,b,\infty)={z-b\over a-b}.
$$

(c) For distinct $z_1,z_2,z_3$ and distinct $w_1,w_2,w_3$ in $\CC\cup\theset{\infty}$, let $R_z(z)\coloneqq(z,z_1,z_2,z_3)$ and $R_w(w)\coloneqq(w,w_1,w_2,w_3)$.
Then $T\coloneqq R_w\inv\circ R_z$ is a Möbius transformation with $T(z_j)=w_j$ for $j=1,2,3$.
:::

::: {.proof}
Parts (a) and (b) follow by substituting $a$, $b$, $c$ into each formula; each formula is a quotient of affine functions of $z$ with nonzero determinant because $a,b,c$ are distinct.
For (c), $R_z$ sends $z_1,z_2,z_3$ to $1,0,\infty$, and $R_w\inv$ sends $1,0,\infty$ to $w_1,w_2,w_3$; a composite of Möbius transformations is a Möbius transformation.
:::
