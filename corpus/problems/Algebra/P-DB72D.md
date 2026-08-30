---
schema: qual/card@1
id: P-DB72D
kind: problem
title: Abelian groups of order 200
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Determine the number of abelian groups of order $200$ up to isomorphism, and list all isomorphism classes in invariant factor and elementary divisor forms.
:::

::: solution
**Goal:** Apply the Fundamental Theorem of Finite Abelian Groups to classify all abelian groups of order $200 = 2^3 \cdot 5^2$.

<1>1. Prime Factorization of $200$:
    *Proof:*
    <2>1. Factoring $200$ into prime powers:
        $$200 = 8 \times 25 = 2^3 \times 5^2.$$

<1>2. Fundamental Theorem of Finite Abelian Groups:
    *Proof:*
    <2>1. Any finite abelian group $G$ decomposes as a direct product of its Sylow $p$-subgroups:
        $$G \cong G_2 \times G_5$$
        where $|G_2| = 2^3 = 8$ and $|G_5| = 5^2 = 25$.
    <2>2. The number of non-isomorphic abelian groups of order $p^k$ equals the **integer partition function** $p(k)$.
    <2>3. Therefore, the total number of non-isomorphic abelian groups of order $200$ is:
        $$N = p(3) \times p(2).$$

<1>3. Partition Calculations:
    *Proof:*
    <2>1. **Partitions of $3$ ($p(3) = 3$):**
        - $3 \implies \mathbb{Z}_8$
        - $2 + 1 \implies \mathbb{Z}_4 \times \mathbb{Z}_2$
        - $1 + 1 + 1 \implies \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$
    <2>2. **Partitions of $2$ ($p(2) = 2$):**
        - $2 \implies \mathbb{Z}_{25}$
        - $1 + 1 \implies \mathbb{Z}_5 \times \mathbb{Z}_5$
    <2>3. Total number of isomorphism classes:
        $$N = 3 \times 2 = 6.$$

<1>4. Explicit List of the 6 Isomorphism Classes:
    *Proof:*
    <2>1. **Elementary Divisor Form:**
        1. $\mathbb{Z}_8 \times \mathbb{Z}_{25} \cong \mathbb{Z}_{200}$ (Cyclic group).
        2. $\mathbb{Z}_8 \times \mathbb{Z}_5 \times \mathbb{Z}_5 \cong \mathbb{Z}_5 \times \mathbb{Z}_{40}$.
        3. $\mathbb{Z}_4 \times \mathbb{Z}_2 \times \mathbb{Z}_{25} \cong \mathbb{Z}_2 \times \mathbb{Z}_{100}$.
        4. $\mathbb{Z}_4 \times \mathbb{Z}_2 \times \mathbb{Z}_5 \times \mathbb{Z}_5 \cong \mathbb{Z}_{10} \times \mathbb{Z}_{20}$.
        5. $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_{25} \cong \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_{50}$.
        6. $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_5 \times \mathbb{Z}_5 \cong \mathbb{Z}_2 \times \mathbb{Z}_{10} \times \mathbb{Z}_{10}$.

<1>5. Conclusion:
    There are exactly $6$ abelian groups of order $200$ up to isomorphism ($p(3) \times p(2) = 3 \times 2 = 6$). Q.E.D.
:::

::: {.solution}
<1>1. $G$ group.
Proof: Sylow.

<1>2. Q.E.D.
Proof: <1>1.
:::
