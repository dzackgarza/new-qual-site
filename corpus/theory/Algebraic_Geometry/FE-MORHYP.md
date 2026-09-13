---
schema: qual/card@1
id: FE-MORHYP
kind: example
title: The hyperbola projection is quasi-finite and not finite
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasi-finite Morphisms
  - Finite Morphisms
  - Counterexamples
relations:
- kind: uses
  target: D-MORQF
review: draft
prompts:
- Give a morphism with finite fibres that is not finite.
- Give an example of a non-closed morphism.
---

::: {.example}
Let $X = V(xy - 1) \subseteq \AA^2_k$ and let $f : X \to \AA^1_k$ be the projection to $x$.
Then $X \cong \GG_m$, every fibre is a single reduced point or empty, so $f$ is quasi-finite, and the image is $\AA^1 \sm \ts{0}$, which is not closed.
A finite morphism is closed, so $f$ is not finite, and one sees it on rings: $k[x] \to k[x, x^{-1}]$ is of finite type and not module-finite.
:::

::: {.remark}
This is the same example that shows $\AA^1$ is not universally closed, viewed from the other side: the hyperbola is a closed subscheme of $\fiberprod{\AA^1}{k}{\AA^1}$ whose image under the projection is not closed.
One example, two standard follow-ups, so it is worth being able to produce it on demand.

The repair is Zariski's main theorem: a separated quasi-finite morphism is an open immersion followed by a finite one, and here the finite morphism is the identity of $\AA^1$ and the open immersion is $\GG_m \injects \AA^1$.
Over a locally Noetherian base, finite is exactly proper plus quasi-finite, and the failure above is the failure of properness.
:::
