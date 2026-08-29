---
schema: qual/card@1
id: P-BL7XW
kind: problem
title: Groups of order $p^3$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Classify all groups of order $p^3$ for $p$ prime up to isomorphism.
:::

::: solution
**Goal:** Classify all isomorphism classes of groups of order $p^3$. There are always 5 isomorphism classes: 3 abelian and 2 non-abelian.

<1>1. The Abelian Groups of order $p^3$:
    *Proof:*
    <2>1. By the Fundamental Theorem of Finitely Generated Abelian Groups, abelian groups of order $p^3$ correspond to integer partitions of 3:
        - $3$: $\mathbb{Z}_{p^3}$ (cyclic of order $p^3$).
        - $2 + 1$: $\mathbb{Z}_{p^2} \times \mathbb{Z}_p$.
        - $1 + 1 + 1$: $\mathbb{Z}_p \times \mathbb{Z}_p \times \mathbb{Z}_p = \mathbb{Z}_p^3$ (elementary abelian).
    <2>2. These three groups are pairwise non-isomorphic.

<1>2. Properties of Non-Abelian Groups of order $p^3$:
    *Proof:*
    <2>1. Let $G$ be non-abelian with $|G| = p^3$.
    <2>2. By the class equation for $p$-groups, $|Z(G)| \ge p$.
    <2>3. Since $G$ is non-abelian, $G/Z(G)$ cannot be cyclic. This forces $|Z(G)| = p$ and $G/Z(G) \cong \mathbb{Z}_p \times \mathbb{Z}_p$.
    <2>4. The commutator subgroup satisfies $[G, G] = Z(G) \cong \mathbb{Z}_p$, so $G$ is nilpotent of class 2.
    <2>5. The exponent $\exp(G)$ can only be $p$ or $p^2$ (it cannot be $p^3$ since $G$ is non-abelian).

<1>3. Case $p = 2$ ($|G| = 8$):
    *Proof:*
    <2>1. The two non-abelian groups of order 8 are:
        - **Dihedral group $D_4$:** $\langle r, s \mid r^4 = 1, s^2 = 1, srs = r^{-1} \rangle$. It has 5 elements of order 2 and 2 elements of order 4.
        - **Quaternion group $Q_8$:** $\langle i, j, k \mid i^2 = j^2 = k^2 = ijk = -1 \rangle$. It has a unique element $-1$ of order 2 and 6 elements of order 4.
    <2>2. $D_4 \not\cong Q_8$ since $Q_8$ has only one element of order 2 while $D_4$ has five.

<1>4. Case $p > 2$ (odd prime):
    *Proof:*
    <2>1. **Group of exponent $p^2$:** The semidirect product $\mathbb{Z}_{p^2} \rtimes \mathbb{Z}_p$ where $\mathbb{Z}_p$ acts on $\mathbb{Z}_{p^2}$ by $x \mapsto x^{1+p}$:
        $$G_1 = \langle a, b \mid a^{p^2} = 1, \, b^p = 1, \, bab^{-1} = a^{1+p} \rangle.$$
        This group has exponent $p^2$.
    <2>2. **Group of exponent $p$ (Heisenberg group over $\mathbb{F}_p$):**
        $$G_2 = \left\{ \begin{pmatrix} 1 & a & c \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix} \;\middle|\; a, b, c \in \mathbb{F}_p \right\} \cong (\mathbb{Z}_p \times \mathbb{Z}_p) \rtimes \mathbb{Z}_p.$$
        Presentation: $\langle a, b, c \mid a^p = b^p = c^p = 1, \, [a, b] = c, \, [a, c] = [b, c] = 1 \rangle$. Every non-identity element has order $p$, so $\exp(G_2) = p$.
    <2>3. $G_1 \not\cong G_2$ because their exponents are $p^2$ and $p$, respectively.
    <2>4. Any other non-abelian semidirect product is isomorphic to one of these two.

<1>5. Summary of Classification:
    For any prime $p$, there are exactly 5 groups of order $p^3$ up to isomorphism:
    - 3 abelian: $\mathbb{Z}_{p^3}$, $\mathbb{Z}_{p^2} \times \mathbb{Z}_p$, $\mathbb{Z}_p^3$.
    - 2 non-abelian:
        - For $p = 2$: $D_4$ and $Q_8$.
        - For $p > 2$: $\mathbb{Z}_{p^2} \rtimes \mathbb{Z}_p$ (exponent $p^2$) and the Heisenberg group $\operatorname{Heis}(\mathbb{F}_p)$ (exponent $p$).

<1>6. Conclusion:
    There are precisely 5 groups of order $p^3$ for every prime $p$. Q.E.D.
:::
