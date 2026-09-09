---
schema: qual/card@1
id: E-HYQMG
kind: problem
title: $X$ is Hausdorff if and only if $\Delta(X)$ is closed in $X\times X$
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Show that a topological space $X$ is Hausdorff if and only if the diagonal $\Delta(X) = \{(x, x) \mid x \in X\}$ is closed in $X \times X$ with the product topology.
:::

::: solution
<1>1. Suppose $X$ is Hausdorff. Let $(x,y)\notin\Delta(X)$, so $x\ne y$. Choose disjoint open neighborhoods $U\ni x$ and $V\ni y$. Then
\[
(x,y)\in U\times V
\]
and $U\times V$ is disjoint from $\Delta(X)$. Hence $(X\times X)\setminus\Delta(X)$ is open, so $\Delta(X)$ is closed.

<1>2. Conversely, suppose $\Delta(X)$ is closed. If $x\ne y$, then
\[
(x,y)\in (X\times X)\setminus\Delta(X),
\]
which is open. Hence some basic open set satisfies
\[
(x,y)\in U\times V\subseteq (X\times X)\setminus\Delta(X).
\]
If $U\cap V$ contained $z$, then $(z,z)\in U\times V$, contradicting disjointness from the diagonal. Thus $U\cap V=\varnothing$, so $x$ and $y$ have disjoint open neighborhoods.

<1>3. Therefore $X$ is Hausdorff if and only if $\Delta(X)$ is closed in $X\times X$.
:::
