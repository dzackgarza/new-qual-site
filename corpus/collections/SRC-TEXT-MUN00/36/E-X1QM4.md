---
schema: qual/card@1
id: E-X1QM4
kind: problem
title: Compact locally euclidean Hausdorff spaces are manifolds
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a Hausdorff space such that each point of $X$ has a neighborhood that is homeomorphic with an open subset of $\mathbb{R}^m$.
Show that if $X$ is compact, then $X$ is an $m$-manifold.
:::

::: {.solution}
By hypothesis, for each \(x\in X\) there is a neighborhood \(U_x\) homeomorphic to an open subset of \(\mathbb R^m\). Choose an open set \(V_x\) with
\[
x\in V_x\subset U_x.
\]
Each \(V_x\) is an open subspace of a Euclidean open set, hence is second countable.

Compactness gives finitely many points \(x_1,\dots,x_r\) such that
\[
X=V_{x_1}\cup\cdots\cup V_{x_r}.
\]
For each \(i\), choose a countable basis \(\mathcal B_i\) for the open subspace \(V_{x_i}\). Since each \(V_{x_i}\) is open in \(X\),
\[
\mathcal B=\bigcup_{i=1}^r\mathcal B_i
\]
is a countable basis for \(X\). The space is Hausdorff by assumption and locally homeomorphic to \(\mathbb R^m\) by hypothesis. Thus it satisfies the standard definition of an \(m\)-manifold.
:::
