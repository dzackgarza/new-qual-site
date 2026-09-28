---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3A-HW1
kind: problem
title: CW structures on $S^2$ and $T^2$
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Create a cell complex for $S^2$ and a cell complex for $T=S^1\times S^1$.
:::

::: {.solution}
<1>1. $S^2$ is a CW complex with one $0$-cell $v_0$ and one $2$-cell attached by the constant map $\partial D^2\to\{v_0\}$.
::: {.proof}
The resulting space is $D^2/\partial D^2$, and $D^2/\partial D^2\cong S^2$: the map $D^2\to S^2$ sending the point at radius $r$ and angle $\theta$ to the point at polar angle $\pi r$ and longitude $\theta$ is a continuous surjection that identifies exactly $\partial D^2$ to the south pole, so it induces a continuous bijection from the compact space $D^2/\partial D^2$ to the Hausdorff space $S^2$.
:::

<1>2. $T$ is a CW complex with one $0$-cell $v_0$, two $1$-cells $a,b$, and one $2$-cell attached along the loop $aba^{-1}b^{-1}$.
::: {.proof}
Both ends of each $1$-cell are attached to $v_0$, so the $1$-skeleton is $S^1\vee S^1$ with loops $a$ and $b$. The $2$-cell is the square $I\times I$, whose boundary, read counterclockwise from $(0,0)$, traverses $a$, $b$, $a^{-1}$, $b^{-1}$. The resulting space is $I\times I/\bigl((x,0)\sim(x,1),\ (0,y)\sim(1,y)\bigr)$, which is homeomorphic to $S^1\times S^1$ via $(x,y)\mapsto(e^{2\pi ix},e^{2\pi iy})$.
:::
:::
