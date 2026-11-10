---
schema: qual/card@1
id: E-Z13JH
kind: problem
title: Infinite sets are connected in the finite complement topology
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
    Read against Munkres, Topology (2000), §23 Exercise 4, printed p. 152, with the finite
    complement topology of Example 3 in §12; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.4, PDF p. 2. In a separation of an infinite set
    with the finite complement topology both sides would be infinite and both complements
    finite, which is impossible. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that if $X$ is an infinite set, it is connected in the finite complement topology.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.4, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs, with the cardinal count made explicit.

Let $X$ be infinite with the finite complement topology and suppose $X=A\cup B$ is a separation, so $A$ and $B$ are disjoint nonempty open sets. Being open and nonempty, $X-A$ is finite and $A\ne X$; since $X$ is infinite, $A$ is infinite, and likewise $B$ is infinite. But $B\subset X-A$, which is finite: a contradiction. So $X$ is connected.
:::
