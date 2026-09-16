---
schema: qual/card@1
id: P-AGH251DUALSHEAF
kind: problem
title: Duals of locally free sheaves and the projection formula
classification:
  areas:
  - algebraic-geometry
  topics:
  - Locally Free Sheaves
  - Sheaf Hom
  - Projection Formula
relations: []
review: draft
---

::: {.problem}
Let $(X, \OO_X)$ be a ringed space, and let $\mce$ be a locally free $\OO_X\dash$module of finite rank.
We define the **dual** of $\mce$, denoted $\mce\dual$, to be the sheaf $\sheafhom_{\OO_X}(\mce, \OO_X)$.

a. Show that $(\mce\dual)\dual \cong \mce$.

b. For any $\OO_X\dash$module $\mcf$,
\[
\sheafhom_{\OO_X}(\mce \tensor \mcf, \mcg) \cong \sheafhom_{\OO_X}(\mcf, \sheafhom_{\OO_X}(\mce, \mcg))
.\]

c. (Projection formula.) If $f: (X, \OO_X) \to (Y, \OO_Y)$ is a morphism of ringed spaces, if $\mcf$ is an $\OO_X\dash$module, and if $\mce$ is a locally free $\OO_Y\dash$module of finite rank, then there is a natural isomorphism
\[
f_*\left(\mcf \tensor_{\OO_X} f^* \mce\right) \cong f_*(\mcf) \tensor_{\OO_Y} \mce
.\]
:::
