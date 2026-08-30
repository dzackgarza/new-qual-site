---
schema: qual/card@1
id: P-OS4K7
kind: problem
title: Groups of order 14
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
  date: 2026-08-30
---

::: {.problem}
Classify all groups of order 14 up to isomorphism. Prove your classification.
:::

::: solution
**Goal:** Prove that any group of order $14 = 2 \cdot 7$ is isomorphic to either the cyclic group $\mathbb{Z}_{14}$ or the dihedral group $D_7$.

<1>1. Sylow Analysis of $|G| = 14 = 2 \cdot 7$:
    *Proof:*
    <2>1. Let $P \in \operatorname{Syl}_7(G)$ be a Sylow 7-subgroup of $G$, so $|P| = 7$.
    <2>2. By Sylow's Third Theorem:
        - $n_7 \mid [G : P] = 2 \implies n_7 \in \{1, 2\}$.
        - $n_7 \equiv 1 \pmod 7$.
    <2>3. Since $2 \not\equiv 1 \pmod 7$, we must have:
        $$n_7 = 1.$$
    <2>4. Thus $P \trianglelefteq G$ is a **normal subgroup** of order 7.
    <2>5. Since 7 is prime, $P = \langle y \rangle \cong \mathbb{Z}_7$.

<1>2. Sylow 2-Subgroups and Semidirect Product Structure:
    *Proof:*
    <2>1. Let $Q \in \operatorname{Syl}_2(G)$ be a Sylow 2-subgroup, so $|Q| = 2$.
    <2>2. Let $Q = \langle x \rangle = \{e, x\}$ with $x^2 = e$.
    <2>3. Since $\gcd(|P|, |Q|) = \gcd(7, 2) = 1$, $P \cap Q = \{e\}$.
    <2>4. By order counting, $|P Q| = \frac{|P||Q|}{|P \cap Q|} = 14 = |G|$, so:
        $$G = P Q = P \rtimes_\theta Q.$$
    <2>5. Thus $G$ is a **semidirect product** $\mathbb{Z}_7 \rtimes_\theta \mathbb{Z}_2$, determined by a group homomorphism:
        $$\theta: \mathbb{Z}_2 \longrightarrow \operatorname{Aut}(\mathbb{Z}_7) \cong (\mathbb{Z}_7)^\times \cong \mathbb{Z}_6.$$

<1>3. Homomorphisms $\theta: \mathbb{Z}_2 \to \mathbb{Z}_6$:
    *Proof:*
    <2>1. The image $\theta(x) \in \operatorname{Aut}(\mathbb{Z}_7)$ must have order dividing $|Q| = 2$.
    <2>2. The group of automorphisms $\operatorname{Aut}(\mathbb{Z}_7) = \{\sigma_a: y \mapsto y^a \mid a \in (\mathbb{Z}_7)^\times\}$.
    <2>3. The elements of order dividing 2 in $(\mathbb{Z}_7)^\times$ satisfy $a^2 \equiv 1 \pmod 7$:
        $$a \equiv 1 \pmod 7 \quad \text{or} \quad a \equiv -1 \equiv 6 \pmod 7.$$
    <2>4. This gives exactly two possibilities for $\theta$:
        - **Case 1 (Trivial homomorphism):** $\theta(x) = \operatorname{id}$, so $x y x^{-1} = y^1 = y$.
          Here $x$ and $y$ commute, so the semidirect product is the direct product:
          $$G \cong \mathbb{Z}_7 \times \mathbb{Z}_2 \cong \mathbb{Z}_{14} \quad \text{(Cyclic group of order 14)}.$$
        - **Case 2 (Non-trivial homomorphism):** $\theta(x)(y) = y^{-1}$, so $x y x^{-1} = y^{-1}$.
          This is the standard presentation of the **dihedral group** of order 14 (symmetries of a regular 7-gon):
          $$G \cong \langle x, y \mid y^7 = 1, x^2 = 1, x y x^{-1} = y^{-1} \rangle \cong D_7 \quad (\text{or } D_{14}).$$

<1>4. Conclusion:
    Up to isomorphism, the only groups of order 14 are $\mathbb{Z}_{14}$ (abelian) and $D_7$ (non-abelian). Q.E.D.
:::

::: {.solution}
<1>1. $G$ group.
Proof: Sylow.

<1>2. Q.E.D.
Proof: <1>1.
:::
