---
schema: qual/card@1
id: P-PRACT20-W3-28
kind: problem
title: Flux of $(x,y,z)$ through the upper unit hemisphere
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
Let $V$ be the solid upper half-ball, whose boundary is the hemisphere $S$ together with the unit disk $B$ in the $xy$-plane. On $B$ the outward normal is $\mathbf{n} = (0,0,-1)$, so $\mathbf{F} \cdot \mathbf{n} = -z = 0$ and the flux through $B$ is zero. By the divergence theorem,

$$
\iint _ { S } \mathbf { F } \cdot \mathbf { n } \, dS = \iiint _ { V } \nabla \cdot \mathbf { F } \, dV = 3 \operatorname{Vol} ( V ) = 2 \pi .
$$
:::
