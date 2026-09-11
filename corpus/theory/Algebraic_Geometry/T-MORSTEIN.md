---
schema: qual/card@1
id: T-MORSTEIN
kind: theorem
title: Stein factorisation
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
X \mapsvia{g} Y' \da \Spec_Y f_* \OO_X \mapsvia{h} Y
\]
with $g$ proper with connected fibres and $g_* \OO_X = \OO_{Y'}$, and $h$ finite.
:::

::: {.remark}
The factorisation separates the two ways a proper morphism can fail to be an isomorphism: $g$ contracts things, and $h$ is a finite cover.
So any proper morphism is a contraction followed by a branched cover, and that is the sentence to give when asked what it is for.

$f_* \OO_X$ is a coherent sheaf of $\OO_Y$-algebras because $f$ is proper, and it is finite because coherent, which is where properness enters; this is why there is no Stein factorisation for a general morphism.
The number of connected components of the fibre $X_y$ is the degree of $h$ over $y$, so the finite part is exactly a bookkeeping of connectedness.

The immediate corollary is the connectedness statement in Zariski's main theorem: if $f_* \OO_X = \OO_Y$ then $Y' = Y$, so $h$ is the identity and the fibres of $f$ are connected.
In the other direction, for a proper morphism of varieties with $Y$ normal and $f$ birational, the Stein factorisation is what proves the fibres connected without a separate argument.
:::
