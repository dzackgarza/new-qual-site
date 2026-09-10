---
schema: qual/card@1
id: P-AMD-VRJDJBSV
kind: problem
title: $\mathbb{R}^3\setminus S^1\simeq S^1\vee S^2$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
relations: []
review: draft
---

::: {.problem}
Show that $\mathbb{R}^3 - S^1 \simeq S^1 \vee S^2$.
:::

::: {.solution}
<1>1. Let $C\subset\mathbb R^3$ be the standard embedded circle and let $N(C)$ be a closed tubular neighborhood. Then
$$
\mathbb R^3\setminus C\simeq \mathbb R^3\setminus\operatorname{int}N(C).
$$
::: {.proof}
Inside the tubular neighborhood $N(C)\cong S^1\times D^2$, radially push each nonzero normal vector in $D^2\setminus\{0\}$ to the boundary circle. Extend this deformation by the identity outside $N(C)$. This gives a deformation retraction of the complement of the core $C=S^1\times\{0\}$ onto the exterior of the open tubular neighborhood.
:::

<1>2. After one-point compactifying $\mathbb R^3$ to $S^3$, the exterior $S^3\setminus\operatorname{int}N(C)$ of the unknot is a solid torus $S^1\times D^2$, and the point at infinity lies in its interior. Hence
$$
\mathbb R^3\setminus\operatorname{int}N(C)\cong (S^1\times D^2)\setminus\{p\}
$$
for an interior point $p$.
::: {.proof}
The complement in $S^3$ of a tubular neighborhood of the unknot is again a solid torus. Passing from $S^3$ back to $\mathbb R^3$ removes the point at infinity, which is disjoint from $N(C)$ and therefore lies in the complementary solid torus.
:::

<1>3. A solid torus with one interior point removed has homotopy type $S^1\vee S^2$.
::: {.proof}
Remove a small open $3$-ball about $p$. The resulting compact manifold is a solid torus with an additional spherical boundary component and deformation-retracts onto a spine obtained from the usual core circle of the solid torus together with that boundary sphere, joined at one point by an arc. Contracting the joining arc gives the wedge $S^1\vee S^2$.
:::

<1>4. Therefore
$$
\boxed{\mathbb R^3\setminus S^1\simeq S^1\vee S^2}.
$$
::: {.proof}
Combine <1>1--<1>3.
:::
:::
