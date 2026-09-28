---
schema: qual/card@1
id: P-D6JY5
kind: problem
title: Orientable covers of non-orientable manifolds have even or infinite degree
classification:
  areas:
  - topology
  topics:
  - Orientation
  - Covering Spaces
  - Manifolds
relations: []
review: draft
---

::: {.problem}
- Show that if $M^\text{orientable} \mapsvia{\pi_k} M^\text{non-orientable}$ is a $k\dash$fold cover, then $k$ is even or $\infty$.
:::

::: {.solution}
<1>1. Let $p:\widetilde M\to M$ be a connected orientable covering of a connected nonorientable manifold, and let $H=p_*(\pi_1\widetilde M)\le\pi_1(M)$.
::: {.proof}
The number of sheets is the index $[\pi_1(M):H]$.
:::

<1>2. The orientation character $w_1:\pi_1(M)\to\mathbb Z/2$ is nontrivial and vanishes on $H$.
::: {.proof}
Nonorientability makes $w_1$ onto. A loop in $\widetilde M$ preserves the chosen orientation there, so its projected loop has trivial orientation character.
:::

<1>3. Therefore $H\subseteq\ker w_1$, and
$$[\pi_1(M):H]=2[\ker w_1:H]$$
whenever the latter index is finite.
::: {.proof}
The kernel of the surjective orientation character has index $2$; use multiplicativity of subgroup indices.
:::

<1>4. Thus an orientable cover of a nonorientable manifold has even finite degree or infinite degree.
::: {.proof}
This follows directly from <1>3.
:::
:::
