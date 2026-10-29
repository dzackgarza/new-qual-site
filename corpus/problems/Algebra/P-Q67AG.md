---
schema: qual/card@1
id: P-Q67AG
kind: problem
title: Every element of a finite ring is a unit or a zero divisor
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Invertibility
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Every $a\in R$ for a finite ring is either a unit or a zero divisor." The statement now introduces $R$ as a finite ring with identity and states the claim as a sentence; a zero divisor is an element $a$ with $ab=0$ for some $b\ne0$.'
---

::: {.problem}
Let $R$ be a finite ring with identity. Prove that every $a\in R$ is either a unit or a zero divisor, that is, an element with $ab=0$ for some $b\ne0$.
:::

::: {.solution}
For $a\in R$, let $L_a:R\to R$ be left multiplication, $L_a(y)=ay$; it is a homomorphism of additive groups.

::: pf

::: pf-step
If $L_a$ is injective, then $a$ is a unit.

::: pf-proof
An injective map of the finite set $R$ to itself is surjective, so $ax=1$ for some $x\in R$. If $xy=0$, then $y=axy=0$, so $L_x$ is injective, hence surjective, and $xz=1$ for some $z$. Then $a=a(xz)=(ax)z=z$, so $xa=1=ax$.
:::

:::

::: pf-step
If $L_a$ is not injective, then $a$ is a zero divisor.

::: pf-proof
Then $ay_1=ay_2$ for some $y_1\ne y_2$, and $b=y_1-y_2\ne0$ satisfies $ab=0$.
:::

:::

:::

:::
