---
schema: qual/card@1
id: E-NT2T3
kind: exercise
title: "Singularities of $1\\over e^z - 1$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Singularities of $1\over e^z - 1$"}
Classify the singularities and compute the residues at any poles of the following function:
\[
f(z) \da {1\over e^z - 1}
.\]

:::

:::{.solution}
Note $e^z = 1$ when $z=z_k\da 2\pi k$ for $k\in \ZZ$, and the claim is that these are all poles of order 1 of $f(z)$.
These are clearly poles of some order, since they are zeros of $1/f$, and the order will be the smallest $n$ for which $\lim_{z\to z_k}(z-z_k)^n f(z)$ exists.
Start by computing the first:
\[
\lim_{z\to z_k}(z-z_k)f(z) = \lim_{z\to z_k} {z-z_k\over e^z - 1} \equalsbecause{\text{LH}} \lim_{z\to z_k} {1\over e^z} = e^{-z_k} = 1
.\]
:::
