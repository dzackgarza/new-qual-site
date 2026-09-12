---
schema: qual/card@1
id: P-DFBUX
kind: problem
title: An interesting subgroup of $(\QQ,+)$
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

::: problem
Give an interesting example of a subgroup of the additive group of the rationals.
:::


::: {.solution}
A useful example is the subgroup of dyadic rationals
\[
\ZZ[1/2]=\left\{\frac{m}{2^n}:m\in\ZZ,\ n\ge0\right\}\subseteq(\QQ,+).
\]

<1>1. This is a subgroup of $(\QQ,+)$.
::: {.proof}
It contains $0$. If $x=a/2^m$ and $y=b/2^n$, then after replacing both denominators by $2^{\max(m,n)}$, the difference $x-y$ again has denominator a power of $2$. Hence the subgroup criterion applies.
:::

<1>2. It is not cyclic.
::: {.proof}
Suppose $\ZZ[1/2]=\langle q\rangle$ for some nonzero rational $q=a/b$ in lowest terms. Every integer multiple of $q$ has reduced denominator dividing $b$. But $\ZZ[1/2]$ contains $1/2^n$ for arbitrarily large $n$, whose reduced denominators are unbounded. Contradiction.
:::

<1>3. It is a proper subgroup of $\QQ$.
::: {.proof}
For example, $1/3\notin\ZZ[1/2]$, since no power of $2$ is divisible by $3$.
:::

Thus $\ZZ[1/2]$ is a proper, noncyclic subgroup of the additive rationals.
:::
