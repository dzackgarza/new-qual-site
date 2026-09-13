---
schema: qual/card@1
id: P-BKF07-7A
kind: problem
title: Factor a matrix satisfying P cubed equals P
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
---

::: {.problem}
Let \(P\in\mathbb R^{n\times n}\) satisfy \(P^3=P\). Let \(r=\operatorname{rank}P>0\). Show that there exist \(U,V\in\mathbb R^{n\times r}\) with
\[
V^TU=I_r
\]
such that
\[
P=USV^T,
\]
where \(S\) is an \(r\times r\) diagonal matrix whose diagonal entries are all \(\pm1\).
:::
