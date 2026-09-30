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
\[
X \mapsvia{g} Y' \definedas \Spec_Y f_* \OO_X \mapsvia{h} Y
\]
with $g$ proper with connected fibres and $g_* \OO_X = \OO_{Y'}$, and $h$ finite.
:::

::: {.remark}
The factorisation separates the two ways a proper morphism can fail to be an isomorphism: $g$ contracts connected fibres, while $h$ is finite.
Thus a proper morphism factors into a contraction followed by a finite cover.

$f_* \OO_X$ is a coherent sheaf of $\OO_Y$-algebras because $f$ is proper, and it is finite because coherent, which is where properness enters; this is why there is no Stein factorisation for a general morphism.
Since $g$ is surjective with connected fibres, the connected components of the fibre $X_y$ are the fibres of $g$ over the points of the finite set $h^{-1}(y)$, so they correspond bijectively to the points of $h^{-1}(y)$.
This count is at most the degree of $h$ over $y$, the length $\dim_{\kappa(y)} (f_* \OO_X \otimes \kappa(y))$, and can be smaller: for $f = h \colon \AA^1_\CC \to \AA^1_\CC$, $t \mapsto t^2$, which is finite with $g = \id$, the fibre over $0$ is the single point $\Spec \CC[t]/(t^2)$ of length $2$.

The immediate corollary is the connectedness statement in Zariski's main theorem: if $f_* \OO_X = \OO_Y$ then $Y' = Y$, so $h$ is the identity and the fibres of $f$ are connected.
In the other direction, for a proper morphism of varieties with $Y$ normal and $f$ birational, the Stein factorisation is what proves the fibres connected without a separate argument.
:::
