---
schema: qual/card@1
id: P-AGH325LOCALSPACE
kind: problem
title: Local cohomology at a point is computed on the local space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Local Cohomology
  - Zariski Spaces
relations: []
review: draft
---

::: problem
Let $X$ be a Zariski space (II, Ex.
3.17). Let $P \in X$ be a closed point, and let $X_P$ be the subset of $X$ consisting of all points $Q \in X$ such that $P \in \bar{\ts{Q}}$.
We call $X_P$ the **local space** of $X$ at $P$, and give it the induced topology.

Let $j: X_P \to X$ be the inclusion, and for any sheaf $\mcf$ on $X$, let $\mcf_P=j^* \mcf$.
Show that for all $i, \mcf$, we have
\[
H_P^i(X, \mcf)=H_P^i(X_P, \mcf_P).
\]
:::
