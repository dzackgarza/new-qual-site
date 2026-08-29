---
schema: qual/card@1
id: P-GT22M
kind: problem
title: If $K/F$ is cyclic and $E/F$ is normal then $E/F$ and $K/E$ are cyclic
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $F \subseteq E \subseteq K$ be a tower of fields such that $K/F$ is a finite cyclic Galois extension.
Suppose $E/F$ is normal.
Prove that both $E/F$ and $K/E$ are cyclic Galois extensions.
:::

::: solution
**Goal:** Prove that if $K/F$ is cyclic and $E/F$ is normal, then $\operatorname{Gal}(E/F)$ and $\operatorname{Gal}(K/E)$ are cyclic.

<1>1. Setting and the Galois Group of $K/F$:
    *Proof:*
    <2>1. By hypothesis, $K/F$ is a finite cyclic Galois extension.
    <2>2. Let $G = \operatorname{Gal}(K/F)$ be the Galois group.
    <2>3. By definition of cyclic extensions, $G$ is a finite **cyclic group**.

<1>2. Galois Correspondence for $K/E$:
    *Proof:*
    <2>1. By the Fundamental Theorem of Galois Theory, the extension $K/E$ is Galois with Galois group:
        $$H = \operatorname{Gal}(K/E) \le G = \operatorname{Gal}(K/F).$$
    <2>2. $H$ is a subgroup of the cyclic group $G$.
    <2>3. A fundamental property of cyclic groups states that **every subgroup of a cyclic group is cyclic**.
    <2>4. Therefore, $H = \operatorname{Gal}(K/E)$ is a cyclic group, so $K/E$ is a **cyclic extension**.

<1>3. Galois Correspondence for $E/F$:
    *Proof:*
    <2>1. Since $E/F$ is normal (and separable, since $K/F$ is separable), $E/F$ is a Galois extension.
    <2>2. By the Fundamental Theorem of Galois Theory, $E/F$ being normal is equivalent to $H = \operatorname{Gal}(K/E)$ being a normal subgroup of $G = \operatorname{Gal}(K/F)$ (which is automatically true since $G$ is abelian/cyclic).
    <2>3. The Galois group of the intermediate extension $E/F$ is isomorphic to the quotient group:
        $$\operatorname{Gal}(E/F) \cong G / H = \operatorname{Gal}(K/F) / \operatorname{Gal}(K/E).$$
    <2>4. A fundamental property of cyclic groups states that **every quotient group of a cyclic group is cyclic** (the image of a generator under the canonical projection generates the quotient).
    <2>5. Therefore, $\operatorname{Gal}(E/F)$ is a cyclic group, so $E/F$ is a **cyclic extension**.

<1>4. Conclusion:
    Subgroups and quotient groups of cyclic groups are cyclic, so both $K/E$ and $E/F$ are cyclic Galois extensions. Q.E.D.
:::
