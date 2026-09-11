---
schema: qual/card@1
id: P-AGH355COMPINT
kind: problem
title: Cohomology of a complete intersection in projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Complete Intersections
  - Projective Space
  - Arithmetic Genus
relations: []
review: draft
---

::: problem
Let $k$ be a field, let $X=\PP_k^r$, and let $Y$ be a closed subscheme of dimension $q \geq 1$, which is a complete intersection (II, Ex. 8.4). Then:

a. for all $n \in \ZZ$, the natural map
\[
H^0(X, \mco_X(n)) \to H^0(Y, \mco_Y(n))
\]
is surjective. This gives a generalization and another proof of (II, Ex. 8.4c), where we assumed $Y$ was normal.

b. $Y$ is connected;

c. $H^i(Y, \mco_Y(n))=0$ for $0<i<q$ and all $n \in \ZZ$;

d. $p_a(Y)=\dim_k H^q(Y, \mco_Y)$.

Hint: Use exact sequences and induction on the codimension, starting from the case $Y=X$ which is (5.1).
:::
