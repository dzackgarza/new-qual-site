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

::: {.problem}
Suppose $A, B\subseteq \RR^n$ are connected and not disjoint.
Prove that $A\union B$ is also connected.
:::

::: {.solution}
Suppose $A\cup B=U\cup V$ with $U,V$ disjoint and open in the subspace topology of $A\cup B$. It suffices to show that $U$ or $V$ is empty.

::: pf

::: {.pf-step #each-in-one}
$A$ lies in $U$ or in $V$, and so does $B$.

::: pf-proof
$A\cap U$ and $A\cap V$ are disjoint, relatively open in $A$, and cover $A$. Since $A$ is connected, one of them is empty. The same holds for $B$.
:::

:::

::: pf-step
$U$ or $V$ is empty.

::: pf-proof
Pick $p\in A\cap B$; say $p\in U$. By step [](#each-in-one){.pf-ref}, $A\subseteq U$ and $B\subseteq U$, since each meets $U$ at $p$. Hence $V=V\cap(A\cup B)=\varnothing$.
:::

:::

:::
:::
