---
schema: qual/card@1
id: P-U7G2X
kind: problem
title: "Let $M$ be a closed, connected, oriented 4-manifold such that $H_2(M; \\ZZ)$\u2026"
classification:
  areas:
  - topology
  topics:
  - euler-characteristic
  - covering-spaces
  - group-actions
  - manifolds
relations: []
review: draft
solved: true
---

Let $M$ be a closed, connected, oriented 4-manifold such that $H_2(M; \ZZ)$ has rank 1. Show that there is not a free $\ZZ_2$ action on $M$.

::: {.solution}
Useful facts:

- $X \surjects_{\times p} Y$ induces $\chi(X) = p\chi(Y)$

- Moral: always try a simple Euler characteristic argument first!

We know that $H_*(M) = [\ZZ, A, \ZZ \times G, A, \ZZ]$ for some group $A$ and some torsion group $G$.
Letting $n=\mathrm{rank}(A)$ and taking the Euler characteristic, we have $\chi(M) = (1)1 + (-1)n + (1)1 + (-1)n + (1)1 = 3-2n$.
Note that this is odd for any $n$.

However, a free action of $\ZZ_2 \actson M$ would produce a double covering $M \surjects_{\times 2} M/\ZZ_2$, and multiplicativity of Euler characteristics would force $\chi(M) = 2 \chi(M/\ZZ_2)$ and thus $3-2n = 2k$ for some integer $k$.
This would require $3-2n$ to be even, so we have a contradiction.
:::
