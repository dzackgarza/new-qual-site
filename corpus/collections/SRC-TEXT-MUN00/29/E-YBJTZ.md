---
schema: qual/card@1
id: E-YBJTZ
kind: problem
title: The one-point compactification of R is the circle
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 6, printed p. 186; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.6, PDF p. 22. The circle is a compact Hausdorff
    space containing a dense copy of the line with one point removed, hence is its one-point
    compactification, unique up to homeomorphism by Exercise 29.5. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that the one-point compactification of $\RR$ is homeomorphic with the circle $S^1$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.6, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the map is theirs.

$\RR$ is locally compact and Hausdorff, and $S^{1}$ is a compact Hausdorff space containing the homeomorphic copy $S^{1}-\{(1,0)\}$ of $\RR$ (via $t\mapsto(\cos 2\pi t,\sin 2\pi t)$ restricted to $(-\tfrac12,\tfrac12)$, or by stereographic projection). A compact Hausdorff space containing a dense homeomorphic copy of $X$ whose complement is a single point is the one-point compactification of $X$ (it satisfies the defining property of §29), and one-point compactifications are unique up to homeomorphism fixing $X$ (Exercise 29.5). So $\RR^{+}\cong S^{1}$.
:::
