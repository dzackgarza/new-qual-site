---
schema: qual/card@1
id: FE-SCHFFLAT
kind: example
title: Flatness of the affine line over the integers, and faithful flatness as faithfulness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Faithfully Flat Modules
  - Affine Schemes
relations:
- kind: uses
  target: D-DEFFFLAT
review: draft
prompts:
- Show that $\AA^1_\ZZ$ is flat over $\Spec \ZZ$.
- Show that $M$ is faithfully flat if and only if $M$ is flat and $- \tensor_R M$ is a faithful functor.
---

::: {.example title="The affine line over the integers"}
$\AA^1_\ZZ = \Spec \ZZ[x] \to \Spec \ZZ$ is flat, because $\ZZ[x]$ is a free $\ZZ$-module with basis $1, x, x^2, \ldots$, and free modules are flat.
More generally $\AA^n_R \to \Spec R$ is flat for every ring $R$.
:::

::: {.proposition}
An $R$-module $M$ is faithfully flat if and only if $M$ is flat and the functor $- \tensor_R M$ on $R$-modules is faithful.
:::

::: {.remark}
The flatness hypothesis is not redundant: faithfulness of $- \tensor_R M$ alone does not give flatness.
For $R = \ZZ$ and $M = \ZZ \oplus \ZZ/2$, $- \tensor_\ZZ M$ is faithful because $M$ has $\ZZ$ as a direct summand, but $M$ is not flat, since $\ZZ \xrightarrow{2} \ZZ$ tensored over $\ZZ$ with $\ZZ/2$ is the zero map on $\ZZ/2 \neq 0$.
:::
