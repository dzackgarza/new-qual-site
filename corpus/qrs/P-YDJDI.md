---
schema: qual/card@1
id: P-YDJDI
kind: problem
title: "Let $G$ be a group containing a subgroup $H$ not equal to $G$ of finit\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Let $G$ be a group containing a subgroup $H$ not equal to $G$ of finite index.
Prove that $G$ has a normal subgroup which is contained in every conjugate of $H$ which is of finite index.

> (DZG) A remark: it's not the conjugates that should be finite index here, but rather the normal subgroup.

:::{.solution}
\envlist

- Let $H\leq G$ and define $n\da [G:H]$.
- Write $G/H = \ts{ x_1 H, \cdots, x_n H }$ for the finitely many cosets.
- Let $G$ act on $G/H$ by left translation, so $g\cdot xH \da gxH$..
  Call the action $\psi: G\to \Sym(G/H)$.
- Then $\Stab(xH) = xHx\inv$ is a subgroup conjugate to $H$, and $K\da \ker \psi = \Intersect_{i=1}^n xHx\inv$ is the intersection of all conjugates of $H$.
- Kernels are normal, so $K\normal G$, and $K\subseteq xHx\inv$ for all $x$, meaning $K$ is contained in every conjugate of $H$.
- The index $[G:K]$ is finite since $G/K \cong \im \psi$ by the first isomorphism theorem, and $\# \im \psi \leq \# \Sym(G/H) = \# S_n = n! < \infty$.

:::


