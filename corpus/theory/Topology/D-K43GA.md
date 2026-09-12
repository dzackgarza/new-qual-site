---
schema: qual/card@1
id: D-K43GA
kind: definition
title: Contractible
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition}
A space $X$ is **contractible** if $\id_X$ is nullhomotopic.
i.e. the identity is homotopic to a constant map $c(x) = x_0$.

Equivalently, $X$ is contractible if $X \homotopic \theset{x_0}$ is homotopy equivalent to a point.
This means that there exists a mutually inverse pair of maps $f: X \into \theset{x_0}$ and $g:\theset{x_0} \into X$ such that $f\circ g \homotopic \id_{\theset{x_0}}$ and $g\circ f \homotopic \id_X$.
The defining homotopy $\id_X \homotopic c$ is itself the data: it deforms $X$ onto a point, which is what makes contractible spaces preserve homotopy invariants.
:::
