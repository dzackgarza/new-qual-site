---
schema: qual/card@1
id: FT-5NI77
kind: theorem
title: 'Riemann''s Removable Singularity Theorem'
classification:
  areas:
  - complex-analysis
  topics:
  - removable-singularities
  - singularities
relations: []
review: draft
---

::: {.theorem title="Riemann's Removable Singularity Theorem"}
Let $U\subset \CC$ be open, $a\in U$, and $f$ holomorphic on $U\setminus\theset{a}$.
Then TFAE

- $f$ extends holomorphically to all of $U$

- $f$ extends continuously to all of $U$

- There exists a neighborhood of $a$ on which $f$ is bounded.

- $\lim_{z\to a} (z-a)f(z) = 0$.
:::
