---
schema: qual/card@1
id: D-GCL7C
kind: definition
title: Generalized circle
prompts:
- What is a generalized circle?
- Which regions does a generalized circle bound?
classification:
  areas:
  - complex-analysis
  topics:
  - Möbius Transformations
relations: []
review: draft
---

::: {.definition}
A \dfn{generalized circle} in $\CP^1$ is a circle in $\CC$, or a line in $\CC$ together with the point $\infty$.
Equivalently, in the coordinates of $\RR^3$ that stereographic projection uses, it is the intersection of the sphere with a plane, the plane $\CC$ itself contributing the generalized circle $\RR\cup\theset{\infty}$.
It bounds two regions: a circle bounds a disc and its exterior, and a line bounds two half-planes.

The wider sense of "circle" is that of [@Ahl73, ch. 3, §3.2, Theorem 14], which states that a linear transformation carries circles into circles with this convention.
:::

::: {.remark}
Under stereographic projection the circles on the sphere correspond exactly to the generalized circles, a circle through the north pole becoming a line; stereographic projection is conformal and carries circles to circles (C. McMullen, *Advanced Complex Analysis*, Theorem 2.12).
:::
