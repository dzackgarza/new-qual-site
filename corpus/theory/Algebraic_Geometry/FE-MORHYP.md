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
The same hyperbola also witnesses failure of universal closedness for $\AA^1$: it is closed in $\AA^1\times\AA^1$ while its projection is not closed.

The repair is Zariski's main theorem: a separated quasi-finite morphism is an open immersion followed by a finite one, and here the finite morphism is the identity of $\AA^1$ and the open immersion is $\GG_m \injects \AA^1$.
Over a locally Noetherian base, finite is exactly proper plus quasi-finite, and the failure above is the failure of properness.
:::
