---
schema: qual/card@1
id: P-HGRO33
kind: problem
title: Subgroups of a group of order 30
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
What can be said about the subgroups of a group of order $30$?
:::

::: {.solution}
<1>1. Sylow subgroups and normality of $P_3$ and $P_5$:
<2>1. Let $G$ be a group of order $|G| = 30 = 2 \cdot 3 \cdot 5$.
By the Sylow Theorems:
- The number $n_5$ of Sylow 5-subgroups satisfies $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 6 \implies n_5 \in \{1, 6\}$.
- The number $n_3$ of Sylow 3-subgroups satisfies $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 10 \implies n_3 \in \{1, 10\}$.
::: {.proof}
Sylow Theorems.
:::
<2>2. If $n_5 = 6$ and $n_3 = 10$, the Sylow 5-subgroups intersect trivially and contain $6 \cdot (5 - 1) = 24$ elements of order 5.
The Sylow 3-subgroups contain $10 \cdot (3 - 1) = 20$ elements of order 3.
The identity and these elements would total at least $24 + 20 + 1 = 45 > 30$ elements, a contradiction.
Thus at least one of $n_5 = 1$ or $n_3 = 1$ must hold.
::: {.proof}
counting elements of distinct prime orders.
:::
<2>3. If $n_5 = 1$, the unique Sylow 5-subgroup $P_5 \triangleleft G$.
Then $H = P_3 P_5$ is a subgroup of order 15.
Every group of order $15 = 3 \times 5$ is cyclic, so $H \cong \mathbb{Z}_{15}$.
Since $[G : H] = 2$, $H \triangleleft G$.
Because $P_3$ is the unique Sylow 3-subgroup of the cyclic group $H$, $P_3$ is characteristic in $H$, hence normal in $G$ ($P_3 \triangleleft G \implies n_3 = 1$).
Symmetrically, $n_3 = 1 \implies n_5 = 1$.
::: {.proof}
characteristic subgroups of normal subgroups are normal.
:::

<1>2. Subgroup structure of $G$:
<2>1. **Subgroups of orders 3, 5, 15:**
In every group of order 30:
- There is a unique, normal subgroup of order 3 ($P_3 \cong \mathbb{Z}_3$).
- There is a unique, normal subgroup of order 5 ($P_5 \cong \mathbb{Z}_5$).
- There is a unique, normal subgroup of order 15 ($H = P_3 P_5 \cong \mathbb{Z}_{15}$).
::: {.proof}
<1>1.
:::
<2>2. **Semidirect product structure:**
Since $[G : H] = 2$, by the Schur–Zassenhaus Theorem (or picking any involution $t \in G \setminus H$), $G \cong \mathbb{Z}_{15} \rtimes_\theta \mathbb{Z}_2$, where $\theta: \mathbb{Z}_2 \to \operatorname{Aut}(\mathbb{Z}_{15}) \cong \mathbb{Z}_2 \times \mathbb{Z}_4$.
There are exactly 4 isomorphism classes:
1. $\mathbb{Z}_{30}$ (cyclic / abelian).
2. $D_{15}$ (dihedral group of order 30).
3. $D_3 \times \mathbb{Z}_5 \cong S_3 \times \mathbb{Z}_5$.
4. $D_5 \times \mathbb{Z}_3$.
::: {.proof}
classification of homomorphisms $\mathbb{Z}_2 \to (\mathbb{Z}/15\mathbb{Z})^\times \cong \mathbb{Z}_2 \times \mathbb{Z}_4$.
:::
<2>3. **Subgroups of orders 2, 6, 10:**
- Subgroups of order 2 (Sylow 2-subgroups): $n_2 = 1$ for $\mathbb{Z}_{30}$, $n_2 = 15$ for $D_{15}$, $n_2 = 3$ for $S_3 \times \mathbb{Z}_5$, and $n_2 = 5$ for $D_5 \times \mathbb{Z}_3$.
- Subgroups of order 6: formed by $P_3 P_2$, isomorphic to $\mathbb{Z}_6$ or $S_3$.
- Subgroups of order 10: formed by $P_5 P_2$, isomorphic to $\mathbb{Z}_{10}$ or $D_5$.
Every group of order 30 has subgroups of all possible divisor orders $\{1, 2, 3, 5, 6, 10, 15, 30\}$.
::: {.proof}
Correspondence Theorem and semidirect product actions.
:::

<1>3. Conclusion:
Every group of order 30 contains a unique normal subgroup of order 15 ($H \cong \mathbb{Z}_{15}$), unique normal Sylow 3- and 5-subgroups, has subgroups of all divisor orders, and belongs to one of the four semidirect product families $\mathbb{Z}_{15} \rtimes \mathbb{Z}_2$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
