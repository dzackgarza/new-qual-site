---
schema: qual/card@1
id: P-HGRO2
kind: problem
title: Count abelian groups of orders 35 and 27
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

::: problem
How many abelian groups of order $35$ are there, up to isomorphism?
How many are there of order $27$?
:::

::: {.solution}
<1>1. Order $35 = 5 \cdot 7$: there is exactly $1$ abelian group, namely $\ZZ/35$.
::: {.proof}
by the fundamental theorem of finite abelian groups, an abelian group of order $35 = 5 \cdot 7$ (a product of distinct primes) is cyclic, so $\ZZ/35$ is the only one.
:::

<1>2. Order $27 = 3^3$: the number of abelian groups is the number of partitions of $3$, which is $3$.
::: {.proof}
the fundamental theorem of finite abelian groups says an abelian group of order $p^3$ is a direct product of cyclic $p$-groups whose orders multiply to $p^3$, i.e. correspond to partitions of $3$.
:::

<1>3. The three abelian groups of order $27$ are $\ZZ/27$, $\ZZ/9 \times \ZZ/3$, and $\ZZ/3 \times \ZZ/3 \times \ZZ/3$.
::: {.proof}
the partitions of $3$ are $3$, $2+1$, and $1+1+1$.
:::

<1>4. Q.E.D.
::: {.proof}
$1$ group of order $35$ (<1>1) and $3$ groups of order $27$ (<1>2, <1>3).
:::
:::
