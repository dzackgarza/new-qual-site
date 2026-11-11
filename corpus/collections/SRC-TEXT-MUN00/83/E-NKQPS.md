---
schema: qual/card@1
id: E-NKQPS
kind: problem
title: The vertex assumption in the normality proof for linear graphs
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 83 Exercise 1, printed p. 505. Why the proof of normality of a linear graph may assume every vertex lies in B or C: vertices can be adjoined to the closed sets. Checked against the printed proof in Section 83. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

In the proof of normality of a linear graph $X$, why did we assume that every vertex of $X$ belongs either to $B$ or to $C$?
:::

::: {.solution}
Let $X^0$ be the set of vertices of the linear graph $X$. As proved just before Lemma 83.1, $X^0$ is a closed discrete subspace of $X$, and in fact every subset of $X^0$ is closed in $X$.

Given the original disjoint closed sets $B,C$, let
$$
D=X^0-(B\cup C).
$$
Then $D$ is closed, so replacing $B$ by $B\cup D$ preserves closedness and keeps it disjoint from $C$. Thus, without loss of generality, every vertex lies in $B$ or in $C$.

This extra condition is used twice in the proof. First, if the open sets chosen separately inside two incident edges overlap, their common point must be the common vertex; knowing that every vertex lies in $B$ or $C$ shows such a point cannot lie simultaneously in the $B$-neighborhood and the $C$-neighborhood. Second, when proving the unions of the edgewise neighborhoods are open in the coherent topology, any extra intersection point between neighborhoods from different edges is again a vertex, and membership in $B$ or $C$ forces it into the appropriate edgewise neighborhood. Without assigning the unused vertices first, these two arguments would leave the behavior at such vertices uncontrolled.
:::
