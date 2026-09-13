---
schema: qual/card@1
id: D-COHFLQ
kind: definition
title: Flasque sheaves and acyclicity
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Flasque Sheaves
  - Acyclic Resolutions
relations:
- kind: uses
  target: D-COHDER
review: draft
prompts:
- What is a flasque sheaf?
- Why are flasque sheaves acyclic?
- Give an example of a flasque sheaf.
---

::: {.definition}
$\mcf$ is *flasque* if every restriction $\mcf(U) \to \mcf(V)$, for $V \subseteq U$, is surjective.
:::

::: {.proposition}
Injective implies flasque, flasque implies $\globsec{X;\wait}\dash$acyclic, and for a short exact sequence with flasque left term the sequence of global sections stays exact.
:::

::: {.remark}
The chain to remember is *injective $\Rightarrow$ flasque $\Rightarrow$ acyclic*, and only the middle class is ever exhibited by hand.
Examples: the Godement sheaf $\prod_x j^x_* \mcf_x$ of discontinuous sections; any constant sheaf on an irreducible space; and $\tilde{I}$ on $\Spec A$ for $I$ an injective $A\dash$module, which is the input to affine vanishing.

The proof of acyclicity is induction on the sequence $0 \to \mcf \to \mci \to \mcg \to 0$ with $\mci$ injective: flasqueness of $\mcf$ forces $\mcg$ flasque and the global sections exact, so $H^1(\mcf) = 0$ and the higher groups shift down.
:::
