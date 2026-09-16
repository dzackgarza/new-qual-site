---
schema: qual/card@1
id: D-COHRIF
kind: definition
title: Higher direct images
classification:
  areas:
  - algebraic-geometry
  topics:
  - Higher Direct Images
  - Cohomology
  - Morphisms
relations:
- kind: uses
  target: D-COHDER
review: draft
prompts:
- What is the higher direct image?
- Compute $R^i f_* \mcf$ for $f$ an affine morphism.
- Why is $H^i(Y, f_*\mcf) \cong H^i(X, \mcf)$ for an affine morphism $f$ and quasicoherent $\mcf$?
- In what sense is cohomology contravariant in the space?
---

::: {.definition}
For $f: X \to Y$, the functor $f_*$ is left exact; set $R^i f_* \mcf \da R^i(f_*)(\mcf)$.
Equivalently, $R^i f_* \mcf$ is the sheafification of
\[
V \mapsto H^i\qty{f\inv(V), \restrictionof{\mcf}{f\inv(V)}} .
\]
:::

::: {.proposition title="Functoriality in the space, and affine morphisms"}
Let $f \colon X \to Y$ be a morphism of schemes.

1. For a sheaf of abelian groups $\mcf$ on $X$ there are natural maps $H^i(Y, f_* \mcf) \to H^i(X, \mcf)$, and for a sheaf of $\OO_Y$-modules $\mcg$ natural maps $H^i(Y, \mcg) \to H^i(X, f^* \mcg)$.

2. If $X$ and $Y$ are quasicompact and separated, $f$ is affine and $\mcf$ is quasicoherent, then $H^i(Y, f_* \mcf) \to H^i(X, \mcf)$ is an isomorphism for every $i$.
:::

::: {.proof}
1. In Čech terms: an open cover $\mathfrak{V} = \{V_j\}$ of $Y$ pulls back to the open cover $f^{-1}\mathfrak{V} = \{f^{-1} V_j\}$ of $X$, and $\Gamma(V_J, f_* \mcf) = \Gamma(f^{-1} V_J, \mcf)$ for every finite intersection, with the same restriction maps, so $C^\bullet(\mathfrak{V}, f_*\mcf) = C^\bullet(f^{-1}\mathfrak{V}, \mcf)$; composing with the map to the colimit over all covers of $X$ gives the first map. In derived-functor terms it is the edge map $H^i(Y, f_* \mcf) \to H^i(X, \mcf)$ of the Leray spectral sequence. For $\mcg$, compose the map induced on cohomology by the unit $\mcg \to f_* f^* \mcg$ of the adjunction $f^* \dashv f_*$ with the first map for $\mcf = f^* \mcg$.

2. Choose a finite affine cover $\mathfrak{V}$ of $Y$. Since $f$ is affine, $f^{-1}\mathfrak{V}$ is a finite affine cover of $X$, and since $X$ and $Y$ are separated all finite intersections in both covers are affine. $f_* \mcf$ is quasicoherent, so both Čech complexes compute cohomology ([[D-PTIW0]]), and by step 1 they are the same complex.
:::

::: {.remark}
Read it as the cohomology of $\mcf$ along the fibres of $f$: a sheaf on the base recording how the cohomology of the fibres varies.
Two computations pin it down.

If $Y = \Spec A$ is affine, then $R^i f_* \mcf = \widetilde{H^i(X,\mcf)}$, so nothing new appears over an affine base.
If $f$ is an affine morphism and $\mcf$ is quasicoherent, then $R^{i>0} f_* \mcf = 0$ and $H^i(X,\mcf) \cong H^i(Y, f_*\mcf)$; a closed immersion is the case used constantly, which is why cohomology can be computed after pushing a sheaf forward from a projective subscheme to the ambient $\PP^n$.

For $f$ projective and $\mcf$ coherent, $R^i f_* \mcf$ is coherent, which is the relative form of Serre finiteness.
:::
