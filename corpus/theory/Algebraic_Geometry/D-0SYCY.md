---
schema: qual/card@1
id: D-0SYCY
kind: definition
title: Smooth and singular points, and the two criteria
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nonsingularity
  - Tangent Spaces
  - Jacobian Criterion
relations:
- kind: uses
  target: D-5LJUX
review: draft
prompts:
- Give two criteria for a variety to be nonsingular at a point.
- What is the Zariski tangent space?
- Why does the Jacobian criterion need the right codimension?
---

::: {.definition title="Zariski tangent space"}
For $p \in X$ with local ring $\OO_{X,p}$ and maximal ideal $\mfm_p$, the **Zariski tangent space** is
\[
T_p X \da (\mfm_p / \mfm_p^2)\dual .
\]
The point $p$ is **smooth** if $\dim_k T_p X = \dim_p X$, and **singular** otherwise, where the inequality $\geq$ always holds.
:::

::: {.proposition title="Jacobian criterion"}
Let $I(X) = \gens{f_1,\ldots,f_r} \subseteq k[x_1,\ldots,x_n]$ with $X$ of pure codimension $r$, and let $J_X(p) = \left[ \partial f_i / \partial x_j (p) \right]$.
Then $p$ is a smooth point exactly when $\rank J_X(p) = r$.
:::

::: {.remark}
The two criteria are the two answers to "give two criteria for nonsingularity": the extrinsic rank condition, which is a computation, and the intrinsic condition that $\OO_{X,p}$ be a regular local ring, which is the one that survives to schemes and to non-closed points.

The rank condition is stated for a *complete intersection* presentation, and that hypothesis is not decorative.
If $X$ is cut out by more equations than its codimension, the rank of $J_X$ drops everywhere and the criterion reports singularities that are not there.
The two criteria are equivalent over a perfect field and part company over an imperfect one: the Jacobian condition is smoothness, which is geometric and survives base change to $\bar{k}$, while regularity of $\OO_{X,p}$ does not.
Over $k = \FF_p(t)$ the closed subscheme $V(x^p - t) \subseteq \AA^1$ is the spectrum of a field, hence regular, but it is not smooth: after base change to $k(t^{1/p})$ it becomes $V((x - t^{1/p})^p)$, which is not even reduced.
This is what the question about curves over perfect fields is about.
:::
