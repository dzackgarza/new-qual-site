---
schema: qual/card@1
id: D-DQPGU
kind: definition
title: Symplectic Group
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Bilinear Forms
relations: []
review: draft
---

:::{.definition title="Symplectic Group"}
\[
\mathrm{Sp}_{2n}(\CC) \da \ts{ A \in \GL_{2n}(\CC) \st A^tJA = J } &&
J \da
\begin{bmatrix}
0 & 1_n
\\
-1_n & 0
\end{bmatrix}
.\]

The block $-1_n$ is essential: $J$ must be **antisymmetric**.
Taking $J$ symmetric, with $+1_n$ in the lower left, defines an orthogonal group for a split quadratic form instead.

:::
