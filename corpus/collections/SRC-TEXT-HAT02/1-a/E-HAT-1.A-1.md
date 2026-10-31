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

::: {.problem}
Let $X$ be a graph in which each vertex is an endpoint of only finitely many edges.
Show that the weak topology on $X$ is a metric topology.
:::

::: {.solution}
Give every edge of $X$ length $1$.
For points $x,y$ in the same connected component, let
$$
\rho(x,y)
$$
be the infimum of the lengths of edgewise paths joining them, and put $\rho(x,y)=\infty$ when they lie in different components.
Define
$$
d(x,y)=\min\{\rho(x,y),1\}.
$$

::: pf

::: pf-step

The function $d$ is a metric on $X$.

::: pf-proof

Symmetry and positive definiteness are immediate from the edge-length construction.
For the triangle inequality, the extended path metric $\rho$ satisfies
$$
\rho(x,z)\le \rho(x,y)+\rho(y,z).
$$
For nonnegative extended real numbers,
$$
\min\{a+b,1\}\le \min\{a,1\}+\min\{b,1\},
$$
so truncating at $1$ preserves the triangle inequality.
Distinct points on the same finite edge have positive path distance, and points in different components have distance $1$.

:::

:::

::: {.pf-step #s2}

The metric topology is contained in the weak topology.

::: pf-proof

On the closure of each edge, the restriction of $d$ gives the usual interval topology locally, since for distances less than $1$ the metric is just edgewise path length.
Therefore every metric-open set has open intersection with every closed edge.
It also has open intersection with the $0$-skeleton.
By the definition of the weak topology on a graph, it is weakly open.

:::

:::

::: {.pf-step #s3}

If $U$ is weakly open and $x$ lies in the interior of an edge, then some $d$-ball about $x$ lies in $U$.

::: pf-proof

The intersection of $U$ with that closed edge is open in the interval topology.
Choose $\varepsilon>0$ smaller than both the distance from $x$ to the two endpoints and the interval radius contained in $U$.
Then
$$
B_d(x,\varepsilon)
$$
stays inside that edge and lies in $U$.

:::

:::

::: {.pf-step #s4}

If $U$ is weakly open and $v$ is a vertex of $X$ lying in $U$, then some $d$-ball about $v$ lies in $U$.

::: pf-proof

Only finitely many edge ends are incident to $v$; a loop edge contributes two ends. Write $r$ for their number.
For each incident end $i$, weak openness gives a number $\varepsilon_i>0$ such that the segment of length $\varepsilon_i$ from that end lies in $U$.
If there are incident ends, set
$$
\varepsilon=\min\{1/2,\varepsilon_1,\dots,\varepsilon_r\}>0.
$$
Any point at $d$-distance less than $\varepsilon$ from $v$ must lie on one of these incident edge segments, hence lies in $U$.
If there are no incident ends, set $\varepsilon=1/2$; then
$$
B_d(v,1/2)=\{v\}\subseteq U.
$$
Thus $B_d(v,\varepsilon)\subseteq U$ in all cases.

:::

:::

::: pf-step

Hence the weak topology equals the topology induced by $d$.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref} every weakly open set is metric open, while step [](#s2){.pf-ref} gives the reverse inclusion.
Therefore the weak topology is metrizable.

:::

:::

:::

:::
