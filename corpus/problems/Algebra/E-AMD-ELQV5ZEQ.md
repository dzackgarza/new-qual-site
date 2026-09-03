---
schema: qual/card@1
id: E-AMD-ELQV5ZEQ
kind: problem
title: Groups of order 99
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Classify all groups of order 99 up to isomorphism.
:::

::: solution
**Goal:** Prove that every group of order $99$ is abelian and determine its isomorphism classes.

<1>1. Sylow subgroup count and normality:
    *Proof:*
    <2>1. The order of $G$ is $|G| = 99 = 3^2 \cdot 11$.
    <2>2. **Sylow 11-subgroups:** By the Sylow theorems, the number $n_{11}$ of Sylow 11-subgroups satisfies:
        $$n_{11} \equiv 1 \pmod{11} \quad \text{and} \quad n_{11} \mid 9.$$
        The divisors of $9$ are $\{1, 3, 9\}$, and only $1 \equiv 1 \pmod{11}$. Thus $n_{11} = 1$.
        Hence the Sylow 11-subgroup $Q \in \operatorname{Syl}_{11}(G)$ is normal ($Q \trianglelefteq G$), with $Q \cong \mathbb{Z}_{11}$.
    <2>3. **Sylow 3-subgroups:** The number $n_3$ of Sylow 3-subgroups satisfies:
        $$n_3 \equiv 1 \pmod 3 \quad \text{and} \quad n_3 \mid 11.$$
        The divisors of $11$ are $\{1, 11\}$. Since $11 \equiv 2 \not\equiv 1 \pmod 3$, we must have $n_3 = 1$.
        Hence the Sylow 3-subgroup $P \in \operatorname{Syl}_3(G)$ is normal ($P \trianglelefteq G$), with $|P| = 9$.

<1>2. Direct product decomposition:
    *Proof:*
    <2>1. Since $|P| = 9$ and $|Q| = 11$ are coprime, $P \cap Q = \{e\}$.
    <2>2. The product $P Q$ has order $|P Q| = \frac{|P| |Q|}{|P \cap Q|} = 99 = |G|$, so $G = P Q$.
    <2>3. Because both $P \trianglelefteq G$ and $Q \trianglelefteq G$, $G$ is the internal direct product:
        $$G \cong P \times Q.$$

<1>3. Classification of groups of order $9$:
    *Proof:*
    <2>1. $P$ has order $p^2 = 3^2$, hence is abelian.
    <2>2. Up to isomorphism, there are two abelian groups of order $9$: $\mathbb{Z}_9$ and $\mathbb{Z}_3 \times \mathbb{Z}_3$.
    <2>3. **Case 1 ($P \cong \mathbb{Z}_9$):**
        $$G \cong \mathbb{Z}_9 \times \mathbb{Z}_{11} \cong \mathbb{Z}_{99}.$$
    <2>4. **Case 2 ($P \cong \mathbb{Z}_3 \times \mathbb{Z}_3$):**
        $$G \cong \mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_{11} \cong \mathbb{Z}_3 \times \mathbb{Z}_{33}.$$

<1>4. Conclusion:
    Up to isomorphism, there are exactly two groups of order $99$, both abelian:
    $$\mathbb{Z}_{99} \quad \text{and} \quad \mathbb{Z}_3 \times \mathbb{Z}_{33}.$$
    Q.E.D.
:::
