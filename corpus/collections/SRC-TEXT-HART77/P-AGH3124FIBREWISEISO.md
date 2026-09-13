---
schema: qual/card@1
id: P-AGH3124FIBREWISEISO
kind: problem
title: Fibrewise isomorphic invertible sheaves differ by a pullback
classification:
  areas:
  - algebraic-geometry
  topics:
  - Semicontinuity
  - Invertible Sheaves
  - Flat Morphisms
  - Picard Group
relations: []
review: draft
---

::: problem
Let $Y$ be an integral scheme of finite type over an algebraically closed field $k$.
Let $f: X \to Y$ be a flat projective morphism whose fibres are all integral schemes.
Let $\mcl, \mcm$ be invertible sheaves on $X$, and assume for each $y \in Y$ that $\mcl_y \cong \mcm_y$ on the fibre $X_y$.

Show that there is an invertible sheaf $\mcn$ on $Y$ such that $\mcl \cong \mcm \tensor f^* \mcn$.

Hint: use the results of this section to show that $f_*(\mcl \tensor \mcm^{-1})$ is locally free of rank $1$ on $Y$.
:::
