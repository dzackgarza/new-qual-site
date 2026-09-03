---
schema: qual/card@1
id: T-NBARV
kind: theorem
title: Classification of Surfaces
classification:
  areas:
  - topology
  topics:
  - Classification
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a compact connected surface and let $b$ be the number of boundary components.
Then exactly one of the following holds:

- $X$ is orientable and is homeomorphic to the connected sum of $g\geq 0$ tori with the interiors of $b$ disjoint discs removed;

- $X$ is nonorientable and is homeomorphic to the connected sum of $k\geq 1$ copies of $\RP^2$ with the interiors of $b$ disjoint discs removed.

The Euler characteristic is
\[
\chi(X)=
\begin{cases}
2-2g-b & \text{if $X$ is orientable}, \\
2-k-b & \text{if $X$ is nonorientable}.
\end{cases}
\]

Thus compact connected surfaces are classified up to homeomorphism by orientability, the number $b$ of boundary components, and $\chi(X)$; equivalently, by $(g,b)$ in the orientable case and $(k,b)$ in the nonorientable case.
For closed surfaces ($b=0$), orientability and Euler characteristic alone determine the homeomorphism type.
:::
