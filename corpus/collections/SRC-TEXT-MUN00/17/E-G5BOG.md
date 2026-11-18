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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 as one step. Re-checked the subspace topology (printed p. 88) and the distribution of the intersection over the two open sets. No statement change.
---

::: {.exercise}

Show that a subspace of a Hausdorff space is Hausdorff.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.12, PDF p. 8** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the proof is theirs, and Whitman's printed p. 165 is the same.

::: pf

::: pf-step

$Y$ is Hausdorff.

::: pf-proof

Let $X$ be Hausdorff and let $Y\subset X$ carry the subspace topology. Take distinct $y_{1},y_{2}\in Y$. They are distinct points of $X$, so there are open sets $U_{1}\ni y_{1}$ and $U_{2}\ni y_{2}$ of $X$ with $U_{1}\cap U_{2}=\varnothing$. Then $V_{i}\coloneqq U_{i}\cap Y$ is open in $Y$ and contains $y_{i}$, and
$$
V_{1}\cap V_{2}=(U_{1}\cap Y)\cap(U_{2}\cap Y)=(U_{1}\cap U_{2})\cap Y=\varnothing ,
$$
so $y_{1}$ and $y_{2}$ have disjoint neighbourhoods in $Y$.

:::

:::

:::
:::
