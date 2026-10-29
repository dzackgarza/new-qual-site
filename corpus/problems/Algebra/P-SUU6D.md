---
schema: qual/card@1
id: P-SUU6D
kind: problem
title: Number of elements of order $4$ in $\Aut(\ZZ/20)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Cyclic Groups
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
How many elements in the automorphism group $\Aut(\ZZ/20\ZZ)$ have order 4?
:::

::: {.solution}

::: pf

::: pf-step

$\Aut(\ZZ/20\ZZ)\cong(\ZZ/20\ZZ)^\times\cong C_2\times C_4$.

::: pf-proof

An endomorphism of the cyclic group $\ZZ/20\ZZ$ is multiplication by some $u$, and it is an automorphism exactly when $u$ is a unit. By the Chinese remainder theorem, $(\ZZ/20\ZZ)^\times\cong(\ZZ/4\ZZ)^\times\times(\ZZ/5\ZZ)^\times\cong C_2\times C_4$.

:::

:::

::: pf-qed

An element $(a,b)\in C_2\times C_4$ has order $\operatorname{lcm}(\operatorname{ord}a,\operatorname{ord}b)$, which is $4$ exactly when $b$ has order $4$. There are $2$ choices of $a$ and $2$ elements of order $4$ in $C_4$, so there are $\boxed{4}$ such automorphisms: multiplication by $3,7,13,17$ modulo $20$.

:::

:::

:::
