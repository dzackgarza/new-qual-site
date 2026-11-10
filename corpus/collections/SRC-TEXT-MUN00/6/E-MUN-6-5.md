---
schema: qual/card@1
id: E-MUN-6-5
kind: problem
title: Finiteness of Cartesian products
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §6 Exercise 5, printed p. 44; the question is
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.5,
    printed p. 78 (tmp/sources/munkres-solutions-whitman.pdf). His answer is the card's:
    with one factor empty the product is empty while the other factor may be infinite,
    and with both factors nonempty the injections a -> (a, b_0) and b -> (a_0, b) into
    the finite product make each factor finite. No defect found.
---

::: {.exercise}
If $A \times B$ is finite, does it follow that $A$ and $B$ are finite?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.5, printed p. 78** (`tmp/sources/munkres-solutions-whitman.pdf`); the counterexample with an empty factor and the argument for nonempty factors, with the two injections into the product, are his.

No. If $B=\varnothing$ and $A=\NN$, then $A\times B=\varnothing$ is
finite, while $A$ is infinite.

If both factors are nonempty, finiteness of $A\times B$ does imply that
each factor is finite. Fixing $b_0\in B$ gives an injection
$a\mapsto(a,b_0)$ from $A$ into $A\times B$. Fixing $a_0\in A$ gives an
injection $b\mapsto(a_0,b)$ from $B$ into $A\times B$. Each image is a
subset of a finite set, hence finite by [[E-MUN-6-2]].
Each factor is in bijection with its image, so both factors are finite.
:::
