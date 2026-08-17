---
schema: qual/card@1
id: P-KSSA7
kind: problem
title: "The Galois group of $x^n - 2$ over $\\QQ$"
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - splitting-fields
  - roots-of-unity
relations: []
review: draft
solved: false
---

::: problem
- The splitting field of $x^n-2$ over $\QQ$ is $\QQ(2^{1/n}, \zeta_n)$.
  Show that $\Gal$ embeds into the affine group $\ZZ/n\ZZ \semidirect \qty{\ZZ/n\ZZ}\units$, by sending $\sigma$ to the pair $(a,b)$ with $\sigma(2^{1/n}) = \zeta_n^a 2^{1/n}$ and $\sigma(\zeta_n) = \zeta_n^b$.

- Deduce that the Galois group is dihedral of order $2n$ exactly when $\phi(n) = 2$, that is for $n = 3, 4, 6$.
  It is **not** $D_n$ in general: the order is at most $n\phi(n)$, which exceeds $2n$ as soon as $\phi(n) > 2$.
:::
