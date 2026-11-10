---
schema: qual/card@1
id: E-N5AYS
kind: problem
title: Disjoint open collections in separable spaces are countable
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), the second item printed under
    the heading "Problem 30.12", printed p. 3 (tmp/sources/munkres-solutions-dougsworld-ch4.pdf);
    its statement is the printed Exercise 30.13 (Munkres, Topology (2000), printed p. 194), which
    that set numbers as 30.12 -- the numbering slip is in the source, and the exercise it answers
    is the one on this card. Checked against the printed exercise; the injection U -> a point of
    D cap U is the source's argument and no correction was needed.
---

::: {.exercise}

Show that if $X$ has a countable dense subset, every collection of disjoint open sets in $X$ is countable.
:::

::: {.solution}
Let $D\subset X$ be countable and dense, and let $\mathcal U$ be a collection of pairwise disjoint open sets. Remove $\varnothing$ if it occurs; this removes at most one member. For each remaining $U\in\mathcal U$, density gives a point $d_U\in D\cap U$. Since the nonempty members of $\mathcal U$ are disjoint, the points $d_U$ are distinct. Thus
$$
U\longmapsto d_U
$$
injects the nonempty members of $\mathcal U$ into $D$. Hence $\mathcal U$ is countable.
:::
