---
schema: qual/card@1
id: E-MJQTF
kind: problem
title: Interior and boundary of a connected set
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

If $A$ is a connected subspace of $X$, does it follow that $\operatorname{Int} A$ and $\operatorname{Bd} A$ are connected?
Does the converse hold?
Justify your answers.
:::

::: {.solution}
Neither the interior nor the boundary of a connected set need be connected.

For the interior, let $A$ be the union of two closed disks in $\mathbb R^2$ tangent at one point. The set $A$ is connected, but its interior is the disjoint union of the two open disks, hence is disconnected.

For the boundary, take the closed annulus
\[
A=\{(x,y):1\le x^2+y^2\le4\}.
\]
It is connected, while its boundary is the disjoint union of the two circles $x^2+y^2=1$ and $x^2+y^2=4$.

The converse also fails. Take $A=\mathbb Q\subset\mathbb R$. Then $A$ is disconnected, but
\[
\operatorname{Int}A=\varnothing
\]
is connected, and since $\mathbb Q$ is dense,
\[
\operatorname{Bd}A=\mathbb R,
\]
which is connected.
:::
