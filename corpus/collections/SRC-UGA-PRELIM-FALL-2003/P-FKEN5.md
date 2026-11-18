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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the base case
    S_1 = 36 = 9 times 4, the telescoping difference S_{n+1} - S_n = (n+3)^3 - n^3 with
    the expansion giving 9(n^2 + 3n + 3), and the induction step adding two multiples of
    9. The shared terms in the difference, and the expansion itself, are now written out;
    the prose stated the difference only in its factored form. The collection's provenance
    is the examination paper alone, so no retained solution set covers the exercise and the
    argument is the card's own.
---

::: {.problem}
Prove by induction that the sum of the cubes of 3 consecutive positive integers is divisible by 9.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Write $S_n\coloneqq n^3+(n+1)^3+(n+2)^3$ for $n\ge1$.

::: pf

::: {.pf-step #base}
$S_1=36=9\cdot4$.

::: pf-proof
$S_1=1^3+2^3+3^3=1+8+27=36$.
:::

:::

::: {.pf-step #step}
For every $n\ge1$, $S_{n+1}-S_n=(n+3)^3-n^3=9\left(n^2+3n+3\right)$.

::: pf-proof
$S_{n+1}$ and $S_n$ share the terms $(n+1)^3$ and $(n+2)^3$, so the difference is $(n+3)^3-n^3$. Expanding, $(n+3)^3=n^3+9n^2+27n+27$, hence the difference is $9n^2+27n+27=9\left(n^2+3n+3\right)$.
:::

:::

::: {.pf-step}
$9\mid S_n$ for every $n\ge1$.

::: pf-proof
Induction on $n$. The case $n=1$ is step [](#base){.pf-ref}. If $9\mid S_n$, then $S_{n+1}=S_n+9\left(n^2+3n+3\right)$ by step [](#step){.pf-ref} is a sum of two multiples of $9$, hence a multiple of $9$. So $9\mid S_n$ for all $n\ge1$, which is the assertion: the sum of the cubes of any three consecutive positive integers $n,n+1,n+2$ is divisible by $9$.
:::

:::

:::
:::
