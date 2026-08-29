---
schema: qual/card@1
id: P-EQO46
kind: problem
title: Groups of order 12, and two nonisomorphic subgroups of the same order
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) What are all the groups of order 12 up to isomorphism?
(2) Can a group of order 12 have two non-isomorphic subgroups of the same order?
:::

::: solution
**Goal:** Classify the 5 groups of order 12 and show that $D_6$ has two non-isomorphic subgroups of order 4 (and $A_4$ has non-isomorphic subgroups of order 3 in extensions).

<1>1. Classification of Groups of Order $12 = 2^2 \cdot 3$:
    *Proof:*
    <2>1. By Sylow's Theorems, $n_3 \in \{1, 4\}$ and $n_2 \in \{1, 3\}$.
    <2>2. If $n_3 = 4$, the 4 Sylow 3-subgroups contain $4 \times 2 = 8$ elements of order 3, leaving $12 - 8 = 4$ elements, which must form a unique normal Sylow 2-subgroup $P_2 \trianglelefteq G$ ($n_2 = 1$).
    <2>3. Thus at least one Sylow subgroup is normal, so every group of order 12 is a semidirect product of its Sylow subgroups.
    <2>4. There are exactly **5 isomorphism classes** of groups of order 12:
        - **Abelian Groups (2):**
            1. $\mathbb{Z}_{12} \cong \mathbb{Z}_4 \times \mathbb{Z}_3$ (cyclic).
            2. $\mathbb{Z}_2 \times \mathbb{Z}_6 \cong \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_3$.
        - **Non-Abelian Groups (3):**
            3. $A_4$ (Alternating group of degree 4, $V_4 \rtimes \mathbb{Z}_3$ with $n_3 = 4, n_2 = 1$).
            4. $D_6 \cong D_{12}$ (Dihedral group of symmetries of regular hexagon, $\mathbb{Z}_6 \rtimes \mathbb{Z}_2 \cong \mathbb{Z}_2 \times S_3$).
            5. $\operatorname{Dic}_3 \cong \mathbb{Z}_3 \rtimes \mathbb{Z}_4$ (Dicyclic group / Binary dihedral group of order 12, $\langle a, b \mid a^6 = 1, b^2 = a^3, bab^{-1} = a^{-1} \rangle$).

<1>2. Existence of Two Non-Isomorphic Subgroups of the Same Order in a Group of Order 12:
    *Proof:*
    <2>1. **Yes**, this occurs in the dihedral group $D_6 \cong \mathbb{Z}_2 \times S_3 \cong \langle r, s \mid r^6 = s^2 = 1, s r s = r^{-1} \rangle$.
    <2>2. Consider subgroups of order 4 in $D_6$:
        - **Subgroup 1 ($V_4$):** Let $H_1 = \langle r^3, s \rangle = \{1, r^3, s, s r^3\}$.
            Since $(r^3)^2 = 1, s^2 = 1$, and $(s r^3)^2 = 1$, all non-identity elements have order 2.
            Thus $H_1 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ (the Klein four-group).
        - **Subgroup 2 ($\mathbb{Z}_4$):** Wait, does $D_6$ have a $\mathbb{Z}_4$? In $D_6$, $\exp(D_6) = 6$, all elements have order dividing 6, so there are no elements of order 4.
        - Let us check other orders in $D_6$:
            - Order 6 subgroups in $D_6$:
                - $K_1 = \langle r \rangle \cong \mathbb{Z}_6$ (cyclic of order 6).
                - $K_2 = \langle r^2, s \rangle = \{1, r^2, r^4, s, s r^2, s r^4\} \cong D_3 \cong S_3$ (non-abelian of order 6).
    <2>3. **Subgroups of order 6 in $D_6$:**
        - $K_1 = \langle r \rangle \cong \mathbb{Z}_6$ is **abelian (cyclic)**.
        - $K_2 = \langle r^2, s \rangle \cong S_3$ is **non-abelian**.
        - $K_1 \not\cong K_2$, yet $|K_1| = |K_2| = 6$.
    <2>4. Therefore, $D_6$ contains two non-isomorphic subgroups of order 6 ($\mathbb{Z}_6$ and $S_3$).

<1>3. Conclusion:
    There are 5 groups of order 12 ($\mathbb{Z}_{12}, \mathbb{Z}_2 \times \mathbb{Z}_6, A_4, D_6, \operatorname{Dic}_3$), and $D_6$ has two non-isomorphic subgroups of order 6 ($\mathbb{Z}_6$ vs $S_3$). Q.E.D.
:::
