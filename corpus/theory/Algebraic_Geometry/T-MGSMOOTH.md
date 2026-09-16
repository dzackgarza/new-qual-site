---
schema: qual/card@1
id: T-MGSMOOTH
kind: theorem
title: The moduli stacks of smooth and stable curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Moduli of Curves
  - Deformation Theory
  - Stable Curves
relations:
- kind: uses
  target: T-DEFEXT
- kind: related-to
  target: D-CRVMOD
review: draft
prompts:
- Why is the moduli space of curves $\mathcal{M}_g$ smooth? Is it proper?
---

::: {.theorem title="Deligne--Mumford"}
Let $g \geq 2$.

1. The moduli stack $\mathcal{M}_g$ of smooth projective curves of genus $g$ is a smooth Deligne--Mumford stack over $\Spec \ZZ$ of relative dimension $3g - 3$, with irreducible geometric fibres.

2. $\mathcal{M}_g$ is not proper.

3. It is an open dense substack of the moduli stack $\overline{\mathcal{M}}_g$ of stable curves, which is smooth and proper over $\Spec \ZZ$.
:::

::: {.remark}
The coarse moduli space $M_g$ is irreducible of dimension $3g-3$ but is singular for $g \geq 4$, at curves with extra automorphisms; smoothness is a property of the stack.
:::
