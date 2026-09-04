---
schema: qual/card@1
id: P-B4N3X
kind: problem
title: A map continuous on each of two closed sets covering $X$ is continuous
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Subspace Topology
relations: []
review: draft
---

::: {.problem}
Let $X$ and $Y$ be topological spaces and let $f : X \to Y$ be a function.

Suppose that $X = A \cup B$ where $A$ and $B$ are closed subsets, and that the restrictions $f \mid_A$ and $f \mid_B$ are continuous (where $A$ and $B$ have the subspace topology).

Prove that $f$ is continuous.
:::

::: {.solution}
Let $C\subseteq Y$ be closed.
Since the restrictions are continuous,
\[
(f|_A)^{-1}(C)=A\cap f^{-1}(C)
\]
is closed in the subspace $A$, and
\[
(f|_B)^{-1}(C)=B\cap f^{-1}(C)
\]
is closed in the subspace $B$.

Because $A$ is closed in $X$, every subset closed in $A$ is closed in $X$.
Hence $A\cap f^{-1}(C)$ is closed in $X$; similarly, $B\cap f^{-1}(C)$ is closed in $X$.

Using $X=A\cup B$,
\[
f^{-1}(C)
=\bigl(A\cap f^{-1}(C)\bigr)
 \cup\bigl(B\cap f^{-1}(C)\bigr).
\]
This is a finite union of closed subsets of $X$, hence is closed.
Thus the inverse image under $f$ of every closed subset of $Y$ is closed, so $f$ is continuous.
:::
