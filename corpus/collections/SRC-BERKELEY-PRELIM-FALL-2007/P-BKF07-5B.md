---
schema: qual/card@1
id: P-BKF07-5B
kind: problem
title: Sum of residues of the reciprocal of a rapidly growing entire function
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
Let \(f\) be entire and let \(a_1,\ldots,a_n\) be all of its zeros in \(\mathbb C\). Suppose there exist \(R>0\) and \(\alpha>1\) such that
\[
|f(z)|\ge |z|^\alpha
\]
for every \(|z|\ge R\). Prove that
\[
\sum_{j=1}^n \operatorname{Res}_{z=a_j}\frac1{f(z)}=0.
\]
:::
