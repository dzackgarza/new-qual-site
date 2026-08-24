---
schema: qual/card@1
id: P-MBHKT
kind: problem
title: Groups of order 18
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
---

::: problem
Classify all groups of order 18 up to isomorphism.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $G$ be a group of order $18 = 2 \cdot 3^2$.
By Sylow's theorem:

- The number $n_3$ of Sylow 3-subgroups satisfies $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 2$, so $n_3 = 1$.

- Let $P$ be the unique Sylow 3-subgroup of $G$.
  Then $P \normal G$, and $\abs P = 9$.

- Since every group of order $p^2$ is abelian, $P \cong \ZZ_9$ or $P \cong \ZZ_3 \times \ZZ_3$.

- Let $Q = \langle y \rangle \cong \ZZ_2$ be a Sylow 2-subgroup.
  Since $P \normal G$ and $P \cap Q = \{1\}$, $G \cong P \rtimes_\theta \ZZ_2$, where $\theta: \ZZ_2 \to \Aut(P)$.

**Case 1: $P \cong \ZZ_9$.** Here $\Aut(\ZZ_9) \cong \ZZ_9^\times \cong \ZZ_6$, which has a unique element of order 2: the inversion automorphism $x \mapsto x^{-1}$.

- If $\theta$ is trivial: $G \cong \ZZ_9 \times \ZZ_2 \cong \ZZ_{18}$.

- If $\theta(y)$ is inversion ($y x y^{-1} = x^{-1}$): $G \cong D_{18}$ (the dihedral group of order 18).

**Case 2: $P \cong \ZZ_3 \times \ZZ_3$.** Here $\Aut(\ZZ_3 \times \ZZ_3) \cong \GL_2(\FF_3)$.
Up to conjugacy in $\GL_2(\FF_3)$, there are two elements of order 2:

1. Trivial map: $G \cong \ZZ_3 \times \ZZ_3 \times \ZZ_2 \cong \ZZ_3 \times \ZZ_6$.

2. Inversion on both coordinates (scalar $-I = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$): $y v y^{-1} = -v$ for all $v \in P$.
   This gives $G \cong (\ZZ_3 \times \ZZ_3) \rtimes \ZZ_2$, which is isomorphic to the generalized dihedral group $D_9 \times \ZZ_3$ or $(\ZZ_3 \times \ZZ_3) \rtimes_{-1} \ZZ_2$.

3. Reflection (e.g. $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$): $y$ inverts one $\ZZ_3$ factor and centralizes the other.
   This gives $G \cong (\ZZ_3 \rtimes_{-1} \ZZ_2) \times \ZZ_3 \cong S_3 \times \ZZ_3$.

Thus, up to isomorphism, there are **5 groups of order 18**:

1. $\ZZ_{18}$ (abelian)

2. $\ZZ_3 \times \ZZ_6$ (abelian)

3. $D_{18}$

4. $S_3 \times \ZZ_3$

5. $(\ZZ_3 \times \ZZ_3) \rtimes_{-1} \ZZ_2$
:::
