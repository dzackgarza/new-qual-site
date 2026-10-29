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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source reads "Every $a\in R$ for a finite ring is either a unit or a zero divisor." without declaring R; the statement declares R a finite commutative ring with identity, the setting of the solution.
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source does not restrict to commutative rings; the statement now keeps the source hypothesis "finite ring" (with identity), and the solution proves the two-sided inverse and the left zero divisor without commutativity.
---

::: {.problem}
Let $R$ be a finite ring with identity. Every $a\in R$ is either a unit or a zero divisor.
:::

::: {.solution}
Let $a\in R$.

::: pf

::: {.pf-step #s1}

If multiplication by $a$ is injective, then $a$ is a unit.

::: pf-proof

Consider
$$
\mu_a:R\to R,\qquad x\mapsto ax.
$$
Since $R$ is finite, an injective self-map is surjective. Thus $1\in\im(\mu_a)$, so there exists $b\in R$ with
$$
ab=1.
$$
Then $\mu_b$ is injective too: if $bx=0$, then $x=abx=0$. The same argument gives $c\in R$ with $bc=1$, and $a=a(bc)=(ab)c=c$, so $ba=1$. Hence $a$ is a two-sided unit.

:::

:::

::: pf-step

If $a$ is not a unit, then $a$ is a zero-divisor.

::: pf-proof

By contraposition of step [](#s1){.pf-ref}, if $a$ is not a unit then $\mu_a$ is not injective. Hence there exist $x\ne y$ with
$$
ax=ay.
$$
Then $0\ne x-y$ and
$$
a(x-y)=0,
$$
so $a$ is a left zero-divisor.

:::

:::

:::

:::
