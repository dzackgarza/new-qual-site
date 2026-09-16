---
schema: qual/card@1
id: P-BKF05-8B
kind: problem
title: A semicircle integral of exponential iz over z vanishes
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
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
---

::: {.problem}
For \(R>0\), let
\[
\Gamma_R=\{z\in\mathbb C:|z|=R,\ \operatorname{Im}z\ge0\}
\]
be the upper semicircle, oriented counterclockwise.
Prove that
\[
\lim_{R\to\infty}\int_{\Gamma_R}\frac{e^{iz}}{z}\,dz=0.
\]
:::
