---
schema: qual/card@1
id: P-CASNS
kind: problem
title: Degree of $\QQ(7^{1/5},5^{1/4})$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $\alpha,\beta$ denote the unique positive real $5^{\text{th}}$ root of 7 and $4^{\text{th}}$ root of 5, respectively.
Determine the degree of $\QQ[\alpha,\beta]$ over $\QQ$.
:::

::: {.solution}
We have $\alpha = 7^{1/5}$ and $\beta = 5^{1/4}$.

1. Consider the polynomial $f(x) = x^5 - 7 \in \QQ[x]$.
   By Eisenstein's criterion at the prime $p = 7$, $f(x)$ is irreducible over $\QQ$.
   Since $\alpha$ is a root of $f(x)$, the minimal polynomial of $\alpha$ over $\QQ$ is $x^5 - 7$, so $[\QQ(\alpha) : \QQ] = 5$.

2. Similarly, consider $g(x) = x^4 - 5 \in \QQ[x]$.
   By Eisenstein's criterion at the prime $p = 5$, $g(x)$ is irreducible over $\QQ$, so $[\QQ(\beta) : \QQ] = 4$.

3. By the tower law, $[\QQ(\alpha,\beta):\QQ]$ is divisible by $[\QQ(\alpha):\QQ]=5$ and by $[\QQ(\beta):\QQ]=4$, hence by $\operatorname{lcm}(5,4)=20$.
On the other hand, $\beta$ is a root of $x^4-5\in\QQ(\alpha)[x]$, so $[\QQ(\alpha,\beta):\QQ(\alpha)]\le 4$ and $[\QQ(\alpha,\beta):\QQ]\le 5\cdot4=20$.
Therefore
$$
[\QQ(\alpha, \beta) : \QQ] = 20.
$$
:::
