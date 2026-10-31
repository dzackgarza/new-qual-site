---
schema: qual/card@1
id: E-HAT-1.B-1
kind: problem
title: "Free simplicial actions are covering space actions"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.B, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the barycentric-coordinate metric to show every orbit is uniformly separated at each point, then chose a small translate-disjoint neighborhood.
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The book says Delta-complex; the stored statement said complex.
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: The barycentric l1 metric does not describe a Delta-complex, whose simplices need not be determined by their vertices, and need not give its topology; rewritten with open stars in the barycentric subdivision.
---

::: {.problem}
Suppose a group $G$ acts simplicially on a $\Delta$-complex $X$, where "simplicially" means that each element of $G$ takes each simplex of $X$ onto another simplex by a linear homeomorphism.
If the action is free, show it is a covering space action.
:::

::: {.solution}
Recall that the action is a covering space action when every point $x\in X$ has a neighborhood $U$ with $g_1U\cap g_2U=\varnothing$ for $g_1\ne g_2$, equivalently $U\cap gU=\varnothing$ for $g\ne1$.
Let $X'$ be the barycentric subdivision of $X$.
Each simplex of $X'$ lies in a simplex of $X$, and its vertices are the barycenters of faces of that simplex of pairwise distinct dimensions.

::: pf

::: {.pf-step #s1}

$G$ acts simplicially on $X'$, and each $g\in G$ preserves the dimension of the face whose barycenter a vertex of $X'$ is.

::: pf-proof

A linear homeomorphism of simplices carries faces to faces of the same dimension and barycenters to barycenters, so it carries the barycentric subdivision of a simplex linearly onto the barycentric subdivision of its image.

:::

:::

::: {.pf-step #s2}

For a vertex $w$ of $X'$ let $\operatorname{st}(w)$ be its open star, the union of the open simplices of $X'$ having $w$ as a vertex.
Then $\operatorname{st}(w)$ is open, $g\operatorname{st}(w)=\operatorname{st}(gw)$, the open stars cover $X$, and if $\operatorname{st}(w)\cap\operatorname{st}(w')\ne\varnothing$ then $w$ and $w'$ are vertices of one simplex of $X'$.

::: pf-proof

The complement of $\operatorname{st}(w)$ is the union of the closed simplices of $X'$ not having $w$ as a vertex, and its intersection with each closed simplex is a union of faces, hence closed; so $\operatorname{st}(w)$ is open in the weak topology.
The identity $g\operatorname{st}(w)=\operatorname{st}(gw)$ follows from step [](#s1){.pf-ref}.
Every point lies in some open simplex, which has a vertex, so the stars cover $X$.
A point of $\operatorname{st}(w)\cap\operatorname{st}(w')$ lies in a unique open simplex, and that simplex has both $w$ and $w'$ as vertices.

:::

:::

::: {.pf-step #s3}

If $g\ne1$ and $w$ is a vertex of $X'$, then $\operatorname{st}(w)\cap g\operatorname{st}(w)=\varnothing$.

::: pf-proof

Suppose the intersection is nonempty.
By step [](#s2){.pf-ref}, $w$ and $gw$ are vertices of one simplex of $X'$.
By step [](#s1){.pf-ref} they are barycenters of faces of the same dimension, and two distinct vertices of a simplex of $X'$ are barycenters of faces of different dimensions, so $gw=w$.
Then $g$ fixes the point $w$, and freeness gives $g=1$, a contradiction.

:::

:::

::: pf-step

Hence the action is a covering space action.

::: pf-proof

Given $x\in X$, choose by step [](#s2){.pf-ref} a vertex $w$ of $X'$ with $x\in\operatorname{st}(w)$ and put $U=\operatorname{st}(w)$.
For $g_1\ne g_2$, step [](#s3){.pf-ref} applied to $g_1^{-1}g_2$ gives $U\cap g_1^{-1}g_2U=\varnothing$, so $g_1U\cap g_2U=\varnothing$.

:::

:::

:::

:::
