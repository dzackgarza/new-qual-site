---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-13
kind: problem
title: Collapse the boundary of a Möbius band
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Quotient Spaces
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Define what is meant by a Möbius band.
Identify the space obtained by identifying the boundary of a Möbius band to a point.
Give a brief explanation.
:::

::: {.solution}
<1>1. A Möbius band is the quotient of the rectangle $[0,1] \times [0,1]$ by the identification $(0, y) \sim (1, 1 - y)$ (gluing the two vertical edges with a half-twist).
Proof: definition of the Möbius band.

<1>2. The boundary of the Möbius band is a single circle (the image of the top and bottom edges, glued end-to-end).
Proof: the two horizontal edges of the rectangle are identified at their endpoints, forming one circle.

<1>3. Collapsing the boundary circle to a point gives the real projective plane $\mathbb{RP}^2$.
Proof: the Möbius band is $\mathbb{RP}^2$ with an open disk removed (equivalently, $\mathbb{RP}^2$ is obtained from a Möbius band by attaching a disk along its boundary); collapsing the boundary circle to a point is exactly attaching a disk (a cone on the boundary circle), which fills in the missing disk.

<1>4. Hence the space obtained is $\mathbb{RP}^2$.
Proof: <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
