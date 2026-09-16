---
schema: qual/card@1
id: PR-MIRACLEFLAT
kind: proposition
title: Finite morphisms of smooth varieties of equal dimension are flat
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Finite Morphisms
  - Cohen-Macaulay Rings
relations:
- kind: uses
  target: D-SCHCMGOR
- kind: uses
  target: D-MORFIN
review: draft
prompts:
- Show that a finite morphism between smooth varieties is flat, and state the hypotheses this needs.
---

::: {.proposition title="Miracle flatness"}
Let $f \colon X \to Y$ be a finite morphism of varieties over a field with $X$ Cohen--Macaulay, $Y$ smooth, and $\dim X = \dim Y$ at every point of $X$.
Then $f$ is flat.
In particular a finite surjective morphism between smooth varieties of the same dimension is flat.
:::

::: {.proof}
1. Flatness is local: for $x \in X$ with $y = f(x)$, show $\OO_{X,x}$ is flat over $\OO_{Y,y}$.

2. $f$ is finite, so the fibre through $x$ is zero-dimensional and $\dim \OO_{X,x} = \dim \OO_{Y,y}$ by the dimension hypothesis.

3. For a local homomorphism $A \to B$ of Noetherian local rings with $A$ regular, $B$ Cohen--Macaulay and $\dim B = \dim A + \dim B/\mfm_A B$, the module $B$ is flat over $A$: a regular system of parameters of $A$ maps to a regular sequence in $B$, because it is part of a system of parameters in the Cohen--Macaulay ring $B$, and a local criterion for flatness applies.
:::

::: {.example}
The hypotheses cannot be dropped.
The inclusion of the origin $\Spec k \to \AA^1_k$ is finite and both schemes are smooth, but it is not flat, since $k = k[t]/(t)$ is a torsion $k[t]$-module; here the dimensions differ.
The normalization $\AA^1 \to V(y^2 - x^3)$, $t \mapsto (t^2, t^3)$, is finite between varieties of the same dimension with smooth source, but the target is not smooth, and the map is not flat: it is birational of degree one and not an isomorphism.
:::
