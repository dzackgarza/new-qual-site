---
schema: qual/card@1
id: P-BKF85-9
kind: problem
title: Maximize Euclidean norm on a quadratic level set
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md; Flash drops the third coordinate from the displayed column vector, while the same sentence states $v\in\mathbb R^3$ and $v^t=(x,y,z)$, forcing $v=(x,y,z)^t$.
---

::: {.problem}
Let
\[
A=\frac16
\begin{pmatrix}
13&-5&-2\\
-5&13&-2\\
-2&-2&10
\end{pmatrix}
\]
and let
\[
v=\begin{pmatrix}x\\y\\z\end{pmatrix}\in\mathbb R^3.
\]
As $v$ ranges over the set satisfying
\[
v^TAv=1,
\]
show that $\|v\|$ is bounded and determine its least upper bound.
:::
