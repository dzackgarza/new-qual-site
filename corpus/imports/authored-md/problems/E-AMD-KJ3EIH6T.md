---
schema: qual/card@1
id: E-AMD-KJ3EIH6T
kind: exercise
title: The four groups of order 28
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Classify all groups of order 28.
:::

::: solution
**Goal:** Classify all groups of order $28 = 2^2 \cdot 7$ up to isomorphism.

<1>1. Sylow analysis:
    *Proof:*
    <2>1. **Sylow 7-subgroups:** $n_7 \equiv 1 \pmod 7$ and $n_7 \mid 4$. Thus $n_7 \in \{1\}$, so there is a unique normal Sylow 7-subgroup $P \cong \mathbb{Z}_7$ ($P \trianglelefteq G$).
    <2>2. **Sylow 2-subgroups:** $n_2 \equiv 1 \pmod 2$ and $n_2 \mid 7$. Thus $n_2 \in \{1, 7\}$.
    <2>3. Let $Q$ be a Sylow 2-subgroup of order $4$. Then $Q \cong \mathbb{Z}_4$ or $Q \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.

<1>2. Semidirect product decomposition:
    *Proof:*
    <2>1. Since $|P| = 7$ and $|Q| = 4$ are coprime, $P \cap Q = \{e\}$ and $|PQ| = 28 = |G|$.
    <2>2. Because $P \trianglelefteq G$, $G \cong P \rtimes_\theta Q$ for some homomorphism $\theta: Q \to \operatorname{Aut}(P)$.
    <2>3. $\operatorname{Aut}(\mathbb{Z}_7) \cong (\mathbb{Z}/7\mathbb{Z})^\times \cong \mathbb{Z}_6$.

<1>3. Case $Q \cong \mathbb{Z}_4$:
    *Proof:*
    <2>1. A homomorphism $\theta: \mathbb{Z}_4 \to \mathbb{Z}_6$ has image order dividing $\gcd(4, 6) = 2$.
    <2>2. **Trivial action ($|\operatorname{im} \theta| = 1$):** $G \cong \mathbb{Z}_7 \times \mathbb{Z}_4 \cong \mathbb{Z}_{28}$.
    <2>3. **Non-trivial action ($|\operatorname{im} \theta| = 2$):** The unique element of order $2$ in $\mathbb{Z}_6$ is $3$, corresponding to inversion $x \mapsto x^{-1}$ in $\mathbb{Z}_7$. The generator of $\mathbb{Z}_4$ maps to this element; thus $\theta(1) = x \mapsto x^6 = x^{-1}$. This gives a non-abelian group $\mathbb{Z}_7 \rtimes \mathbb{Z}_4$.

<1>4. Case $Q \cong \mathbb{Z}_2 \times \mathbb{Z}_2$:
    *Proof:*
    <2>1. A homomorphism $\theta: \mathbb{Z}_2 \times \mathbb{Z}_2 \to \mathbb{Z}_6$ has image in the unique subgroup $\{0, 3\} \cong \mathbb{Z}_2$ of $\mathbb{Z}_6$.
    <2>2. **Trivial action:** $G \cong \mathbb{Z}_7 \times \mathbb{Z}_2 \times \mathbb{Z}_2 \cong \mathbb{Z}_{14} \times \mathbb{Z}_2$.
    <2>3. **Non-trivial action:** At least one generator of $\mathbb{Z}_2 \times \mathbb{Z}_2$ acts by inversion on $\mathbb{Z}_7$.
        Any two non-trivial homomorphisms $\theta, \theta': \mathbb{Z}_2^2 \to \mathbb{Z}_2$ differ by an automorphism of $\mathbb{Z}_2^2$, so they yield isomorphic semidirect products.
    <2>4. This gives the dihedral group $D_7 \times \mathbb{Z}_2 \cong D_{14}$.

<1>5. Complete classification:
    The four groups of order 28 are:
    1. $\mathbb{Z}_{28}$ (abelian, cyclic).
    2. $\mathbb{Z}_{14} \times \mathbb{Z}_2$ (abelian, non-cyclic).
    3. $\mathbb{Z}_7 \rtimes \mathbb{Z}_4$ (non-abelian, $Q \cong \mathbb{Z}_4$ acts by inversion).
    4. $D_{14} \cong D_7 \times \mathbb{Z}_2$ (non-abelian, $Q \cong \mathbb{Z}_2^2$).

<1>6. Conclusion:
    There are exactly four groups of order 28, up to isomorphism. Q.E.D.
:::
