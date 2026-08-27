---
schema: qual/card@1
id: PR-AQ6YR
kind: proposition
title: Cross ratio construction of conformal maps
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
---

:::{.proposition}
Define generalized cross-ratios as
\[
(z_1, z_2, z_3, z_4) &\da {z_1 - z_3\over z_1-z_4}{z_2 - z_4 \over z_2 - z_3} \\
R(z) \da (z, a,b,c) &\da {z - b\over z-c}{a - c\over a - c} \\
.\]

Given any three points, $R(z)$ sends
\[
a &\to 1 \\
b &\to 0 \\
c &\to \infty
.\]


One can use this to produce a map sending any three points to any other three points:
\[
T(z) \da 
(w; w_1, w_2, w_3)\inv
\circ
(z; z_1,z_2, z_3)
.\]

If any of the $z_i$ are $\infty$, the convention is to remove the corresponding terms where they appear:
:::
