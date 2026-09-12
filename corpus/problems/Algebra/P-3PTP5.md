---
schema: qual/card@1
id: P-3PTP5
kind: problem
title: A commutative unital ring is a field iff its only ideals are $\{0\}$ and $R$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Ideals
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

::: problem
Prove that a commutative ring with unit is a field if and only if its only ideals are {0} and the whole ring

:::


::: {.solution}
<1>1. If $R$ is a field, then its only ideals are $\{0\}$ and $R$.
::: {.proof}
Let $I\subseteq R$ be a nonzero ideal and choose $0\ne a\in I$. Since $R$ is a field, $a^{-1}\in R$, so
\[
1=a^{-1}a\in I.
\]
Hence $I=R$. Thus the only ideals are $0$ and $R$.
:::

<1>2. Conversely, suppose the only ideals of the commutative unital ring $R$ are $\{0\}$ and $R$. Then every nonzero element is a unit.
::: {.proof}
Take $0\ne a\in R$. The principal ideal $(a)$ is nonzero, so by hypothesis
\[
(a)=R.
\]
Hence $1\in(a)$, so there exists $b\in R$ with
\[
ab=1.
\]
Thus $a$ is a unit.
:::

<1>3. Therefore $R$ is a field.
::: {.proof}
By <1>2, every nonzero element of $R$ is invertible. Since $R$ is commutative with $1$, this is exactly the definition of a field.
:::
:::
