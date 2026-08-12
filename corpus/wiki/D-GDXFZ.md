---
schema: qual/card@1
id: D-GDXFZ
kind: definition
title: "Proper: Several equivalent definitions."
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="Proper"}

Several equivalent definitions.
Let $f: X\to Y$ be continuous, then $f$ is **proper** iff

- Most general: preimages of compact sets are compact: if $K \subseteq Y$ is compact, then $f\inv(K) \subseteq X$ is compact.

- For $Y$ Hausdorff and locally compact, $f$ is a closed map with compact fibers: $f\inv(\ts{y})$ is compact for every $y\in Y$.

- For $X$ Hausdorff and $Y$ locally compact, $f$ is universally closed: the map $f\times \id_Z: X\times Z\to Y\times Z$ is a closed map for every space $Z$.

- For $X, Y$ metric spaces, if $\ts{x_i}$ is a sequence that eventually escapes every compact set in $X$, $\ts{f(x_i)}$ eventually escapes every compact set in $Y$.
:::
