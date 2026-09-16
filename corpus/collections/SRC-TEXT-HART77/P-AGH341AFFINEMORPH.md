---
schema: qual/card@1
id: P-AGH341AFFINEMORPH
kind: problem
title: Cohomology is preserved by pushforward along an affine morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Affine Morphisms
  - Quasicoherent Sheaves
relations: []
review: draft
---

::: problem
Let $f: X \to Y$ be an affine morphism of noetherian separated schemes (II, Ex.
5.17). Show that for any quasi-coherent sheaf $\mcf$ on $X$, there are natural isomorphisms for all $i \geq 0$,
\[
H^i(X, \mcf) \cong H^i(Y, f_* \mcf).
\]

Hint: Use (II, 5.8).
:::

::::: {.solution}
<1>1. For every open cover $\mathfrak{V}$ of $Y$, the Čech complexes $C^\bullet(\mathfrak{V}, f_* \mcf)$ and $C^\bullet(f^{-1}\mathfrak{V}, \mcf)$ are equal.

::: {.proof}
For every finite intersection $V_J$ of members of $\mathfrak{V}$, $\Gamma(V_J, f_* \mcf) = \Gamma(f^{-1} V_J, \mcf)$ by definition of $f_*$, with the same restriction maps.
:::

<1>2. If $\mathfrak{V}$ is a finite open affine cover of $Y$, then $f^{-1}\mathfrak{V}$ is a finite open affine cover of $X$.

::: {.proof}
$f$ is affine, so the preimage of each affine open of $Y$ is affine.
:::

<1>3. Q.E.D.

::: {.proof}
$f_* \mcf$ is quasi-coherent by (II, 5.8), and $X$ and $Y$ are Noetherian and separated, so Čech cohomology for any open affine cover computes the cohomology of a quasi-coherent sheaf (III, 4.5).
Choose a finite open affine cover $\mathfrak{V}$ of $Y$; by steps <1>1 and <1>2,
$$H^i(Y, f_* \mcf) \cong \check{H}^i(\mathfrak{V}, f_* \mcf) = \check{H}^i(f^{-1}\mathfrak{V}, \mcf) \cong H^i(X, \mcf).$$
The isomorphisms are natural in $\mcf$, since a morphism of quasi-coherent sheaves induces compatible maps of both Čech complexes.
:::
:::::
