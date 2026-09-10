---
schema: qual/card@1
id: E-J5IB5
kind: problem
title: Surfaces with k holes
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a 2-manifold; let $U_1, \ldots, U_k$ be a collection of disjoint open sets in $X$; and suppose that for each $i$, there is a homeomorphism $h_i$ of the open unit ball $B^2$ with $U_i$.
Let $\epsilon = 1/2$ and let $B_\epsilon$ be the open ball of radius $\epsilon$.
Show that the space $Y = X - \bigcup h_i(B_\epsilon)$ is a 2-manifold with boundary, and that $\partial Y$ has $k$ components.
The space $Y$ is called "X-with-$k$-holes."
:::

::: {.solution}
For each \(i\), write
\[
D_i=h_i(B_{1/2})\subset U_i.
\]
The sets \(D_i\) are pairwise disjoint open disks. Put
\[
Y=X-\bigcup_{i=1}^k D_i.
\]
As a closed subspace of the Hausdorff second-countable surface \(X\), the space \(Y\) is Hausdorff and second countable.

Away from the circles
\[
C_i=h_i(\{z:\|z\|=1/2\}),
\]
points of \(Y\) have the same ordinary surface charts they had in \(X\). At a point of \(C_i\), use polar coordinates in the annulus
\[
h_i\bigl(\{1/2\le\|z\|<3/4\}\bigr).
\]
Locally the inequality \(r\ge1/2\) becomes a half-plane inequality, so each such point has a chart onto an open subset of \(H^2\) taking \(C_i\) to the boundary line. Hence \(Y\) is a 2-manifold with boundary.

By the intrinsic-boundary criterion of [[E-RKSXA]], its boundary is exactly
\[
\partial Y=C_1\sqcup\cdots\sqcup C_k.
\]
Each \(C_i\) is homeomorphic to \(S^1\), and the circles are pairwise disjoint because the original \(U_i\)'s are disjoint. Thus \(\partial Y\) has exactly \(k\) connected components.
:::
