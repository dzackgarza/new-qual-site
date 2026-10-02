---
schema: qual/card@1
id: FE-CRVLOWG
kind: example
title: The canonical models in genus $2$, $3$, and $4$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Canonical Divisor
  - Curves
  - Complete Intersections
relations:
- kind: uses
  target: T-D8TUX
- kind: uses
  target: D-CRVHYP
review: draft
prompts:
- Describe the curves of genus $2$.
- Describe the curves of genus $3$.
- Describe the curves of genus $4$.
---

Let $k$ be an algebraically closed field and let $C$ be a smooth projective curve over $k$.

::: {.example title="Genus 2"}
Every curve of genus $2$ is hyperelliptic: $\deg K = 2$ and $\ell(K) = 2$, so $\abs{K}$ is itself the $g^1_2$.
The canonical map is the degree-two morphism $C \to \PP^1$; if $\operatorname{char}k\ne2$, Riemann--Hurwitz gives $6$ branch points.
$C$ embeds in $\PP^3$ by any divisor of degree $5$, since $5 \geq 2g+1$.
:::

::: {.example title="Genus 3"}
$\deg K = 4$ and $\abs{K}$ maps $C \to \PP^2$.
If $C$ is not hyperelliptic this is an embedding as a smooth plane quartic, and conversely every smooth plane quartic has $\omega_C \cong \OO_C(1)$ and so is canonical.
The hyperelliptic locus in $\mathcal{M}_3$ has dimension $5$, while $\dim \mathcal{M}_3 = 6$.
:::

::: {.example title="Genus 4"}
$\deg K = 6$ and $\abs{K}$ embeds a non-hyperelliptic $C$ in $\PP^3$ as a sextic.
That curve lies on a unique quadric surface $Q$ and is the complete intersection of $Q$ with a cubic surface.
Conversely a smooth complete intersection of a quadric and a cubic in $\PP^3$ has degree $6$ and $\omega \cong \OO(1)$, so it is the canonical curve of a genus-$4$ curve.
If $Q$ is smooth, then $Q\cong\PP^1\times\PP^1$, the curve has bidegree $(3,3)$, and the two rulings give two $g^1_3$'s. If $Q$ is a quadric cone, its ruling gives one $g^1_3$.
:::

::: {.remark}
For a non-hyperelliptic curve, $\abs{K}$ embeds $C$ as a curve of degree $2g-2$ in $\PP^{g-1}$, and for $g=3,4$ that image has the named models above.
For a non-hyperelliptic genus-$4$ curve, Max Noether's theorem makes the restriction maps
$$
H^0(\PP^3,\OO(m))\longrightarrow H^0(C,mK_C)
$$
surjective for $m\geq1$. Since
$$
h^0(\PP^3,\OO(2))=10,\qquad h^0(C,2K_C)=12+1-4=9,
$$
the space of quadrics containing $C$ is one-dimensional. For cubics,
$$
h^0(\PP^3,\OO(3))-h^0(C,3K_C)=20-15=5.
$$
The four products of the unique quadric with linear forms span only a four-dimensional subspace, so there is a cubic surface $S$ containing $C$ but not containing $Q$. The complete intersection $Q\cap S$ has degree $6=\deg C$, hence $C=Q\cap S$.
:::
