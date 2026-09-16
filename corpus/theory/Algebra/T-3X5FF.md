---
schema: qual/card@1
id: T-3X5FF
kind: theorem
title: 'Sylow''s third theorem: numerical constraints'
classification:
  areas:
  - algebra
  topics:
  - Groups
relations:
- kind: uses
  target: T-OBPSZ
- kind: uses
  target: T-RRK4J
review: reviewed
---

::: {.theorem}
Let $G$ be a finite group and $p$ a prime, write $\abs G=p^a m$ with $p\nmid m$, and let $n_p$ be the number of [[D-7TQ2M|Sylow $p$-subgroups]] of $G$.
Then
$$
n_p\mid m,
\qquad
n_p\equiv1\pmod p,
\qquad
n_p=[G:N_G(P)]
$$
for every Sylow $p$-subgroup $P$, where $N_G(P)$ is the [[D-OZ2RR|normalizer]] of $P$.
:::

::: {.proof}
Let $G$ act by conjugation on the set $\Syl_p(G)$ of Sylow $p$-subgroups.
By [[T-RRK4J|Sylow's second theorem]] the action is transitive, and the stabilizer of $P$ is $N_G(P)$, so the orbit-stabilizer theorem gives $n_p=[G:N_G(P)]$.
Since $P\leq N_G(P)$, $n_p$ divides $[G:P]=m$.

Now restrict the action to $P$.
If $Q\in\Syl_p(G)$ is fixed by $P$, then $P\leq N_G(Q)$, so $P$ and $Q$ are Sylow $p$-subgroups of $N_G(Q)$ in which $Q$ is normal; by Sylow's second theorem in $N_G(Q)$ they are conjugate there, so $P=Q$.
Thus $P$ is the only fixed point, and every other $P$-orbit has size a positive power of $p$, so $n_p\equiv1\pmod p$.
:::
