---
schema: qual/card@1
id: P-KIAFG
kind: problem
title: Dedekind domains and class numbers
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Ideals
  - Commutative Algebra
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
What is a Dedekind domain, what is its ideal class group, and what is the class number?
:::

::: {.solution}

::: pf

::: pf-step
A Dedekind domain is an integral domain $R$ that is Noetherian, integrally closed in its fraction field, and in which every nonzero prime ideal is maximal.

::: pf-proof
Equivalently, every nonzero proper ideal of $R$ factors uniquely as a product of nonzero prime ideals.
:::

:::

::: pf-step
The ideal class group is $\Cl(R)=I(R)/P(R)$, where $K=\Frac(R)$, $I(R)$ is the group of nonzero fractional ideals of $R$ under multiplication, and $P(R)=\{aR : a\in K^\times\}$ is its subgroup of principal fractional ideals.

::: pf-proof
In a Dedekind domain every nonzero fractional ideal is invertible, so $I(R)$ is a group. The class group measures the failure of ideals to be principal: $\Cl(R)=0$ if and only if $R$ is a PID.
:::

:::

::: pf-step
When $\Cl(R)$ is finite, the class number is $h(R)=\abs{\Cl(R)}$.

::: pf-proof
For the ring of integers $\OO_K$ of a number field $K$, the class group is finite, so the class number is defined. Class number $1$ means that $\OO_K$ is a PID, hence a UFD.
:::

:::

:::

:::
