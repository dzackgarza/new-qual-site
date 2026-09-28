---
schema: qual/card@1
id: D-RMQ7W
kind: definition
title: Mapping cylinder
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
Let $f\colon X\to Y$ be a continuous map and $I=[0,1]$.
The \dfn{mapping cylinder} of $f$ is the quotient space
$$
M_f\coloneqq\qty{(X\times I)\disjoint Y}/\qty{(x,1)\sim f(x)\text{ for } x\in X}
$$
[@Hat02].
:::

::: {.proposition}
Let $\iota\colon X\to M_f$ be the map $x\mapsto[(x,0)]$ and $r\colon M_f\to Y$ the map with $r([(x,t)])=f(x)$ and $r([y])=y$.
Then $\iota$ is an embedding, $f=r\circ\iota$, and $M_f$ [[D-UH3L5|deformation retracts]] onto $Y$ by sliding each segment $\ts{x}\times I$ to its endpoint $f(x)$; in particular $r$ is a [[D-HFR32|homotopy equivalence]].
Thus every continuous map factors as an embedding followed by a homotopy equivalence [@Hat02].
:::
