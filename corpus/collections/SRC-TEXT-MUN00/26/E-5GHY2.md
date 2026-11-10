---
schema: qual/card@1
id: E-5GHY2
kind: problem
title: Projections with compact factor are closed maps
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 7, printed p. 171, with the tube
    lemma; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.7, PDF p. 13. A point outside the image gives a
    slice disjoint from the closed set, and the tube lemma produces a neighbourhood of it
    disjoint from the image. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that if $Y$ is compact, then the projection $\pi_1: X \times Y \to X$ is a closed map.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.7, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the tube-lemma argument is theirs.

Let $Y$ be compact, $C\subset X\times Y$ closed, and $x_{0}\notin\pi_{1}(C)$. The slice $x_{0}\times Y$ is compact (it is homeomorphic with $Y$) and lies in the open set $(X\times Y)-C$, so by the tube lemma it has a tube $W\times Y\subset(X\times Y)-C$ with $W$ a neighbourhood of $x_{0}$. Then $W\cap\pi_{1}(C)=\varnothing$, so $\pi_{1}(C)$ is closed. Hence $\pi_{1}$ is a closed map.
:::
