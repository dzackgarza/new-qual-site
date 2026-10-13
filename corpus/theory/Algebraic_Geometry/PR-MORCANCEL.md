---
schema: qual/card@1
id: PR-MORCANCEL
kind: proposition
title: The cancellation theorem for properties of morphisms
slogan: "A base-change-stable compositional property cancels through a morphism once that morphism's diagonal has the property."
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms
  - Base Change
  - Diagonal Morphism
relations:
- kind: uses
  target: D-MORLOCAL
- kind: uses
  target: D-T2J3Q
- kind: related-to
  target: PR-MORBC
review: draft
prompts:
- If $\rho \circ \pi$ has a property $P$ stable under base change and composition, when does $\pi$ have $P$?
- Why is a morphism between proper $k$-schemes proper?
---

::: {.proposition title="Cancellation"}
Let $P$ be a class of morphisms of schemes stable under base change and composition ([[D-MORLOCAL]]). Let $\pi \colon X \to Y$ and $\rho \colon Y \to Z$ be morphisms and $\tau = \rho \circ \pi$.
If $\tau \in P$ and the diagonal $\delta_\rho \colon Y \to Y \times_Z Y$ is in $P$, then $\pi \in P$.
:::

::: {.proof}
Let
$$
p_2\colon X\times_ZY\longrightarrow Y
$$
be the second projection. It is the base change of $\tau\colon X\to Z$ along $\rho\colon Y\to Z$, so $p_2\in P$.

The graph
$$
\Gamma_\pi\colon X\longrightarrow X\times_ZY,
\qquad
x\longmapsto(x,\pi(x)),
$$
is the base change of $\delta_\rho$ along
$$
(\pi\circ p_1,p_2)\colon X\times_ZY\longrightarrow Y\times_ZY.
$$
Hence $\Gamma_\pi\in P$. Since
$$
\pi=p_2\circ\Gamma_\pi,
$$
stability under composition gives $\pi\in P$.
:::

::: {.corollary}
Let $P$ be stable under base change and composition, and $\rho \circ \pi \in P$.

1. If $P$ contains all closed immersions and $\rho$ is separated, then $\pi \in P$ ([[P-AGH248PROPSTAB]], part (e)).

2. If $P$ contains all quasicompact morphisms and $\rho$ is quasi-separated, then $\pi \in P$.
:::

::: {.example}
Proper morphisms are stable under base change and composition and contain the closed immersions.
If $X$ and $Y$ are proper over a field $k$, with structure morphisms $\tau \colon X \to \Spec k$ and $\rho \colon Y \to \Spec k$, then every $k$-morphism $\pi \colon X \to Y$ is proper, by part 1 of the corollary, since $\rho$ is separated.
:::
