---
schema: qual/card@1
id: P-UCLAB12W-01
kind: problem
title: Hausdorff distance on closed subsets of the unit interval
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Winter 2012. The source says all closed subsets of [0,1], which includes the empty set although its displayed Hausdorff formula is undefined there; this card adds the forced nonempty hypothesis.
---

::: {.problem}
Let $\Omega$ be the set of all nonempty closed subsets of $[0,1]$ and define
\[
\rho(A,B)=\max\left\{
\sup_{x\in A}\inf_{y\in B}|x-y|,
\sup_{y\in B}\inf_{x\in A}|x-y|
\right\}.
\]
Show that $(\Omega,\rho)$ is a metric space.
:::
