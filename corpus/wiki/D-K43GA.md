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
This means that there exists a mutually inverse pair of maps $f: X \into \theset{x_0}$ and $g:\theset{x_0} \into X$ such that $f\circ g \homotopic \id_{\theset{x_0}}$ and $g\circ f \homotopic \id_X$.[^contractible_is_useful]
:::

[^contractible_is_useful]: Useful because it hands you a homotopy to work with.
