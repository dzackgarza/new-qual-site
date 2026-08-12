---
schema: qual/card@1
id: PR-74KHY
kind: proposition
title: "Given any three points $z_1, z_2, z_3$, the following M\u00f6bius transform\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.proposition title="?"}
Given any three points $z_1, z_2, z_3$, the following Möbius transformation sends them to $1, 0, \infty$ respectively:
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


:::
