---
schema: qual/card@1
id: P-RI3ZA
kind: problem
title: Normality of field extensions is not transitive
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Counterexamples
relations: []
review: draft
---

::: problem
False: take $K \leq L \leq M$ as $\QQ \leq \QQ(\sqrt[3]2) \leq \QQ(\sqrt[3]2, \zeta_3)$.
Then $M$ is the splitting field of $x_3-2$, and in characteristic zero is thus Galois.
But $L$ is not the splitting field of any irreducible polynomial in $\QQ[x]$, so it is *not* Galois.
:::
