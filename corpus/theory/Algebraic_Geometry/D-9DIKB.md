---
schema: qual/card@1
id: D-9DIKB
kind: definition
title: Irreducible and Noetherian spaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Irreducibility
  - Noetherian Spaces
relations: []
review: draft
prompts:
- What does it mean for a topological space to be irreducible?
- What does it mean for a topological space to be Noetherian?
- Why is $\AA^n$ Noetherian?
---

::: {.definition title="Irreducible"}
A nonempty topological space is **irreducible** if it is not the union of two proper closed subsets.
Equivalently, any two nonempty open subsets meet.
:::

::: {.definition title="Noetherian"}
A topological space is **Noetherian** if its closed subsets satisfy the descending chain condition.
:::

::: {.remark}
The descending chain condition is on all closed subsets, irreducible or not.
$\AA^n$ is Noetherian because the correspondence turns a descending chain of closed sets into an ascending chain of radical ideals in $k[x_1,\ldots,x_n]$, which stabilises by the Hilbert basis theorem.
:::
