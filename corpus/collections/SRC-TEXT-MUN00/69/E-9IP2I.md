---
schema: qual/card@1
id: E-9IP2I
kind: problem
title: Free products of finite cyclic groups determine their factors
classification:
  areas:
  - topology
  topics:
  - Free Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Prove the following.

Theorem.
Let $G = G_1 * G_2$, where $G_1$ and $G_2$ are cyclic of orders $m$ and $n$, respectively.
Then $m$ and $n$ are uniquely determined by $G$.

(a) Show $G/[G, G]$ has order $mn$.

(b) Determine the largest integer $k$ such that $G$ has an element of order $k$.
(See [[E-175IG]].)

(c) Prove the theorem.
:::

::: solution
**Goal:** Prove that the orders $m$ and $n$ of the cyclic factors in the free product $G = (\mathbb{Z}/m\mathbb{Z}) * (\mathbb{Z}/n\mathbb{Z})$ are uniquely determined by the isomorphism class of $G$.

<1>1. Part (a): Order of the abelianization $G/[G, G]$.
    *Proof:*
    <2>1. By the abelianization property of free products (Theorem 69.2), the abelianization of a free product is isomorphic to the direct sum of the abelianizations of its factors:
        $$G / [G, G] \cong G_1^{\text{ab}} \oplus G_2^{\text{ab}}.$$
    <2>2. Since $G_1 \cong \mathbb{Z}/m\mathbb{Z}$ and $G_2 \cong \mathbb{Z}/n\mathbb{Z}$ are abelian, $G_1^{\text{ab}} = G_1$ and $G_2^{\text{ab}} = G_2$.
    <2>3. Thus $G / [G, G] \cong (\mathbb{Z}/m\mathbb{Z}) \oplus (\mathbb{Z}/n\mathbb{Z})$.
    <2>4. The order of this finite abelian group is $|G / [G, G]| = |\mathbb{Z}/m\mathbb{Z}| \cdot |\mathbb{Z}/n\mathbb{Z}| = mn$.

<1>2. Part (b): Maximum finite order of an element in $G$.
    The largest finite order $k$ of an element in $G$ is $k = \max(m, n)$.
    *Proof:*
    <2>1. By the standard classification of torsion elements in free products (Kurosh Subgroup Theorem / [[E-175IG]]), every element of finite order in $G_1 * G_2$ is conjugate to an element of $G_1$ or an element of $G_2$.
    <2>2. Conjugate elements have identical orders.
    <2>3. The elements of $G_1$ have orders dividing $m$, with the generator having order $m$.
    <2>4. The elements of $G_2$ have orders dividing $n$, with the generator having order $n$.
    <2>5. Any element of $G$ not conjugate to an element of a factor is cyclically reduced of syllable length $\ge 2$, hence has infinite order.
    <2>6. Therefore, the set of finite orders of elements in $G$ is $\{d \in \mathbb{Z}_+ \mid d \mid m \text{ or } d \mid n\}$, whose maximum element is $k = \max(m, n)$.

<1>3. Part (c): Unique determination of $m$ and $n$.
    *Proof:*
    <2>1. The abstract group structure of $G$ determines two algebraic invariants:
        - The order of its abelianization: $P = |G / [G, G]| = mn$.
        - The maximum finite order of an element in $G$: $M = \max(m, n)$.
    <2>2. Assuming without loss of generality that $m \ge n$, we have:
        $$m = M \quad \text{and} \quad n = \frac{P}{M}.$$
    <2>3. Thus the multiset $\{m, n\}$ is uniquely determined by the group invariants $P$ and $M$ of $G$. Q.E.D.
:::
