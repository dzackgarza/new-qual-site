---
schema: qual/card@1
id: P-BKF04-6A
kind: problem
title: A congruence condition on square-free $n$ forcing every group of order $n$ to be abelian
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $n$ be a square-free positive integer (i.e., $n=1$ or $n$ is prime or $n$ is a product of distinct primes). Assume that for every product of primes $pq_1\cdots q_r$ dividing $n$, with $r>0$, we have $q_1\cdots q_r\not\equiv1\pmod p$. Prove that every group $G$ of order $n$ is abelian.
:::

::: {.solution}
Suppose $p\mid n$ and let $P$ be a Sylow $p$-subgroup of $G$. Let $N$ be the normalizer of $P$. By Sylow's theorems, the number of Sylow $p$-subgroups is $[G:N]\equiv1\pmod p$. Since $N$ contains $P$ and $n$ is square-free, $[G:N]=q_1\cdots q_r$ for distinct primes $q_i\neq p$ with $pq_1\cdots q_r\mid n$. The hypothesis implies that $r=0$, hence $N=G$, so $P$ is normal. Now let $n=p_1\cdots p_k$ and let $P_1,\ldots,P_k$ be the corresponding normal Sylow subgroups. Let $Q_i\subseteq G$ be the product of the $P_j$ with $j\neq i$. Then $Q_i$ is a normal subgroup of order $n/p_i$, so $G/Q_i$ is cyclic of order $p_i$. Thus there is a surjective homomorphism $\phi_i\colon G\to\ZZ/p_i\ZZ$ for each $i$, and combining these gives a homomorphism $\phi\colon G\to\prod_i\ZZ/p_i\ZZ$. Let $K=\ker(\phi)$. Since each $\phi_i$ factors through $G/K$, every $p_i$ divides $\abs{G/K}$. This implies $K=\{1\}$. Then $\phi$ is an injective homomorphism between two groups of equal order, hence an isomorphism, and $G$ is abelian.
:::
