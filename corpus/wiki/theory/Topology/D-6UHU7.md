---
schema: qual/card@1
id: D-6UHU7
kind: definition
title: Deformation Retract
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
relations: []
review: draft
---

:::{.definition}
A map $r$ in $A\mathrel{\textstyle\substack{\injects^{\iota}\\\textstyle\dashleftarrow_{r}}} X$ that is a retraction (so $r\circ \iota = \id_{A}$) *that also satisfies* $\iota \circ r \homotopic \id_{X}$.

> Note that this is equality in one direction, but only homotopy equivalence in the other.

Equivalently, a map $F:I\cross X\to X$ such that 
\[
F_{0}(x) &= \id_{X}
F_{t}(x)\mid_{A} &= \id_{A}
F_{1}(X) &= A
.\]

Alt:

A **deformation retract** is a homotopy $H:X\cross I \into X$ from $\id_X$ to $\id_A$ where $\ro{H}{A} = \id_A$ fixes $A$ at all times.
$$
H: X\cross I \to X \\
H(x, 0) = \id_X \\
H(x, 1) = \id_A \\
x\in A \implies H(x, t) \in A \quad \forall t
$$

:::{.remark}
A deformation retract between a space and a subspace is a homotopy equivalence, and further $X\homotopic Y$ iff there is a $Z$ such that both $X$ and $Y$ are deformation retracts of $Z$. Moreover, if $A$ and $B$ both have deformation retracts onto a common space $X$, then $A \homotopic B$.


:::

:::
