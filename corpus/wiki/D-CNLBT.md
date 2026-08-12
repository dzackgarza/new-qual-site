---
schema: qual/card@1
id: D-CNLBT
kind: definition
title: "Oriented manifold"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="Oriented manifold"}
An $n\dash$manifold $M$ together with a consistent choice of local orientations: generators $\mu_x$ of $H_n(M, M\sm\ts{x};\ZZ)\cong\ZZ$ such that every $x$ has a ball neighborhood $B$ and a class $\mu_B \in H_n(M, M\sm B;\ZZ)$ restricting to $\mu_y$ for every $y\in B$.
$M$ is **orientable** iff such a choice exists, and a connected orientable $M$ has exactly two orientations.
A closed connected oriented $M$ carries a fundamental class $[M]\in H_n(M;\ZZ)$ restricting to $\mu_x$ at every point.
:::

::: {.concept}
See Hatcher, §3.3, pp. 234 and 236.
:::
