---
schema: qual/card@1
id: E-P3RLK
kind: problem
title: Closed subsets of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

Let $A\subset X$ with $A$ closed and $X$ compact, and show that $A$ is compact.

::: {.solution}
Let $\mathcal U$ be an open cover of $A$ by subsets open in the subspace topology.
For each $U\in\mathcal U$, choose an open set $V_U\subseteq X$ with $U=A\cap V_U$.
Since $A$ is closed, $X\setminus A$ is open, and
\[
\{V_U:U\in\mathcal U\}\cup\{X\setminus A\}
\]
is an open cover of $X$.
Compactness of $X$ gives a finite subcover
\[
V_{U_1},\ldots,V_{U_n},X\setminus A.
\]
Intersecting with $A$ removes the last set and gives
\[
A=(A\cap V_{U_1})\cup\cdots\cup(A\cap V_{U_n})
=U_1\cup\cdots\cup U_n.
\]
Thus every open cover of $A$ has a finite subcover, so $A$ is compact.
:::
