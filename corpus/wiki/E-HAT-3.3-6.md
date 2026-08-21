---
schema: qual/card@1
id: E-HAT-3.3-6
kind: exercise
title: "Connected sums of manifolds"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
solved: false
---

Given two disjoint connected $n$-manifolds $M_1$ and $M_2$, a connected $n$-manifold $M_1 \sharp M_2$, their connected sum, can be constructed by deleting the interiors of closed $n$-balls $B_1 \subset M_1$ and $B_2 \subset M_2$ and identifying the resulting boundary spheres $\partial B_1$ and $\partial B_2$ via some homeomorphism between them.
(Assume that each $B_i$ embeds nicely in a larger ball in $M_i$.)

(a) Show that if $M_1$ and $M_2$ are closed then there are isomorphisms $H_i(M_1 \sharp M_2; \mathbb{Z}) \approx H_i(M_1; \mathbb{Z}) \oplus H_i(M_2; \mathbb{Z})$ for $0 < i < n$, with one exception: If both $M_1$ and $M_2$ are nonorientable, then $H_{n-1}(M_1 \sharp M_2; \mathbb{Z})$ is obtained from $H_{n-1}(M_1; \mathbb{Z}) \oplus H_{n-1}(M_2; \mathbb{Z})$ by replacing one of the two $\mathbb{Z}_2$ summands by a $\mathbb{Z}$ summand.

(b) Show that $\chi(M_1 \sharp M_2) = \chi(M_1) + \chi(M_2) - \chi(S^n)$ if $M_1$ and $M_2$ are closed.
