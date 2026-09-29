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

::: pf

::: pf-step

Let $p:\widetilde M\to M$ be a connected orientable covering of a connected nonorientable manifold, and let $H=p_*(\pi_1\widetilde M)\le\pi_1(M)$.

::: pf-proof

The number of sheets is the index $[\pi_1(M):H]$.

:::

:::

::: pf-step

The orientation character $w_1:\pi_1(M)\to\mathbb Z/2$ is nontrivial and vanishes on $H$.

::: pf-proof

Nonorientability makes $w_1$ onto. A loop in $\widetilde M$ preserves the chosen orientation there, so its projected loop has trivial orientation character.

:::

:::

::: {.pf-step #s3}

Therefore $H\subseteq\ker w_1$, and
$$[\pi_1(M):H]=2[\ker w_1:H]$$
whenever the latter index is finite.

::: pf-proof

The kernel of the surjective orientation character has index $2$; use multiplicativity of subgroup indices.

:::

:::

::: pf-step

Thus an orientable cover of a nonorientable manifold has even finite degree or infinite degree.

::: pf-proof

This follows directly from step [](#s3){.pf-ref}.

:::

:::

:::

:::
