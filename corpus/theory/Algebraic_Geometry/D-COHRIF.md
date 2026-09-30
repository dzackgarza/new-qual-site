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
For $f: X \to Y$, the functor $f_*$ is left exact; set $R^i f_* \mcf \definedas R^i(f_*)(\mcf)$.
Equivalently, $R^i f_* \mcf$ is the sheafification of
$$
V \mapsto H^i\qty{\inverseof{f}(V), \restrictionof{\mcf}{\inverseof{f}(V)}} .
$$
:::

::: {.proposition title="Functoriality in the space, and affine morphisms"}
Let $f \colon X \to Y$ be a morphism of schemes.

1. For a sheaf of abelian groups $\mcf$ on $X$ there are natural maps $H^i(Y, f_* \mcf) \to H^i(X, \mcf)$, and for a sheaf of $\OO_Y$-modules $\mcg$ natural maps $H^i(Y, \mcg) \to H^i(X, f^* \mcg)$.

2. If $X$ and $Y$ are quasicompact and separated, $f$ is affine and $\mcf$ is quasicoherent, then $H^i(Y, f_* \mcf) \to H^i(X, \mcf)$ is an isomorphism for every $i$ ([[P-AGH341AFFINEMORPH]]).
:::

::: {.remark}
If $X$ is Noetherian, $Y = \Spec A$ is affine, and $\mcf$ is quasicoherent, then $R^i f_* \mcf \cong \widetilde{H^i(X,\mcf)}$ [@Har10a, Proposition III.8.5].
If $f$ is an affine morphism and $\mcf$ is quasicoherent, then $R^{i} f_* \mcf = 0$ for $i>0$ and $H^i(X,\mcf) \cong H^i(Y, f_*\mcf)$.
For a closed subscheme $i\colon X\hookrightarrow\PP^n$ and a quasicoherent sheaf $\mcf$ on $X$, this gives $H^i(X,\mcf)\cong H^i(\PP^n,i_*\mcf)$.

If $Y$ is Noetherian, $f$ is projective, and $\mcf$ is coherent, then $R^i f_* \mcf$ is coherent [@Har10a, Theorem III.8.8]; for $Y=\Spec k$ this is the finite-dimensionality of $H^i(X,\mcf)$ [@Har10a, Theorem III.5.2].
:::
