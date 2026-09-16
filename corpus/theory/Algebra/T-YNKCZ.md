---
schema: qual/card@1
id: T-YNKCZ
kind: theorem
title: Recognizing internal direct products of finitely many subgroups
classification:
  areas:
  - algebra
  topics:
  - Direct Products
  - Normal Subgroups
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a group with subgroups $H_1,\ldots,H_n$ such that

- $H_i \normal G$ for all $i$,

- $G = H_1 \cdots H_n$, and

- for each $k$, $H_k \intersect \left(H_1 \cdots H_{k-1}H_{k+1} \cdots H_n\right) = \theset{e}$.

Then the map $\prod_{i=1}^n H_i\to G$, $(h_1,\ldots,h_n)\mapsto h_1\cdots h_n$, is an isomorphism, so $G \cong \prod_{i=1}^n H_i$.
:::
