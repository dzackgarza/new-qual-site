---
schema: qual/card@1
id: E-2V2VL
kind: problem
title: Compact subspaces of metric spaces are closed and bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 4, printed p. 171, with Theorem
    26.3; the stored statement is the printed one, including the request for a
    counterexample.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.4, PDF p. 12. Finitely many balls about a point
    of Y cover Y; an infinite discrete metric space is closed and bounded and not compact.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that every compact subspace of a metric space is bounded in that metric and is closed.
Find a metric space in which not every closed bounded subspace is compact.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.4, PDF p. 12** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument and the counterexample are theirs.

Let $Y$ be a compact subspace of the metric space $X$; metric spaces are Hausdorff, so $Y$ is closed by Theorem 26.3.

*Bounded.* Fix $y\in Y$; the balls $B_{d}(y,n)$, $n\in\ZZ_{+}$, cover $Y$, so finitely many of them do, and the largest radius $N$ among them satisfies $Y\subset B_{d}(y,N)$.

*A closed bounded non-compact subspace.* Let $X$ be an infinite set with the discrete metric. It is closed in itself and bounded ($X=B_{d}(x,2)$ for any $x$), but the cover by the one-point sets has no finite subcover, so $X$ is not compact.
:::
