---
schema: qual/card@1
id: E-NZ4WI
kind: problem
title: A set open in a subspace but not in the ambient space
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
  - Point-Set Topology
relations: []
review: draft
---

::: {.problem}
Give an example of spaces $A\subseteq B \subseteq X$ such that $A$ is open in $B$ but $A$ is *not* open in $X$.
:::

::: {.solution}

::: pf

::: pf-step

Take $A = B = [0, 1]$ and $X = \RR$. Then $A$ is open in $B$.

::: pf-proof

Every space is open in itself.

:::

:::

::: pf-step

$A = [0,1]$ is not open in $\RR$.

::: pf-proof

The point $1$ is not an interior point of $[0,1]$: every interval $(1-\varepsilon, 1+\varepsilon)$ contains $1 + \varepsilon/2 \notin [0,1]$.

:::

:::

:::

:::
