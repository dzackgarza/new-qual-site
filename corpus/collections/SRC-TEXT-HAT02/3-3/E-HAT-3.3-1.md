---
schema: qual/card@1
id: E-HAT-3.3-1
kind: problem
title: Nonorientable 1-manifolds without Hausdorff
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 1; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: two copies of $\RR$ glued along their punctured lines by a homeomorphism
    that is increasing on one component of the overlap and decreasing on the other, so no choice of
    direction on the two charts is consistent; the two origins are distinct but inseparable, which
    is what the failure of the Hausdorff condition buys.
---

::: {.problem}
Show that there exist nonorientable 1-dimensional manifolds if the Hausdorff condition is dropped from the definition of a manifold.
:::

::: {.solution}
Take two copies $\RR_+$ and $\RR_-$ of the real line. Identify their punctured lines by the homeomorphism
$$
h:\RR_+\setminus\{0\}\longrightarrow\RR_-\setminus\{0\},
\qquad
h(t)=
\begin{cases}
t,&t>0,\\
1/t,&t<0.
\end{cases}
$$
Let $X$ be the resulting quotient. Each copy of $\RR$ maps homeomorphically onto an open subset of $X$, so these two maps give 1-dimensional manifold charts. The images overlap on the two components of the punctured line. The chart transition is increasing on the positive component and decreasing on the negative component.

An orientation of either connected chart must choose one of its two directions throughout that chart. No choices for the two charts can make their transition preserve orientation on both components of the overlap. Thus $X$ is nonorientable.

The two origins are distinct but cannot be separated by disjoint open neighborhoods: every neighborhood of each contains the same points represented by sufficiently small positive $t$. Therefore $X$ is non-Hausdorff.
:::
