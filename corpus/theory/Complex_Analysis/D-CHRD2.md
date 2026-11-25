---
schema: qual/card@1
id: D-CHRD2
kind: definition
title: Chordal metric on the Riemann sphere
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Sphere
  - Metric Spaces
relations: []
review: draft
---

::: {.definition}
The \dfn{chordal metric} on $\CP^1$ is the Euclidean distance between the stereographic projections of two points on the unit sphere.
For $z,w\in\CC$,
$$
d(z,w)=\frac{2\abs{z-w}}{\sqrt{1+\abs z^2}\sqrt{1+\abs w^2}},
\qquad
d(z,\infty)=\frac{2}{\sqrt{1+\abs z^2}},
$$
so $d(0,\infty)=2$ is the diameter of the sphere, and on the sphere of diameter $1$ of [[D-3QTVR]] every distance is halved.

This is [@Ahl73, ch. 1, §2.4, (28)], where the sphere is the unit sphere.
:::
