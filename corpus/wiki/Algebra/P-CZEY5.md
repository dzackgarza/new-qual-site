---
schema: qual/card@1
id: P-CZEY5
kind: problem
title: The integers $n$ with $\phi(n)=2$ are $3,4,6$
classification:
  areas:
  - algebra
  topics:
  - Number Theory
  - Cyclic Groups
relations: []
review: draft
---

::: problem
Suppose $\phi(n) = 2$.
Take a prime factorization of $n$, so we have
$$
2 = \phi(n) = \prod_{i=1}^m \phi(p_i^{k_i}) 
$$

Since the only factors of 2 are 1 and 2, we must have $\phi(p_i^{k_i}) = 2$ for exactly one $i$, and the rest must be equal to 1.

Consider the term that equals 2. We have $\phi(p_i^{k_i}) = p^{k_i - 1}(p-1) = 2$, so we must have either

- Case 1: $p-1 = 2$ and $p^{k_i - 1} = 1$, so $p=3$ and $k_i = 1$.
  So $3 \divides n$, but $3^\ell$ does *not* divide $n$ for any $\ell > 1$.

- Case 2: $p^{k_i - 1} = 2$ and $(p-1) = 1$, so $p=2$ and $k_i = 2$.
  Thus $2^2$ divides $n$ but $2^\ell$ does not for any $\ell > 2$.

In either case, it remains to check are whether the other factors where $\phi(p_j^{k_j}) = 1$ can contribute any other distinct divisors to $n$.
We can note that $\phi(p_j^{k_j}) = 1$ iff $p^{k_j-1}(p-1) = 1$, so this forces $p=2$ and $k_j = 1$.
So $n$ may or may not contain a single factor of 2, but by uniqueness of prime factorization, this can only happen in case 1. Note that this also forces $2\divides n$ but $2^2$ does not divide $n$.

In summary, we've found that $\phi(n) = 2$ implies that

- $3 \divides n$, 9 does not divide $n$, and

  - $2\divides n$, 4 does not divide $n$

  - $2$ does not divide $n$

- $2^2 \divides n, 2^3$ does not divide n.

This reduces the possibilities to the finite set $n \in \theset{6,3,4}$, and $\phi(6) = \phi(3) = \phi(4) = 2$.
$\qed$
:::
