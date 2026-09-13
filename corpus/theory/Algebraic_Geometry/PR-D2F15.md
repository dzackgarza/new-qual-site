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
Resolution of singularities is a hard theorem in general and a subdivision algorithm here, which is the reason toric varieties are worth an afternoon before an exam: they turn every hard statement in the subject into a finite computation with lattice points.

Two cones to recognise on sight.
The cone on $(0,1)$ and $(1,0)$ is smooth and gives $\AA^2$.
The cone on $(0,1)$ and $(d,-1)$ is not, and gives the cone over the rational normal curve of degree $d$ — for $d = 2$, the quadric cone $V(xy - z^2)$, whose singularity is resolved by inserting the ray $(1,0)$, which is the blowup.

The same dictionary supplies examples on demand for questions asked elsewhere: a normal variety that is not smooth, a Weil divisor that is not Cartier, a class group with torsion.
:::
