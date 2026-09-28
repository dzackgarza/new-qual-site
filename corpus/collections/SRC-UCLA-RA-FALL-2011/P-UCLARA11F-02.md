---
schema: qual/card@1
id: P-UCLARA11F-02
kind: problem
title: Fourier transform of sphere measure and an L2 functional
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $d\sigma$ denote surface measure on the unit sphere $S^2\subset\mathbb R^3$, so that $\int_{S^2}d\sigma=4\pi$.

(a) For $\xi\in\mathbb R^3$, compute
\[
\int_{S^2} e^{i x\cdot \xi}\,d\sigma(x).
\]

(b) Using this, or otherwise, show that
\[
f\longmapsto \int_{S^2}\int_{S^2} f(x+y)\,d\sigma(x)\,d\sigma(y)
\]
extends uniquely from $C_c^\infty(\mathbb R^3)$ to a bounded linear functional on $L^2(\mathbb R^3)$.
:::
