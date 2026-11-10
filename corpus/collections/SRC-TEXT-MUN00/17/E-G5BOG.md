---
schema: qual/card@1
id: E-G5BOG
kind: problem
title: Subspaces of Hausdorff spaces are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 12, printed p. 101, with the
    definition of the subspace topology in §16; the stored statement is the printed
    sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.12, PDF p. 8. The traces on the subspace of two
    disjoint open sets of the space are disjoint open sets of the subspace.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Show that a subspace of a Hausdorff space is Hausdorff.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.12, PDF p. 8** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the proof is theirs, and Whitman's printed p. 165 is the same.

Let $X$ be Hausdorff and $Y\subset X$ a subspace. Let $y_{1}\ne y_{2}$ in $Y$. They are distinct points of $X$, so there are open sets $U_{1}\ni y_{1}$, $U_{2}\ni y_{2}$ of $X$ with $U_{1}\cap U_{2}=\varnothing$. Then $V_{i}=U_{i}\cap Y$ are open in $Y$, they contain $y_{i}$, and
$$
V_{1}\cap V_{2}=(U_{1}\cap Y)\cap(U_{2}\cap Y)=(U_{1}\cap U_{2})\cap Y=\varnothing .
$$
So $Y$ is Hausdorff.
:::
