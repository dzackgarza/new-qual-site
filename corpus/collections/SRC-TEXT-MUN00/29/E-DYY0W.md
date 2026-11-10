---
schema: qual/card@1
id: E-DYY0W
kind: problem
title: Coset spaces of locally compact groups are locally compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 9, printed p. 186, with
    Supplementary Exercise TG.5(c) and Exercise 29.3; the stored statement is the printed
    sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.9, PDF p. 23. The quotient map to the coset
    space is continuous and open, so the image of the locally compact group is locally
    compact. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that if $G$ is a locally compact topological group and $H$ is a subgroup, then $G/H$ is locally compact.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.9, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the one-line argument is theirs.

Let $p:G\to G/H$ be the quotient map. It is continuous and surjective, and it is open by Supplementary Exercise TG.5(c); since $G$ is locally compact, $p(G)=G/H$ is locally compact by Exercise 29.3.
:::
