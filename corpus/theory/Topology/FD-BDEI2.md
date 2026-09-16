---
schema: qual/card@1
id: FD-BDEI2
kind: definition
title: Deformation retract
prompts:
- What does it mean for $A \subset X$ to be a deformation retract of $X$?
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $A \subseteq X$ a subspace, and $I = [0,1]$.
The subspace $A$ is a \dfn{deformation retract} of $X$ if there exists a continuous map $F\colon X\cross I\to X$, with $F_t\coloneqq F(\wait, t)$, such that
$$
\begin{aligned}
F(x, 0) &= x \text{ for all } x\in X, &&\text{that is, } F_0 = \id_X, \\
F(x, 1) &\in A \text{ for all } x\in X, &&\text{that is, } F_1(X) \subseteq A, \\
F(a, 1) &= a \text{ for all } a\in A, &&\text{that is, } F_1\vert_A = \id_A.
\end{aligned}
$$
:::

::: {.remark}
Equivalently, there is a [[D-NCLVD|retraction]] $r\colon X\to A$ such that $\iota\circ r$ is [[D-Z7I7F|homotopic]] to $\id_X$, where $\iota\colon A\injects X$ is the inclusion.
The [[D-2O3N7|deformation retraction]] of [@Hat02, p. 2] additionally requires $F(a, t) = a$ for all $a\in A$ and $t\in I$.
:::
