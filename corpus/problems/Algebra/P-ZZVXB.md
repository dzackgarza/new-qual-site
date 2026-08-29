---
schema: qual/card@1
id: P-ZZVXB
kind: problem
title: Abelian groups of order 9, and groups of order 27
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) Classify all abelian groups of order 9 up to isomorphism. Prove that they are not isomorphic to each other.
(2) Classify all abelian groups of order 27 up to isomorphism, and list the non-abelian groups of order 27.
:::

::: solution
**Goal:** Classify abelian groups of order $p^2$ and $p^3$ (for $p = 3$) using the Fundamental Theorem of Finite Abelian Groups.

<1>1. Classification of Abelian Groups of Order 9 ($p^2$ with $p=3$):
    *Proof:*
    <2>1. By the **Fundamental Theorem of Finite Abelian Groups**, any finite abelian $p$-group is isomorphic to a direct sum of cyclic $p$-power groups corresponding to the integer partitions of the exponent $k$ in $|G| = p^k$.
    <2>2. For $|G| = 9 = 3^2$, the exponent is 2. The integer partitions of 2 are:
        - $2$: corresponding to $\mathbb{Z}_9$ (cyclic group of order 9).
        - $1 + 1$: corresponding to $\mathbb{Z}_3 \times \mathbb{Z}_3$ (elementary abelian group of order 9).
    <2>3. Thus there are exactly **2 isomorphism classes** of abelian groups of order 9:
        $$G \cong \mathbb{Z}_9 \quad \text{or} \quad G \cong \mathbb{Z}_3 \times \mathbb{Z}_3.$$

<1>2. Proof that $\mathbb{Z}_9 \not\cong \mathbb{Z}_3 \times \mathbb{Z}_3$:
    *Proof:*
    <2>1. We compare the element orders / exponents of the two groups:
        - In $\mathbb{Z}_9$, the generator $1$ has order $\operatorname{ord}(1) = 9$. Thus $\mathbb{Z}_9$ contains elements of order 9 (in fact, $\varphi(9) = 6$ elements of order 9).
        - In $\mathbb{Z}_3 \times \mathbb{Z}_3$, every element $(a, b)$ satisfies $3(a, b) = (3a, 3b) = (0, 0)$.
          Thus every non-identity element in $\mathbb{Z}_3 \times \mathbb{Z}_3$ has order 3, and the group has exponent $\exp(\mathbb{Z}_3 \times \mathbb{Z}_3) = 3$.
    <2>2. Since group isomorphism preserves element orders and the exponent of a group, $\mathbb{Z}_9 \not\cong \mathbb{Z}_3 \times \mathbb{Z}_3$.

<1>3. Classification of Abelian Groups of Order 27 ($p^3$ with $p=3$):
    *Proof:*
    <2>1. For $|G| = 27 = 3^3$, the integer partitions of 3 are:
        - $3$: $\mathbb{Z}_{27}$.
        - $2 + 1$: $\mathbb{Z}_9 \times \mathbb{Z}_3$.
        - $1 + 1 + 1$: $\mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_3$.
    <2>2. These three groups are mutually non-isomorphic:
        - $\mathbb{Z}_{27}$ has an element of order 27 (exponent 27).
        - $\mathbb{Z}_9 \times \mathbb{Z}_3$ has maximal element order 9 (exponent 9) and contains $3^2 - 1 = 8$ elements of order dividing 3.
        - $\mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_3$ has maximal element order 3 (exponent 3) and contains $3^3 - 1 = 26$ elements of order 3.

<1>4. Non-Abelian Groups of Order 27:
    *Proof:*
    <2>1. For any odd prime $p$, there are exactly **two non-isomorphic non-abelian groups** of order $p^3$:
        1. **Heisenberg group over $\mathbb{F}_3$ (exponent $p = 3$):**
           $$UT_3(\mathbb{F}_3) = \left\{ \begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} \;\middle|\; a, b, c \in \mathbb{F}_3 \right\} \cong (\mathbb{Z}_3 \times \mathbb{Z}_3) \rtimes \mathbb{Z}_3.$$
        2. **Semidirect product of exponent $p^2 = 9$:**
           $$\mathbb{Z}_9 \rtimes \mathbb{Z}_3 = \langle x, y \mid x^9 = 1, y^3 = 1, y x y^{-1} = x^4 \rangle.$$

<1>5. Conclusion:
    There are 2 abelian groups of order 9 ($\mathbb{Z}_9, \mathbb{Z}_3^2$) and 3 abelian groups of order 27 ($\mathbb{Z}_{27}, \mathbb{Z}_9 \times \mathbb{Z}_3, \mathbb{Z}_3^3$), along with 2 non-abelian groups of order 27. Q.E.D.
:::
