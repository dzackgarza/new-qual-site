---
schema: qual/card@1
id: P-IE52K
kind: problem
title: Sylow theorems, and groups of order 1225
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Abelian Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
a. State the three Sylow theorems.

b. Prove that any group of order 1225 is abelian.

c. Write down exactly one representative in each isomorphism class of abelian groups of order 1225.
:::

::: solution
The Sylow theorems state:

1. If $p^a$ is the largest power of $p$ dividing $|G|$, then $G$ has a subgroup of order $p^a$.
2. Every $p$-subgroup is contained in a Sylow $p$-subgroup, and all Sylow $p$-subgroups are conjugate.
3. The number $n_p$ of Sylow $p$-subgroups satisfies
\[
n_p\equiv1\pmod p,
\qquad
n_p\mid |G|/p^a.
\]

Now
\[
1225=5^2\cdot7^2.
\]
For Sylow $7$-subgroups,
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid25.
\]
The divisors $1,5,25$ leave only $n_7=1$. Similarly
\[
n_5\equiv1\pmod5,
\qquad
n_5\mid49,
\]
and among $1,7,49$ only $1$ is congruent to $1$ modulo $5$. Thus both Sylow subgroups $P_5$ and $P_7$ are normal.

Their intersection is trivial because their orders are coprime. Since both are normal, for $x\in P_5$ and $y\in P_7$ the commutator $[x,y]$ lies in both subgroups, hence is $1$. Therefore
\[
G=P_5\times P_7.
\]
Every group of order $p^2$ is abelian, so both factors are abelian and therefore $G$ is abelian.

The abelian groups of order $1225$ are obtained by choosing one of the two abelian types of order $25$ and independently one of the two types of order $49$. Thus exactly one representative of each isomorphism class is
\[
C_{25}\times C_{49},
\qquad
C_{25}\times C_7\times C_7,
\qquad
C_5\times C_5\times C_{49},
\qquad
C_5\times C_5\times C_7\times C_7.
\]
:::
