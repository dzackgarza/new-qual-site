---
schema: qual/card@1
id: E-NT2T3
kind: exercise
title: Singularities of $1\over e^z - 1$
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Residues
  - Singularities
relations: []
review: draft
---

:::{.exercise}
Classify the singularities and compute the residues at any poles of the following function:
\[
f(z) \da {1\over e^z - 1}
.\]

:::

:::{.solution}
Note $e^z = 1$ when $z=z_k\da 2\pi k$ for $k\in \ZZ$, and the claim is that these are all poles of order 1 of $f(z)$.
These are poles of some order: each $z_k$ is a zero of $1/f$ (since $e^{z_k} - 1 = 0$), so $f$ has a singularity at $z_k$; and the order of the pole is the smallest $n$ for which $\lim_{z\to z_k}(z-z_k)^n f(z)$ exists.
Start by computing the first:
\[
\lim_{z\to z_k}(z-z_k)f(z) = \lim_{z\to z_k} {z-z_k\over e^z - 1} \equalsbecause{\text{LH}} \lim_{z\to z_k} {1\over e^z} = e^{-z_k} = 1
.\]
:::
