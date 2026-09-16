---
schema: qual/card@1
id: P-AGH218GAMMALEFTEX
kind: problem
title: The global sections functor is left exact
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Exact Sequences
  - Global Sections
relations: []
review: draft
---

::: {.problem}
For any open subset $U \subseteq X$, show that the functor $\Gamma(U, \wait)$ from sheaves on $X$ to abelian groups is left exact.
That is, if
\[
0 \to \mcf' \to \mcf \to \mcf''
\]
is an exact sequence of sheaves, then
\[
0 \to \Gamma(U, \mcf') \to \Gamma(U, \mcf) \to \Gamma(U, \mcf'')
\]
is an exact sequence of groups.
:::

::: {.remark}
The functor $\Gamma(U, \wait)$ is not exact in general; Hartshorne II.1.21 supplies a counterexample on $\PP^1$.
:::
