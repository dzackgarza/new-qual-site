---
schema: qual/card@1
id: FT-BAV4D
kind: theorem
title: Euler's theorem
slogan: 'A unit modulo $n$ raised to $\phi(n)$ is $1$ modulo $n$.'
prompts:
- State Euler's theorem, and say why coprimality is needed.
classification:
  areas:
  - algebra
  topics:
  - Number Theory
  - Cyclic Groups
relations: []
review: draft
---

::: {.theorem}
Let $n\ge1$ and let $a\in\ZZ$ with $\gcd(a,n)=1$.
Then
$$
a^{\phi(n)}\equiv1\pmod n,
$$
where $\phi$ is the [[D-JX3YC|Euler totient function]].
:::

::: {.proof}
The class of $a$ lies in the group $(\ZZ/n\ZZ)^\times$ of order $\phi(n)$, so its order divides $\phi(n)$ by Lagrange's theorem.
:::

::: {.example}
If $n>1$ and $d=\gcd(a,n)>1$, then $a^k\not\equiv1\pmod n$ for every $k\ge1$, since $d$ divides both $a^k$ and $n$ but not $1$.
For $a=2$ and $n=4$, $2^{\phi(4)}=2^2=4\equiv0\pmod4$.
:::
