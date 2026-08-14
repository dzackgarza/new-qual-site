---
schema: qual/card@1
id: PR-74KHY
kind: proposition
title: "Three points determine a M\u00f6bius transformation"
classification:
  areas:
  - complex-analysis
  topics:
  - fractional-linear-transformations
  - conformal-maps
relations: []
review: draft
---
:::{.proposition title="Three points determine a Möbius transformation"}
Given any three distinct points $z_1, z_2, z_3$, the following Möbius transformation sends them to $0, 1, \infty$ respectively, and is the unique one that does:
\[
T(z)
&\da { (z-z_1) (z_2-z_3) \over (z-z_3) (z_2 - z_1)}
\\
z_1 & \mapsto 0 \\
z_2 & \mapsto 1 \\
z_3 & \mapsto \infty
.\]
Such a map is sometimes denoted $(z; z_1, z_2, z_3)$.
One can use this to produce a map sending any three points to any other three points:
\[
T(z) \da
(w; w_1, w_2, w_3)\inv
\circ
(z; z_1,z_2, z_3)
.\]

:::{.remark}
Ahlfors, *Complex Analysis*, ch. 3, §3.2 (The Cross Ratio), Definition 12.
Ahlfors normalizes with four arguments, $(z_1,z_2,z_3,z_4)$ being the image of $z_1$ under the map carrying $z_2, z_3, z_4$ to $1, 0, \infty$; the three-argument form above is that map with $z_2, z_3, z_4$ relabelled $z_2, z_1, z_3$.
Substituting each of $z_1, z_2, z_3$ into $T$ gives $0, 1, \infty$, in that order.
:::

:::
