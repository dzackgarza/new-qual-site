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
<1>1. For every closed $C\subseteq Y$, the sets $A\cap f^{-1}(C)$ and $B\cap f^{-1}(C)$ are closed in the subspaces $A$ and $B$, respectively.
::: {.proof}
Since the restrictions are continuous,
\[
(f|_A)^{-1}(C)=A\cap f^{-1}(C)
\]
is closed in the subspace $A$, and
\[
(f|_B)^{-1}(C)=B\cap f^{-1}(C)
\]
is closed in the subspace $B$.
:::

<1>2. The two sets in <1>1 are closed in $X$.
::: {.proof}
Because $A$ is closed in $X$, every subset closed in $A$ is closed in $X$.
Hence $A\cap f^{-1}(C)$ is closed in $X$.
The same argument applies to $B\cap f^{-1}(C)$ because $B$ is closed in $X$.
:::

<1>3. For every closed $C\subseteq Y$, the set $f^{-1}(C)$ is closed in $X$.
::: {.proof}
Using $X=A\cup B$,
\[
f^{-1}(C)
=\bigl(A\cap f^{-1}(C)\bigr)
 \cup\bigl(B\cap f^{-1}(C)\bigr).
\]
By <1>2, both sets on the right are closed in $X$, so their finite union is closed.
:::

<1>4. $f$ is continuous.
::: {.proof}
By <1>3, the inverse image under $f$ of every closed subset of $Y$ is closed in $X$.
This is the closed-set criterion for continuity.
:::
:::
