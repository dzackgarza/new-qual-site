---
schema: qual/card@1
id: E-E5ZWY
kind: problem
title: Every order topology is regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Order Topology
relations: []
review: draft
---

::: {.exercise}

Show that every order topology is regular.
:::

::: {.solution}
An ordered space in the order topology is Hausdorff: if \(x<y\), then either there is \(z\) with \(x<z<y\), in which case the rays \((-\infty,z)\) and \((z,\infty)\) separate \(x\) and \(y\), or there is no point between them, in which case \((-\infty,y)\) and \((x,\infty)\) do so.

We prove regularity. Let \(x\in U\) with \(U\) open. Choose a convex basic open set \(B\) with
\[
x\in B\subset U.
\]
We claim there is a convex open neighborhood \(V\) of \(x\) with
\[
\overline V\subset B.
\]
For each finite endpoint of \(B\), choose an interior cut strictly between that endpoint and \(x\) when such a point exists. If no such point exists, then \(x\) is the immediate successor (or predecessor) of that endpoint, so the corresponding one-sided ray beginning at \(x\) is already open. Doing this independently on the left and right gives a convex basic neighborhood \(V\) whose possible closure endpoints still lie inside \(B\). Thus \(\overline V\subset B\subset U\).

Equivalently, if \(A=X\setminus U\) is closed and \(x\notin A\), then \(V\) and \(X\setminus\overline V\) are disjoint open neighborhoods of \(x\) and \(A\), respectively. Hence every order topology is regular.
:::
