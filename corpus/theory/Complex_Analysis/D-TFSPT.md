---
schema: qual/card@1
id: D-TFSPT
kind: definition
title: Limit point
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Limits
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, let $S\subseteq X$, and let $x\in X$.
The point $x$ is a \dfn{limit point} of $S$ if every neighborhood of $x$ contains a point of $S$ other than $x$.
:::

::: {.proposition}
Let $K$ be a [[D-EILKJ|compact]] subset of a topological space $X$.
Every infinite subset $S\subseteq K$ has a limit point in $K$.
:::

::: {.proof}
Suppose no point of $K$ is a limit point of $S$.
Then each $x\in K$ has an open neighborhood $U_x$ with $U_x\cap S\subseteq\{x\}$.
The sets $U_x$ cover $K$, so finitely many $U_{x_1},\ldots,U_{x_m}$ cover $K$, and then $S\subseteq\{x_1,\ldots,x_m\}$ is finite.
:::
