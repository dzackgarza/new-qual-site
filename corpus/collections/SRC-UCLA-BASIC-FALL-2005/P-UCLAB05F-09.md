---
schema: qual/card@1
id: P-UCLAB05F-09
kind: problem
title: Dimension of intersections of subspaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
Suppose $V_1$ and $V_2$ are subspaces of a finite-dimensional vector space $V$.

(a) Show that
\[
\dim(V_1\cap V_2)
=
\dim(V_1)+\dim(V_2)-\dim\bigl(\operatorname{span}(V_1,V_2)\bigr),
\]
where $\operatorname{span}(V_1,V_2)$ is the smallest subspace containing both $V_1$ and $V_2$.

(b) Let $n=\dim V$.
Use part (a) to show that, if $k<n$, an intersection of $k$ subspaces of dimension $n-1$ always has dimension at least $n-k$.

Suggestion: use induction on $k$.
:::
