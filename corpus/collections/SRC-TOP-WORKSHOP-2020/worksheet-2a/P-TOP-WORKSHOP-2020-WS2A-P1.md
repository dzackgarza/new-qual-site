---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-P1
kind: problem
title: An open connected subset of Euclidean space is path connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(May 2015) If $X=\mathbb R^n$ with the usual Euclidean topology and $U\subseteq X$ is an open, connected subspace of $X$, show that $U$ is also path connected.
:::

::: {.solution}
Every point \(x\in U\) has an open Euclidean ball
\[
B(x,r)\subseteq U.
\]
Balls in \(\mathbb R^n\) are convex, hence path connected: for \(p,q\in B(x,r)\), the straight-line path
\[
\gamma(t)=(1-t)p+tq
\]
stays inside the ball. Therefore \(U\) is locally path connected.

In any locally path-connected space, path components are open: if \(C\) is a path component and \(x\in C\), choose a path-connected open neighborhood \(V\ni x\); then every point of \(V\) is joined to \(x\), so \(V\subseteq C\). Hence each path component of \(U\) is open in \(U\).

The path components partition \(U\). If there were at least two of them, one component and the union of all the others would be disjoint nonempty open subsets whose union is \(U\), contradicting connectedness. Thus \(U\) has exactly one path component and is path connected.
:::
