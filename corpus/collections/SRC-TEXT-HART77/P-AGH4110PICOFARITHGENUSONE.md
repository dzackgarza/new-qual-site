---
schema: qual/card@1
id: P-AGH4110PICOFARITHGENUSONE
kind: problem
title: $\Pic X$ is in bijection with $X_{\reg}$ when $p_a(X)=1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Riemann-Roch
relations: []
review: draft
---

::: problem
Let $X$ be an integral projective scheme of dimension 1 over $k$, which is locally complete intersection, and has $p_a=1$.
Fix a point $P_0 \in X_{\reg}$.
Imitate (1.3.7) to show that the map $P \mapsto \mcl(P-P_0)$ gives a one-to-one correspondence between the points of $X_{\reg}$ and the elements of the group $\Pic X$.

This generalizes (II, 6.11.4) and (II, Ex.
6.7).
:::

::: {.remark}
Erratum: the target group is $\Pic^0 X$, not $\Pic X$.
The sheaf $\mcl(P-P_0)$ has degree $0$, so the map $P \mapsto \mcl(P-P_0)$ lands in the subgroup $\Pic^0 X$ of invertible sheaves of degree $0$, and the one-to-one correspondence is between the points of $X_{\reg}$ and $\Pic^0 X$ [@Har10a, Exercise IV.1.10].
:::
