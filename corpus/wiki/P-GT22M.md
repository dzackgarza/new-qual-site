---
schema: qual/card@1
id: P-GT22M
kind: problem
title: If $K/F$ is cyclic and $E/F$ is normal then $E/F$ and $K/E$ are cyclic
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - cyclic-groups
  - normal-subgroups
relations: []
review: draft
solved: false
---

::: problem
We have $F \leq E \leq K$. Suppose that

- $K / F$ is cyclic, so $\Gal(K / F)$ is a cyclic group,
- $E / F$ is normal


We then want to show that

1.  $E/F$ is cyclic, i.e. $\Gal(E/F)$ is cyclic, and
2.  $K/E$ is cyclic, i.e. $\Gal(K/E)$ is cyclic.

By the fundamental theorem of Galois theory, $E/F$ is normal if and only if

a. $\Gal(K/E) \normal \Gal(K/F)$, and
b. $\Gal(E/F) \cong \Gal(K/F) / \Gal(K/E)$.

Since $\Gal(K/F)$ is a cyclic group and every subgroup of a cyclic group is itself cyclic, (a) lets us conclude that (1) holds.

Similarly, since $\Gal(K/F)$ is a cyclic group and every *quotient* of a cyclic group is cyclic, (b) lets us conclude (2).
:::
