---
schema: qual/card@1
id: D-C3JIU
kind: definition
title: Principal Part and Residue at poles
classification:
  areas:
  - complex-analysis
  topics:
  - Principal Parts
  - Residues
  - Poles
  - Laurent Series
relations: []
review: draft
---

:::{.definition}
If $f$ has a pole of order $n$ at $z_0$, then there exist a holomorphic $G$ in a neighborhood of $z_0$ such that
\[
f(z) = {a_{-n} \over (z-z_0)^n } + \cdots + {a_{-1} \over z-z_0} + G(z) \da P(z) + G(z)
.\]

The term $P(z)$ is referred to as the *principal part of $f$ at $z_0$* consists of terms with negative degree, and the *residue* of $f$ at $z_0$ is the coefficient $a_{-1}$.
:::
