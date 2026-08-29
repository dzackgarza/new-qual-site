---
schema: qual/card@1
id: P-ALGS08B
kind: problem
title: "Classification of all groups with 99 elements"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Classify all groups of order $99 = 3^2 \cdot 11$ up to isomorphism.
:::

::: solution
**Goal:** Prove that every group of order 99 is abelian, and classify the isomorphism types using Sylow theory and the Fundamental Theorem of Finitely Generated Abelian Groups.

<1>1. Sylow Subgroups Analysis:
    *Proof:*
    <2>1. Let $G$ be a group of order $|G| = 99 = 3^2 \cdot 11 = 9 \cdot 11$.
    <2>2. Let $n_p$ denote the number of Sylow $p$-subgroups of $G$:
        - For $p = 11$:
          $$n_{11} \equiv 1 \pmod{11} \quad \text{and} \quad n_{11} \mid 9.$$
          The divisors of 9 are $\{1, 3, 9\}$.
          Since $1 \equiv 1$, $3 \not\equiv 1$, and $9 \not\equiv 1 \pmod{11}$, we must have $n_{11} = 1$.
          Thus the Sylow 11-subgroup $P_{11}$ is unique and **normal**:
          $$P_{11} \trianglelefteq G, \qquad P_{11} \cong \mathbb{Z}/11\mathbb{Z}.$$
        - For $p = 3$:
          $$n_3 \equiv 1 \pmod 3 \quad \text{and} \quad n_3 \mid 11.$$
          The divisors of 11 are $\{1, 11\}$.
          Since $11 \equiv 2 \not\equiv 1 \pmod 3$, we must have $n_3 = 1$.
          Thus the Sylow 3-subgroup $P_3$ is unique and **normal**:
          $$P_3 \trianglelefteq G, \qquad |P_3| = 9 = 3^2.$$

<1>2. Direct Product Structure:
    *Proof:*
    <2>1. Since both $P_{11} \trianglelefteq G$ and $P_3 \trianglelefteq G$, and their orders are coprime ($\gcd(11, 9) = 1$):
        $$P_{11} \cap P_3 = \{e\}, \qquad |P_{11} P_3| = |P_{11}| |P_3| = 11 \cdot 9 = 99 = |G|.$$
    <2>2. Therefore, $G$ is the internal direct product:
        $$G \cong P_3 \times P_{11}.$$

<1>3. Classification of the Direct Factors:
    *Proof:*
    <2>1. The Sylow 11-subgroup has prime order 11, so it is uniquely isomorphic to the cyclic group:
        $$P_{11} \cong \mathbb{Z}/11\mathbb{Z}.$$
    <2>2. The Sylow 3-subgroup has order $3^2 = 9$. Every group of order $p^2$ (for $p$ prime) is abelian and isomorphic to either $\mathbb{Z}/p^2\mathbb{Z}$ or $\mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/p\mathbb{Z}$.
    <2>3. Thus there are exactly two possibilities for $P_3$:
        1. $P_3 \cong \mathbb{Z}/9\mathbb{Z}$,
        2. $P_3 \cong \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$.

<1>4. The Isomorphism Classes:
    *Proof:*
    <2>1. **Case 1 ($P_3 \cong \mathbb{Z}_9$):**
        $$G_1 \cong \mathbb{Z}_9 \times \mathbb{Z}_{11} \cong \mathbb{Z}_{99} \text{ (the cyclic group of order 99)}.$$
    <2>2. **Case 2 ($P_3 \cong \mathbb{Z}_3 \times \mathbb{Z}_3$):**
        $$G_2 \cong \mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_{11} \cong \mathbb{Z}_3 \times \mathbb{Z}_{33}.$$
    <2>3. $G_1$ has an element of order 9 (and order 99), whereas $G_2$ has exponent $\operatorname{lcm}(3, 11) = 33$, so $G_1 \not\cong G_2$.

<1>5. Conclusion:
    Every group of order 99 is abelian, and there are exactly two groups of order 99 up to isomorphism:
    1. $\mathbb{Z}_{99} \cong \mathbb{Z}_9 \times \mathbb{Z}_{11}$,
    2. $\mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_{11} \cong \mathbb{Z}_3 \times \mathbb{Z}_{33}$.
    Q.E.D.
:::
