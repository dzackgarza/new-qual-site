---
schema: qual/card@1
id: T-MGSMOOTH
kind: theorem
title: The moduli stacks of smooth and stable curves
slogan: '$\mathcal M_g$ is smooth of dimension $3g-3$ but not proper; adding stable curves gives the smooth proper compactification $\overline{\mathcal M}_g$.'
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
The smoothness statement concerns the Deligne--Mumford stack. Étale-locally near a curve $C$, the coarse moduli space is a quotient of the smooth deformation space of $C$ by the finite group $\Aut(C)$. Thus the coarse space can have quotient singularities even though the stack is smooth; whether the quotient is singular depends on the actual representation of $\Aut(C)$ on the deformation space, not only on the fact that $\Aut(C)$ is nontrivial.
:::
