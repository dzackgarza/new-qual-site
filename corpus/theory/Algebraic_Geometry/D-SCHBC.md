---
schema: qual/card@1
id: D-SCHBC
kind: definition
title: Base change, and properties stable under it
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Fibre Products
  - Morphisms Of Schemes
relations:
- kind: uses
  target: D-SCHFPR
review: draft
prompts:
- What is base change?
- What does it mean for a property of morphisms to be stable under base change, or local on the base?
---

::: {.definition}
For $X \to S$ and a morphism $T \to S$, the **base change** of $X$ to $T$ is $X_T \da \fiberprod{X}{S}{T}$, with its projection $X_T \to T$.

A property $P$ of morphisms is **stable under base change** if $X \to S$ having $P$ forces $X_T \to T$ to have $P$ for every $T \to S$.
It is **local on the base** if $X \to S$ has $P$ whenever there is an open cover $\ts{V_i}$ of $S$ with each $f\inv(V_i) \to V_i$ having $P$.
:::

::: {.remark}
Base change is one operation used for three purposes, and saying which one you mean is most of the answer.
Extending the ground field, $X \mapsto \fiberprod{X}{\Spec k}{\Spec L}$, is how "geometrically connected" and "geometrically integral" get their names: the property is required to survive every field extension, and connectedness alone does not, as $\Spec \CC$ over $\RR$ shows.
Restricting to a fibre is base change along $\Spec \kappa(y) \to Y$.
Spreading out a family is base change along a map of bases.

Almost every adjective — closed immersion, separated, proper, finite, flat, smooth, affine — is stable under base change and local on the base, which is what makes them usable: you check them on an affine cover and they survive every substitution of base.
Surjectivity of the map on *points* and dominance are the notable properties that need care, and being asked for a property that is not stable is a request for a counterexample, not a list.
:::
