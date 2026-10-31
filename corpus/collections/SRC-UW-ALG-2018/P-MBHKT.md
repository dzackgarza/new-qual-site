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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Classify all groups of order 18 up to isomorphism.
:::

::: {.solution}
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

**Case 2: $P \cong \ZZ_3 \times \ZZ_3$.** Here $\Aut(\ZZ_3 \times \ZZ_3) \cong \GL_2(\FF_3)$, and $\theta(y)$ is an element $A$ with $A^2 = I$.
Such an $A$ is diagonalizable over $\FF_3$ with eigenvalues in $\{1,-1\}$ (its minimal polynomial divides $t^2-1=(t-1)(t+1)$, which has distinct roots), so up to conjugacy in $\GL_2(\FF_3)$ there are three choices.
Conjugate choices of $\theta(y)$ give isomorphic semidirect products.

1. $A = I$: $G \cong \ZZ_3 \times \ZZ_3 \times \ZZ_2 \cong \ZZ_3 \times \ZZ_6$.

2. $A = -I$: $y v y^{-1} = -v$ for all $v \in P$.
This gives the generalized dihedral group $G \cong (\ZZ_3 \times \ZZ_3) \rtimes_{-1} \ZZ_2$.

3. $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$: $y$ centralizes one $\ZZ_3$ factor and inverts the other.
This gives $G \cong \ZZ_3 \times (\ZZ_3 \rtimes_{-1} \ZZ_2) \cong \ZZ_3 \times S_3$.

**The five groups are pairwise nonisomorphic.**
$\ZZ_{18}$ and $\ZZ_3 \times \ZZ_6$ are the abelian ones, and they differ because only $\ZZ_{18}$ is cyclic.
Among the three nonabelian groups, the Sylow 3-subgroup is $\ZZ_9$ only for $D_{18}$.
The centre of $\ZZ_3 \times S_3$ is $\ZZ_3 \times 1$, which is nontrivial, whereas $(\ZZ_3 \times \ZZ_3) \rtimes_{-1} \ZZ_2$ has trivial centre: an element $vy$ with $v \in P$ does not commute with any $w \in P$ with $w \ne -w$, that is $w \ne 0$, and a nonzero $v \in P$ does not commute with $y$.

Thus, up to isomorphism, there are **5 groups of order 18**:

1. $\ZZ_{18}$ (abelian)

2. $\ZZ_3 \times \ZZ_6$ (abelian)

3. $D_{18}$

4. $\ZZ_3 \times S_3$

5. $(\ZZ_3 \times \ZZ_3) \rtimes_{-1} \ZZ_2$
:::
