---
schema: qual/card@1
id: FD-BDEI2
kind: definition
title: Deformation Retract
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
relations: []
review: draft
---

::: {.definition title="Deformation Retract"}
Deformation Retract: A subspace $A \subset X$ is a *deformation retract* of $X$ iff there exists a deformation retraction: a continuous map $F:X\cross I$ to $X$ such that

$$
\begin{align*}
F(x, 0) &= x  \iff F_0 = \id_X \\
F(x, 1) &\in A \iff F_1(X) \subseteq A \\
F(a, 1) &= a \iff F_1\mid_A = \id_A
.\end{align*}
$$
Equivalently it is a homotopy between a retraction $X\to A$ and $\id_X$.
:::
