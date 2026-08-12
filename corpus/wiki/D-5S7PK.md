---
schema: qual/card@1
id: D-5S7PK
kind: definition
title: "Pushout"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="Pushout"}
For maps $f: Z\to X$ and $g: Z\to Y$, the **pushout** is
\[
X \disjoint_Z Y \da \qty{X \disjoint Y}/\qty{f(z)\sim g(z) \st z\in Z}
\]
together with the two inclusions, universal among objects receiving compatible maps from $X$ and $Y$.
It is the colimit of $X \leftarrow Z \to Y$, and is dual to the pullback.
Attaching one space to another along a map is a pushout, and van Kampen says $\pi_1$ carries such a pushout of spaces to a pushout of groups, the amalgamated free product.
:::

::: {.concept}
See Hatcher, §4.H, p. 461.
:::
