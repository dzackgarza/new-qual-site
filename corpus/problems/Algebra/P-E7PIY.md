---
schema: qual/card@1
id: P-E7PIY
kind: problem
title: Fundamental theorem of symmetric polynomials
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
State the fundamental theorem of symmetric polynomials.
:::

::: {.solution}
Let $R$ be a commutative ring and let $e_1,\ldots,e_n$ denote the elementary symmetric polynomials in $R[x_1,\ldots,x_n]$.

::: pf

::: {.pf-step #statement}
Every symmetric polynomial $f\in R[x_1,\ldots,x_n]^{S_n}$ can be written uniquely as $f=F(e_1,\ldots,e_n)$ for some polynomial $F\in R[t_1,\ldots,t_n]$.

::: pf-proof
This is the fundamental theorem of symmetric polynomials.
:::

:::

::: pf-step
Equivalently, $R[x_1,\ldots,x_n]^{S_n}=R[e_1,\ldots,e_n]$, and $e_1,\ldots,e_n$ are algebraically independent over $R$.

::: pf-proof
Existence in step [](#statement){.pf-ref} is the equality of rings, and uniqueness is the statement that the evaluation map $R[t_1,\ldots,t_n]\to R[x_1,\ldots,x_n]$, $t_i\mapsto e_i$, is injective, which is algebraic independence.
:::

:::

:::

:::
