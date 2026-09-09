---
schema: qual/card@1
id: E-HAT-1.A-1
kind: problem
title: Weak topology on a graph with finite vertex degree is a metric topology
classification:
  areas:
  - topology
  topics:
  - Graphs
  - Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the unit-edge path metric, truncated across components, and finite valence to compare metric and weak neighborhoods at vertices.
---

Let $X$ be a graph in which each vertex is an endpoint of only finitely many edges.
Show that the weak topology on $X$ is a metric topology.


::: {.solution}
Give every edge of $X$ length $1$.
For points $x,y$ in the same connected component, let
\[
\rho(x,y)
\]
be the infimum of the lengths of edgewise paths joining them, and put $\rho(x,y)=\infty$ when they lie in different components.
Define
\[
d(x,y)=\min\{\rho(x,y),1\}.
\]

<1>1. The function $d$ is a metric on $X$.
::: {.proof}
Symmetry and positive definiteness are immediate from the edge-length construction.
For the triangle inequality, the extended path metric $\rho$ satisfies
\[
\rho(x,z)\le \rho(x,y)+\rho(y,z).
\]
For nonnegative extended real numbers,
\[
\min\{a+b,1\}\le \min\{a,1\}+\min\{b,1\},
\]
so truncating at $1$ preserves the triangle inequality.
Distinct points on the same finite edge have positive path distance, and points in different components have distance $1$.
:::

<1>2. The metric topology is contained in the weak topology.
::: {.proof}
On the closure of each edge, the restriction of $d$ gives the usual interval topology locally, since for distances less than $1$ the metric is just edgewise path length.
Therefore every metric-open set has open intersection with every closed edge.
It also has open intersection with the $0$-skeleton.
By the definition of the weak topology on a graph, it is weakly open.
:::

<1>3. If $U$ is weakly open and $x$ lies in the interior of an edge, then some $d$-ball about $x$ lies in $U$.
::: {.proof}
The intersection of $U$ with that closed edge is open in the interval topology.
Choose $\epsilon>0$ smaller than both the distance from $x$ to the two endpoints and the interval radius contained in $U$.
Then
\[
B_d(x,\epsilon)
\]
stays inside that edge and lies in $U$.
:::

<1>4. If $U$ is weakly open and $v$ is a vertex of $X$ lying in $U$, then some $d$-ball about $v$ lies in $U$.
::: {.proof}
Only finitely many edges
\[
e_1,\dots,e_r
\]
are incident to $v$.
For each $e_i$, weak openness gives a number $\epsilon_i>0$ such that the initial segment of $e_i$ of length $\epsilon_i$ from $v$ lies in $U$.
If $r>0$, set
\[
\epsilon=\min\{1/2,\epsilon_1,\dots,\epsilon_r\}>0.
\]
Any point at $d$-distance less than $\epsilon$ from $v$ must lie on one of these incident edge segments, hence lies in $U$.
If $v$ is isolated, then
\[
B_d(v,1/2)=\{v\}\subseteq U.
\]
Thus $B_d(v,\epsilon)\subseteq U$ in all cases.
:::

<1>5. Hence the weak topology equals the topology induced by $d$.
::: {.proof}
By <1>3--<1>4 every weakly open set is metric open, while <1>2 gives the reverse inclusion.
Therefore the weak topology is metrizable.
:::
:::
