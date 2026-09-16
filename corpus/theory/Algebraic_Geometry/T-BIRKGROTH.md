---
schema: qual/card@1
id: T-BIRKGROTH
kind: theorem
title: Vector bundles on the projective line split
classification:
  areas:
  - algebraic-geometry
  topics:
  - Vector Bundles
  - Projective Line
  - Twisting Sheaves
relations:
- kind: uses
  target: T-MODVB
- kind: uses
  target: D-CB9XS
review: draft
prompts:
- What is the Birkhoff--Grothendieck theorem?
---

::: {.theorem title="Birkhoff--Grothendieck"}
Let $k$ be a field.
Every locally free sheaf of finite rank on $\PP^1_k$ is isomorphic to $\OO(a_1) \oplus \cdots \oplus \OO(a_r)$ for integers $a_1 \geq \cdots \geq a_r$, and these integers are uniquely determined.
[@Har10a, Exercise V.2.6]
:::

::: {.example}
The tangent bundle of $\PP^2$ restricted to a line $\ell$ is $\OO_\ell(2) \oplus \OO_\ell(1)$: the tangent bundle of the line is the first summand and the normal bundle $\OO_\ell(1)$ the second.
:::
