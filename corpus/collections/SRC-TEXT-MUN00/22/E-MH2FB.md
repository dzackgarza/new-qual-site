---
schema: qual/card@1
id: E-MH2FB
kind: problem
title: Continuity of $xy^{-1}$ characterizes topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 1, printed p. 145,
    with the definition of topological group printed there; the stored statement is the
    printed equivalence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.1, printed p. 259.
    Both directions are his: from the group axioms the map x y -> x y^{-1} is a composite of
    multiplication with the continuous map (x,y) -> (x, y^{-1}), and conversely separate
    continuity of that map gives inversion (fixing the first variable at the identity) and
    then multiplication. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Let $H$ denote a group that is also a topological space satisfying the $T_1$ axiom.
Show that $H$ is a topological group if and only if the map of $H \times H$ into $H$ sending $x \times y$ into $x \cdot y^{-1}$ is continuous.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.1, printed p. 259** (`tmp/sources/munkres-solutions-whitman.pdf`); both directions are his, and "positron0802", *Solutions to Topology, Chapter 2*, Supplementary Exercise 1, gives the same.

Let $H$ be a group and a $T_{1}$ space, and let $h:H\times H\to H$, $h(x,y)=x\cdot y^{-1}$.

*If $H$ is a topological group then $h$ is continuous.* The multiplication $m:H\times H\to H$ and the inversion $\iota:H\to H$ are continuous, so $i_{H}\times\iota:H\times H\to H\times H$ is continuous (Exercise 18.10), and $h=m\circ(i_{H}\times\iota)$ is a composite of continuous maps.

*If $h$ is continuous then $H$ is a topological group.* Since $h$ is continuous it is continuous in each variable separately (Exercise 18.11). Fixing the first variable at the identity $e$,
$$
x\longmapsto h(e,x)=e\cdot x^{-1}=x^{-1}
$$
is continuous, so inversion is continuous. Using this, the map
$$
(x,y)\longmapsto h\big(x,\,y^{-1}\big)=x\cdot\big(y^{-1}\big)^{-1}=x\cdot y
$$
is a composite of continuous maps ($(x,y)\mapsto(x,y^{-1})$ is continuous because inversion is, by Exercise 18.10), so multiplication is continuous. Hence $H$ is a topological group.
:::
