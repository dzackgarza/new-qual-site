---
schema: qual/card@1
id: P-AMD-62OZUWBP
kind: problem
title: In a finite ring every element is a unit or a zero-divisor
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Invertibility
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
Every $a\in R$ for a finite ring is either a unit or a zero divisor.
:::


::: {.solution}
Let $R$ be a finite commutative ring with identity, and let $a\in R$.

<1>1. If multiplication by $a$ is injective, then $a$ is a unit.
::: {.proof}
Consider
\[
\mu_a:R\to R,\qquad x\mapsto ax.
\]
Since $R$ is finite, an injective self-map is surjective. Thus $1\in\operatorname{im}(\mu_a)$, so there exists $b\in R$ with
\[
ab=1.
\]
Hence $a$ is a unit.
:::

<1>2. If $a$ is not a unit, then $a$ is a zero-divisor.
::: {.proof}
By contraposition of <1>1, if $a$ is not a unit then $\mu_a$ is not injective. Hence there exist $x\ne y$ with
\[
ax=ay.
\]
Then $0\ne x-y$ and
\[
a(x-y)=0,
\]
so $a$ is a zero-divisor.
:::

Therefore every element of a finite commutative ring with identity is either a unit or a zero-divisor.
:::
