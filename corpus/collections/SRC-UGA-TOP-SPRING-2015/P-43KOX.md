---
schema: qual/card@1
id: P-43KOX
kind: problem
title: The product of two connected spaces is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
---

::: {.problem}
Prove that the product of two connected topological spaces is connected.
:::

::: {.solution}
Fix $(a,b)\in X\times Y$.

<1>1. The horizontal slice
\[
X_b=X\times\{b\}
\]
and every vertical slice
\[
Y_x=\{x\}\times Y
\]
are connected.
::: {.proof}
The projection $X_b\to X$ is a homeomorphism, and the projection $Y_x\to Y$ is a homeomorphism.
The spaces $X$ and $Y$ are connected by hypothesis.
:::

<1>2. For every $x\in X$, the subspace
\[
T_x=X_b\cup Y_x
\]
is connected.
::: {.proof}
By <1>1, both $X_b$ and $Y_x$ are connected.
They meet at the point $(x,b)$, so their union is connected.
:::

<1>3. The family $\{T_x:x\in X\}$ has a common point.
::: {.proof}
For every $x\in X$, the point $(a,b)$ lies in the horizontal slice $X_b\subseteq T_x$.
:::

<1>4. The union of the $T_x$ is all of $X\times Y$.
::: {.proof}
If $(x,y)\in X\times Y$, then $(x,y)\in Y_x\subseteq T_x$.
Hence
\[
X\times Y=\bigcup_{x\in X}T_x.
\]
:::

<1>5. $X\times Y$ is connected.
::: {.proof}
By <1>2 each $T_x$ is connected, by <1>3 they share a common point, and by <1>4 their union is $X\times Y$.
A union of connected subspaces with a common point is connected.
:::

![Image](../../assets/figures/2020-01-21-20%3A53.png)
:::
