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
Show that any finite abelian group is isomorphic to the direct product of its Sylow subgroups.
:::

::: {.solution}
Let $G$ be a finite abelian group of order $\abs{G} = p_1^{a_1} \cdots p_k^{a_k}$, where $p_1, \ldots, p_k$ are distinct primes and $a_i \ge 1$. For each $i$ define
$$P_i = \left\{ x \in G : x^{p_i^{a_i}} = e \right\}.$$

::: pf

::: pf-step

Each $P_i$ is the unique Sylow $p_i$-subgroup of $G$.

::: pf-proof

Because $G$ is abelian, $(xy)^{p_i^{a_i}} = x^{p_i^{a_i}} y^{p_i^{a_i}} = e$ for $x, y \in P_i$, and $(x^{-1})^{p_i^{a_i}} = e$, so $P_i$ is a subgroup. The order of every element of $P_i$ is a power of $p_i$, so by Cauchy's theorem $P_i$ is a $p_i$-group, and $\abs{P_i}\le p_i^{a_i}$ by Lagrange's theorem. Every Sylow $p_i$-subgroup has exponent dividing $p_i^{a_i}$, so it lies in $P_i$; hence $\abs{P_i} = p_i^{a_i}$ and $P_i$ is the only Sylow $p_i$-subgroup.

:::

:::

::: {.pf-step #s2}

For each $j$, let $Q_j = \prod_{i \ne j} P_i$. Then $P_j \cap Q_j = \{e\}$.

::: pf-proof

Every element of $Q_j$ has order dividing $\prod_{i \neq j} p_i^{a_i} = \abs{G} / p_j^{a_j}$, and every element of $P_j$ has order dividing $p_j^{a_j}$. An element $z \in P_j \cap Q_j$ therefore has order dividing $\gcd(p_j^{a_j}, \abs{G}/p_j^{a_j}) = 1$, so $z = e$.

:::

:::

::: {.pf-step #s3}

$G = P_1 P_2 \cdots P_k$.

::: pf-proof

Let $m_i = \abs{G} / p_i^{a_i}$. Since the $p_i$ are distinct primes, $\gcd(m_1, \ldots, m_k) = 1$, and Bézout's identity gives integers $u_i$ with $\sum_{i=1}^k u_i m_i = 1$. For $g \in G$,
$$g = g^{\sum_{i} u_i m_i} = \prod_{i=1}^k g^{u_i m_i},$$
and $g_i = g^{u_i m_i}$ satisfies $g_i^{p_i^{a_i}} = (g^{\abs{G}})^{u_i} = e$, so $g_i \in P_i$.

:::

:::

::: pf-step

The map $\Phi: P_1 \times \cdots \times P_k \to G$, $\Phi(g_1, \ldots, g_k) = g_1 \cdots g_k$, is an isomorphism.

::: pf-proof

Since $G$ is abelian, $\Phi$ is a homomorphism, and it is surjective by step [](#s3){.pf-ref}. If $\Phi(g_1, \ldots, g_k) = e$, then for each $j$, $g_j^{-1} = \prod_{i \neq j} g_i \in P_j \cap Q_j$, so $g_j = e$ by step [](#s2){.pf-ref}. Hence $\Phi$ is injective.

:::

:::

:::

:::
