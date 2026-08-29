---
schema: qual/card@1
id: P-4MISE
kind: problem
title: Groups of order 15
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Determine the number of groups of order $15$ up to isomorphism, and prove your result.
:::

::: solution
**Goal:** Prove that there is exactly $1$ group of order $15$ up to isomorphism, which is the cyclic group $\mathbb{Z}_{15}$.

<1>1. Sylow Analysis of $|G| = 15 = 3 \times 5$:
    *Proof:*
    <2>1. Let $G$ be a group of order $|G| = 15 = 3 \times 5$.
    <2>2. Let $P \in \operatorname{Syl}_5(G)$ be a Sylow 5-subgroup and $Q \in \operatorname{Syl}_3(G)$ be a Sylow 3-subgroup.
    <2>3. By Sylow's Third Theorem:
        - The number $n_5$ of Sylow 5-subgroups satisfies:
          $$n_5 \mid 3 \implies n_5 \in \{1, 3\}, \qquad n_5 \equiv 1 \pmod 5.$$
          Since $3 \not\equiv 1 \pmod 5$, we must have $n_5 = 1$.
        - The number $n_3$ of Sylow 3-subgroups satisfies:
          $$n_3 \mid 5 \implies n_3 \in \{1, 5\}, \qquad n_3 \equiv 1 \pmod 3.$$
          Since $5 \equiv 2 \not\equiv 1 \pmod 3$, we must have $n_3 = 1$.
    <2>4. Therefore, both $P$ and $Q$ are **normal subgroups** of $G$:
        $$P \trianglelefteq G \quad \text{and} \quad Q \trianglelefteq G.$$

<1>2. Direct Product Decomposition:
    *Proof:*
    <2>1. Since $|P| = 5$ and $|Q| = 3$ are distinct primes, their intersection is trivial:
        $$P \cap Q = \{e\}.$$
    <2>2. The product subgroup $P Q \le G$ has order:
        $$|P Q| = \frac{|P||Q|}{|P \cap Q|} = \frac{5 \times 3}{1} = 15 = |G|.$$
    <2>3. Since $P \trianglelefteq G$, $Q \trianglelefteq G$, and $P \cap Q = \{e\}$, the group $G$ is the **internal direct product**:
        $$G \cong P \times Q.$$

<1>3. Cyclic Identification:
    *Proof:*
    <2>1. Since $|P| = 5$ and $|Q| = 3$ are prime orders, $P \cong \mathbb{Z}_5$ and $Q \cong \mathbb{Z}_3$.
    <2>2. By the Chinese Remainder Theorem (since $\gcd(3, 5) = 1$):
        $$G \cong \mathbb{Z}_5 \times \mathbb{Z}_3 \cong \mathbb{Z}_{15}.$$
    <2>3. Thus every group of order 15 is **cyclic**.

<1>4. Conclusion:
    There is exactly $1$ group of order 15 up to isomorphism, namely $\mathbb{Z}_{15}$. Q.E.D.
:::
