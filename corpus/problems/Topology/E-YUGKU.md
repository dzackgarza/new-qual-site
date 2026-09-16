---
schema: qual/card@1
id: E-YUGKU
kind: problem
title: Product, subspace, and quotient topologies
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Subspace Topology
  - Quotient Spaces
relations: []
review: draft
---

::: {.exercise}
- State the definition of the product topology, the subspace topology, and the quotient topology.
:::

::: {.solution}
<1>1. The product topology on $X\times Y$ is the topology with basis $\{U\times V:U\subseteq X\text{ open},\ V\subseteq Y\text{ open}\}$.
::: {.proof}
This is the defining basis for the product topology.
:::

<1>2. If $A\subseteq X$, the subspace topology on $A$ is $\{A\cap U:U\subseteq X\text{ open}\}$.
::: {.proof}
This is the definition of the topology induced by the inclusion $A\hookrightarrow X$.
:::

<1>3. If $q:X\twoheadrightarrow Y$ is a surjection, the quotient topology on $Y$ is defined by
$$U\subseteq Y\text{ open}\iff q^{-1}(U)\subseteq X\text{ open}.$$
::: {.proof}
This is the definition of the quotient topology induced by $q$.
:::
:::
