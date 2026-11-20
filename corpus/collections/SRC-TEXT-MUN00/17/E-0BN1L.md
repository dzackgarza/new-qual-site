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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 as the two cases (an element between $x$ and $y$, or none) and the dichotomy. Re-checked that the open rays are basis elements of the order topology (§14, printed p. 84) and that $(-\infty,y)\cap(x,+\infty)=\varnothing$ when no element lies between. No statement change.
---

::: {.exercise}

Show that every order topology is Hausdorff.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.10** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the two-ray argument is theirs. Whitman, printed pp. 164--165, gives a longer proof by cases on basis elements; the argument below is the shorter one.

Let $X$ be an ordered set carrying the order topology, and let $x<y$ in $X$. An open ray of $X$ is a basis element of the order topology (§14).

::: pf

::: {.pf-step #with-between}

If some $c\in X$ satisfies $x<c<y$, then $x$ and $y$ have disjoint neighbourhoods.

::: pf-proof

The open rays $(-\infty,c)$ and $(c,+\infty)$ are basis elements of the order topology, hence open; they contain $x$ and $y$ respectively, and they are disjoint.

:::

:::

::: {.pf-step #without-between}

If no element of $X$ lies strictly between $x$ and $y$, then $x$ and $y$ have disjoint neighbourhoods.

::: pf-proof

The open rays $(-\infty,y)$ and $(x,+\infty)$ are basis elements of the order topology; they contain $x$ and $y$ respectively, and they are disjoint, since a point $z$ in both would satisfy $x<z<y$, which no element does.

:::

:::

::: pf-step

$X$ is Hausdorff.

::: pf-proof

Let $x\ne y$ in $X$; interchanging the names if necessary, $x<y$. Either some $c$ satisfies $x<c<y$, and step [](#with-between){.pf-ref} separates the points, or no element lies strictly between $x$ and $y$, and step [](#without-between){.pf-ref} separates them. These two cases exhaust the possibilities, so every two distinct points of $X$ have disjoint neighbourhoods.

:::

:::

:::
:::
