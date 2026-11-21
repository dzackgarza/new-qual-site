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
    Munkres §61 Exercise 2, printed p. 381. Searched outside the checkout for issue #144; the thread the throttled
    address could not open was read from the orchestrator's machine, recorded in tmp/sources/mse-searches-144.md,
    thread tmp/sources/mse-1394696-E-LP6WS.md. Math StackExchange 1394696, "A generalization of Jordan curve theorem
    involving Warsaw circle" (asked 2015-08-12), answer 1394737 by user98602 (2015-08-12) asserts a criterion: a
    compact X in R^2 whose first Cech homology is Z has a complement with two components, one bounded, one
    unbounded, and the Warsaw circle satisfies it. That is an assertion through Alexander duality, which the book
    does not prove and which would need the Cech theory it does not have, and it concerns the Warsaw circle rather
    than the closed topologist's sine curve. Nothing is transcribed, and the card keeps the proof rewritten in this
    event. The mathematics is checked against the book: A_1 is closed and connected, being the closure of the graph
    of sin(1/x) on (0,1], A_2 is a compact connected broken line, their intersection is exactly the two points
    (0,-1) and (1, sin 1), and Theorem 61.4 (printed p. 380) separates S^2 by the union of two closed connected sets
    meeting in exactly two points.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader of this card reported that the compactness of A_1 was used and never proved: the proof
    established that A_1 is closed and connected and then said that h(A_1) is compact. A_1 is contained
    in [0, 1] x [-1, 1], so it is bounded, and a closed and bounded subspace of R^2 is compact, Theorem
    27.3 (printed p. 173); the proof now says so, and it now says that h(A_1) and h(A_2) are compact as
    continuous images of the compact sets A_1 and A_2, Theorem 26.5 (printed p. 166), before Theorem
    26.3 (printed p. 165) closes them in S^2. Nothing else on the card was changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the two closed halves of the closed
    topologist's sine curve are compact and connected, that their intersection is exactly
    the two named points (segment by segment), and that Theorem 61.4 (general separation
    theorem, printed p. 380) applies to their images under a homeomorphism. The argument is
    the card's own; no retained set is cited. Munkres §61, printed p. 398. The printed
    statement needed no repair.
---

::: {.exercise}

Let $A$ be the subset of $\RR^2$ consisting of the union of the topologist's sine curve and the broken-line path from $(0, -1)$ to $(0, -2)$ to $(1, -2)$ to $(1, \sin 1)$.
See Figure 61.4. We call $A$ the closed topologist's sine curve.
Show that if $C$ is a subspace of $S^2$ homeomorphic to the closed topologist's sine curve, then $C$ separates $S^2$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It checks the two hypotheses of the general separation theorem, Munkres §61 Theorem 61.4.

Let $A_{1}$ be the topologist's sine curve, the union of the graph $\{(x,\sin(1/x))\mid 0<x\le1\}$ with the segment $\{0\}\times[-1,1]$, and let $A_{2}$ be the broken line from $(0,-1)$ to $(0,-2)$ to $(1,-2)$ to $(1,\sin1)$; then $A=A_{1}\cup A_{2}$.

::: pf

::: {.pf-step #clopen}
$A_{1}$ and $A_{2}$ are compact and connected.

::: pf-proof
$A_{1}$ is the closure in $\RR^{2}$ of the graph $G$ of $g(x)=(x,\sin(1/x))$ on $(0,1]$, which is connected, being a continuous image of the connected set $(0,1]$; the closure of a connected set is connected (Theorem 23.4). It is contained in $[0,1]\times[-1,1]$, hence bounded, and closed, so it is compact (Theorem 27.3). $A_{2}$ is the image of the connected set $[0,3]$ under a continuous broken-line parametrization, hence connected, and compact as a continuous image of a compact set (Theorem 26.5).
:::

:::

::: {.pf-step #intersection}
$A_{1}\cap A_{2}=\{(0,-1),\ (1,\sin1)\}$.

::: pf-proof
$A_{2}$ is the union of three segments: from $(0,-1)$ to $(0,-2)$, from $(0,-2)$ to $(1,-2)$, and from $(1,-2)$ to $(1,\sin1)$. The first lies in $\{0\}\times[-2,-1]$ and meets the part of $A_{1}$ on the second coordinate axis, namely $\{0\}\times[-1,1]$, only at $(0,-1)$, and meets the graph part, whose first coordinate is positive, in nothing. The second lies on the line $y=-2$ and meets the graph part, where $y\in[-1,1]$, in nothing, and is disjoint from $\{0\}\times[-1,1]$. The third lies on the line $x=1$, and the only point of $A_{1}$ with first coordinate $1$ is $(1,\sin1)$, which is its upper endpoint. So the intersection is those two points, and each of them lies in both sets.
:::

:::

::: {.pf-step #separation}
If $C\subset S^{2}$ is homeomorphic to $A$, then $C$ separates $S^{2}$.

::: pf-proof
Let $h:A\to C$ be a homeomorphism. Then $h(A_{1})$ and $h(A_{2})$ are connected, being continuous images of connected sets, and compact, being continuous images of the compact sets of step [](#clopen){.pf-ref}, hence closed in the Hausdorff space $S^{2}$ (Theorem 26.3). Their intersection is the two points $h(0,-1)$ and $h(1,\sin1)$ and their union is $C$. Two closed connected subsets of $S^{2}$ whose intersection consists of exactly two points have a union that separates $S^{2}$ (Theorem 61.4), so $C$ separates $S^{2}$.
:::

:::

:::
:::
