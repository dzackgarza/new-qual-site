---
schema: qual/card@1
id: P-6POHT
kind: problem
title: Consecutive Fibonacci numbers are relatively prime
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
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Recall that the Fibonacci numbers are defined by $F_0 = 1, F_1 = 1$, and then $$F_n = F_{n-1} + F_{n-2} \quad \text{for integers } n \geq 2.$$

Prove that any two successive Fibonacci numbers $F_n, F_{n+1}$ are relatively prime.
:::

::: solution
<1>1. For every $n\ge1$,
\[
\gcd(F_{n+1},F_n)=\gcd(F_n,F_{n-1}).
\]
::: {.proof}
Since $F_{n+1}=F_n+F_{n-1}$,
\[
\gcd(F_{n+1},F_n)
=\gcd(F_n+F_{n-1},F_n)
=\gcd(F_{n-1},F_n),
\]
using the Euclidean identity $\gcd(a+b,b)=\gcd(a,b)$.
:::

<1>2. Iterating <1>1 gives
\[
\gcd(F_{n+1},F_n)=\gcd(F_1,F_0)=1
\]
for every $n\ge0$.
::: {.proof}
For $n=0$, this is immediate from $F_0=F_1=1$. For $n\ge1$, repeated application of <1>1 lowers the indices until the pair $(F_1,F_0)$ is reached.
:::

<1>3. Hence every two successive Fibonacci numbers are relatively prime.
:::
