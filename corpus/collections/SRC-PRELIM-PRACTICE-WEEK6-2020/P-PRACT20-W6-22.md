---
schema: qual/card@1
id: P-PRACT20-W6-22
kind: problem
title: Factorials ending in exactly $99$ zeros
classification:
  areas:
  - prelim
  topics:
  - Number Theory
  - Factorials
relations: []
review: draft
---

::: {.problem}
For how many positive integers $k$ does $k!$ end in exactly $99$ zeros?
:::

::: {.solution}
The answer is $5$.

The number of trailing zeros of $k!$ is the exponent of $10$ dividing $k!$. Since $k!$ has at least as many factors of $2$ as of $5$, this is the exponent of $5$ in $k!$, which by Legendre's formula is

$$
Z(k)=\sum_{j\geq1}\left\lfloor\frac{k}{5^j}\right\rfloor.
$$

$Z$ is nondecreasing and changes only when $k$ passes a multiple of $5$, so $Z$ is constant on each block $\{5N,5N+1,\dots,5N+4\}$. A value is skipped when $k$ is divisible by $25$, since then $Z$ increases by at least $2$. Here

$$
Z(399)=79+15+3=97,\qquad Z(400)=80+16+3=99,\qquad Z(405)=81+16+3=100.
$$

So $Z(k)=99$ exactly for $k=400,401,402,403,404$, and there are $5$ such integers.
:::
