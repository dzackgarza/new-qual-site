---
schema: qual/card@1
id: P-HGRO2
kind: problem
title: Number of abelian groups of orders $35$ and $27$
classification:
  areas: [algebra]
  topics: [Abelian Groups]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
How many abelian groups of order $35$ are there, up to isomorphism?
How many are there of order $27$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Order $35 = 5 \cdot 7$: there is exactly $1$ abelian group, namely $\ZZ/35$.

::: pf-proof

by the fundamental theorem of finite abelian groups, an abelian group of order $35 = 5 \cdot 7$ (a product of distinct primes) is cyclic, so $\ZZ/35$ is the only one.

:::

:::

::: {.pf-step #s2}

Order $27 = 3^3$: the number of abelian groups is the number of partitions of $3$, which is $3$.

::: pf-proof

the fundamental theorem of finite abelian groups says an abelian group of order $p^3$ is a direct product of cyclic $p$-groups whose orders multiply to $p^3$, i.e. correspond to partitions of $3$.

:::

:::

::: {.pf-step #s3}

The three abelian groups of order $27$ are $\ZZ/27$, $\ZZ/9 \times \ZZ/3$, and $\ZZ/3 \times \ZZ/3 \times \ZZ/3$.

::: pf-proof

the partitions of $3$ are $3$, $2+1$, and $1+1+1$.

:::

:::

::: pf-qed

$1$ group of order $35$ (step [](#s1){.pf-ref}) and $3$ groups of order $27$ (steps [](#s2){.pf-ref} and [](#s3){.pf-ref}).

:::

:::

:::
