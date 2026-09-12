---
schema: qual/card@1
id: D-MORPROJ
kind: definition
title: Projective and quasi-projective morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Morphisms
  - Proper Morphisms
  - Proj
relations:
- kind: uses
  target: D-MORIMM
- kind: uses
  target: D-8XX95
review: draft
prompts:
- What is a projective morphism?
- Why is a projective morphism proper?
---

::: {.definition title="Projective"}
$f : X \to Y$ is **projective** if it factors as a closed immersion followed by the projection,
\[
X \injects \PP^N_Y \to Y, \qquad \PP^N_Y \da \fiberprod{\PP^N_\ZZ}{\Spec \ZZ}{Y} ,
\]
for some $N$.
It is **quasi-projective** if it factors as an open immersion into a scheme projective over $Y$.
:::

::: {.remark}
Projective morphisms are proper: closed immersions are proper, properness is stable under composition and base change, and $\PP^N_\ZZ \to \Spec \ZZ$ is proper. The universal closedness of projective space follows from homogeneous elimination.

The relative $\Proj$ supplies the examples: for a graded ring $S$ with $S_0 = A$ and $S$ generated in degree one by finitely many elements, $\Proj S \to \Spec A$ is projective.
Blowups are projective for the same reason, and that is why a blowup of a projective variety stays projective.
:::
