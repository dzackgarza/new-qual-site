---
schema: qual/card@1
id: P-LARQ2
kind: problem
title: Possible element orders in a group of order 20
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all three element-order questions and both source hints with Lerman practice problem 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Applied Cauchy's theorem to the prime divisors 2 and 5, and checked the source's direct-product counterexample has no element of order 4."
---

::: {.problem}
Let $G$ be a finite group of order $20$.

1. Must $G$ have an element of order $2$?

2. Must $G$ have an element of order $5$?

3. Must $G$ have an element of order $4$?

Justify each answer.
:::

::: {.solution}
The answers are: order $2$, yes; order $5$, yes; order $4$, no.

<1>1. Every group of order $20$ has elements of orders $2$ and $5$.
::: {.proof}
Since
$$
|G|=20=2^2\cdot5,
$$
both primes $2$ and $5$ divide $|G|$. Cauchy's theorem for finite groups therefore gives an element of order $2$ and an element of order $5$.
:::

<1>2. An element of order $4$ need not exist.
::: {.proof}
Consider
$$
G=C_2\times C_2\times C_5.
$$
Its order is $2\cdot2\cdot5=20$. For an element $(a,b,c)$, its order is the least common multiple of the three component orders. The first two component orders divide $2$, and the third divides $5$, so every element order divides
$$
\operatorname{lcm}(2,2,5)=10.
$$
More explicitly, the only possible element orders are $1,2,5,$ and $10$. Hence this group has no element of order $4$, providing the required counterexample.
:::
:::
