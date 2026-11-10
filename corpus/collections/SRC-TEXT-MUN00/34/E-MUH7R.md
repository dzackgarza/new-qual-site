---
schema: qual/card@1
id: E-MUH7R
kind: problem
title: Compact Hausdorff spaces are metrizable exactly when second countable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S34.pdf, Exercise 34.3 (Theorem 1), page 1 of the file
    (tmp/sources/munkres-solutions-poulsen-S34.pdf, Internet Archive snapshot 20180827202044), and
    "Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 34.3, printed p. 10
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 34 Exercise 3, printed p. 218, Theorem 32.3, Exercise 30.4 and Theorem 34.1. Its two
    directions are the card's: a second-countable compact Hausdorff space is regular, hence
    metrizable by Theorem 34.1; a compact metrizable space is second countable, and the card writes
    the finite 1/n-nets and the rational balls about their union. No correction to the mathematics
    was needed.
---

::: {.exercise}

Let $X$ be a compact Hausdorff space.
Show that $X$ is metrizable if and only if $X$ has a countable basis.
:::

::: {.solution}
If $X$ has a countable basis, then compact Hausdorffness implies regularity, and the Urysohn metrization theorem gives a compatible metric.

Conversely, suppose $X$ is compact and metrizable with metric $d$. For each $n\ge1$, compactness gives finitely many points
$$
x_{n,1},\dots,x_{n,k_n}
$$
such that the balls $B(x_{n,j},1/n)$ cover $X$. Let
$$
D=\{x_{n,j}:n\ge1,1\le j\le k_n\}.
$$
Then $D$ is countable and dense. The family of balls
$$
B(d,q),\qquad d\in D,\ q\in\QQ_{>0},
$$
is countable and forms a basis for the metric topology. Thus $X$ has a countable basis.

Hence a compact Hausdorff space is metrizable exactly when it is second countable.
:::
