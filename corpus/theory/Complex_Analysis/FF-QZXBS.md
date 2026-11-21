---
schema: qual/card@1
id: FF-QZXBS
kind: fact
title: Types of isolated singularities by the behaviour of $\abs{f}$
slogan: 'Near an isolated singularity: bounded means removable, modulus tending to infinity means pole, and neither means essential.'
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

The three cases and the two growth conditions are those of [@Ahl73, ch. 4, §3.2, Zeros and Poles], where removable is Theorem 7 of §3.1 with $\lim(z-p)f(z)=0$, a pole is $\lim\abs{f}=\infty$ with the representation $(z-p)^{-h}f_h(z)$, and the remaining case is called essential; the bound criterion is the boundedness of $(z-p)f(z)$ near $p$.
:::
