---
schema: qual/card@1
id: E-HAT-2.1-1
kind: problem
title: Quotient $\Delta$-complex of 2-simplex with two edges identified
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Identified the quotient polygon as the standard one-triangle model of the Möbius band.
---

What familiar space is the quotient $\Delta$-complex of a 2 simplex $[\nu_0, \nu_1, \nu_2]$ obtained by identifying the edges $[\nu_0, \nu_1]$ and $[\nu_1, \nu_2]$, preserving the ordering of vertices?


::: {.solution}
Let
\[
a=[\nu_0,\nu_1]\sim[\nu_1,\nu_2]
\]
with the identification preserving the displayed vertex order, and let
\[
b=[\nu_0,\nu_2]
\]
be the remaining boundary edge.

<1>1. All three vertices become a single vertex in the quotient.
::: {.proof}
The edge identification sends
\[
\nu_0\mapsto\nu_1,
\qquad
\nu_1\mapsto\nu_2.
\]
Hence
\[
\nu_0\sim\nu_1\sim\nu_2.
\]
:::

<1>2. The quotient has one $2$-cell, one interior edge class $a$, and one boundary edge $b$.
The attaching word of the $2$-cell is
\[
a^2b^{-1}
\]
up to reversing all orientations.
::: {.proof}
Orient the triangle by $[\nu_0,\nu_1,\nu_2]$.
Its oriented boundary is
\[
[\nu_0,\nu_1]+[\nu_1,\nu_2]-[\nu_0,\nu_2].
\]
The first two edges both map to $a$ with the same orientation, while the third maps to $b$.
Thus the quotient polygon has boundary word $aab^{-1}$.
:::

<1>3. This is the standard polygon model of the Möbius band.
::: {.proof}
A Möbius band may be obtained from a rectangle by identifying one pair of opposite sides with reversed transverse orientation.
Cutting that rectangle along a diagonal gives a triangle whose two successive sides are identified in the same directed order; the third side remains the boundary circle.
Equivalently, the core circle is represented by $a$ and the boundary circle represents $a^2$, exactly the relation
\[
b=a^2
\]
encoded by <1>2.
:::

<1>4. Therefore the familiar quotient space is
\[
\boxed{\text{the Möbius band}.}
\]
::: {.proof}
This is <1>3.
:::
:::
