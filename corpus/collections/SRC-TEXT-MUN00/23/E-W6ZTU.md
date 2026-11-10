---
schema: qual/card@1
id: E-W6ZTU
kind: problem
title: Discrete spaces are totally disconnected
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
    Read against Munkres, Topology, §23 Exercise 5, printed p. 152, with Example 4 for the
    rationals; both questions are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.5, PDF p. 2. In a discrete space a subspace
    with two points is separated by a singleton and its complement; the converse fails, the
    rationals being totally disconnected and not discrete. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

A space is totally disconnected if its only connected subspaces are one-point sets.
Show that if $X$ has the discrete topology, then $X$ is totally disconnected.
Does the converse hold?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.5, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both halves are theirs.

Let $X$ be discrete and let $Y\subset X$ contain two distinct points $p\ne q$. Then $\{p\}$ and $Y-\{p\}$ are nonempty, disjoint, and open in $Y$ (traces of the open sets $\{p\}$ and $X-\{p\}$), and their union is $Y$: a separation. So the only connected subspaces of a discrete space are one-point sets, that is, $X$ is totally disconnected.

The converse fails: $\QQ$ with the usual topology is totally disconnected — for any two distinct $p,q\in\QQ$ choose an irrational $a$ between them, and $\QQ\cap(-\infty,a)$, $\QQ\cap(a,\infty)$ separate the subspace $\{p,q\}$; any subspace with two points is separated the same way — yet $\QQ$ is not discrete, since one-point sets are not open.
:::
