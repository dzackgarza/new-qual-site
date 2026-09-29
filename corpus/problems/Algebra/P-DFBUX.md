---
schema: qual/card@1
id: P-DFBUX
kind: problem
title: Dyadic rationals form a proper noncyclic subgroup of $(\QQ,+)$
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Subgroups
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
Give an interesting example of a subgroup of the additive group of the rationals.
:::

::: {.solution}
The subgroup of dyadic rationals is
\[
\ZZ[1/2]=\left\{\frac{m}{2^n}:m\in\ZZ,\ n\ge0\right\}\subseteq(\QQ,+).
\]

::: pf

::: pf-step

This is a subgroup of $(\QQ,+)$.

::: pf-proof

It contains $0$. If $x=a/2^m$ and $y=b/2^n$, then after replacing both denominators by $2^{\max(m,n)}$, the difference $x-y$ again has denominator a power of $2$. Hence the subgroup criterion applies.

:::

:::

::: pf-step

It is not cyclic.

::: pf-proof

Suppose $\ZZ[1/2]=\langle q\rangle$ for some nonzero rational $q=a/b$ in lowest terms. Every integer multiple of $q$ has reduced denominator dividing $b$. But $\ZZ[1/2]$ contains $1/2^n$ for arbitrarily large $n$, whose reduced denominators are unbounded. Contradiction.

:::

:::

::: pf-step

It is a proper subgroup of $\QQ$.

::: pf-proof

For example, $1/3\notin\ZZ[1/2]$, since no power of $2$ is divisible by $3$.

:::

:::

:::

Thus $\ZZ[1/2]$ is a proper, noncyclic subgroup of the additive rationals.
:::
