---
schema: qual/card@1
id: E-MD9QR
kind: problem
title: The ordered square is locally connected but not locally path connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 3, printed p. 162, with Example 1
    and Example 6 of §24 and Theorem 24.1; the two questions are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.3, PDF pp. 8-9. Basis intervals of the ordered
    square are connected, so it is locally connected; no neighbourhood of p x 1 is path
    connected, since a path leaving it would inject an uncountable interval into the
    rationals; the path components are the vertical fibres. The presentation of the last
    paragraph is repaired. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that the ordered square is locally connected but not locally path connected.
What are the path components of this space?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.3, PDF pp. 8--9** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs, with the wording of the last paragraph repaired.

*The ordered square $I_{o}^{2}$ is locally connected.* Let $x\times y$ and a neighbourhood $U$ of it be given; $U$ contains a basis interval. Since $I_{o}^{2}$ is a linear continuum (Example 1 of §24), that interval is connected (Theorem 24.1), so it is a connected neighbourhood of $x\times y$ inside $U$.

*It is not locally path connected at the points $p\times1$ and $q\times0$ with $0<p,q<1$.* Suppose $V$ is a path-connected neighbourhood of $p\times1$. As a neighbourhood, $V$ contains a point $q\times0$ with $q>p$. By the intermediate value theorem the image of a path in $V$ from $p\times1$ to $q\times0$ contains every point between them, so for each $x\in(p,q)$ the set $U_{x}=f^{-1}(\{x\}\times(0,1))$ is a nonempty open subset of $[0,1]$; choosing a rational $q_{x}\in U_{x}$ gives an injection of the uncountable interval $(p,q)$ into $\QQ$, which is impossible. The points $q\times0$ are treated the same way.

*The path components are the segments $\{x\}\times[0,1]$.* Each such segment is homeomorphic with $[0,1]$, hence path connected; and if two points in different segments, say $x\times y$ and $x'\times y'$ with $x<x'$, lay in one path component, the argument above applied with $p=x'$... precisely, a path joining them would force an injection of $(x,x')$ into $\QQ$. So the path components are exactly the fibres.
:::
