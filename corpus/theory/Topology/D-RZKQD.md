---
schema: qual/card@1
id: D-RZKQD
kind: definition
title: Suspension and reduced suspension
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homotopy
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $I=[0,1]$.
The \dfn{suspension} $SX$ is the quotient of $X\times I$ obtained by collapsing $X\times\ts{0}$ to one point and $X\times\ts{1}$ to another point [@Hat02, p. 8].
For a based space $(X,x_0)$, the \dfn{reduced suspension} is
$$
\Sigma X\coloneqq\frac{X\times I}{(X\times\ts{0})\cup(X\times\ts{1})\cup(\ts{x_0}\times I)},
$$
the quotient of $SX$ obtained by collapsing the segment $\ts{x_0}\times I$ to a point [@Hat02, p. 12].
:::

::: {.remark}
$SX$ is the union of two copies of the [[D-II4M4|cone]] $CX$ $CX=(X\times I)/(X\times\ts{0})$ glued along their copies of $X\times\ts{1}\cong X$.
:::
