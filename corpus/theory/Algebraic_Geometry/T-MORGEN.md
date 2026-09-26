---
schema: qual/card@1
id: T-MORGEN
kind: theorem
title: Generic smoothness
slogan: 'In characteristic zero, a dominant map from a smooth variety becomes smooth after shrinking the target to a nonempty open.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Generic Behaviour
  - Characteristic Zero
relations:
- kind: uses
  target: D-MORSM
- kind: uses
  target: FE-MORFROB
review: draft
prompts:
- What is generic smoothness?
- Why does generic smoothness need characteristic zero?
---

::: {.theorem title="Generic smoothness"}
Let $\characteristic k = 0$ and let $f : X \to Y$ be a dominant morphism of varieties over $k$ with $X$ smooth.
Then there is a nonempty open $V \subseteq Y$ such that $\ro{f}{f^{-1}(V)} : f^{-1}(V) \to V$ is smooth.
:::

::: {.remark}
The theorem says that bad behaviour of a morphism is confined to a proper closed subset, so one may always shrink the base and assume smoothness.
It is used to define ramification divisors, prove Sard-type statements, and reduce statements about a family to its general member.

Characteristic zero is essential: Frobenius gives a dominant morphism from a smooth variety that is smooth over no nonempty open.
The proof in characteristic zero rests on separability of every field extension of $k(Y)$, which is exactly what fails in characteristic $p$.

The companion statement, generic flatness, has no characteristic-zero restriction: a finite type morphism to an integral Noetherian base is flat over a nonempty open.
:::
