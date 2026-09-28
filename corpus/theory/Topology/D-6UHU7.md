---
schema: qual/card@1
id: D-6UHU7
kind: definition
title: Deformation retraction
prompts:
- What does it mean for $A \subset X$ to be a deformation retract of $X$?
- What map exhibits $A \subset X$ as a deformation retract of $X$?
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $A\subseteq X$ a subspace, and $\iota\colon A\injects X$ the inclusion.
A \dfn{deformation retraction} of $X$ onto $A$ is a [[D-Z7I7F|homotopy]] $F\colon X\cross I\to X$, written $F_t \coloneqq F(\wait, t)$, such that for all $t\in I$:
$$
F_0 = \id_X, \qquad F_1(X) \subseteq A, \qquad F_t(a) = a \text{ for all } a\in A
.$$
The subspace $A$ is a \dfn{deformation retract} of $X$ if there exists a deformation retraction of $X$ onto $A$.
:::

::: {.remark}
If $F$ is a deformation retraction of $X$ onto $A$, then $r\coloneqq F_1\colon X\to A$ is a [[D-NCLVD|retraction]], $r\circ\iota = \id_A$, and $F$ is a homotopy from $\id_X$ to $\iota\circ r$.
Hence $\iota$ is a [[D-HFR32|homotopy equivalence]] with homotopy inverse $r$.
:::

::: {.remark}
Two spaces $X$ and $Y$ are homotopy equivalent if and only if there exists a space $Z$ containing both $X$ and $Y$ as deformation retracts; for a homotopy equivalence $f\colon X\to Y$, the [[D-RMQ7W|mapping cylinder]] of $f$ is such a $Z$.
:::

::: {.concept}
[@Hat02].
:::
