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
Let $k$ be a field of characteristic $0$, and let $f\colon X\to Y$ be a dominant morphism of varieties over $k$ with $X$ smooth over $k$.
Then there is a nonempty open subset $V\subseteq Y$ such that
$$
f^{-1}(V)\longrightarrow V
$$
is smooth.
:::

::: {.remark}
Under the hypotheses of the theorem, the nonsmooth locus does not dominate $Y$, so after shrinking the target the morphism is smooth.

Characteristic zero is essential: Frobenius gives a dominant morphism from a smooth variety that is smooth over no nonempty open.
At the generic point, the extension of function fields
$$
k(Y)\subseteq k(X)
$$
is separably generated in characteristic zero. Equivalently, the module of relative differentials has the expected generic rank. Generic freeness and openness of the smooth locus then give the required open subset of $Y$. In characteristic $p$, a dominant extension can be purely inseparable; Frobenius is the basic example.

The companion statement, generic flatness, has no characteristic-zero restriction: a finite type morphism to an integral Noetherian base is flat over a nonempty open.
:::
