---
schema: qual/card@1
id: D-CNPOL
kind: definition
title: Polar equation of a conic
classification:
  areas:
  - complex-analysis
  topics:
  - Conic Sections
  - Geometry
relations: []
review: draft
---

::: {.definition}
Let $F$ be a point, $D$ a line not through $F$, and $e\geq0$.
The \dfn{conic} with focus $F$, directrix $D$ and eccentricity $e$ is the locus of points $P$ with $\abs{PF}=e\,\abs{PD}$.
With $F$ at the origin and $D$ the line $x=d$, a point of the conic has polar coordinates $(r,\theta)$ satisfying
$$
r=\frac{ed}{1+e\cos\theta},
$$
an ellipse for $0<e<1$, a parabola for $e=1$, and a hyperbola for $e>1$.

The foci and the directrices of the ellipse and the hyperbola are read off the focal forms (16) and (17) of [@Ahl73, ch. 3, §4.2, A Survey of Elementary Mappings]: there the foci are the points $\pm1$, so the eccentricity is $c/a=2/(\rho+\rho^{-1})$ for the ellipse of (16).
:::
