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
Define $H^i(X, \mcf) \definedas R^i \globsec{X; \wait}(\mcf)$: choose an injective resolution $\mcf \injects \mci^\bullet$, apply $\globsec{X; \wait}$, and take cohomology.
:::

::: {.remark title="Enough injectives"}
The construction requires enough injective objects.
For each $x$, embed the stalk $\mcf_x \injects I_x$ into an injective $\OO_{X,x}\dash$module, let $j^x: \theset{x} \injects X$, and set $\mci \definedas \prod_{x \in X} j^x_* I_x$.
Then $\Hom(\mcg, \mci) = \prod_x \Hom_{\OO_{X,x}}(\mcg_x, I_x)$, a composite of the exact stalk functors with exact $\Hom$ functors, so $\mci$ is injective, and $\mcf \injects \mci$.
:::

::: {.remark title="Acyclic resolutions"}
For every resolution $\mcf\to\mcl^\bullet$ by $\globsec{X;\wait}\dash$acyclic sheaves, $H^i(X,\mcf)\cong H^i(\globsec{X;\mcl^\bullet})$ [@Har10a, Proposition III.1.2A].
Flasque sheaves are acyclic [@Har10a, Proposition III.2.5], and every sheaf embeds in the flasque sheaf $U\mapsto\prod_{x\in U}\mcf_x$ of discontinuous sections.
Hence $H^i$ is effaceable for $i>0$, and $(H^i)_{i\ge0}$ is a universal $\delta\dash$functor [@Har10a, Theorem III.1.3A]: for every $\delta\dash$functor $(T^i)$ from $\Sh(X;\Ab)$ to $\Ab$, every natural transformation $H^0\to T^0$ extends uniquely to a morphism of $\delta\dash$functors $(H^i)\to(T^i)$.
:::
