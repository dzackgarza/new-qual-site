---
schema: qual/card@1
id: E-FODKS
kind: problem
title: An irreducible generates any principal ideal containing it in a PID
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Ideals
  - Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used irreducibility and properness to show the two generators are associates.
---

::: {.exercise}
Let $R$ be a PID and let $I=(b)\subsetneq R$. If $a\in I$ is irreducible, prove that
$$
(a)=(b)=I.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #associates}
$a$ and $b$ are associates.

::: pf-proof
Since $a\in(b)$, there is $r\in R$ with $a=rb$. Because $a$ is irreducible, $r$ or $b$ is a unit. Since $(b)$ is proper, $b$ is not a unit, so $r$ is a unit.
:::

:::

::: pf-step
$(a)=(b)=I$.

::: pf-proof
Associates generate the same ideal, so step [](#associates){.pf-ref} gives $(a)=(b)$, and $(b)=I$ by hypothesis.
:::

:::

:::

:::
