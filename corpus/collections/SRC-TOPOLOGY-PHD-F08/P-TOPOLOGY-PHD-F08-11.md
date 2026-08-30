---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-11
kind: problem
title: Connected components in a locally connected space are open
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Point-Set Topology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
A topological space $X$ is said to be locally connected if the connected components of each point form a base of neighborhoods of $X$.
Prove that in a locally connected space the connected components of $X$ are open in $X$.
:::

::: remark
The phrase “the connected components of each point form a base of neighborhoods of $X$” is retained from the source page.
:::

::: {.solution}
<1>1. Local connectedness and connected neighborhoods:
<2>1. Let $C$ be a connected component of $X$, and let $x \in C$ be an arbitrary point.
Proof: setup.
<2>2. Since $X$ is locally connected, $x$ has a connected open neighborhood $U \subseteq X$ with $x \in U$.
Proof: definition of local connectedness.

<1>2. Containment of the neighborhood in the connected component:
<2>1. Because $U$ is connected and $x \in U \cap C$, the union $U \cup C$ is connected.
Proof: union of connected sets having a non-empty intersection is connected.
<2>2. By definition, the connected component $C$ is a maximal connected subset of $X$.
Therefore $U \cup C = C$, which implies $U \subseteq C$.
Proof: maximality of connected components.

<1>3. Openness of connected components:
<2>1. For every point $x \in C$, there exists an open set $U_x$ such that $x \in U_x \subseteq C$.
Thus:
\[
C = \bigcup_{x \in C} U_x.
\]
Because an arbitrary union of open sets is open, $C$ is an open subset of $X$.
Proof: characterization of open sets as unions of basis/neighborhood elements.

<1>4. Conclusion:
In any locally connected topological space, every connected component is open. Q.E.D.
Proof: <1>1 through <1>3.
:::
