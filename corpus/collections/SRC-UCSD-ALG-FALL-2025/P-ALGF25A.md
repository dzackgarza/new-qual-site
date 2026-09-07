---
schema: qual/card@1
id: P-ALGF25A
kind: problem
title: Exactly two groups of order $3 \cdot 5 \cdot 13$ up to isomorphism
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared the statement with Problem 1 on page 2 of the official FA25 algebra exam PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked the Sylow counts, semidirect-product decomposition, and uniqueness of the nontrivial order-three action on the normal cyclic subgroup of order 65.
---

::: problem
Prove that, up to isomorphism, there exist exactly two groups of order $3 \cdot 5 \cdot 13$.
:::

::: {.solution}
<1>1. Every group $G$ of order $3\cdot5\cdot13$ has a normal cyclic subgroup $N$ of order $65$.
::: {.proof}
Let $n_{13}$ and $n_5$ be the numbers of Sylow $13$- and Sylow $5$-subgroups.
The Sylow congruences and divisibilities give
\[
n_{13}\equiv1\pmod{13},\qquad n_{13}\mid15,
\]
and
\[
n_5\equiv1\pmod5,\qquad n_5\mid39.
\]
Among the divisors of $15$, only $1$ is congruent to $1$ modulo $13$, and among the divisors of $39$, only $1$ is congruent to $1$ modulo $5$.
Thus the Sylow subgroups $Q$ of order $13$ and $R$ of order $5$ are both unique and hence normal.

Since $Q\cap R=1$ and both are normal, their commutator subgroup satisfies
\[
[Q,R]\subseteq Q\cap R=1.
\]
Hence $N=QR=Q\times R$ has order $65$.
Both $Q$ and $R$ are cyclic of prime order, so $N\cong C_{13}\times C_5\cong C_{65}$.
It is normal because it is a product of normal subgroups.
:::

<1>2. The group $G$ is a semidirect product $C_{65}\rtimes C_3$.
::: {.proof}
Let $P$ be a Sylow $3$-subgroup of $G$.
Then $|P|=3$, $N\cap P=1$, and $N$ is normal.
Therefore $NP$ is a subgroup and
\[
|NP|=\frac{|N||P|}{|N\cap P|}=65\cdot3=|G|.
\]
Thus $G=NP$ and
\[
G\cong N\rtimes P\cong C_{65}\rtimes C_3.
\]
The isomorphism type is therefore determined by the conjugation homomorphism
\[
\varphi:C_3\longrightarrow\operatorname{Aut}(C_{65}),
\]
up to changing generators of the two cyclic factors.
:::

<1>3. There are exactly two possible actions up to isomorphism: the trivial action and one nontrivial action.
::: {.proof}
By the Chinese remainder theorem,
\[
\operatorname{Aut}(C_{65})
\cong (\mathbb Z/65\mathbb Z)^\times
\cong (\mathbb Z/5\mathbb Z)^\times\times(\mathbb Z/13\mathbb Z)^\times.
\]
The two factors are cyclic of orders $4$ and $12$, respectively.
Consequently the first factor has no nontrivial element of order dividing $3$, while the second has a unique subgroup of order $3$.

Thus the image of $\varphi$ is either trivial or that unique subgroup of order $3$.
In the latter case there are two injective homomorphisms $C_3$ onto this subgroup, but they differ by the automorphism of $C_3$ sending a generator to its inverse.
The resulting semidirect products are therefore isomorphic.
Hence there are at most two isomorphism classes.
:::

<1>4. Both possibilities occur and they are not isomorphic.
::: {.proof}
For the trivial action, the semidirect product is the direct product
\[
C_{65}\times C_3\cong C_{195},
\]
which is abelian.

For the nontrivial action, choose an automorphism of $C_{13}$ of order $3$, extend it trivially across the $C_5$ factor of $C_{65}$, and form $C_{65}\rtimes C_3$.
The action is nontrivial, so the resulting group is nonabelian.
It therefore cannot be isomorphic to $C_{195}$.

Thus exactly two groups of order $3\cdot5\cdot13$ exist up to isomorphism.
:::
:::
