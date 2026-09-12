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

::: problem
- Show that if $X\mapsvia{f} X^n$ is not surjective, then $f$ is nullhomotopic.
:::

::: {.solution}
<1>1. As written, the problem is not well-formed: the notation $X^n$ is undefined, and the original migrated source already contains exactly this text.
::: {.proof}
No definition of $X^n$ or relation between $X$ and the exponent $n$ appears in the card or its original migrated version, so the target space is not determined.
:::

<1>2. The standard intended theorem for spheres is true: if $f:S^n\to S^n$ is not surjective, then $f$ is null-homotopic.
::: {.proof}
Choose $p\in S^n\setminus f(S^n)$. Then $f$ factors through $S^n\setminus\{p\}\cong\mathbb R^n$, which is contractible. Hence the factorization, and therefore $f$, is null-homotopic.
:::
:::
