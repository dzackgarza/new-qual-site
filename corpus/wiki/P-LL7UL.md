---
schema: qual/card@1
id: P-LL7UL
kind: problem
title: "Let $K$ be a Galois extension of a field $F$ with $[K: F] = 2015$. Prove that $K$\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Let $K$ be a Galois extension of a field $F$ with $[K: F] = 2015$.
Prove that $K$ is an extension by radicals of the field $F$.
:::

:::{.concept}
\envlist

- If $N \normal G$ is a normal subgroup and $H\leq G$ is any subgroup containing $N$, then $N$ is normal in $H$ since $hNh\inv \subseteq gNg\inv = N$.
- In characteristic zero, a polynomial is solvable by radicals iff its Galois group is a solvable group.
:::

:::{.solution}
Let $G\da \Gal(K/F)$, then it suffices to show that $G$ is always a solvable group, i.e. any group of order $n=2015$ is solvable.
Factor $2015 = 5\cdot 13\cdot 31$ -- this is a $pqr$ factorization, and in fact any group with exactly 3 prime factors (so $n$ is squarefree in particular) will be solvable.
Let $p=5, q=13, r=31$ so that $p<q<r$.
We aim to construct a composition series whose successive quotients are simple groups.
Applying Sylow 3 yields

- $n_p \divides qr, n_p \equiv 1 \mod p \implies n_5 \divides 13\cdot 31 = 403$ and $n_5\equiv 1 \mod 5$.
  - So $n_5 \in \ts{1, 13, 31}$ by divisibility and imposing the congruence forces $n_5\in \ts{1, 31}$ since $13\not\equiv 1 \mod 5$.
- $n_q \divides pr, n_q \equiv 1 \mod q \implies n_{13} \divides 5\cdot 31 = 155$ and $n_{13}\equiv 1 \mod 13$.
  - So $n_{13} \in \ts{1,5,31}$ by divisibility and the congruence imposes $n_{13}\in \ts{1}$ since $5,31 \not\equiv 1\mod 13$.
  In particular, there is one Sylow 13-subgroup which is normal.
- $n_r \divides pq, n_r \equiv 1 \mod r \implies n_{31} \divides 5 \cdot 13 = 65$ and $n_{31}\equiv 1 \mod 31$.
  - So $n_{31}\in \ts{1,5,13}$ by divisibility and the congruence imposes $n_{31}\in \ts{1}$ since $5,13 \not\equiv 1\mod 31$.
  In particular, the one Sylow 31-subgroup is normal.

Let $H_{13}, H_{31}$ be the two normal subgroups of $G$.
Taking the quotient $\tilde G \da G/H_{31}$ yields a group of order $5\cdot 13$, and a similar argument as above using the Sylow theorems shows that $\tilde G$ has a normal subgroup of order 13.
By the subgroup correspondence theorem, this yields a normal subgroup $N_1\normal G$ containing $H_{31}$ which has order $13\cdot 31$.
So define $N_2 \da H_{31}$ to obtain
\[
G \trianglerighteq N_1 \trianglerighteq N_2 \da H_{31} \trianglerighteq 0
.\]
Since the quotients $N_i/N_{i+1}$ have prime power order, they are cyclic and thus simple.
We know $N_1$ is normal in $G$ since it came from extending a normal group in a quotient, and we know $N_2$ is normal in $N_1$ since it was normal in all of $G$.
So $G$ is solvable.
:::
