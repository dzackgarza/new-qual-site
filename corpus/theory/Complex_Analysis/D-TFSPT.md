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

This is [@Rud76, ch. 2, Definition 2.18(c)], stated there for a metric space with the neighborhoods $N_r(p)$ of (a) of the same definition; the card states it for a topological space, which is the same condition with the topology's neighborhoods in place of the balls.
:::

::: {.proposition}
Let $K$ be a [[D-EILKJ|compact]] subset of a topological space $X$.
Every infinite subset $S\subseteq K$ has a limit point in $K$.
:::
