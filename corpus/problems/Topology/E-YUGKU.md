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

::: pf

::: pf-step

The product topology on $X\times Y$ is the topology with basis $\{U\times V:U\subseteq X\text{ open},\ V\subseteq Y\text{ open}\}$.

::: pf-proof

This is the defining basis for the product topology.

:::

:::

::: pf-step

If $A\subseteq X$, the subspace topology on $A$ is $\{A\cap U:U\subseteq X\text{ open}\}$.

::: pf-proof

This is the definition of the topology induced by the inclusion $A\hookrightarrow X$.

:::

:::

::: pf-step

If $q:X\twoheadrightarrow Y$ is a surjection, the quotient topology on $Y$ is defined by
$$U\subseteq Y\text{ open}\iff q^{-1}(U)\subseteq X\text{ open}.$$

::: pf-proof

This is the definition of the quotient topology induced by $q$.

:::

:::

:::

:::
