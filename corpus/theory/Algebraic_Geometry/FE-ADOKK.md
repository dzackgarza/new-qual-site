---
schema: qual/card@1
id: FE-ADOKK
kind: example
title: The Picard group of a nodal and of a cuspidal curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Picard Group
  - Singularities
  - Normalization
relations:
- kind: uses
  target: D-5PQ5W
review: draft
prompts:
- Compute $\Pic(k[t^2,t^3])$.
- What is the Picard group of a nodal cubic?
---

::: {.example}
Let $C$ be a singular curve with normalization $\nu : \tilde{C} \to C$.
Comparing units gives the exact sequence
\[
0 \to \OO_C^* \to \nu_* \OO_{\tilde{C}}^* \to \mcs \to 0
\]
with $\mcs$ a skyscraper at the singular points, and its cohomology sequence computes $\Pic(C)$ from $\Pic(\tilde{C})$ and the local unit groups.

For the **cusp** $A = k[t^2,t^3] \subseteq k[t]$, the conductor square gives $\Pic(\Spec A) \cong k^+ = \GG_a$.
For the **node** $k[x,y]/(y^2 - x^2(x+1))$, the same computation gives $\GG_m$.
:::

::: {.remark}
The slogan is that normalization replaces the singular point by its preimage, and what is lost is the identification data: at a node two branches are glued, and the gluing is a choice of ratio of the two values, hence $\GG_m$; at a cusp the branches coincide to first order, and what is glued is a value together with a derivative, hence $\GG_a$.

For the projective versions the same answers appear as $\Pic^0$: the nodal cubic has $\Pic^0 = \GG_m$ and the cuspidal cubic has $\Pic^0 = \GG_a$, which is the degeneration of the group law on an elliptic curve as the discriminant goes to zero.
Being able to say which singularity gives which group is the point of the question.
:::
