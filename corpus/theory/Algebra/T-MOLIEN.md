---
schema: qual/card@1
id: T-MOLIEN
kind: theorem
title: Molien's formula
slogan: 'the Hilbert series of an invariant ring from the conjugacy classes of the group'
classification:
  areas:
  - algebra
  topics:
  - Invariant Theory
  - Hilbert Series
relations: []
review: draft
---

::: {.theorem}
Let $G\subseteq\GL(V)$ be a finite subgroup of the general linear group of a finite-dimensional complex vector space $V$, acting on $\CC[V]$, and let $(\CC[V]^G)_d$ be the invariants homogeneous of degree $d$.
Then the Hilbert series of the invariant ring is
$$
\sum_{d\geq0}\dim_\CC(\CC[V]^G)_d\,t^d = \frac{1}{\size G}\sum_{g\in G}\frac{1}{\det(1-tg)} .
$$

This is Molien's theorem: Cox--Little--O'Shea, *Ideals, Varieties, and Algorithms*, Chapter 7, §3 names it and refers for its proof to Benson--Grove, *Finite Reflection Groups*, Chapter 7, and Sturmfels, *Algorithms in Invariant Theory*, Chapter 2.
:::
