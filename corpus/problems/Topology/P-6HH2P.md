---
schema: qual/card@1
id: P-6HH2P
kind: problem
title: A manifold is orientable if $\pi_1$ has no subgroup of index $2$
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
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $M$ be a connected topological/smooth manifold.
Prove that if the fundamental group $\pi_1(M)$ has no subgroup of index 2, then $M$ is **orientable**.
:::

::: {.solution}

::: pf

::: pf-step

A connected manifold $M$ has an orientation character
\[
w:\pi_1(M,x_0)\longrightarrow\{\pm1\}\cong\mathbb Z/2,
\]
which records whether transport of a local orientation around a loop preserves or reverses it.

:::

::: pf-step

The manifold is orientable if and only if $w$ is trivial.

::: pf-proof

::: pf-step

If $M$ is orientable, a global orientation is preserved along every loop, so $w=1$.

:::

::: pf-step

Conversely, if $w$ is trivial, a choice of local orientation at $x_0$ transports independently of path to every point, producing a global orientation.

:::

:::

:::

::: pf-step

Suppose $M$ were nonorientable. Then $w$ would be nontrivial. Since its codomain has order $2$, nontriviality makes $w$ surjective, and therefore
\[
\ker w\le\pi_1(M)
\]
has index $2$.

:::

::: pf-step

This contradicts the hypothesis that $\pi_1(M)$ has no subgroup of index $2$. Hence $M$ is orientable.

:::

::: pf-step

Equivalently, $\ker w$ is the subgroup corresponding to the connected orientation double cover of a nonorientable manifold.

:::

:::

:::
