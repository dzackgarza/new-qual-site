---
schema: qual/card@1
id: E-QGR6H
kind: problem
title: Compact unions of closed metrizable subspaces are metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a compact Hausdorff space that is the union of the closed subspaces $X_1$ and $X_2$.
If $X_1$ and $X_2$ are metrizable, show that $X$ is metrizable.
[Hint: Construct a countable collection $\mathcal{A}$ of open sets of $X$ whose intersections with $X_i$ form a basis for $X_i$, for $i = 1, 2$. Assume $X_1 - X_2$ and $X_2 - X_1$ belong to $\mathcal{A}$. Let $\mathcal{B}$ consist of finite intersections of elements of $\mathcal{A}$.]
:::

::: {.solution}
Since each \(X_i\) is closed in compact \(X\), each \(X_i\) is compact. Being metrizable, each \(X_i\) therefore has a countable basis \(\mathcal B_i\).

For every \(B\in\mathcal B_i\), choose an open set \(\widetilde B\subset X\) such that
\[
\widetilde B\cap X_i=B.
\]
Let \(\mathcal A\) be the countable collection of all these chosen lifts, together with the two open sets
\[
X\setminus X_1,\qquad X\setminus X_2.
\]
Let \(\mathcal C\) be the collection of all finite intersections of members of \(\mathcal A\). It is countable.

We show \(\mathcal C\) is a basis for \(X\). Let \(x\in U\) with \(U\subset X\) open. For each \(i=1,2\):

- if \(x\in X_i\), choose \(B_i\in\mathcal B_i\) with
\[
x\in B_i\subset U\cap X_i,
\]
and let \(\widetilde B_i\in\mathcal A\) be its chosen lift;
- if \(x\notin X_i\), use the member \(X\setminus X_i\in\mathcal A\).

The intersection \(C\) of the resulting one or two members of \(\mathcal A\) contains \(x\). For each \(i\),
\[
C\cap X_i\subset U\cap X_i.
\]
Since \(X=X_1\cup X_2\), this implies \(C\subset U\). Hence \(\mathcal C\) is a countable basis for \(X\).

By the preceding compact-Hausdorff metrization criterion, \(X\) is metrizable.
:::
