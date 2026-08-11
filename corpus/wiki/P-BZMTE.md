---
schema: qual/card@1
id: P-BZMTE
kind: problem
title: "To see that $\\phi(n)$ is even for all $n>2$, we can take a prime fact\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

To see that $\phi(n)$ is even for all $n>2$, we can take a prime factorization of $n$ and write
$$
\phi(n) = \phi\left( \prod_{i=1}^m p_i^{k_i}\right) = \prod_{i=1}^m \phi(p_i^{k_i}) = \prod_{i=1}^m p^{k_i - 1}(p - 1) = \prod_{i=1}^m p^{k_i - 1} \prod_{i=1}^m (p - 1)
$$

where each $k_i \geq 1 \implies k_i-1 \geq 0$.
But every prime power is odd, and a product of odd numbers is odd, so the first product is odd.
It is also true that $p-1$ is even for every prime $p$, and the second term is a product of even terms and thus even.
So $\phi(n)$ is the product of an even and an odd number, which is always even.
