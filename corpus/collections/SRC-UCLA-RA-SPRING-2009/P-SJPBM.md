---
schema: qual/card@1
id: P-SJPBM
kind: problem
title: No corner-to-corner conformal homeomorphism from a square onto a $2\times 1$
  rectangle
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Let $Q$ be the closed unit square in $\CC$ and let $R$ be the closed rectangle in $\CC$ with vertices $\{0,2,i,2+i\}$.
Prove there does not exist a surjective homeomorphism $f: Q\to R$ that is conformal on the interior of $Q$ and maps corners to corners.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own reflection argument follows, with the reduction, the extension across the sides and the contradiction from the side ratio as separate steps.

::: pf

::: {.pf-step #reduce}
If a surjective homeomorphism $f:Q\to R$ conformal on the interior and carrying corners to corners existed, then after composing with a rotation or reflection of $Q$ one may assume $f$ fixes the vertex $0$ and carries the edge $[0,i]$ to the edge $[0,2]$.

::: pf-proof
$f$ maps the four vertices of $Q$ onto the four vertices of $R$, and it maps edges to edges: the boundary of $Q$ is a simple closed curve and $f$ is a homeomorphism, so $f\restriction_{\partial Q}$ is a homeomorphism of circles carrying vertices to vertices and hence cyclically permuting them. Composing with a symmetry of $Q$, which is a homeomorphism conformal on the interior and permuting the vertices, arranges the stated normalisation; symmetries of $Q$ preserve the conclusion.
:::

:::

::: {.pf-step #extend}
Such an $f$ extends to a conformal automorphism $F$ of $\CC$.

::: pf-proof
$f$ is conformal (biholomorphic) on the interior of $Q$. The Schwarz reflection principle extends a biholomorphism across a boundary edge contained in a line: reflecting the square across the edge $[0,i]$ extends $f$ to a biholomorphism of the union of $Q$ and its mirror image, and iterating this over the vertical edges extends $f$ to the strip $0\le\operatorname{Im}\zeta\le1$ mapped bijectively to the strip $0\le\operatorname{Im}\zeta\le2$; reflecting then over the horizontal edges, which are boundary lines of the image strip, and iterating, extends $f$ to a biholomorphism $F$ of $\CC$. Each reflection is legitimate because $f$ maps an edge of $Q$ onto an edge of $R$, and both are line segments.
:::

:::

::: {.pf-step #linear}
$F(z)=az+b$ with $a\ne0$.

::: pf-proof
$F$ is an injective entire function, so by Picard's little theorem or by the standard classification of conformal automorphisms of $\CC$ it is affine: $F(z)=az+b$ with $a\ne0$.
:::

:::

::: {.pf-step #ratio}
An affine map carries the four edges of $Q$ to four segments of equal length $\abs{a}$, but $R$ has two sides of length $2$ and two of length $1$.

::: pf-proof
The edges of $Q$ all have length $1$, and an affine map multiplies all lengths by the constant factor $\abs{a}$; the edges of $R$ have lengths $2,1,2,1$.
:::

:::

::: {.pf-qed}
By steps [](#extend){.pf-ref} and [](#linear){.pf-ref} the map would have to be affine, and step [](#ratio){.pf-ref} shows no affine map carries the unit square onto a $2\times1$ rectangle. So no such homeomorphism exists.
:::

:::

:::
