---
schema: qual/card@1
id: P-AGH2517AFFMOR
kind: problem
title: Affine morphisms and the relative spectrum
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Morphisms
  - Relative Spectrum
  - Quasi-coherent Sheaves
relations: []
review: draft
---

::: problem
A morphism $f: X \to Y$ of schemes is **affine** if there is an open affine cover $\ts{V_i}$ of $Y$ such that $f\inv(V_i)$ is affine for each $i$.

a. Show that $f: X \to Y$ is affine if and only if for every open affine $V \subseteq Y$, $f\inv(V)$ is affine.
   *Hint:* reduce to the case $Y$ affine.

b. An affine morphism is quasi-compact and separated. Any finite morphism is affine.

c. Let $Y$ be a scheme, and let $\mca$ be a quasi-coherent sheaf of $\OO_Y\dash$algebras, i.e. a sheaf of rings which is at the same time a quasi-coherent sheaf of $\OO_Y\dash$modules.
   Show that there is a unique scheme $X$ and a morphism $f: X \to Y$ such that for every open affine $V \subseteq Y$, $f\inv(V) \cong \Spec \mca(V)$, and for every inclusion $U \injects V$ of open affines of $Y$ the morphism $f\inv(U) \injects f\inv(V)$ corresponds to the restriction homomorphism $\mca(V) \to \mca(U)$.
   The scheme $X$ is called $\Spec \mca$.
   *Hint:* construct $X$ by gluing together the schemes $\Spec \mca(V)$.

d. If $\mca$ is a quasi-coherent $\OO_Y\dash$algebra, then $f: X = \Spec \mca \to Y$ is affine and $\mca \cong f_* \OO_X$.
   Conversely, if $f: X \to Y$ is affine, then $\mca = f_* \OO_X$ is a quasi-coherent sheaf of $\OO_Y\dash$algebras and $X \cong \Spec \mca$.

e. Let $f: X \to Y$ be affine and let $\mca = f_* \OO_X$.
   Show that $f_*$ induces an equivalence of categories from quasi-coherent $\OO_X\dash$modules to quasi-coherent $\mca\dash$modules.
   *Hint:* for any quasi-coherent $\mca\dash$module $\mcm$, construct a quasi-coherent $\OO_X\dash$module $\tilde\mcm$, and show that $f_*$ and $\sim$ are inverse to each other.
:::
