---
schema: qual/card@1
id: PR-UFVPY
kind: proposition
title: "How to find the minimal polynomial"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.proposition title="How to find the minimal polynomial"}
Let $m(x)$ denote the minimal polynomial $A$.

1. Find the characteristic polynomial $\chi(x)$; this annihilates $A$ by Cayley-Hamilton.
   Then $m(x) \divides \chi(x)$, so just test the finitely many products of irreducible factors.

2. Pick any $\vector v$ and compute $T\vector v, T^2\vector v, \cdots T^k\vector v$ until a linear dependence is introduced.
   Write this as $p(T) = 0$; then $\min_A(x) \divides p(x)$.
:::
