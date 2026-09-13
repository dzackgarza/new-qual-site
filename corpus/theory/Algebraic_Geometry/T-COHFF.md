---
schema: qual/card@1
id: T-COHFF
kind: theorem
title: The theorem on formal functions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Higher Direct Images
  - Proper Morphisms
relations:
- kind: uses
  target: D-COHRIF
review: draft
prompts:
- State the theorem on formal functions.
- Deduce Zariski's connectedness theorem.
---

::: {.theorem}
Let $f: X \to Y$ be proper with $Y$ Noetherian, $\mcf$ coherent on $X$, and $y \in Y$ with maximal ideal $\mfm_y$.
Write $X_n$ for the subscheme cut out by $\mfm_y^n \OO_X$.
Then the completion of the stalk satisfies
\[
\hat{\qty{R^i f_* \mcf}_y} \cong \varprojlim_n H^i\qty{X_n, \mcf/\mfm_y^n \mcf} .
\]
:::

::: {.remark}
The content is that the cohomology of the fibre, thickened to all orders, computes the completed stalk: infinitesimal data along $f\inv(y)$ determines the germ of the direct image.
Properness is load-bearing and is what makes the inverse limit converge to something algebraic; the statement is false for open immersions.

Two corollaries are the reason it is on a syllabus.
Zariski's connectedness theorem: if $f: X \to Y$ is proper with $f_* \OO_X = \OO_Y$, then every fibre is connected.
And the version of Zariski's main theorem for a birational proper morphism to a normal variety: the fibres are connected, so no fibre breaks into pieces, which is what "no blowing down to two points" means in practice.
:::
