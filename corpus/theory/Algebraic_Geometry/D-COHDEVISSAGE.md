---
schema: qual/card@1
id: D-COHDEVISSAGE
kind: definition
title: Dévissage of coherent sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coherent Sheaves
  - Dévissage
  - Noetherian Induction
relations:
- kind: related-to
  target: T-MODRES
review: draft
prompts:
- What is dévissage?
---

::: {.proposition title="Filtration of a coherent sheaf"}
Let $X$ be a Noetherian scheme and $\mcf$ a coherent $\OO_X$-module.
There is a filtration $0 = \mcf_0 \subseteq \mcf_1 \subseteq \cdots \subseteq \mcf_m = \mcf$ by coherent subsheaves such that for each $j$ there are an integral closed subscheme $i_j \colon Z_j \hookrightarrow X$ and a nonzero coherent ideal sheaf $\mathcal{I}_j \subseteq \OO_{Z_j}$ with $\mcf_j / \mcf_{j-1} \cong i_{j*} \mathcal{I}_j$.
:::

::: {.definition title="Dévissage"}
\dfn{Dévissage} is the reduction of a statement about all coherent sheaves on a Noetherian scheme to the sheaves $i_* \mathcal{I}$ of the proposition.
If a property $P$ of coherent sheaves holds for an extension whenever it holds for the subsheaf and the quotient, and holds for $i_* \mathcal{I}$ for every integral closed subscheme $i \colon Z \hookrightarrow X$ and nonzero coherent ideal $\mathcal{I} \subseteq \OO_Z$, then $P$ holds for every coherent sheaf, by induction along the filtration.
:::

::: {.example}
Grothendieck's proof that $R^i f_* \mcf$ is coherent for $f$ proper and $\mcf$ coherent uses dévissage together with Noetherian induction on the support: it reduces to sheaves on an integral scheme, where Chow's lemma reduces the proper case to the projective case.
:::
