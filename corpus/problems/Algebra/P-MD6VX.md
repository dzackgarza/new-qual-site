---
schema: qual/card@1
id: P-MD6VX
kind: problem
title: Why the character table is square
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Why is the character table a square?
:::

::: {.solution}
Let $G$ be a finite group. Its character table has one row for each irreducible complex character and one column for each conjugacy class.

::: pf

::: {.pf-step #dim}
The complex vector space of class functions on $G$ has dimension equal to the number of conjugacy classes of $G$.

::: pf-proof
A class function is determined by its values on the conjugacy classes, and these values can be chosen independently, so the indicator functions of the conjugacy classes form a basis.
:::

:::

::: {.pf-step #basis}
The irreducible complex characters form a basis of the space of class functions.

::: pf-proof
They form an orthonormal basis of that space for the standard inner product of class functions.
:::

:::

::: pf-step
The character table is square.

::: pf-proof
By steps [](#dim){.pf-ref} and [](#basis){.pf-ref}, the number of irreducible complex characters equals the number of conjugacy classes, so the table has as many rows as columns.
:::

:::

:::

:::
