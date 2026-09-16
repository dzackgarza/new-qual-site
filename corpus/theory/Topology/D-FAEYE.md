---
schema: qual/card@1
id: D-FAEYE
kind: definition
title: Connected components
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space.
For $x, y\in X$ write $x\sim y$ if there is a [[D-ZNVPP|connected]] subspace $C\subseteq X$ with $x, y\in C$.
The equivalence classes of $\sim$ are the \dfn{connected components} of $X$.
:::

::: {.proposition}
The relation $\sim$ is an equivalence relation on $X$.
:::

::: {.proof}
The singleton $\ts{x}$ is connected, so $x\sim x$, and $\sim$ is symmetric by definition.
If $x, y\in C$ and $y, z\in D$ with $C$ and $D$ connected, then $C\cup D$ is connected, as a union of connected subspaces with the common point $y$, and contains $x$ and $z$; so $\sim$ is transitive.
:::
