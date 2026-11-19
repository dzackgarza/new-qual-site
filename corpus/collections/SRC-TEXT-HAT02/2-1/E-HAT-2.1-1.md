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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 140 carries the running head 131,
    so the printed page is the one the card's earlier event claimed. The durable part of the locator
    is that printed page; the file path names this machine's copy and `tmp/sources` does not survive a
    VM reset. No mathematics changed.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 1 of §2.1, printed p. 131. Correct: the order-preserving
    identification sends $v_0\mapsto v_1\mapsto v_2$, so the three vertices merge; the oriented
    boundary $[v_0,v_1]+[v_1,v_2]-[v_0,v_2]$ becomes $2a-b$, giving $C_2=\ZZ$, $C_1=\ZZ\langle a,b\rangle$,
    $\partial_2=2a-b$, hence $H_0=\ZZ$, $H_1=\ZZ$ and $H_2=0$ — the homology of the Möbius band,
    which is the space the quotient polygon is: the rectangle with one pair of opposite sides
    identified in reverse, cut along a diagonal, and its boundary circle representing $a^2=b$.
    Removed one thing only: a closing step whose proof was the single word-reference to step s3
    (STYLE-08). Not claimed: a published solution, and no certificate.
---

::: {.problem}
This is Exercise 1 of Section 2.1 of Hatcher, *Algebraic Topology* (2002), printed p. 131, read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf` (printed page = PDF page - 9); the statement below is its wording.

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

:::

:::
