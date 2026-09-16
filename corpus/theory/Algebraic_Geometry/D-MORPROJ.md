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
- Show that $X$ is a projective variety over $k$ if and only if it is an integral closed subscheme of some $\PP^n_k$.
---

::: {.definition title="Projective"}
$f : X \to Y$ is \dfn{projective} if it factors as a closed immersion followed by the projection,
\[
X \injects \PP^N_Y \to Y, \qquad \PP^N_Y \da \fiberprod{\PP^N_\ZZ}{\Spec \ZZ}{Y} ,
\]
for some $N$.
It is **quasi-projective** if it factors as an open immersion into a scheme projective over $Y$.
:::

::: {.remark}
For $Y$ Noetherian, projective implies proper, and this implication carries most of the properness one ever uses.
Its proof is the whole content: closed immersions are proper, properness is stable under composition, and $\PP^N_\ZZ \to \Spec \ZZ$ is universally closed, which is the elimination theorem.
So "projective implies proper" is "the resultant exists", and that is the answer to the follow-up asking where the closedness comes from.

The relative $\Proj$ supplies the examples: for a graded ring $S$ with $S_0 = A$ and $S$ generated in degree one by finitely many elements, $\Proj S \to \Spec A$ is projective.
Blowups are projective for the same reason, and that is why a blowup of a projective variety stays projective.
:::

::: {.example}
A projective variety over an algebraically closed field $k$ is the same as an integral closed subscheme of some $\PP^n_k$, equivalently a closed subscheme that is reduced and irreducible.
An arbitrary closed subscheme of $\PP^n_k$ is a projective $k$-scheme but need not be a variety: $V(x_0^2) \subseteq \PP^1_k$ is a nonreduced point, and $V(x_0 x_1) \subseteq \PP^1_k$ is two points.
:::
