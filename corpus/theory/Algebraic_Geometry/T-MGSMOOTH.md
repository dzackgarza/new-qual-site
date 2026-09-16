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

::: {.proof}
1. *Smoothness:* at a curve $C$ the deformation space is $H^1(C, T_C)$, of dimension $3g-3$, and obstructions lie in $H^2(C, T_C) = 0$ because $C$ is a curve; for a stable curve the same holds with $\operatorname{Ext}^1(\Omega_C, \OO_C)$ and $\operatorname{Ext}^2(\Omega_C, \OO_C) = 0$.
2. *Deligne--Mumford:* $H^0(C, T_C) = 0$ for $g \geq 2$, so automorphism groups are finite and unramified.
3. *Failure of properness:* take a pencil of plane quartics, of genus $3$, whose general member is smooth and whose special member $C_0$ has a single node.
   Over a small punctured disc around $C_0$ the monodromy on $H^1$ of the fibres is a Dehn twist, of infinite order by the Picard--Lefschetz formula, so no finite base change of the family extends to a family of smooth curves; by the valuative criterion $\mathcal{M}_3$ is not proper, and the same construction works for every $g \geq 2$.
4. *Properness of $\overline{\mathcal{M}}_g$:* the stable reduction theorem says every family of stable curves over the generic point of a discrete valuation ring extends, after a finite base change, to a family of stable curves over the ring, uniquely.
:::

::: {.remark}
The coarse moduli space $M_g$ is irreducible of dimension $3g-3$ but is singular for $g \geq 4$, at curves with extra automorphisms; smoothness is a property of the stack.
:::
