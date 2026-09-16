---
schema: qual/card@1
id: P-FKEN5
kind: problem
title: The sum of cubes of three consecutive positive integers is divisible by $9$
classification:
  areas:
  - prelim
  topics:
  - Induction
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Prove by induction that the sum of the cubes of 3 consecutive positive integers is divisible by 9.
:::

::: {.solution}
For $n\ge1$, let
\[
S_n=n^3+(n+1)^3+(n+2)^3.
\]
We prove by induction that $9\mid S_n$.

For $n=1$,
\[
S_1=1+8+27=36,
\]
which is divisible by $9$.

Assume $9\mid S_n$. Then
\[
S_{n+1}-S_n=(n+3)^3-n^3
=9(n^2+3n+3),
\]
which is divisible by $9$. Hence $S_{n+1}$ is divisible by $9$. By induction, the sum of the cubes of any three consecutive positive integers is divisible by $9$.
:::
