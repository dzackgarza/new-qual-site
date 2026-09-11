---
schema: qual/card@1
id: T-MORGEN
kind: theorem
title: Generic smoothness
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
That is how it is used: to define the ramification divisor, to prove Sard-type statements, and to reduce a question about a family to the general member.

Characteristic zero is the hypothesis to flag, and Frobenius is the counterexample: it is a dominant morphism from a smooth variety that is smooth over no nonempty open, because it is nowhere smooth.
The proof in characteristic zero rests on separability of every field extension of $k(Y)$, which is exactly what fails in characteristic $p$.

The companion statement, generic flatness, has no such restriction: a finite type morphism to an integral Noetherian base is flat over a nonempty open.
Distinguishing which half needs characteristic zero is the usual follow-up.
:::
