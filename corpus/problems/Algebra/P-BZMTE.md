---
schema: qual/card@1
id: P-BZMTE
kind: problem
title: $\varphi(n)$ is even for $n>2$
classification:
  areas:
  - algebra
  topics:
  - Number Theory
  - Roots of Unity
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
Prove that $\varphi(n)$ is even for every integer $n>2$.
:::

::: {.solution}
Write $n=\prod_{i=1}^r p_i^{a_i}$ with distinct primes $p_i$ and $a_i\ge1$.

::: pf

::: {.pf-step #formula}

$\varphi(n)=\prod_{i=1}^r p_i^{a_i-1}(p_i-1)$.

::: pf-proof

$\varphi$ is multiplicative on coprime arguments by the Chinese remainder theorem, and $\varphi(p^a)=p^a-p^{a-1}$ because exactly the $p^{a-1}$ multiples of $p$ in $\{1,\ldots,p^a\}$ are not coprime to $p^a$.

:::

:::

::: pf-step

$\varphi(n)$ is even.

::: pf-proof

If some $p_i$ is odd, then $p_i-1$ is an even factor in step [](#formula){.pf-ref}. Otherwise $n=2^a$, and $n>2$ gives $a\ge2$, so $\varphi(n)=2^{a-1}$ is even.

:::

:::

:::

:::
