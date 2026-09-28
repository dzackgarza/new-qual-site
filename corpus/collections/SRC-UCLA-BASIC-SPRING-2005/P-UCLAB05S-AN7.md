---
schema: qual/card@1
id: P-UCLAB05S-AN7
kind: problem
title: Openness of invertibility and continuity of matrix inversion
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 7 of the official UCLA Basic Exam, May 2005 PDF. The source parenthetically calls the displayed metric the usual metric on $\mathbb R^{n^2}$; for complex matrices it is the Euclidean metric on $\mathbb C^{n^2}\cong\mathbb R^{2n^2}$.
---

::: {.problem}
Equip $M_n(\mathbb C)$ with the metric
\[
\operatorname{dist}(A,B)
=\left(\sum_{i,j}|A_{ij}-B_{ij}|^2\right)^{1/2}.
\]

(a) Suppose $F:\mathbb R\to M_n(\mathbb C)$ is continuous.
Show that
\[
\{x\in\mathbb R:F(x)\text{ is invertible}\}
\]
is open in the usual topology on $\mathbb R$.

(b) Show that on the set above, the map
\[
x\longmapsto F(x)^{-1}
\]
is continuous.
:::
