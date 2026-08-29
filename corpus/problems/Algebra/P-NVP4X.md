---
schema: qual/card@1
id: P-NVP4X
kind: problem
title: Groups of order 55
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
  date: 2026-08-29
---

::: problem
Discuss groups of order 55.
:::

::: {.solution}
<1>1. $55 = 5 \cdot 11$, so a group $G$ of order $55$ has Sylow $5$- and $11$-subgroups.
Proof: prime factorization.

<1>2. The Sylow $11$-subgroup is normal.
<2>1. $n_{11} \equiv 1 \pmod{11}$ and $n_{11} \mid 5$.
Proof: Sylow's third theorem.
<2>2. Hence $n_{11} = 1$.
Proof: the only divisor of $5$ congruent to $1$ mod $11$ is $1$.
<2>3. Therefore the Sylow $11$-subgroup $P \cong \ZZ/11$ is normal.
Proof: a Sylow subgroup is normal iff it is unique.

<1>3. The Sylow $5$-subgroup $Q \cong \ZZ/5$ satisfies $n_5 \in \{1, 11\}$.
Proof: $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 11$, so $n_5 = 1$ or $11$.

<1>4. $G \cong P \rtimes Q$ (semidirect product).
Proof: $P \trianglelefteq G$ (<1>2), $P \cap Q = 1$ (orders coprime), and $|PQ| = 55 = |G|$, so $G = P \rtimes Q$.

<1>5. Classification.
<2>1. If $n_5 = 1$, then $Q \trianglelefteq G$ and $G \cong \ZZ/5 \times \ZZ/11 \cong \ZZ/55$.
Proof: both Sylow subgroups are normal and intersect trivially, so $G$ is their direct product.
<2>2. If $n_5 = 11$, then $G$ is the nonabelian semidirect product $\ZZ/11 \rtimes \ZZ/5$.
Proof: $\operatorname{Aut}(\ZZ/11) \cong \ZZ/10$ has a unique subgroup of order $5$, giving a nontrivial action of $\ZZ/5$ on $\ZZ/11$; the resulting semidirect product is nonabelian (a Frobenius group of order $55$).

<1>6. Hence there are exactly two groups of order $55$ up to isomorphism: the cyclic group $\ZZ/55$ and the nonabelian group $\ZZ/11 \rtimes \ZZ/5$.
Proof: <1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
