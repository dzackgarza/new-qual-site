---
schema: qual/card@1
id: E-AMD-I4NOLHWA
kind: problem
title: Groups of order 10
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Classify all groups of order 10.
:::

::: solution
**Goal:** Classify all groups of order $10$ up to group isomorphism.

<1>1. Sylow structure and semidirect product:
    *Proof:*
    <2>1. The order of $G$ is $|G| = 10 = 2 \cdot 5$.
    <2>2. By the Sylow theorems, the number $n_5$ of Sylow 5-subgroups satisfies $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 2$, which forces $n_5 = 1$.
    <2>3. Thus the unique Sylow 5-subgroup $P = \langle y \rangle \cong \mathbb{Z}_5$ is normal in $G$ ($P \trianglelefteq G$).
    <2>4. Let $Q = \langle x \rangle \cong \mathbb{Z}_2$ be a Sylow 2-subgroup.
    <2>5. Because $|P| = 5$ and $|Q| = 2$ are coprime, $P \cap Q = \{e\}$ and $|P Q| = 10 = |G|$.
    <2>6. Thus $G$ is an internal semidirect product:
        $$G \cong P \rtimes_\theta Q \cong \mathbb{Z}_5 \rtimes_\theta \mathbb{Z}_2,$$
        where $\theta: \mathbb{Z}_2 \to \operatorname{Aut}(\mathbb{Z}_5)$ defines the action $\theta(x)(y) = x y x^{-1}$.

<1>2. Classification of actions $\theta: \mathbb{Z}_2 \to \operatorname{Aut}(\mathbb{Z}_5)$:
    *Proof:*
    <2>1. The automorphism group is $\operatorname{Aut}(\mathbb{Z}_5) \cong (\mathbb{Z}/5\mathbb{Z})^\times \cong \mathbb{Z}_4$.
    <2>2. In $(\mathbb{Z}/5\mathbb{Z})^\times$, the elements of order dividing $2$ are $1$ and $4 \equiv -1 \pmod 5$.
    <2>3. There are exactly two homomorphisms $\theta: \mathbb{Z}_2 \to \operatorname{Aut}(\mathbb{Z}_5)$:
        - **Trivial action ($\theta(x) = \operatorname{id}$):** $x y x^{-1} = y$.
        - **Inversion action ($\theta(x) = -\operatorname{id}$):** $x y x^{-1} = y^{-1}$.

<1>3. Determination of the two isomorphism classes:
    *Proof:*
    <2>1. **Case 1 (Trivial action):** $x$ and $y$ commute, so $G \cong \mathbb{Z}_5 \times \mathbb{Z}_2 \cong \mathbb{Z}_{10}$ is cyclic.
    <2>2. **Case 2 (Inversion action):** $G$ has presentation $\langle y, x \mid y^5 = 1, x^2 = 1, x y x^{-1} = y^{-1} \rangle$, which is the dihedral group $D_5$ of order $10$.

<1>4. Conclusion:
    Up to isomorphism, the only groups of order $10$ are:
    $$\mathbb{Z}_{10} \quad \text{and} \quad D_5.$$
    Q.E.D.
:::
