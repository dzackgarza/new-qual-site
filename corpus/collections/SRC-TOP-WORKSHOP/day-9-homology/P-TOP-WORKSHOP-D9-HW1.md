---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-HW1
kind: problem
title: Homology of $S^n$ for all $n\ge 0$
classification:
  areas:
  - topology
  topics:
  - Homology
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
Compute the homology groups of $S^n$ for all $n\ge 0$.
:::

::: {.solution}
For \(n\ge1\), the sphere \(S^n\) has a CW structure with one \(0\)-cell and one \(n\)-cell, with no cells in intermediate dimensions. Its cellular chain complex therefore gives
\[
H_k(S^n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z,&k=n,\\
0,&\text{otherwise}.
\end{cases}
\]
Equivalently,
\[
\widetilde H_k(S^n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=n,\\
0,&k\ne n.
\end{cases}
\]

For \(n=0\), \(S^0\) consists of two points, so
\[
H_0(S^0;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z,
\qquad
H_k(S^0;\mathbb Z)=0\quad(k>0),
\]
and \(\widetilde H_0(S^0)\cong\mathbb Z\).
:::
