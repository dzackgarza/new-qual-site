---
schema: qual/card@1
id: P-AGH272LINPROJ
kind: problem
title: Morphisms from the same linear system differ by a linear projection
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Invertible Sheaves
  - Linear Projection
relations: []
review: draft
---

::: problem
Let $X$ be a scheme over a field $k$.
Let $\mcl$ be an invertible sheaf on $X$, and let $\ts{s_0, \ldots, s_n}$ and $\ts{t_0, \ldots, t_m}$ be two sets of sections of $\mcl$ which generate the same subspace $V \subseteq \Gamma(X, \mcl)$, and which generate the sheaf $\mcl$ at every point.
Suppose $n \leq m$.

Show that the corresponding morphisms $\varphi: X \to \PP^n_k$ and $\psi: X \to \PP^m_k$ differ by a suitable linear projection $\PP^m - L \to \PP^n$ and an automorphism of $\PP^n$, where $L$ is a linear subspace of $\PP^m$ of dimension $m - n - 1$.
:::
