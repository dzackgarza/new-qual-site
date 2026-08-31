---
schema: qual/card@1
id: P-USPU6
kind: problem
title: A finite abelian group is the product of its Sylow subgroups
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Abelian Groups
  - Direct Products
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
- Show that any finite abelian group is isomorphic to the direct product of its Sylow subgroups
:::

::: solution
**Goal:** Prove that every finite abelian group $G$ is isomorphic to the direct product of its Sylow subgroups.

<1>1. Definition of the Sylow subgroups:
    *Proof:*
    <2>1. Let $G$ be a finite abelian group of order $|G| = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, where $p_1, \dots, p_k$ are distinct primes and $a_i \ge 1$.
    <2>2. For each $i \in \{1, \dots, k\}$, define
    $$P_i = \left\{ x \in G : x^{p_i^{a_i}} = e \right\}.$$
    <2>3. Because $G$ is abelian, $(xy)^{p_i^{a_i}} = x^{p_i^{a_i}} y^{p_i^{a_i}} = e$ for all $x, y \in P_i$, and $(x^{-1})^{p_i^{a_i}} = e$, so $P_i$ is a subgroup of $G$.
    <2>4. The order of every element in $P_i$ is a power of $p_i$, so $P_i$ is a $p_i$-subgroup. By Lagrange's Theorem and Sylow's Theorems (or Cauchy's Theorem), $|P_i| = p_i^{a_i}$, so $P_i$ is the unique Sylow $p_i$-subgroup of $G$.
    <2>5. Since $G$ is abelian, $P_i \trianglelefteq G$ for all $i$.

<1>2. Linear independence / trivial intersections of Sylow subgroups:
    *Proof:*
    <2>1. For each $j \in \{1, \dots, k\}$, define $Q_j = P_1 P_2 \cdots P_{j-1} P_{j+1} \cdots P_k$.
    <2>2. Every element $y \in Q_j$ has order dividing $\prod_{i \neq j} p_i^{a_i} = |G| / p_j^{a_j}$, which is relatively prime to $p_j$.
    <2>3. Every element $x \in P_j$ has order dividing $p_j^{a_j}$.
    <2>4. If $z \in P_j \cap Q_j$, then the order $o(z)$ divides both $p_j^{a_j}$ and $|G|/p_j^{a_j}$.
    <2>5. Since $\gcd(p_j^{a_j}, |G|/p_j^{a_j}) = 1$, $o(z) = 1$, which forces $z = e$.
    <2>6. Thus $P_j \cap Q_j = \{e\}$ for all $j \in \{1, \dots, k\}$.

<1>3. Generation of $G$ via Bézout's identity:
    *Proof:*
    <2>1. For each $i \in \{1, \dots, k\}$, let $m_i = |G| / p_i^{a_i}$.
    <2>2. Since $p_1, \dots, p_k$ are distinct primes, $\gcd(m_1, m_2, \dots, m_k) = 1$.
    <2>3. By Bézout's identity in $\mathbb{Z}$, there exist integers $u_1, u_2, \dots, u_k \in \mathbb{Z}$ such that
    $$\sum_{i=1}^k u_i m_i = 1.$$
    <2>4. For any $g \in G$:
    $$g = g^1 = g^{\sum_{i=1}^k u_i m_i} = \prod_{i=1}^k g^{u_i m_i}.$$
    <2>5. For each $i$, let $g_i = g^{u_i m_i}$. Then $g_i^{p_i^{a_i}} = g^{u_i m_i p_i^{a_i}} = g^{u_i |G|} = (g^{|G|})^{u_i} = e^{u_i} = e$.
    <2>6. Thus $g_i \in P_i$ for each $i$, which proves that $g \in P_1 P_2 \cdots P_k$.
    <2>7. Therefore $G = P_1 P_2 \cdots P_k$.

<1>4. Construction of the direct product isomorphism:
    *Proof:*
    <2>1. Define the map $\Phi: P_1 \times P_2 \times \cdots \times P_k \to G$ by
    $$\Phi(g_1, g_2, \dots, g_k) = g_1 g_2 \cdots g_k.$$
    <2>2. Since $G$ is abelian, $\Phi$ is a group homomorphism.
    <2>3. By <1>3, $\Phi$ is surjective.
    <2>4. If $\Phi(g_1, \dots, g_k) = e$, then for each $j$, $g_j^{-1} = \prod_{i \neq j} g_i \in P_j \cap Q_j$.
    <2>5. By <1>2, $P_j \cap Q_j = \{e\}$, so $g_j = e$ for all $j$.
    <2>6. Thus $\ker \Phi = \{(e, \dots, e)\}$, so $\Phi$ is injective.
    <2>7. Therefore $\Phi$ is an isomorphism.

<1>5. Conclusion:
    *Proof:*
    The finite abelian group $G$ is isomorphic to the direct product of its Sylow subgroups $P_1 \times P_2 \times \cdots \times P_k$.
:::
