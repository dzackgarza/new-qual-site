---
schema: qual/card@1
id: P-HGRO3
kind: problem
title: Subgroups of abelian groups of orders $35$ and $27$
classification:
  areas: [algebra]
  topics: [Abelian Groups]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard group-theory oral-question extraction immediately following the questions on abelian groups of orders 35 and 27.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Determine the subgroups of the abelian groups of orders $35$ and $27$.
:::

::: solution
By the classification theorem, the abelian group of order $35$ is
$C_{35}$, while the abelian groups of order $27$ are
\[
C_{27},\qquad C_9\times C_3,\qquad C_3^3.
\]

<1>1. The subgroups of $C_{35}$ are the unique cyclic subgroups of orders
$1,5,7,$ and $35$.
::: proof
A cyclic group has exactly one subgroup for every positive divisor of its
order, and the divisors of $35$ are $1,5,7,35$.
:::

<1>2. The subgroups of $C_{27}$ are the unique cyclic subgroups of orders
$1,3,9,$ and $27$.
::: proof
Apply the same divisor classification for subgroups of a cyclic group.
:::

<1>3. The group $C_9\times C_3$ has four subgroups of order $3$ and four
subgroups of order $9$; besides these it has only the trivial subgroup and the
whole group.
::: proof
Write $G=C_9\times C_3$. Its $3$-torsion subgroup
\[
G[3]=\{x\in G:3x=0\}\cong C_3^2
\]
has four one-dimensional $\mathbf F_3$-subspaces, hence exactly four subgroups
of order $3$.

There are $27-|G[3]|=18$ elements of order $9$. Each cyclic subgroup of order
$9$ has $\varphi(9)=6$ generators, so $G$ has exactly $18/6=3$ cyclic
subgroups of order $9$. The subgroup $G[3]\cong C_3^2$ is one additional,
noncyclic subgroup of order $9$. Thus there are four subgroups of order $9$.

By Lagrange's theorem every subgroup order divides $27$, so the listed
subgroups, together with $0$ and $G$, exhaust all possibilities.
:::

<1>4. The subgroups of $C_3^3$ are precisely its vector subspaces over
$\mathbf F_3$: one subgroup of order $1$, thirteen of order $3$, thirteen of
order $9$, and one of order $27$.
::: proof
View $V=C_3^3$ as a three-dimensional vector space over $\mathbf F_3$.
Its group subgroups are exactly its linear subspaces. The number of
one-dimensional subspaces is
\[
\frac{3^3-1}{3-1}=13.
\]
By duality, or by the Gaussian binomial coefficient
$\binom31_3=\binom32_3$, there are also thirteen two-dimensional subspaces.
The zero subspace and $V$ itself are unique.
:::
:::
