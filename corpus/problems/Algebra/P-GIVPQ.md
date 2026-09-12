---
schema: qual/card@1
id: P-GIVPQ
kind: problem
title: Semisimple algebras and the Artin–Wedderburn theorem
classification:
  areas:
  - algebra
  topics:
  - Semisimplicity
  - Algebras
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
What is a semisimple algebra?
State the structure theorem for semisimple algebras.
:::


::: {.solution}
A ring $A$ is **semisimple** if the left $A$-module ${}_AA$ is semisimple, i.e. a direct sum of simple submodules. Equivalently, every left $A$-module is semisimple; equivalently, every short exact sequence of left $A$-modules splits.

The Artin–Wedderburn theorem states that a ring is semisimple iff it is isomorphic to a finite product
\[
A\cong\prod_{i=1}^r M_{n_i}(D_i),
\]
where each $D_i$ is a division ring and $n_i\ge1$.

For a finite-dimensional algebra over a field $k$, the division rings $D_i$ are finite-dimensional over $k$. In particular, if $k$ is algebraically closed and $A$ is finite-dimensional over $k$, then each $D_i=k$, so
\[
A\cong\prod_{i=1}^r M_{n_i}(k).
\]

The integers $r,n_i$ and the division rings $D_i$ are determined uniquely up to permutation and isomorphism.
:::
