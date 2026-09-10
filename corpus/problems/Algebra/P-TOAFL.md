---
schema: qual/card@1
id: P-TOAFL
kind: problem
title: Classification of groups of order $10$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
---

::: problem
Classify all groups of order $10$.
:::

::: solution
Let $|G|=10=2\cdot5$.

Sylow's theorem gives
\[
n_5\mid2,
\qquad
n_5\equiv1\pmod5.
\]
Thus
\[
n_5=1.
\]
So the Sylow $5$-subgroup
\[
P\cong C_5
\]
is normal.

Let $Q\cong C_2$ be a Sylow $2$-subgroup. Since $P\cap Q=1$ and $|PQ|=10$, one has
\[
G\cong C_5\rtimes C_2.
\]
The action is determined by a homomorphism
\[
C_2\to\operatorname{Aut}(C_5)\cong C_4.
\]
There are exactly two possibilities for the image:

- the trivial action, giving
  \[
  C_5\times C_2\cong C_{10};
  \]
- the unique nontrivial element of order $2$ in $C_4$, namely inversion on $C_5$, giving the dihedral group of order $10$.

Therefore there are exactly two groups of order $10$ up to isomorphism:
\[
\boxed{C_{10}\quad\text{and}\quad D_{10}.}
\]
:::
