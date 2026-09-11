---
schema: qual/card@1
id: P-PRACT20-W3-28
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 28"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
What is the flux of $\mathbf { F } ( x , y , z ) = ( x , y , z )$ through the surface $z = { \sqrt { 1 - x ^ { 2 } - y ^ { 2 } } }$ with normal pointing upward?
:::

::: {.solution}
The flux through the surface is given by the surface integral of F · n where n is the normal to the surface.
We can evaluate this easily using Gauss’ divergence theorem:

$$
\iint _ { S } \mathbf { F } \cdot \mathbf { n } d S = \iiint _ { V } \nabla \cdot \mathbf { F } d V = 3 \mathrm { V o l } ( V ) = 2 \pi .
$$

[Note: ordinarily we would also need to account for the flux through the bottom of the surface, but the flux of F through the bottom is zero here since $\mathbf { F } \cdot \mathbf { n } = - z = 0$ on the xy-plane.]
:::
