---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-G04-AXES
kind: problem
title: The fundamental group of three-dimensional space with its axes removed
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(Jan ’02) Find the fundamental group of the space $X$ consisting of $\mathbb R^3$ with the three coordinate axes removed.
:::

::: {.solution}
Let \(L\) be the union of the three coordinate axes. Since \(0\in L\), every point of \(X=\mathbb R^3\setminus L\) is nonzero. Radial projection gives a deformation retraction
\[
X\longrightarrow S^2\setminus(L\cap S^2).
\]
The six points of \(L\cap S^2\) are
\[
\pm e_1,\ \pm e_2,\ \pm e_3.
\]
Hence \(X\simeq S^2\setminus\{6\text{ points}\}\). Removing one of these points identifies the punctured sphere with \(\mathbb R^2\); removing the remaining five points gives \(\mathbb R^2\) minus five points, which deformation retracts onto a wedge of five circles. Therefore
\[
\boxed{\pi_1(X)\cong F_5}.
\]
:::
