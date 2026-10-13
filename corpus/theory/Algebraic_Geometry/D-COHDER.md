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
Define $H^i(X, \mcf) \coloneqq R^i \globsec{X; \wait}(\mcf)$: choose an injective resolution $\mcf \injects \mci^\bullet$, apply $\globsec{X; \wait}$, and take cohomology.
:::

::: {.remark title="Enough injectives"}
The construction requires enough injective objects.
For each $x$, embed the stalk $\mcf_x$ into an injective abelian group $I_x$, let $j^x: \theset{x} \injects X$, and set $\mci \coloneqq \prod_{x \in X} j^x_* I_x$.
Then $\Hom(\mcg, \mci) \cong \prod_x \Hom_{\ZZ}(\mcg_x, I_x)$. The stalk functors are exact and the functors $\Hom_{\ZZ}(-,I_x)$ are exact, so $\mci$ is injective; the chosen stalk embeddings induce a monomorphism $\mcf \injects \mci$.
:::

::: {.remark title="Acyclic resolutions"}
If $\mcf\to\mca^\bullet$ is a resolution by $\globsec{X;\wait}$-acyclic sheaves, then
$$
H^i(X,\mcf)\cong H^i\bigl(\globsec{X;\mca^\bullet}\bigr).
$$
Flasque sheaves are $\globsec{X;\wait}$-acyclic, so flasque resolutions compute sheaf cohomology.
The functors $(H^i)_{i\geq0}$ form the universal cohomological $\delta$-functor extending global sections. Thus a natural transformation from $H^0$ to the degree-zero term of another cohomological $\delta$-functor extends uniquely to a morphism from $(H^i)$ to that $\delta$-functor. Additional hypotheses are required for such a comparison to be an isomorphism in positive degrees.
:::
