---
schema: qual/card@1
id: E-MJQTF
kind: problem
title: Interior and boundary of a connected set
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 11, printed p. 158; the stored
    statement is the printed two questions.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.11, PDF p. 6. Two tangent discs give a
    connected set whose interior is disconnected, the open interval gives a connected set
    with a two-point boundary, and the rationals give the failure of the converse.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

If $A$ is a connected subspace of $X$, does it follow that $\operatorname{Int} A$ and $\operatorname{Bd} A$ are connected?
Does the converse hold?
Justify your answers.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.11, PDF p. 6** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the two counterexamples are theirs.

**The interior of a connected set need not be connected.** Let $B^{2}$ be the closed unit disc in $\RR^{2}$ and $C$ the closed disc of radius $1$ with centre $2\times0$; then $1\times0\in B^{2}\cap C$, so $A=B^{2}\cup C$ is connected (Theorem 23.3). Its interior is the union of the two open discs, which are disjoint nonempty open sets whose union is $\operatorname{Int}A$: a separation.

**The boundary of a connected set need not be connected.** Take $A=(0,1)\subset\RR$, connected, whose boundary is $\{0,1\}$, a two-point discrete space.

**Nor does the converse hold:** $\QQ$ is not connected, but $\operatorname{Bd}\QQ=\RR$ is connected; and $\operatorname{Int}\QQ=\varnothing$ is connected (vacuously, being empty) while $\QQ$ is not.
:::
