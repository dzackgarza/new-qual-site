---
schema: qual/card@1
id: FF-SOE5P
kind: fact
title: Euler's totient of a prime power
prompts:
- What is $\phi(p^k)$?
classification:
  areas:
  - algebra
  topics:
  - Number Theory
relations: []
review: draft
---

::: {.fact}
For a prime $p$ and an integer $k\ge1$, the [[D-JX3YC|Euler totient]] of $p^k$ is
$$
\phi(p^k)=p^{k-1}(p-1)=p^k\qty{1-\frac1p}.
$$
:::

::: {.proof}
An integer $m$ with $1\le m\le p^k$ fails to be coprime to $p^k$ exactly when $p\divides m$, and there are $p^{k-1}$ such multiples of $p$.
So $\phi(p^k)=p^k-p^{k-1}$.
:::
