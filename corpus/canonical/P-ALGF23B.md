---
schema: qual/card@1
id: P-ALGF23B
kind: problem
title: "Groups of order pm with a self-normalizing Sylow p-subgroup"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
solved: false
---

::: problem
Suppose $G$ is a finite group, $p$ is prime, $m$ is an integer, $\gcd(p, m) = 1$, and $|G| = pm$. Suppose $P$ is a Sylow $p$-subgroup and $N_G(P) = P$.

(a) Prove that if $G$ has a subgroup $H$ of order $m$, then
$$H = \{x \in G \mid o(x) \neq p\}.$$
Deduce that in this case, $H$ is a characteristic subgroup.

(b) Suppose $G$ is solvable. Prove that $G$ has a normal subgroup $N$ such that $G/N \cong \mathbb{Z}/\ell\mathbb{Z}$ for some prime $\ell$.

(c) Suppose $G$ is solvable. Prove that $G$ has a normal subgroup of order $m$.

Hint: Use induction on $|G|$, the subgroup $N$ from the previous part, and a Sylow $\ell$-subgroup of $N$ if needed.
:::
