---
schema: qual/card@1
id: P-SLWIE
kind: problem
title: $\pi^2/\sin^2(\pi z)=\sum_{n\in\mathbb{Z}}(z-n)^{-2}$
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Poles
  - Principal Parts
  - Identity Theorem
  - Trigonometry
relations: []
review: draft
---

Define
\[
f(z) &= {\pi^2 \over \sin^2 \qty{\pi z} } \\
g(z) &= \sum_{n\in \ZZ} {1\over (z-n)^2}
.\]

a. Show that $f$ and $g$ have the same singularities in $\CC$.
b. Show that $f$ and $g$ have the same singular parts at each of their singularities.
c. Show that $f, g$ each have period one and approach zero uniformly on $0\leq x \leq 1$ as $\abs{y}\to \infty$.
d. Conclude that $f = g$.

:::{.solution}
:::{.concept}
Idea: show their $f-g$ is analytic by taking away all of the negative powers, and bounded by (c).
:::

:::

