---
schema: qual/card@1
id: P-LARQ7
kind: problem
title: Examples distinguishing principal, prime, and maximal ideals
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all three requested ideal examples with Lerman practice problem 7."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified each example directly, including nonprincipality of (x,y) in a two-variable polynomial ring and the quotient criteria for prime and maximal ideals."
---

::: {.problem}
Give each of the following examples:

1. A principal ideal that is not prime.

2. A prime ideal that is not principal.

3. A prime ideal that is not maximal.
:::

::: {.solution}
Let $k$ be any field.

<1>1. The ideal $(6)\subset\mathbb Z$ is principal but not prime.
::: {.proof}
It is principal by definition. Moreover
$$
2\cdot3=6\in(6),
$$
while neither $2$ nor $3$ belongs to $(6)$. Hence $(6)$ fails the defining property of a prime ideal.
:::

<1>2. The ideal $(x,y)\subset k[x,y]$ is prime but not principal.
::: {.proof}
Evaluation at $(0,0)$ gives a surjective homomorphism
$$
k[x,y]\to k
$$
with kernel $(x,y)$. Hence
$$
k[x,y]/(x,y)\cong k,
$$
so $(x,y)$ is maximal and therefore prime.

Suppose $(x,y)=(f)$ were principal. Since $x,y\in(f)$, the polynomial $f$ divides both $x$ and $y$. In the UFD $k[x,y]$, any common divisor of the relatively prime irreducibles $x$ and $y$ is a unit. Thus $f$ would be a unit, so $(f)=k[x,y]$, contradicting $(x,y)\ne k[x,y]$. Therefore $(x,y)$ is not principal.
:::

<1>3. The ideal $(x)\subset k[x,y]$ is prime but not maximal.
::: {.proof}
The evaluation homomorphism at $x=0$ identifies
$$
k[x,y]/(x)\cong k[y].
$$
The quotient $k[y]$ is an integral domain, so $(x)$ is prime. It is not a field, since $y$ is not invertible. Therefore $(x)$ is not maximal.
:::
:::
