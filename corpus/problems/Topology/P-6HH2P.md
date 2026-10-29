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
Prove that if the fundamental group $\pi_1(M)$ has no subgroup of index 2, then $M$ is orientable.
:::

::: {.solution}

Fix $x_0\in M$. Transporting a local orientation at $x_0$ around a loop either preserves or reverses it, and this depends only on the homotopy class of the loop. This defines the orientation character, a homomorphism $w:\pi_1(M,x_0)\to\{\pm1\}\cong\ZZ/2$.

::: pf

::: {.pf-step #trivial-character}

If $w$ is trivial, then $M$ is orientable.

::: pf-proof

Transport a local orientation at $x_0$ along paths to every point of $M$. Two paths from $x_0$ to $x$ differ by a loop at $x_0$, which preserves the orientation since $w$ is trivial, so the result is independent of the path. Transport along paths is locally constant, so this is a global orientation.

:::

:::

::: pf-step

$M$ is orientable.

::: pf-proof

Otherwise $w$ is nontrivial by step [](#trivial-character){.pf-ref}. Since its codomain has order $2$, $w$ is surjective, and $\ker w$ is a subgroup of $\pi_1(M,x_0)$ of index $2$, contradicting the hypothesis.

:::

:::

:::

:::
