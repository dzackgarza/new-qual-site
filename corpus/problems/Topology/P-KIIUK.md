---
schema: qual/card@1
id: P-KIIUK
kind: problem
title: Non-surjective maps $X\to X^n$ are nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
relations: []
review: draft
---

::: {.problem}
- Show that if $X\mapsvia{f} X^n$ is not surjective, then $f$ is nullhomotopic.
:::

::: {.solution}

::: pf

::: pf-step

The notation $X^n$ is not defined in the statement, so the target space is not determined.

:::

::: pf-step

For spheres, if $f:S^n\to S^n$ is not surjective, then $f$ is null-homotopic.

::: pf-proof

Choose $p\in S^n\setminus f(S^n)$. Then $f$ factors through $S^n\setminus\{p\}\cong\mathbb R^n$, which is contractible. Hence the factorization, and therefore $f$, is null-homotopic.

:::

:::

:::

:::
