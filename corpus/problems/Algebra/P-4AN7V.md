---
schema: qual/card@1
id: P-4AN7V
kind: problem
title: $\mathbb Z/n\mathbb Z$ as a direct sum of fields
classification:
  areas:
  - algebra
  topics:
  - Chinese Remainder Theorem
  - Fields
  - Rings
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

::: {.problem}
Determine for which integers the ring $\mathbb{Z}/n\mathbb{Z}$ is a direct sum of fields.
Carefully prove your answer.
:::


::: {.solution}
Assume $n\ge2$.

<1>1. If $n$ is squarefree, then $\ZZ/n\ZZ$ is a finite direct product of fields.
::: {.proof}
Write
\[
n=p_1p_2\cdots p_r
\]
with distinct primes $p_i$. The ideals $(p_i)$ are pairwise comaximal, so the Chinese remainder theorem gives
\[
\ZZ/n\ZZ
\cong \prod_{i=1}^r \ZZ/p_i\ZZ.
\]
Each factor is the field $\FF_{p_i}$. Since the product is finite, it is also the direct sum of these rings as additive groups.
:::

<1>2. If $n$ is not squarefree, then $\ZZ/n\ZZ$ is not a direct product of fields.
::: {.proof}
Suppose $p^2\mid n$ for some prime $p$. The class
\[
a=[n/p]\in\ZZ/n\ZZ
\]
is nonzero, because $n\nmid n/p$, but
\[
a^2=[n^2/p^2]=0
\]
in $\ZZ/n\ZZ$, because $n\mid n^2/p^2$ when $p^2\mid n$. Thus $\ZZ/n\ZZ$ contains a nonzero nilpotent.

A finite direct product of fields is reduced: if $(x_i)^m=0$, then each $x_i^m=0$ in a field, hence each $x_i=0$. Therefore a ring with a nonzero nilpotent cannot be a product of fields.
:::

<1>3. Therefore
\[
\ZZ/n\ZZ	ext{ is a direct product of fields}
\quad\Longleftrightarrow\quad
n	ext{ is squarefree}.
\]
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
