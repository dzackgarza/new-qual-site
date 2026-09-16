---
schema: qual/card@1
id: P-YFDNV
kind: problem
title: Real division algebras
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Classification
  - Semisimplicity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
State Frobenius's Theorem classifying all finite-dimensional associative division algebras over the real numbers $\mathbb{R}$, and state the generalized Hurwitz / Adams theorem for normed / alternative division algebras.
:::

::: {.solution}
There are three related statements that should be distinguished.

**Frobenius' theorem.** The finite-dimensional associative division algebras over $\mathbb R$ are exactly
\[
\boxed{\mathbb R,\ \mathbb C,\ \mathbb H}.
\]
Their real dimensions are $1,2,4$.

**Hurwitz' theorem.** The finite-dimensional real normed division algebras, equivalently positive-definite real composition division algebras, are exactly
\[
\boxed{\mathbb R,\ \mathbb C,\ \mathbb H,\ \mathbb O},
\]
of dimensions $1,2,4,8$. The octonions $\mathbb O$ are nonassociative but alternative.

For more general finite-dimensional real division algebras, one no longer has uniqueness up to isomorphism in dimensions $4$ and $8$. What survives is the dimension restriction: the existence of a finite-dimensional real division algebra forces
\[
\boxed{\dim_\mathbb R D\in\{1,2,4,8\}},
\]
a consequence of the Hopf-invariant-one/division-algebra results of Bott--Milnor--Kervaire and Adams.

Thus Frobenius is an isomorphism classification in the associative case; Hurwitz is an isomorphism classification in the normed composition case; and the general topological theorem is a dimension restriction, not an isomorphism classification.
:::
