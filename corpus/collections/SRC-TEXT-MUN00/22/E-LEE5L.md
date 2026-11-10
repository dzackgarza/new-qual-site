---
schema: qual/card@1
id: E-LEE5L
kind: problem
title: A quotient map that is neither open nor closed
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Exercise 3, printed p. 145, with Example 1 of
    §22 for the retraction argument; the subspace A and the two claims are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 22.3, PDF p. 27. The restricted projection is a
    composite of a retraction and a homeomorphism, hence a quotient map; the open half-plane
    in A maps to (0,infinity) and the closed set cut out by the tangent graph maps to an
    open interval, so it is neither open nor closed. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
---

::: {.exercise}

Let $\pi_1: \RR \times \RR \to \RR$ be projection on the first coordinate.
Let $A$ be the subspace of $\RR \times \RR$ consisting of all points $x \times y$ for which either $x \geq 0$ or $y = 0$ (or both); let $q: A \to \RR$ be obtained by restricting $\pi_1$.
Show that $q$ is a quotient map that is neither open nor closed.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.3, PDF p. 27** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the whole construction with both witnesses is theirs.

Let $A=\{(x,y)\mid x\ge0 \text{ or } y=0\}\subset\RR^{2}$ and let $q=\pi_{1}\restrict_{A}:A\to\RR$.

*$q$ is a quotient map.* The retraction $r:A\to\RR\times\{0\}$, $r(x,y)=x\times0$, is continuous (it is the restriction of the continuous map $(x,y)\mapsto x\times0$ of $\RR^{2}$) and fixes $\RR\times\{0\}$; by Exercise 22.2(b) it is a quotient map. The map $h:\RR\times\{0\}\to\RR$, $h(x\times0)=x$, is a homeomorphism, hence a quotient map. So $q=h\circ r$ is a quotient map, as a composite of quotient maps.

*$q$ is not open.* The set $(\RR\times(0,\infty))\cap A$ is open in $A$, but its image under $q$ is $(0,\infty)$, which is not open in $\RR$.

*$q$ is not closed.* Let $C=\{x\times\tan x\mid \pi/2<x<3\pi/2\}$, which is the intersection of the graph of $\tan$ with the strip $\pi/2<x<3\pi/2$; the graph is closed in $\RR^{2}$ and the strip is closed, so $C$ is closed in $\RR^{2}$, hence $C\cap A$ is closed in $A$. But $q(C\cap A)=(\pi/2,3\pi/2)$ is not closed in $\RR$.
:::
