---
schema: qual/card@1
id: D-TD6AO
kind: definition
title: Colimit of a directed system
classification:
  areas:
  - topology
  topics:
  - category-theory
relations: []
review: draft
---

::: {.definition title="Colimit"}
For a directed system $(X_{i}, f_{ij})$, the **colimit** is the object $X$ receiving maps $\iota_{i}: X_{i} \to X$ with $\iota_j \circ f_{ij} = \iota_i$ whenever $i \leq j$, universal among such: given any $Y$ and maps $\psi_{i}: X_{i} \to Y$ compatible with the $f_{ij}$, there is a unique $X \to Y$ through which every $\psi_i$ factors.
The maps go **out of** the system; reversing every arrow gives the limit, whose maps go into the system.
Colimits are computed as a quotient of the disjoint union, $\varinjlim_i X_i = \qty{ \Disjoint_i X_i } / \qty{ x \sim f_{ij}(x) }$.
:::

::: {.concept}
See Weibel, *An Introduction to Homological Algebra*, 2.6.7 for the universal property; Hatcher, §3.3, p. 243 for the quotient construction over a directed set.
:::
