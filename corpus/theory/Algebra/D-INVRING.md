---
schema: qual/card@1
id: D-INVRING
kind: definition
title: The invariant ring of a linear action
classification:
  areas:
  - algebra
  topics:
  - Invariant Theory
  - Group Actions
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group acting linearly on a finite-dimensional vector space $V$ over a field $k$, so that $G$ acts on the polynomial ring $k[V]$ by $k$-algebra automorphisms.
The \dfn{invariant ring} of the action is the subring
$$
k[V]^G \coloneqq \theset{f\in k[V]\st g\cdot f = f \text{ for all } g\in G}.
$$
It is a graded subring: a polynomial is fixed by $G$ exactly when each of its homogeneous components is, since $G$ acts by graded automorphisms, and $(k[V]^G)_d$ denotes its degree-$d$ part.
:::
