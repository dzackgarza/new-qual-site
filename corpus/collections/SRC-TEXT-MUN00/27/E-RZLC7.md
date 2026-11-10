---
schema: qual/card@1
id: E-RZLC7
kind: problem
title: Connected metric spaces with more than one point are uncountable
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §27 Exercise 4, printed p. 178, with Exercise
    20.3(a); the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 27.4, PDF p. 17. The continuous function z -> d(x,
    z) has connected image in R containing 0 and a positive value, hence uncountably many
    values. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that a connected metric space having more than one point is uncountable.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.4, PDF p. 17** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $X$ be a connected metric space with at least two points $x\ne y$. The distance function $d:X\times X\to\RR$ is continuous (Exercise 20.3(a)), so $d_{x}(z)=d(x,z)$ is continuous on $X$; the image $d_{x}(X)$ is a connected subspace of $\RR$ containing $0$ and $\delta=d(x,y)>0$, hence contains $[0,\delta]$, which is uncountable. Since $d_{x}$ is a function onto a set with uncountably many values, $X$ is uncountable.
:::
