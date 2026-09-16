---
schema: qual/card@1
id: FF-QZXBS
kind: fact
title: Types of isolated singularities by the behaviour of $\abs{f}$
prompts:
- How are removable singularities, poles and essential singularities told apart by the behaviour of $\abs{f}$?
classification:
  areas:
  - complex-analysis
  topics:
  - Singularities
  - Poles
  - Essential Singularities
  - Removable Singularities
relations: []
review: draft
---

::: {.fact}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $\theset{z : 0<\abs{z-p}<r}$, so that $p$ is an [[D-IWIA5|isolated singularity]] of $f$.

- $p$ is a [[D-BQLJV|removable singularity]] if and only if $\abs{f}$ is bounded on some punctured disc about $p$.

- $p$ is a [[D-AUD6K|pole]] if and only if $\lim_{z\to p} \abs{f(z)} = \infty$.

- $p$ is an [[D-VKP6N|essential singularity]] if and only if neither of these holds.
:::
