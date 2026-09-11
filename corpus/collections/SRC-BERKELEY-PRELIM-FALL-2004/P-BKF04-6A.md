---
schema: qual/card@1
id: P-BKF04-6A
kind: problem
title: UC Berkeley Fall 2004 prelim 6A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let n be a square-free positive integer $( i . e . , n = 1 \mathrm { o r } n$ is prime or n is a product of distinct primes). Assume that for every product of primes $p q _ { 1 } \cdots q _ { r }$ dividing n, with $r > 0$ , we have $q _ { 1 } \cdots q _ { r } \not \equiv 1$ (mod p). Prove that every group G of order n is abelian.
:::

::: {.solution}
Suppose p|n and let P be a Sylow p-subgroup of G. Let N be the normalizer of P . By Sylow’s theorems, the number of Sylow p-subgroups is $[ G : N ] \equiv 1 { \pmod { p } }$ Since N contains P , we have $[ G : N ] = q _ { 1 } \cdot \cdot \cdot q _ { r }$ , where $p q _ { 1 } \cdots q _ { r } | n$ . Our hypothesis implies that $r = 0$ , hence $N = G$ , so P is normal. Now let $n = p _ { 1 } \cdots p _ { k }$ and let $P _ { 1 } , \ldots , P _ { k }$ be the corresponding normal Sylow subgroups. Let $Q _ { i } \subseteq G$ be the product of the $P _ { j } \mathrm { ^ { * } s }$ , omitting $P _ { i }$ Then $Q _ { i }$ is normal and $G / Q _ { i }$ is cyclic of order $p _ { i }$ . Thus we have a surjective homomorphism $\phi _ { i } \colon G \to \mathbb { Z } / p _ { i } \mathbb { Z }$ for each $i ,$ and combining these, we get a homomorphism $\begin{array} { r } { \phi \colon G \to \prod _ { i } \mathbb { Z } / p _ { i } \mathbb { Z } } \end{array}$ Let $K = \ker ( \phi )$ . Since each $\phi _ { i }$ factors through $G / K$ , every $p _ { i }$ divides $| G / K |$ . This implies $K = 0$ . Then φ is an injective homomorphism between two groups of equal order, hence an isomorphism.
:::
