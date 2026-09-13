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
- What does smoothness give you for free?
---

::: {.definition title="Smooth"}
$f : X \to Y$ is **smooth** if it is flat, locally of finite presentation, and has geometrically regular fibres.
It is **smooth of relative dimension $n$** if in addition every irreducible component of every fibre has dimension $n$, equivalently $\Omega_{X/Y}$ is locally free of rank $n$ on a flat, locally finitely presented $f$.
:::

::: {.remark}
The definition is three conditions and each is doing separate work, which is exactly what gets asked.
Flatness makes it a family rather than a union of unrelated fibres; finite presentation makes it algebraic; geometric regularity of the fibres is the smoothness itself, and *geometrically* is not decoration.
Over a non-perfect field the fibre can be regular and not geometrically regular: $\Spec k[x]/(x^p - t)$ over $k = \FF_p(t)$ is a regular point that becomes non-reduced after base change to $\kbar$, so it is a regular fibre of a non-smooth morphism.

What smoothness buys is the whole toolkit at once: smooth implies flat, so numerical invariants are constant; $\Omega_{X/Y}$ is locally free, so there is a relative cotangent bundle and a relative canonical sheaf; and smooth morphisms are stable under base change and composition, so the class is closed under the constructions one performs.
Relative dimension $0$ is étale, and smoothness is thus "étale up to $n$ free parameters", which is the statement that a smooth morphism locally factors as an étale map to $\AA^n_Y$.
:::
