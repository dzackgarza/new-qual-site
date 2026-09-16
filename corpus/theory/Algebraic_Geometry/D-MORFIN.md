---
schema: qual/card@1
id: D-MORFIN
kind: definition
title: Finite morphisms, and finite against finite type
classification:
  areas:
  - algebraic-geometry
  topics:
  - Finite Morphisms
  - Finite Type Morphisms
  - Branched Covers
relations:
- kind: uses
  target: D-MORAFF
- kind: related-to
  target: D-MORFT
review: draft
prompts:
- What is a finite morphism?
- How does finite differ from finite type?
- What are the consequences of a morphism being finite?
---

::: {.definition title="Finite"}
$f : X \to Y$ is \dfn{finite} if $Y$ has an affine cover by $\Spec B_i$ with $f^{-1}(\Spec B_i) = \Spec A_i$ affine and $A_i$ a $B_i$-module of finite type ([[D-DEFFGMOD]]).
:::

::: {.proposition title="Maps of proper curves"}
Let $C$ and $C'$ be irreducible curves proper over a field $k$.
Every $k$-morphism $f: C \to C'$ is proper, so $f(C)$ is an irreducible closed subset of $C'$: $f$ is either constant with value a closed point or surjective.
If $C$ is nonsingular, $C'$ is integral and $f$ is surjective, then $f$ is finite and $k(C')\subseteq k(C)$ is a finite extension.
[@Har10a, Corollary II.4.8, Proposition II.6.8]
:::

::: {.remark}
The one-line distinction is the one the examiner wants: finitely generated as a module is strictly stronger than finitely generated as an algebra.
$k[x]$ has one algebra generator over $k$ and infinite rank as a $k$-module, so $\AA^1_k \to \Spec k$ is of finite type and not finite.
Hence finite implies finite type and never conversely.

Finite morphisms are affine, proper, closed, surjective onto their image, and have finite fibres, and the fibres have a length that a flat hypothesis makes constant.
They are the branched covers of the subject: a nonconstant morphism of smooth projective curves is finite, which is why every statement about such a map is a statement about a finite extension of function fields.
Closedness is the going up theorem read on spectra, which is the standard follow-up.
:::
