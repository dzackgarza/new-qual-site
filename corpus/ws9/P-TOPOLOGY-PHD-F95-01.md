---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-01
kind: problem
title: The pasting lemma for two closed subspaces
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Subspace Topology
relations: []
review: draft
solved: false
---

::: {.problem title="?"}
Let $A$ and $B$ be closed subspaces of a topological space $X$ with $X=A\cup B$.
Suppose that $f:A\to Y$ and $g:B\to Y$ are continuous, and $f(x)=g(x)$ for all $x\in A\cap B$.
Prove that $h:X\to Y$ by
$$
h(x)=
\begin{cases}
f(x) & \text{if }x\in A,\\
g(x) & \text{if }x\in B
\end{cases}
$$
is continuous.
Is it necessary for both $A$ and $B$ to be closed?
Discuss.
:::
