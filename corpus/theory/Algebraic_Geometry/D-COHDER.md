---
schema: qual/card@1
id: D-COHDER
kind: definition
title: Sheaf cohomology as the derived functor of global sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Derived Functors
  - Injective Resolutions
relations:
- kind: related-to
  target: D-PTIW0
review: draft
prompts:
- Define sheaf cohomology.
- Why does the category of sheaves of abelian groups have enough injectives?
- Which resolutions compute cohomology?
---

::: {.definition}
For $X$ a topological space, $\globsec{X; \wait}: \Sh(X; \Ab) \to \Ab$ is left exact.
Define $H^i(X, \mcf) \da R^i \globsec{X; \wait}(\mcf)$: choose an injective resolution $\mcf \injects \mci^\bullet$, apply $\globsec{X; \wait}$, and take cohomology.
:::

::: {.remark title="Enough injectives"}
The construction needs injective resolutions to exist, and the argument is worth being able to give.
For each $x$, embed the stalk $\mcf_x \injects I_x$ into an injective $\OO_{X,x}\dash$module, let $j^x: \ts{x} \injects X$, and set $\mci \da \prod_{x \in X} j^x_* I_x$.
Then $\Hom(\mcg, \mci) = \prod_x \Hom_{\OO_{X,x}}(\mcg_x, I_x)$, a composite of the exact stalk functors with exact $\Hom$ functors, so $\mci$ is injective, and $\mcf \injects \mci$.
:::

::: {.remark title="What you actually compute with"}
Nobody computes with injectives.
Cohomology can be computed from *any* resolution by $\globsec{X;\wait}\dash$acyclic sheaves, and the useful supply is flasque sheaves.
The formal reason the answer does not depend on the choice is the $\delta\dash$functor characterisation: $(H^i)$ is a universal $\delta\dash$functor because each $H^{i>0}$ is effaceable, every sheaf embedding into a flasque (hence acyclic) one.
Any other $\delta\dash$functor agreeing in degree $0$ therefore maps to it uniquely, which is how Čech cohomology and derived functor cohomology get compared at all.
:::
