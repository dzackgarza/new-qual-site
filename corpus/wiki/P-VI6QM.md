---
schema: qual/card@1
id: P-VI6QM
kind: problem
title: "Let $G$ be a group of order 105 and let $P, Q, R$ be Sylow 3, 5, 7 sub\u2026"
classification:
  areas:
  - algebra
  topics:
  - sylow-theory
  - normal-subgroups
  - cyclic-groups
relations: []
review: draft
solved: true
---
Let $G$ be a group of order 105 and let $P, Q, R$ be Sylow 3, 5, 7 subgroups respectively.

a.
Prove that at least one of $Q$ and $R$ is normal in $G$.

b.
Prove that $G$ has a cyclic subgroup of order 35.

c.
Prove that both $Q$ and $R$ are normal in $G$.

d.
Prove that if $P$ is normal in $G$ then $G$ is cyclic.

:::{.concept}
\envlist

- The $pqr$ theorem.
- Sylow 3: $\abs{G} = p^n m$ implies $n_p \divides m$ and $n_p \cong 1 \mod p$.

- **Theorem**: If $H, K \leq G$ and any of the following conditions hold, $HK$ is a subgroup:
  - $H\normal G$ (wlog)
  - $[H, K] = 1$
  - $H \leq N_G(K)$ 

- **Theorem**: For a positive integer $n$, all groups of order $n$ are cyclic $\iff n$ is
squarefree and, for each pair of distinct primes $p$ and $q$ dividing $n$, $q - 1 \neq 0 \mod p$.

- **Theorem:** 
\[
A_i\normal G, \quad G = A_1 \cdots A_k,\quad A_k \intersect \prod_{i\neq k} A_i = \emptyset \implies G = \prod A_i
.\]

- The intersection of subgroups is a again a subgroup.
- Any subgroups of coprime order intersect trivially?

:::

:::{.solution}
\envlist

:::{.proof title="of 1"}
\envlist

- We have 

- $n_3 \divides 5\cdot 7, \quad n_3 \cong 1 \mod 3 \implies n_3 \in \theset{1, 5, 7, 35} \setminus \theset{5, 35}$
- $n_5 \divides 3\cdot 7, \quad n_5 \cong 1 \mod 5 \implies n_5 \in \theset{1, 3, 7, 21}\setminus \theset{3, 7}$
- $n_7 \divides 3\cdot 5, \quad n_7 \cong 1 \mod 7 \implies n_7 \in \theset{1, 3, 5, 15}\setminus\theset{3, 5}$

- Thus
\[
n_3 \in \theset{1, 7} \quad n_5 \in \theset{1, 21} \quad n_7 \in \theset{1, 15}
.\]

- Toward a contradiction, if $n_5\neq 1$ and $n_7 \neq 1$, then 
\[
\abs{\syl(5) \union \syl(7)} = (5-1)n_5 + (7-1)n_7 + 1 
&= 4(21) + 6(15) = 174 > 105 \text{ elements}
\]
  using the fact that Sylow $p\dash$subgroups for distinct primes $p$ intersect trivially (?).

:::

:::{.proof title="of 2"}
\envlist
- By (a), either $Q$ or $R$ is normal.
- Thus $QR \leq G$ is a subgroup, and it has order $\abs{Q} \cdot \abs{R} = 5\cdot 7 = 35$.
- By the $pqr$ theorem, since $5$ does not divide $7-1=6$, $QR$ is cyclic.

:::

:::{.remark}
Part (b) not finished!
:::

:::{.proof title="of 3"}
\envlist

- We want to show $Q, R\normal G$, so we proceed by showing $\textbf{not }\qty{n_5 = 21 \text{ or } n_7 = 15}$, which is equivalent to $\qty{n_5 = 1 \text{ and } n_7 = 1}$ by the previous restrictions.

- Note that we can write
\[
G = \theset{\text{elements of order } n} \disjoint \theset{\text{elements of order not } n}
.\]
  for any $n$, so we count for $n=5, 7$:

  - Elements in $QR$ of order **not** equal to 5: $\abs{QR - Q\theset{\id} + \theset{\id}} = 35 - 5 + 1 = 31$
  - Elements in $QR$ of order **not** equal to 7: $\abs{QR - \theset{\id}R + \theset{\id}} = 35 - 7 + 1 = 29$

- Since $QR \leq G$, we have

  - Elements in $G$ of order **not** equal to 5 $\geq 31$.
  - Elements in $G$ of order **not** equal to 7 $\geq 29$.

- Now both cases lead to contradictions:

  - $n_5 = 21$:
\[
\abs{G}  &= \abs{\theset{\text{elements of order } 5} \disjoint \theset{\text{elements of order not } 5}} \\
&\geq n_5(5-1) + 31 = 21(4) + 31 = 115 > 105 = \abs{G}
.\]

  - $n_7 = 15$:
\[
\abs{G}  &= \abs{\theset{\text{elements of order } 7} \disjoint \theset{\text{elements of order not } 7}} \\
&\geq n_7(7-1) + 29 = 15(6) + 29 = 119 > 105 = \abs{G}
.\]

:::

:::{.proof title="of 4"}
Suppose $P$ is normal and recall $\abs{P} = 3, \abs{Q} = 5, \abs{R} = 7$.

- $P\intersect QR = \theset{e}$ since $(3, 35) = 1$ 
- $R\intersect PQ = \theset{e}$ since $(5, 21) = 1$ 
- $Q\intersect RP = \theset{e}$ since $(7, 15) = 1$ 

We also have $PQR = G$ since $\abs{PQR} = \abs{G}$ (???).

We thus have an internal direct product 
\[
G \cong P\cross Q \cross R \cong \ZZ_3 \cross \ZZ_5 \cross \ZZ_7 \cong \ZZ_{105}
.\]
by the Chinese Remainder Theorem, which is cyclic.

:::

:::

