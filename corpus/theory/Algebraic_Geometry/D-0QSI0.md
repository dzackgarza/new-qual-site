---
schema: qual/card@1
id: D-0QSI0
kind: definition
title: Stalks and germs
classification:
  areas:
  - algebraic-geometry
  topics:
  - Stalks
  - Sheaves
relations:
- kind: uses
  target: D-RCCFY
review: draft
prompts:
- What is the stalk of a sheaf?
- What is a germ?
- Show that the stalk at $p$ of the sheaf of holomorphic functions on an $n$-dimensional complex manifold is the ring $\CC\{z_1, \ldots, z_n\}$ of convergent power series.
- Show that for a real smooth manifold the Taylor map from the stalk of $C^\infty$ functions at $p$ to $\RR[[x_1, \ldots, x_n]]$ has a nonzero kernel.
- For an affine variety $X$ and $p \in X$, show that $\OO_{X,p} \cong A(X)_{\mfm_p}$.
- Give a morphism of sheaves that is surjective on stalks but not on global sections.
---

::: {.definition title="Stalk"}
For a presheaf $\mcf$ on $X$ and a point $p$,
\[
\mcf_p \da \colim_{U \ni p} \mcf(U) ,
\]
the colimit over open neighbourhoods of $p$ ordered by reverse inclusion.
An element of $\mcf_p$ is a \dfn{germ} of a section at $p$: a pair $(U, s)$ with $s \in \mcf(U)$, where two pairs are identified when the sections agree on some smaller neighbourhood.
:::

::: {.remark}
The colimit is filtered, which is what makes the stalk behave: filtered colimits are exact, so passing to stalks is exact, and that is why every diagram-chasing notion for sheaves can be checked there.

A germ remembers a section only near $p$, so it is strictly less information than a section, and strictly more than a value: on the sheaf of smooth functions the germ at $0$ knows every derivative, while the value knows none.
:::
