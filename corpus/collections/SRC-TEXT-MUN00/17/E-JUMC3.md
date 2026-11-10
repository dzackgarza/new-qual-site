---
schema: qual/card@1
id: E-JUMC3
kind: problem
title: Differences of open and closed sets
classification:
  areas:
  - topology
  topics:
  - Closed Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 4, printed p. 100; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.4, PDF p. 6. The two identities X - (U - A) =
    (X - U) cup A and X - (A - U) = (X - A) cup U give the two conclusions as a union of two
    closed sets and a union of two open sets. (tmp/sources/munkres-solutions-positron-
    ch2.pdf).
---

::: {.exercise}

Show that if $U$ is open in $X$ and $A$ is closed in $X$, then $U - A$ is open in $X$, and $A - U$ is closed in $X$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.4, PDF p. 6** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the two complements are theirs. Whitman proves the same two statements on his printed p. 160 by way of a set identity and its corollary.

Since $U\subset X$ and $A\subset X$,
$$
X-(U-A)=(X-U)\cup A,\qquad X-(A-U)=(X-A)\cup U .
$$
The first is a union of two closed sets ($X-U$ is closed because $U$ is open, and $A$ is closed), hence closed, so $U-A$ is open in $X$. The second is a union of two open sets ($X-A$ is open because $A$ is closed, and $U$ is open), hence open, so $A-U$ is closed in $X$.
:::
