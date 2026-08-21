---
schema: qual/card@1
id: P-GAAX7
kind: problem
title: Derived subgroup equals the centre for nonabelian groups of order $p^3$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Commutators
  - Centralizers and Normalizers
relations: []
review: draft
solved: false
---

::: problem
Since $G$ is a $p\dash$group, it has a nontrivial center.
Since $p$ is prime and $Z(G)$ is a subgroup, this forces $\size Z(G) \in \theset{p, p^2}$, where $p^3$ is ruled out because this would make $G$ abelian.

Supposing that $\size Z(G) = p^2$,we would have $[G: Z(G)] = p$, and since $Z(G) \normal G$, we can take the quotient and $\size\left(G/Z(G)\right) = p$.
But this means $G/Z(G)$ is cyclic, which implies that $G$ is abelian, a contradiction.

So we must have $\size Z(G) = p$, and $\size\left(G/Z(G)\right) = p^2$.

But any group of $p^2$ is abelian, and we can characterize $G' \definedas [G, G]$ in the following way:

> $G' \leq G$ is the unique subgroup of $G$ such that if $N \normal G$ and $G/N$ is abelian, then $N \leq G'$.

We can thus conclude that $G' \leq Z(G)$.
It can not be the case that $G' = \theset{e}$, since this would make $G$ abelian.
This forces $G' = Z(G)$ as desired.
$\qed$
:::
