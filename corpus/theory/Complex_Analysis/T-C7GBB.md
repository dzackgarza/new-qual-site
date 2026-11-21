---
schema: qual/card@1
id: T-C7GBB
kind: theorem
title: Gauss--Lucas theorem
slogan: 'Critical points of a polynomial cannot escape the convex hull of its zeros.'
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
relations: []
review: draft
---

::: {.theorem}
Let $p\in\CC[z]$ be a nonconstant polynomial.
Then every zero of $p'$ lies in the convex hull of the set of zeros of $p$.

This is [@Ahl73, ch. 2, §1.3, Theorem 1], Lucas's theorem.
The book states it in the half-plane form, that all zeros of $p'$ lie in any half-plane containing all zeros of $p$, and adds that the smallest convex polygon containing the zeros of $p$ also contains the zeros of $p'$; the statement above is that sharper formulation.
:::
