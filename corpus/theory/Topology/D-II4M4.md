---
schema: qual/card@1
id: D-II4M4
kind: definition
title: Cone on a space
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homotopy
  - Quotient Spaces
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $I = [0,1]$.
The \dfn{cone} on $X$ is the quotient space
$$
CX\coloneqq(X\times I)/(X\times\ts{0}),
$$
in which $X\times\ts{0}$ is collapsed to a point.
:::

::: {.proposition}
If $X$ is nonempty, then $CX$ is [[D-K43GA|contractible]], and $x\mapsto[(x, 1)]$ is an embedding of $X$ into $CX$.
:::

::: {.example}
The cone $CS^1$ on the circle is homeomorphic to the closed disk $D^2$, by $[(z, t)]\mapsto tz$ for $z\in S^1\subseteq\CC$ and $t\in I$.
:::

::: {.concept}
See [@Hat02].
:::
