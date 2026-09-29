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

::: {.problem}
- Show that any finite abelian group is isomorphic to the direct product of its Sylow subgroups
:::

::: {.solution}
**Goal:** Prove that every finite abelian group $G$ is isomorphic to the direct product of its Sylow subgroups.

::: pf

::: pf-step

Definition of the Sylow subgroups:
    *Proof:*

::: pf-proof

::: pf-step

Let $G$ be a finite abelian group of order $|G| = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, where $p_1, \dots, p_k$ are distinct primes and $a_i \ge 1$.

:::

::: pf-step

For each $i \in \{1, \dots, k\}$, define
    $$P_i = \left\{ x \in G : x^{p_i^{a_i}} = e \right\}.$$

:::

::: pf-step

Because $G$ is abelian, $(xy)^{p_i^{a_i}} = x^{p_i^{a_i}} y^{p_i^{a_i}} = e$ for all $x, y \in P_i$, and $(x^{-1})^{p_i^{a_i}} = e$, so $P_i$ is a subgroup of $G$.

:::

::: pf-step

The order of every element in $P_i$ is a power of $p_i$, so $P_i$ is a $p_i$-subgroup. By Lagrange's Theorem and Sylow's Theorems (or Cauchy's Theorem), $|P_i| = p_i^{a_i}$, so $P_i$ is the unique Sylow $p_i$-subgroup of $G$.

:::

::: pf-step

Since $G$ is abelian, $P_i \trianglelefteq G$ for all $i$.

:::

:::

:::

::: {.pf-step #s2}

Linear independence / trivial intersections of Sylow subgroups:
    *Proof:*

::: pf-proof

::: pf-step

For each $j \in \{1, \dots, k\}$, define $Q_j = P_1 P_2 \cdots P_{j-1} P_{j+1} \cdots P_k$.

:::

::: pf-step

Every element $y \in Q_j$ has order dividing $\prod_{i \neq j} p_i^{a_i} = |G| / p_j^{a_j}$, which is relatively prime to $p_j$.

:::

::: pf-step

Every element $x \in P_j$ has order dividing $p_j^{a_j}$.

:::

::: pf-step

If $z \in P_j \cap Q_j$, then the order $o(z)$ divides both $p_j^{a_j}$ and $|G|/p_j^{a_j}$.

:::

::: pf-step

Since $\gcd(p_j^{a_j}, |G|/p_j^{a_j}) = 1$, $o(z) = 1$, which forces $z = e$.

:::

::: pf-step

Thus $P_j \cap Q_j = \{e\}$ for all $j \in \{1, \dots, k\}$.

:::

:::

:::

::: {.pf-step #s3}

Generation of $G$ via Bézout's identity:
    *Proof:*

::: pf-proof

::: pf-step

For each $i \in \{1, \dots, k\}$, let $m_i = |G| / p_i^{a_i}$.

:::

::: pf-step

Since $p_1, \dots, p_k$ are distinct primes, $\gcd(m_1, m_2, \dots, m_k) = 1$.

:::

::: pf-step

By Bézout's identity in $\mathbb{Z}$, there exist integers $u_1, u_2, \dots, u_k \in \mathbb{Z}$ such that
    $$\sum_{i=1}^k u_i m_i = 1.$$

:::

::: pf-step

For any $g \in G$:
    $$g = g^1 = g^{\sum_{i=1}^k u_i m_i} = \prod_{i=1}^k g^{u_i m_i}.$$

:::

::: pf-step

For each $i$, let $g_i = g^{u_i m_i}$. Then $g_i^{p_i^{a_i}} = g^{u_i m_i p_i^{a_i}} = g^{u_i |G|} = (g^{|G|})^{u_i} = e^{u_i} = e$.

:::

::: pf-step

Thus $g_i \in P_i$ for each $i$, which proves that $g \in P_1 P_2 \cdots P_k$.

:::

::: pf-step

Therefore $G = P_1 P_2 \cdots P_k$.

:::

:::

:::

::: pf-step

Construction of the direct product isomorphism:
    *Proof:*

::: pf-proof

::: pf-step

Define the map $\Phi: P_1 \times P_2 \times \cdots \times P_k \to G$ by
    $$\Phi(g_1, g_2, \dots, g_k) = g_1 g_2 \cdots g_k.$$

:::

::: pf-step

Since $G$ is abelian, $\Phi$ is a group homomorphism.

:::

::: pf-step

By step [](#s3){.pf-ref}, $\Phi$ is surjective.

:::

::: pf-step

If $\Phi(g_1, \dots, g_k) = e$, then for each $j$, $g_j^{-1} = \prod_{i \neq j} g_i \in P_j \cap Q_j$.

:::

::: pf-step

By step [](#s2){.pf-ref}, $P_j \cap Q_j = \{e\}$, so $g_j = e$ for all $j$.

:::

::: pf-step

Thus $\ker \Phi = \{(e, \dots, e)\}$, so $\Phi$ is injective.

:::

::: pf-step

Therefore $\Phi$ is an isomorphism.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    *Proof:*
    The finite abelian group $G$ is isomorphic to the direct product of its Sylow subgroups $P_1 \times P_2 \times \cdots \times P_k$.
:::
