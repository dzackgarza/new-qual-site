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
State Frobenius's Theorem classifying all finite-dimensional associative division algebras over the real numbers $\RR$, and state the generalized Hurwitz / Adams theorem for normed / alternative division algebras.
:::

::: {.solution}
Write $\HH$ for the quaternions and $\octonions$ for the octonions.
The three results below are stated with their standard names; the question asks only for statements.

::: pf

::: pf-step
(Frobenius) A finite-dimensional associative division algebra over $\RR$ is isomorphic to exactly one of $\boxed{\RR,\ \CC,\ \HH}$, of real dimensions $1,2,4$.

::: pf-proof
This is Frobenius' theorem.
:::

:::

::: pf-step
(Hurwitz, Zorn) A finite-dimensional real normed division algebra, equivalently a real composition algebra with positive-definite norm, is isomorphic to exactly one of $\boxed{\RR,\ \CC,\ \HH,\ \octonions}$, of dimensions $1,2,4,8$; the same four algebras are the finite-dimensional alternative division algebras over $\RR$.
The octonions are alternative and not associative.

::: pf-proof
The normed case is Hurwitz' theorem, and the alternative case is Zorn's theorem.
:::

:::

::: pf-step
(Bott--Milnor, Kervaire, Adams) If $D$ is a finite-dimensional real division algebra with no associativity assumption, then $\boxed{\dim_\RR D\in\{1,2,4,8\}}$.

::: pf-proof
Bott--Milnor and Kervaire proved the dimension restriction; Adams' Hopf invariant one theorem gives the same restriction through the parallelizable spheres $S^0,S^1,S^3,S^7$.
In dimensions $4$ and $8$ there are infinitely many non-isomorphic such algebras, so this result restricts the dimension and does not classify up to isomorphism.
:::

:::

:::

:::
