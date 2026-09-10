---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3A-HW3
kind: problem
title: Classification of compact surfaces without boundary (warm-up)
classification:
  areas:
  - topology
  topics:
  - Classification
  - Surfaces
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
Briefly describe the classification of compact surfaces without boundary.
:::

::: {.solution}
Every connected compact surface without boundary is homeomorphic to exactly one surface in the following list:

1. the sphere \(S^2\) (the orientable genus-\(0\) surface);
2. for each \(g\ge1\), the orientable surface
\[
\Sigma_g=T^2\#\cdots\#T^2
\]
with \(g\) torus summands;
3. for each \(k\ge1\), the nonorientable surface
\[
N_k=\mathbb{RP}^2\#\cdots\#\mathbb{RP}^2
\]
with \(k\) projective-plane summands.

The orientable and nonorientable families do not overlap. Within each family the genus is a homeomorphism invariant; for example
\[
\chi(\Sigma_g)=2-2g,
\qquad
\chi(N_k)=2-k.
\]
A compact surface without boundary that is not connected is a finite disjoint union of such connected surfaces.
:::
