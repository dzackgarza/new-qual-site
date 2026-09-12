---
schema: qual/card@1
id: D-MORSM
kind: definition
title: Smooth morphisms and relative dimension
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Relative Dimension
  - Flatness
relations:
- kind: uses
  target: D-MORETALE
- kind: uses
  target: D-MORFT
review: draft
prompts:
- What is a smooth morphism?
- What is a smooth morphism of relative dimension n?
- What properties follow from smoothness?
---

::: {.definition title="Smooth"}
$f : X \to Y$ is **smooth** if it is flat, locally of finite presentation, and has geometrically regular fibres.
It is **smooth of relative dimension $n$** if in addition every irreducible component of every fibre has dimension $n$; for a smooth $f$, this is equivalent to $\Omega_{X/Y}$ being locally free of rank $n$.
:::

::: {.remark}
Over a non-perfect field the fibre can be regular and not geometrically regular: $\Spec k[x]/(x^p - t)$ over $k = \FF_p(t)$ is a regular point that becomes non-reduced after base change to $\kbar$, so it is a regular fibre of a non-smooth morphism.

For a smooth morphism of relative dimension $n$, $\Omega_{X/Y}$ is the relative cotangent bundle and $\bigwedge^n\Omega_{X/Y}$ is the relative canonical sheaf. Smooth morphisms are stable under base change and composition.
Smooth morphisms of relative dimension $0$ are étale. A smooth morphism of relative dimension $n$ locally factors as an étale map to $\AA^n_Y$ followed by the projection.
:::
