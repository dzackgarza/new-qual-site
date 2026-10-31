---
schema: qual/card@1
id: P-UCTOP290-S4-13
kind: problem
title: Six-sheeted cover from a free-group map to $S_3$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-corrected
  by: chatgpt
  date: 2026-10-31
  note: >-
    Sheet 4, Problem 13 says the kernel is a subgroup of S3, but the
    displayed map has domain F2. The kernel is a subgroup of F2.
    Read the statement against the extraction and PDF page image.
---

::: {.problem}
Let $F_2=\pi_1(S^1\vee S^1)=\langle a,b\rangle$.
Let $\phi:F_2\to S_3$ send $a$ to $(12)$ and $b$ to $(123)$.
Construct the covering space corresponding to $\ker\phi$.
:::

::: {.solution}

Take one vertex for each $g\in S_3$.
At every vertex draw the directed edges
$$
g\xrightarrow{a}g(12),
\qquad
g\xrightarrow{b}g(123).
$$
There are six vertices. The $a$-edges form three two-cycles,
and the $b$-edges form two three-cycles. These instructions
give a labeled drawing of the graph.

Map each vertex to the wedge point of $S^1\vee S^1$ and each
edge to the circle with its label. Right multiplication by either
permutation is a bijection of $S_3$, so every vertex has one
incoming and one outgoing edge of each label. Thus the map is
a covering. Since $(12)$ and $(123)$ generate $S_3$, the graph
is connected.

A word $w$ lifted from the identity vertex ends at $\phi(w)$.
The based loop subgroup is therefore exactly $\ker\phi$.
Left multiplication on the vertex labels gives the deck group
$S_3$ of this regular six-sheeted cover.

:::
