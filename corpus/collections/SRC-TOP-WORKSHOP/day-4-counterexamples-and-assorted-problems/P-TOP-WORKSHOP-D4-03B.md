---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-03B
kind: problem
title: Projection from a product with a compact factor is closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
  - Continuity
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
(Jan ’08 # B8) Suppose that $X$ is an arbitrary topological space and $Y$ is a compact space.
Consider the projection map $\pi:X\times Y\to X$ defined by $\pi(x,y)=x$.
Prove that if $X\times Y$ has the product topology, then $\pi$ is a closed map.
:::

::: {.solution}
Let \(C\subseteq X\times Y\) be closed. We show \(\pi(C)\) is closed. Take \(x_0\notin\pi(C)\). Then
\[
\{x_0\}\times Y\subseteq (X\times Y)\setminus C.
\]
For each \(y\in Y\), choose basic open sets \(U_y\subseteq X\), \(V_y\subseteq Y\) such that
\[
(x_0,y)\in U_y\times V_y\subseteq (X\times Y)\setminus C.
\]
The sets \(V_y\) cover the compact space \(Y\), so choose \(y_1,\dots,y_n\) with
\[
Y=V_{y_1}\cup\cdots\cup V_{y_n}.
\]
Set \(U=U_{y_1}\cap\cdots\cap U_{y_n}\). Then \(U\) is an open neighborhood of \(x_0\), and for every \(x\in U\) and \(y\in Y\), some \(i\) has \(y\in V_{y_i}\), hence
\[
(x,y)\in U_{y_i}\times V_{y_i}\subseteq (X\times Y)\setminus C.
\]
Thus \(U\cap\pi(C)=\varnothing\). Therefore \(X\setminus\pi(C)\) is open, so \(\pi(C)\) is closed.
:::
