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
- event: source-corrected
  by: claude
  date: 2026-10-31
  note: >-
    The card wrote the vertices of the simplex as the Greek letter, `\nu_0`,
    where Hatcher writes them `v_0`; the vertex symbol is restored throughout.
    Found by comparing the statement with the printed exercise.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof: the order-preserving identification merges the three vertices, the two boundary edges become a single edge class $a$ with $b$ a loop, and the $\Delta$-complex chain complex gives $H_1=\ZZ$ and $H_0=\ZZ$, so the quotient is $S^1$.
---

::: {.problem}
What familiar space is the quotient $\Delta$-complex of a 2 simplex $[v_0, v_1, v_2]$ obtained by identifying the edges $[v_0, v_1]$ and $[v_1, v_2]$, preserving the ordering of vertices?
:::

::: {.solution}
Let
$$
a=[v_0,v_1]\sim[v_1,v_2]
$$
with the identification preserving the displayed vertex order, and let
$$
b=[v_0,v_2]
$$
be the remaining boundary edge.

::: pf

::: pf-step

All three vertices become a single vertex in the quotient.

::: pf-proof

The edge identification sends
$$
v_0\mapsto v_1,
\qquad
v_1\mapsto v_2.
$$
Hence
$$
v_0\sim v_1\sim v_2.
$$

:::

:::

::: {.pf-step #s2}

The quotient has one $2$-cell, one interior edge class $a$, and one boundary edge $b$.
The attaching word of the $2$-cell is
$$
a^2b^{-1}
$$
up to reversing all orientations.

::: pf-proof

Orient the triangle by $[v_0,v_1,v_2]$.
Its oriented boundary is
$$
[v_0,v_1]+[v_1,v_2]-[v_0,v_2].
$$
The first two edges both map to $a$ with the same orientation, while the third maps to $b$.
Thus the quotient polygon has boundary word $aab^{-1}$.

:::

:::

::: {.pf-step #s3}

This is the standard polygon model of the Möbius band.

::: pf-proof

A Möbius band may be obtained from a rectangle by identifying one pair of opposite sides with reversed transverse orientation.
Cutting that rectangle along a diagonal gives a triangle whose two successive sides are identified in the same directed order; the third side remains the boundary circle.
Equivalently, the core circle is represented by $a$ and the boundary circle represents $a^2$, exactly the relation
$$
b=a^2
$$
encoded by step [](#s2){.pf-ref}.

:::

:::

::: pf-step

Therefore the familiar quotient space is
$$
\boxed{\text{the Möbius band}.}
$$

::: pf-proof

This is step [](#s3){.pf-ref}.

:::

:::

:::

:::
