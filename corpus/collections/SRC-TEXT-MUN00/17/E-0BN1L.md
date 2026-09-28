---
schema: qual/card@1
id: E-0BN1L
kind: problem
title: Order topologies are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Order Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that every order topology is Hausdorff.
:::

::: {.solution}
Let $(X,<)$ be a simply ordered set with the order topology, and let $x,y\in X$ with $x<y$.
The open rays $\{z\in X:z<a\}$ and $\{z\in X:z>a\}$, for $a\in X$, are open in the order topology.

<1>1. If some $c\in X$ satisfies $x<c<y$, then $x$ and $y$ have disjoint open neighborhoods.

::: {.proof}
Take $U=\{z:z<c\}$ and $V=\{z:z>c\}$.
Then $x\in U$, $y\in V$, and no $z$ satisfies both $z<c$ and $z>c$, so $U\cap V=\varnothing$.
:::

<1>2. If no $c\in X$ satisfies $x<c<y$, then $x$ and $y$ have disjoint open neighborhoods.

::: {.proof}
Take $U=\{z:z<y\}$ and $V=\{z:z>x\}$.
Then $x\in U$ and $y\in V$, and a point of $U\cap V$ would satisfy $x<z<y$, so $U\cap V=\varnothing$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 cover both cases, so any two distinct points of $X$ have disjoint open neighborhoods.
:::
:::
