---
schema: qual/card@1
id: D-A3PUW
kind: definition
title: Cellular Homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Degree
relations: []
review: draft
---

::: {.definition title="Cellular Homology"}
For $X$ a CW complex, the cellular chain complex has $C_n^{\cell}(X) \da H_n(X^n, X^{n-1})$, free abelian on the $n\dash$cells of $X$, with differential $d_n$ the composite
\[
H_n(X^n, X^{n-1}) \mapsvia{\del} H_{n-1}(X^{n-1}) \to H_{n-1}(X^{n-1}, X^{n-2})
,\]
whose matrix entries are the degrees of the maps $S^{n-1}_\alpha \to X^{n-1}\to S^{n-1}_\beta$.
Its homology $H_n^{\cell}(X)$ is naturally isomorphic to $H_n(X)$.
:::

::: {.concept}
See Hatcher, §2.2, Theorem 2.35, p. 139.
:::
