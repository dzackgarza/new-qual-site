---
schema: qual/card@1
id: P-MPD2Q
kind: problem
title: The union of two intersecting connected sets is connected
classification:
  areas:
  - complex-analysis
  topics:
  - Connectedness
  - Point-Set Topology
relations: []
review: draft
---

::: problem
Suppose $A, B\subseteq \RR^n$ are connected and not disjoint.
Prove that $A\union B$ is also connected.
:::

::: solution
Suppose, for contradiction, that $A\cup B$ is disconnected. Then there are
disjoint nonempty sets $U,V$, open in the subspace topology of $A\cup B$, such
that
\[
A\cup B=U\cup V.
\]
Because $A$ is connected, it must lie entirely in one of $U,V$; likewise $B$
must lie entirely in one of them. Since $A\cap B\ne\varnothing$, the two sets
cannot lie in different members of the separation. Hence both $A$ and $B$ lie
in the same one, leaving the other empty, a contradiction. Therefore
$A\cup B$ is connected.
:::
