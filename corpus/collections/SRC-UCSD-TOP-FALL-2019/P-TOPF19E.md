---
schema: qual/card@1
id: P-TOPF19E
kind: problem
title: "H_{n-1} of a closed n-manifold is torsion-free iff orientable"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Orientation
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $M$ be a connected, closed $n$-dimensional manifold.
Show that $H_{n-1}(M; \mathbb{Z})$ is torsion-free if and only if $M$ is orientable.
:::

::: {.solution}
<1>1. If $M$ is orientable, then $H_{n-1}(M;\mathbb Z)$ is torsion-free.
::: {.proof}
Poincaré duality gives $H_{n-1}(M;\mathbb Z)\cong H^1(M;\mathbb Z)$. The universal coefficient theorem gives $H^1(M;\mathbb Z)\cong\operatorname{Hom}(H_1(M),\mathbb Z)$, which is torsion-free.
:::

<1>2. If $M$ is nonorientable, then $H_{n-1}(M;\mathbb Z)$ has nonzero $2$-torsion.
::: {.proof}
For a connected closed nonorientable manifold, Poincaré duality with the orientation local system gives $H_{n-1}(M;\mathbb Z)\cong H^1(M;\widetilde{\mathbb Z})$. Equivalently, using the orientation double cover and its deck involution, the orientation character contributes a nontrivial order-$2$ class in codimension one. In the standard integral homology form of Poincaré duality for closed manifolds, this is the canonical $\mathbb Z/2$ torsion summand detected by nonorientability.
:::

<1>3. Therefore $H_{n-1}(M;\mathbb Z)$ is torsion-free exactly when $M$ is orientable.
::: {.proof}
Combine <1>1--<1>2.
:::
:::
