---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-11
kind: problem
title: Connected components are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Define the term “connected component” for a topological space.
Prove that a connected component is connected.
:::

::: {.solution}
<1>1. A connected component of $X$ is a maximal connected subset of $X$ (maximal with respect to inclusion among connected subsets).
Proof: definition.

<1>2. Equivalently, the connected component of a point $x \in X$ is the union of all connected subsets of $X$ containing $x$.
Proof: the union of all connected subsets containing $x$ is connected (they all share $x$), and it is maximal.

<1>3. A connected component is connected.
<2>1. Let $C$ be a connected component, and let $x \in C$.
Proof: take a point of $C$.
<2>2. $C$ is the union of all connected subsets of $X$ containing $x$.
Proof: <1>2.
<2>3. The union of connected subsets that all contain a common point $x$ is connected.
Proof: if such a union were disconnected, it would be a disjoint union of two nonempty separated sets, but both would have to contain $x$ (since $x$ is in every member and hence in the union), a contradiction.
<2>4. Hence $C$ is connected.
Proof: <2>2 and <2>3.

<1>4. Q.E.D.
Proof: <1>3.
:::
