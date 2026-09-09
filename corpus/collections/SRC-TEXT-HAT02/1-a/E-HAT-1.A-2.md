---
schema: qual/card@1
id: E-HAT-1.A-2
kind: problem
title: Connected graph retracts onto any connected subgraph
classification:
  areas:
  - topology
  topics:
  - Graphs
  - Retractions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Extended the identity on the connected subgraph cellwise over all remaining vertices and edges, using weak-topology continuity.
---

Show that a connected graph retracts onto any connected subgraph.


::: {.solution}
Let $A\subseteq X$ be a connected subgraph.
Choose a vertex
\[
a_0\in A.
\]

<1>1. Define a map on the vertices of $X$ by
\[
r(v)=
\begin{cases}
v,&v\in A,\\a_0,&v\notin A.
\end{cases}
\]
::: {.proof}
This already restricts to the identity on the $0$-skeleton of $A$.
:::

<1>2. For every edge $e$ of $X$ not contained in $A$, extend $r$ continuously across $e$ by mapping it to a path in $A$ joining the images of its endpoints.
::: {.proof}
Let the endpoints of $e$ be $v,w$.
Since $A$ is connected, hence path connected as a graph, there is an edge path
\[
\alpha_e:I\to A
\]
from $r(v)$ to $r(w)$.
Choose a characteristic parametrization of $e$ by $I$ and define $r$ on $e$ to be $\alpha_e$.
For an edge lying in $A$, define $r$ to be the identity.
The definitions agree at all common endpoints by construction.
:::

<1>3. The resulting map
\[
r:X\to A
\]
is continuous.
::: {.proof}
Its restriction to the closure of every edge is continuous by <1>2, and its restriction to the $0$-skeleton is continuous.
The graph has the weak CW topology, so a map out of $X$ is continuous precisely when its restrictions to the closed cells are continuous.
Hence $r$ is continuous.
:::

<1>4. The map $r$ is a retraction of $X$ onto $A$.
::: {.proof}
On every vertex and every edge of $A$, the construction used the identity map.
Thus
\[
r|_A=\operatorname{id}_A.
\]
:::
:::
