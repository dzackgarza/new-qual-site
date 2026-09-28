---
schema: qual/card@1
id: D-3VEC5
kind: definition
title: Acyclic spaces and chain complexes
classification:
  areas:
  - topology
  topics:
  - Homology
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
A topological space $X$ is \dfn{acyclic} if its reduced singular homology vanishes, $\tilde H_n(X;\ZZ) = 0$ for all $n$.
A chain complex $(C_*, \del)$ is \dfn{acyclic} if $H_n(C_*) = 0$ for all $n$.
:::

::: {.remark}
A nonempty space is acyclic if and only if the map to a point induces isomorphisms on all homology groups.
A chain complex is acyclic if and only if it is [[D-STPAM|exact]].
:::

::: {.concept}
[@Hat02].
:::
