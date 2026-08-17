---
schema: qual/card@1
id: E-W6MWU
kind: exercise
title: "Disc to upper half-plane, cross-ratio"
classification:
  areas:
  - complex-analysis
  topics:
  - fractional-linear-transformations
  - conformal-maps
relations: []
review: draft
solved: true
---
:::{.exercise title="Disc to upper half-plane, cross-ratio"}
Find a conformal map $\HH \to \DD$ using cross-ratios.
:::

:::{.solution}
Idea: rotate the upper hemisphere $(\HH)$ of $\CP^1$ to make the equator $\bd \DD$, "zoom" by placing $i$ at the center so $0\to i\mapsto -1\to 0$ and $i\to \infty\mapsto 0\to 1$.
Accomplish this by sending

- $\infty\to 1$
- $i\to 0$
- $-i\to \infty$

Use the cross-ratio
\[
R(z) \da (z, \infty, i, -i) = {z-i \over z-(-i)} {\infty - (-i) \over \infty - i} = {z-i\over z+i}
.\]

Checking that this works:

- If $z\in \RR$ then $\abs{z-i} = \abs{z+i}$ so $\abs{F(z)} = 1$.
- If $z\in \HH$ then $\abs{z-i}\leq \abs{z+i}$ so $\abs{F(z)}< 1$.


:::

