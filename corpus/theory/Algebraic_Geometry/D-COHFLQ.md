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
- What is a flabby sheaf?
---

::: {.definition}
$\mcf$ is \dfn{flasque}, or \dfn{flabby}, if every restriction $\mcf(U) \to \mcf(V)$, for $V \subseteq U$, is surjective.
:::

::: {.proposition}
Injective implies flasque, flasque implies $\globsec{X;\wait}\dash$acyclic, and for a short exact sequence with flasque left term the sequence of global sections stays exact.
:::

::: {.remark}
Every sheaf $\mcf$ embeds in the flasque sheaf $\prod_x j^x_* \mcf_x$ of discontinuous sections, so every sheaf has a resolution by flasque, hence $\globsec{X;\wait}\dash$acyclic, sheaves.

The proof of acyclicity is induction on the sequence $0 \to \mcf \to \mci \to \mcg \to 0$ with $\mci$ injective: flasqueness of $\mcf$ forces $\mcg$ flasque and the global sections exact, so $H^1(\mcf) = 0$ and the higher groups shift down.
:::

::: {.example title="Flasque sheaves"}
The following sheaves are flasque:

- the sheaf $\prod_x j^x_* \mcf_x$ of discontinuous sections of any sheaf $\mcf$, where $j^x\colon\theset{x}\injects X$;

- every constant sheaf on an irreducible topological space [@Har10a, Exercise II.1.16];

- the sheaf $\tilde{I}$ on $\Spec A$ for a Noetherian ring $A$ and an injective $A\dash$module $I$ [@Har10a, Proposition III.3.4]; Hartshorne uses this to prove that $H^i(\Spec A,\tilde M)=0$ for $i>0$.
:::
