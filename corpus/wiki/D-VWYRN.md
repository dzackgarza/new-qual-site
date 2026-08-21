---
schema: qual/card@1
id: D-VWYRN
kind: definition
title: Pullback
classification:
  areas:
  - topology
  topics:
  - Category Theory
relations: []
review: draft
---

::: {.definition title="Pullback"}
For maps $f: X\to Z$ and $g: Y\to Z$, the **pullback** is
\[
X \cross_Z Y \da \ts{ (x,y) \in X\cross Y \st f(x) = g(y) }
\]
together with the two projections, universal among objects mapping compatibly to $X$ and $Y$.
It is the limit of the diagram $X\to Z \leftarrow Y$; taking $Z = \pt$ recovers the product.
:::

::: {.concept}
See Hatcher, §4.H, p. 461.
:::
