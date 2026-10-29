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
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "Source text: if M^orientable -> M^non-orientable is a k-fold cover then k is even or infinity. Connectedness of both spaces, which the solution uses, is now stated."
---

::: {.problem}
Let $M$ be a connected non-orientable manifold and let $\pi:\widetilde M\to M$ be a $k$-fold covering map with $\widetilde M$ connected and orientable. Show that $k$ is even or $k=\infty$.
:::

::: {.solution}

::: pf

::: pf-step

Let $H=\pi_*(\pi_1\widetilde M)\le\pi_1(M)$.

::: pf-proof

The number of sheets is the index $[\pi_1(M):H]$.

:::

:::

::: pf-step

The orientation character $w_1:\pi_1(M)\to\ZZ/2$ is nontrivial and vanishes on $H$.

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
