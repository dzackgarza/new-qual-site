---
schema: qual/card@1
id: E-GZX7B
kind: exercise
title: Components of locally compact paracompact Hausdorff spaces are second countable
classification:
  areas:
  - topology
  topics:
  - Paracompactness
  - Compactness
relations: []
review: draft
---

::: {.exercise title="Munkres §41.10"}

Theorem.
If $X$ is a Hausdorff space that is locally compact and paracompact, then each component of $X$ has a countable basis.

Proof.
If $X_0$ is a component of $X$, then $X_0$ is locally compact and paracompact.
Let $\mathcal{C}$ be a locally finite covering of $X_0$ by sets open in $X_0$ that have compact closures.
Let $U_1$ be a nonempty element of $\mathcal{C}$, and in general let $U_n$ be the union of all elements of $\mathcal{C}$ that intersect $\overline{U}_{n-1}$.
Show that $\overline{U}_n$ is compact, and the sets $U_n$ cover $X_0$.
:::
