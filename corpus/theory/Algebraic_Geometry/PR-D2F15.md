---
schema: qual/card@1
id: PR-D2F15
kind: proposition
title: Smoothness and resolution, read off the fan
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Resolution of Singularities
  - Fans
relations:
- kind: uses
  target: PR-O8V3I
review: draft
prompts:
- When is a toric variety smooth?
- How do you resolve a toric singularity?
---

::: {.proposition}
$U_\sigma$ is smooth exactly when the minimal generators of $\sigma$ are part of a $\ZZ$-basis of $N$; such a cone is called **smooth**. $X_\Sigma$ is smooth exactly when every cone of $\Sigma$ is.
It is $\QQ$-factorial exactly when every cone is simplicial.
:::

::: {.proposition title="Toric resolution"}
Every fan admits a refinement into smooth cones, obtained by repeatedly subdividing along lattice points, and the induced morphism $X_{\Sigma'} \to X_\Sigma$ is a proper birational resolution.
:::

::: {.remark}
Resolution of singularities is a hard theorem in general; here it is a subdivision algorithm: repeatedly inserting lattice points refines every fan into smooth cones, and the induced morphism is a proper birational resolution. The dictionary turns each hard statement into a finite computation with lattice points, and supplies examples on demand for questions asked elsewhere: a normal variety that is not smooth, a Weil divisor that is not Cartier, a class group with torsion.
:::
