---
schema: qual/card@1
id: P-PDRT9
kind: problem
title: Intermediate fields of a Galois extension with group $\ZZ_{42}$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
  - Field Extensions
relations: []
review: draft
---

::: problem
Let $L/K$ be a finite Galois extension with
\[
\operatorname{Gal}(L/K)\cong C_{42}.
\]
List the proper nontrivial intermediate fields and their degrees over $K$.
:::

::: {.solution}
By the Galois correspondence, intermediate fields correspond bijectively and inclusion-reversingly to subgroups of $C_{42}$.

A cyclic group has exactly one subgroup of order $d$ for every divisor $d\mid42$. The proper nontrivial subgroup orders are
\[
2,3,6,7,14,21.
\]
If a subgroup has order $d$, its fixed field $E$ satisfies
\[
[E:K]=[C_{42}:H]=\frac{42}{d}.
\]
Therefore there is exactly one intermediate field of each degree
\[
21,14,7,6,3,2.
\]
Equivalently, for every proper nontrivial divisor $e$ of $42$, there is a unique intermediate extension of degree $e$ over $K$.
:::
