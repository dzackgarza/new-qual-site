---
schema: qual/card@1
id: E-0BN1L
kind: problem
title: Order topologies are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 10, printed p. 101, with the
    definition of the order topology in §14; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.10, PDF p. 7. The argument is the two-ray one:
    if an element lies between x and y the rays below it and above it separate them, and if
    none does the rays below y and above x do. Whitman's printed pp. 164-165 proves the same
    statement by cases on basis elements. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Show that every order topology is Hausdorff.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.10, PDF p. 7** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the two-ray argument is theirs. Whitman, printed pp. 164--165, gives a longer proof by cases on basis elements; the argument below is the shorter one.

Let $X$ be an ordered set in the order topology, and let $x\ne y$ in $X$; assume $x<y$.

If there is $c\in X$ with $x<c<y$, then $(-\infty,c)$ and $(c,+\infty)$ are open rays, hence basis elements of the order topology on $X$ (§14, printed p. 84), they contain $x$ and $y$ respectively, and they are disjoint.

If there is no element strictly between $x$ and $y$, then $(-\infty,y)$ and $(x,+\infty)$ are open rays containing $x$ and $y$ respectively, and they are disjoint: a point $z$ in both would satisfy $x<z<y$.

In either case $x$ and $y$ have disjoint neighbourhoods, so $X$ is Hausdorff.
:::
