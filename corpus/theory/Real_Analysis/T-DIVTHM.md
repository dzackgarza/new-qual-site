---
schema: qual/card@1
id: T-DIVTHM
kind: theorem
title: The divergence theorem
slogan: 'flux across a closed surface equals the integral of the divergence over the solid it bounds'
classification:
  areas:
  - real-analysis
  topics:
  - Divergence Theorem
  - Vector Calculus
relations: []
review: draft
---

::: {.theorem}
Let $V\subseteq\RR^n$ be a compact region whose boundary $\bd V$ is a finite union of smooth pieces, let $\nu$ be the outward unit normal of $\bd V$, and let $F$ be a $C^1$ vector field on an open set containing $V$.
Then
$$
\int_{\bd V} F\cdot\nu\,dS = \int_V \nabla\cdot F\,dV .
$$
:::
