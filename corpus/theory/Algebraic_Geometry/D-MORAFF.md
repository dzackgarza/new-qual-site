---
schema: qual/card@1
id: D-MORAFF
kind: definition
title: Affine morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Morphisms
  - Relative Spec
  - Morphisms
relations:
- kind: uses
  target: D-MORIMM
review: draft
prompts:
- What is an affine morphism?
- Give examples of affine morphisms, and say what they imply.
---

::: {.definition title="Affine"}
$f : X \to Y$ is **affine** if $f^{-1}(V)$ is affine for every affine open $V \subseteq Y$.
Equivalently, it is enough that this holds for the opens of one affine cover of $Y$.
:::

::: {.remark}
The affine-communication argument shows that the condition can be checked on a single affine cover.
Every affine morphism is separated and quasicompact.

Closed immersions are affine, any morphism of affine schemes is affine, and finite morphisms are affine.
Open immersions are not: $\AA^2 \sm \ts{0} \to \AA^2$ has non-affine source.

The structural statement behind the definition is that an affine morphism to $Y$ is the same data as a quasicoherent sheaf of $\OO_Y$-algebras, via $X = \Spec_Y f_* \OO_X$.
Relative spectra occur in the constructions of Stein factorisation and normalisation.
:::
