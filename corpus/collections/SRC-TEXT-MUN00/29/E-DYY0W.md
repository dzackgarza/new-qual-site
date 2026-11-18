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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the quotient map of a topological group by
    a subgroup is continuous, onto and open (Supplementary Exercise TG.5(c), the preimage of
    the image being a union of translates of the open set), and that a continuous open image
    of a locally compact space is locally compact (§29 Exercise 3). positron0802, Chapter 3
    Exercise 29.9, PDF p. 23. The printed statement needed no repair.
---

::: {.exercise}

Show that if $G$ is a locally compact topological group and $H$ is a subgroup, then $G/H$ is locally compact.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.9, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the one-line argument is theirs.

::: pf

::: {.pf-step #open}
The quotient map $p:G\to G/H$ is continuous, surjective and open.

::: pf-proof
A quotient map is continuous and surjective by definition. It is open by Supplementary Exercise TG.5(c): the quotient of a topological group by a subgroup is open, the projection being open because $p^{-1}\big(p(U)\big)=UH=\bigcup_{h\in H}Uh$ is a union of translates of the open set $U$.
:::

:::

::: {.pf-step #locally-compact}
$G/H$ is locally compact.

::: pf-proof
$G$ is locally compact by hypothesis, $p$ is continuous and open by step [](#open){.pf-ref}, and $p$ is onto $G/H$; so $G/H=p(G)$ is locally compact by Munkres §29 Exercise 3, whose second half says that a continuous open image of a locally compact space is locally compact.
:::

:::

:::
:::
