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

::: {.solution}
::: pf

::: pf-step

(a) The abelianization $G/[G, G]$ has order $mn$.

::: pf-proof

::: pf-step

By the abelianization property of free products (Theorem 69.2), the abelianization of a free product is isomorphic to the direct sum of the abelianizations of its factors:
        $$G / [G, G] \cong G_1^{\text{ab}} \oplus G_2^{\text{ab}}.$$

:::

::: pf-step

Since $G_1 \cong \ZZ/m\ZZ$ and $G_2 \cong \ZZ/n\ZZ$ are abelian, $G_1^{\text{ab}} = G_1$ and $G_2^{\text{ab}} = G_2$.

:::

::: pf-step

Thus $G / [G, G] \cong (\ZZ/m\ZZ) \oplus (\ZZ/n\ZZ)$.

:::

::: pf-step

The order of this finite abelian group is $\cardinality{G / [G, G]} = \cardinality{\ZZ/m\ZZ} \cdot \cardinality{\ZZ/n\ZZ} = mn$.

:::

:::

:::

::: pf-step

(b) The largest order $k$ of an element of finite order in $G$ is $\boxed{k = \max(m, n)}$.

::: pf-proof

::: pf-step

By the standard classification of torsion elements in free products (Kurosh Subgroup Theorem / [[E-175IG]]), every element of finite order in $G_1 * G_2$ is conjugate to an element of $G_1$ or an element of $G_2$.

:::

::: pf-step

Conjugate elements have identical orders.

:::

::: pf-step

The elements of $G_1$ have orders dividing $m$, with the generator having order $m$.

:::

::: pf-step

The elements of $G_2$ have orders dividing $n$, with the generator having order $n$.

:::

::: pf-step

Any element of $G$ not conjugate to an element of a factor is cyclically reduced of syllable length $\ge 2$, hence has infinite order.

:::

::: pf-step

Therefore, the set of finite orders of elements in $G$ is $\{d \in \ZZ_+ \mid d \mid m \text{ or } d \mid n\}$, whose maximum element is $k = \max(m, n)$.

:::

:::

:::

::: pf-step

(c) The group $G$ determines $m$ and $n$.

::: pf-proof

::: pf-step

The abstract group structure of $G$ determines two algebraic invariants:
        - The order of its abelianization: $P = \cardinality{G / [G, G]} = mn$.
        - The maximum finite order of an element in $G$: $M = \max(m, n)$.

:::

::: pf-step

Assuming without loss of generality that $m \ge n$, we have:
        $$m = M \quad \text{and} \quad n = \frac{P}{M}.$$

:::

::: pf-step

Thus the multiset $\{m, n\}$ is uniquely determined by the group invariants $P$ and $M$ of $G$.

:::

:::

:::

:::

:::
