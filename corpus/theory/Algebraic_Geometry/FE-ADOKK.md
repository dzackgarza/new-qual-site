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
$$
0 \to \OO_C^* \to \nu_* \OO_{\tilde{C}}^* \to \mcs \to 0
$$
with $\mcs$ a skyscraper at the singular points, and its cohomology sequence computes $\Pic(C)$ from $\Pic(\tilde{C})$ and the local unit groups.

For the cusp $A = k[t^2,t^3] \subseteq k[t]$, the conductor square gives $\Pic(\Spec A) \cong k^+ = \GG_a$.
For the node $k[x,y]/(y^2 - x^2(x+1))$, the same computation gives $\GG_m$.
:::

::: {.remark}
At a node $p$ with $\nu^{-1}(p)=\ts{p_1,p_2}$, the stalk $\mcs_p$ is $(k^\times\times k^\times)/k^\times\cong k^\times$, the ratio of the values of a unit of $\OO_{\tilde C}$ at $p_1$ and $p_2$; so the node contributes $\GG_m$.
At the cusp of $\Spec k[t^2,t^3]$, with $\nu^{-1}(p)=\ts{\tilde p}$ and $\OO_{C,p}$ the functions whose derivative in $t$ vanishes at $\tilde p$, the stalk $\mcs_p$ is $(k[t]/(t^2))^\times/k^\times\cong k^+$, via $a+bt\mapsto b/a$; so the cusp contributes $\GG_a$.

For the projective cubics, $\Pic^0$ of the nodal cubic is $\GG_m$ and $\Pic^0$ of the cuspidal cubic is $\GG_a$; in each case the smooth locus, with the chord-tangent group law, is isomorphic to $\Pic^0$.
:::
