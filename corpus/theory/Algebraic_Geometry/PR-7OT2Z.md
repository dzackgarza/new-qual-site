---
schema: qual/card@1
id: PR-7OT2Z
kind: proposition
title: The ideal-variety correspondence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Nullstellensatz
  - Prime Ideals
relations:
- kind: uses
  target: T-JRTS2
review: draft
prompts:
- Which ideals correspond to closed subsets of $\AA^n$?
- Which ideals correspond to irreducible closed subsets?
- What is the coordinate ring of a closed subset, and when is it a domain?
---

::: {.proposition}
Over an algebraically closed field $k$, the maps $V$ and $I$ are mutually inverse, order-reversing bijections between the radical ideals of $k[x_1,\ldots,x_n]$ and the Zariski-closed subsets of $\AA^n$.
Under that bijection:

| Ideal $J$ | Closed set $V(J)$ |
| --- | --- |
| radical | closed |
| prime | irreducible |
| maximal | a point |
| $(1)$ | $\emptyset$ |
| $(0)$ | $\AA^n$ |
:::

::: {.remark}
The correspondence is what turns a geometric question into a computation in a ring, so the useful direction on an exam is usually right to left: $V(J)$ is irreducible exactly when $J$ is prime, which is a question about $k[x_1,\ldots,x_n]/J$ being a domain.

For a closed $X \subseteq \AA^n$ the coordinate ring is $k[X] \da k[x_1,\ldots,x_n]/I(X)$, the polynomial functions restricted to $X$, and the same dictionary reappears inside it: closed subsets of $X$ correspond to radical ideals of $k[X]$, and $X$ is irreducible exactly when $k[X]$ is a domain.
:::
