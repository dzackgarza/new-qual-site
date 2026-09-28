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
$f : X \to Y$ is \dfn{affine} if $f^{-1}(V)$ is affine for every affine open $V \subseteq Y$.
Equivalently, it is enough that this holds for the opens of one affine cover of $Y$.
:::

::: {.remark}
The condition may be checked on one affine cover by the affine-communication argument.
Every affine morphism is separated and quasicompact.

Closed immersions are affine, any morphism of affine schemes is affine, and finite morphisms are affine.
An open immersion need not be affine: $\AA^2 \sm \ts{0} \to \AA^2$ has non-affine source.

The functors $(f\colon X\to Y)\mapsto f_*\OO_X$ and $\mathcal A\mapsto\Spec_Y\mathcal A$ are inverse anti-equivalences between affine morphisms to $Y$ and quasicoherent sheaves of $\OO_Y$-algebras; in particular $X \cong \Spec_Y f_* \OO_X$ for $f$ affine.
Relative spectra occur in the constructions of Stein factorisation and normalisation.
:::
