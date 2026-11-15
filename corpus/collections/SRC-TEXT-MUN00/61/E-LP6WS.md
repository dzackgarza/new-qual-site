---
schema: qual/card@1
id: E-LP6WS
kind: problem
title: The closed topologist's sine curve separates the sphere
classification:
  areas:
  - topology
  topics:
  - Jordan Separation Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published solution of Munkres §61 Exercise 2 (printed p. 381)
    and located none (issue #144; the queries and the sources are in the COMPLAINTS.md entry for
    §61--§64). The proof is rewritten in prose because its step structure carried an authoring
    defect: three of its five steps had a proof consisting only of a reference to an earlier step,
    and their cross-references were written with empty link text, `[](#s1){.pf-ref}`. The mathematics
    is the same and is checked against the book: $A_1$ is closed and connected because it is the
    closure of the connected graph of $\sin(1/x)$ on $(0,1]$, $A_2$ is a compact connected broken
    line, their intersection is exactly the two points $(0,-1)$ and $(1,\sin1)$, and Theorem 61.4
    (printed p. 380) separates $S^2$ by the union of two closed connected sets meeting in exactly two
    points; the homeomorphic image $C$ is separated because a homeomorphism carries compact sets to
    compact sets, which are closed in $S^2$ by Theorem 26.3 (printed p. 165). The intersection of
    $A_1$ and $A_2$ is now argued point by point rather than asserted. Nothing else on the card was
    changed.
---

::: {.exercise}

Let $A$ be the subset of $\RR^2$ consisting of the union of the topologist's sine curve and the broken-line path from $(0, -1)$ to $(0, -2)$ to $(1, -2)$ to $(1, \sin 1)$.
See Figure 61.4. We call $A$ the closed topologist's sine curve.
Show that if $C$ is a subspace of $S^2$ homeomorphic to the closed topologist's sine curve, then $C$ separates $S^2$.
:::

::: {.solution}

Let $A_1$ be the topologist's sine curve, the union of the graph $\theset{(x,\sin(1/x)) \mid 0<x\le1}$ with the segment $\theset{0}\times[-1,1]$, and let $A_2$ be the broken line from $(0,-1)$ to $(0,-2)$ to $(1,-2)$ to $(1,\sin1)$; then $A=A_1\cup A_2$.

The set $A_1$ is closed and connected. It is the closure in $\RR^2$ of the graph of $g(x)=(x,\sin(1/x))$ on $(0,1]$, which is connected, being a continuous image of the connected set $(0,1]$; and the closure of a connected set is connected. The broken line $A_2$ is the image of $[0,3]$ under a continuous map, so it is compact and connected. Their intersection is exactly $\theset{(0,-1),\ (1,\sin1)}$: the first segment of $A_2$ leaves $(0,-1)$ downward and meets the segment $\theset{0}\times[-1,1]$, the only part of $A_1$ on the second coordinate axis, only at $(0,-1)$; the second segment lies on the line $y=-2$, off $A_1$; and the third segment lies on the line $x=1$ from $(1,-2)$ up to $(1,\sin1)$, while the only point of $A_1$ with first coordinate $1$ is $(1,\sin1)$.

Now let $h:A\to C$ be a homeomorphism. The sets $h(A_1)$ and $h(A_2)$ are connected, and compact, hence closed in $S^2$ (Theorem 26.3, printed p. 165); their intersection is the two points $h(0,-1)$ and $h(1,\sin1)$, and their union is $C$. Theorem 61.4, the general separation theorem (printed p. 380), states that two closed connected subsets of $S^2$ whose intersection consists of exactly two points have a union that separates $S^2$. Hence $C$ separates $S^2$.
:::
