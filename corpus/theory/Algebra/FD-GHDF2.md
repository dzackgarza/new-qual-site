---
schema: qual/card@1
id: FD-GHDF2
kind: proposition
title: Sign of a permutation from its cycle decomposition
prompts:
- How do you read the sign of a permutation off its disjoint cycle decomposition?
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
---

::: {.proposition}
Let $\sgn\colon S_n\to\theset{\pm1}$ be the sign homomorphism, and let $\sigma\in S_n$ have disjoint cycle decomposition $\sigma=c_1\cdots c_t$ with $c_j$ a cycle of length $k_j$.
Then
$$
\sgn(\sigma)=\prod_{j=1}^t(-1)^{k_j-1}.
$$
In particular, a cycle of length $k$ is odd if and only if $k$ is even, and $\sigma$ is odd if and only if an odd number of the $c_j$ have even length.
:::

::: {.proof}
A $k$-cycle is a product of $k-1$ transpositions: $(a_1\,a_2\,\cdots\,a_k)=(a_1\,a_k)(a_1\,a_{k-1})\cdots(a_1\,a_2)$.
Since each transposition has sign $-1$ and $\sgn$ is a homomorphism, $\sgn(c_j)=(-1)^{k_j-1}$, and the displayed formula follows by multiplying over $j$.
The factor $(-1)^{k_j-1}$ equals $-1$ exactly when $k_j$ is even, so the product equals $-1$ exactly when the number of even-length cycles is odd.
:::
