---
schema: qual/card@1
id: T-MORSTEIN
kind: theorem
title: Stein factorisation
slogan: 'A proper morphism factors into a connected-fibre contraction followed by a finite morphism.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Stein Factorisation
  - Proper Morphisms
  - Connected Fibres
relations:
- kind: uses
  target: D-MORAFF
- kind: uses
  target: T-MORZMT
review: draft
prompts:
- State the Stein factorisation.
- What is it used for?
---

::: {.theorem title="Stein factorisation"}
Let $f : X \to Y$ be a proper morphism of Noetherian schemes.
Then $f$ factors as
$$
X \mapsvia{g} Y' \coloneqq \Spec_Y f_* \OO_X \mapsvia{h} Y
$$
with $g$ proper with connected fibres and $g_* \OO_X = \OO_{Y'}$, and $h$ finite.
:::

::: {.remark}
The factorization isolates a connected-fibre morphism followed by a finite morphism.

$f_* \OO_X$ is a coherent $\OO_Y$-module because $f$ is proper and $Y$ is Noetherian. Hence it is a finite $\OO_Y$-algebra, so $Y'\to Y$ is finite.
Since $g$ is surjective with connected fibres, the connected components of the fibre $X_y$ are the fibres of $g$ over the points of the finite set $h^{-1}(y)$, so they correspond bijectively to the points of $h^{-1}(y)$.
The number of connected components is therefore at most the scheme-theoretic length
$$
\dim_{\kappa(y)}\bigl(f_*\OO_X\tensor_{\OO_Y}\kappa(y)\bigr)
$$
of the finite fibre of $h$. It can be strictly smaller: for $f=h\colon\AA^1_\CC\to\AA^1_\CC$, $t\mapsto t^2$, the fibre over $0$ is the single point $\Spec\CC[t]/(t^2)$ of length $2$.

The immediate corollary is the connectedness statement in Zariski's main theorem: if $f_* \OO_X = \OO_Y$ then $Y' = Y$, so $h$ is the identity and the fibres of $f$ are connected.
For a proper birational morphism of varieties with $Y$ normal, $h$ is finite and birational, hence an isomorphism by normality of $Y$; so $f_*\OO_X=\OO_Y$ and the fibres of $f$ are connected.
:::
