---
schema: qual/card@1
id: P-BZMTE
kind: problem
title: "To see that $\\phi(n)$ is even for all $n>2$, we can take a prime fact\u2026"
classification:
  areas:
  - algebra
  topics:
  - number-theory
  - roots-of-unity
relations: []
review: draft
solved: false
---

::: problem
To see that $\phi(n)$ is even for all $n>2$, we can take a prime factorization of $n$ and write
$$
\phi(n) = \phi\left( \prod_{i=1}^m p_i^{k_i}\right) = \prod_{i=1}^m \phi(p_i^{k_i}) = \prod_{i=1}^m p_i^{k_i - 1}(p_i - 1)
$$

where each $k_i \geq 1$.
Now split on whether $n$ has an odd prime factor.

- If some $p_i$ is odd, then $p_i - 1$ is even, and one even factor makes the whole product even.

- Otherwise $n = 2^k$, and $n>2$ forces $k\geq 2$.
  Then $\phi(n) = 2^{k-1}$ with $k-1\geq 1$, which is even.

Either way $\phi(n)$ is even.
The case split is necessary because $2-1 = 1$ is odd, so the factor $p_i - 1$ supplies no evenness when $p_i = 2$.
:::
