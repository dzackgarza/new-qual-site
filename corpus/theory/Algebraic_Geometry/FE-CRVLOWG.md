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

::: {.example title="Genus 2"}
Every curve of genus $2$ is hyperelliptic: $\deg K = 2$ and $\ell(K) = 2$, so $\abs{K}$ is itself the $g^1_2$.
The canonical map is the double cover $C \to \PP^1$, branched at $6$ points.
$C$ embeds in $\PP^3$ by any divisor of degree $5$, since $5 \geq 2g+1$.
:::

::: {.example title="Genus 3"}
$\deg K = 4$ and $\abs{K}$ maps $C \to \PP^2$.
If $C$ is not hyperelliptic this is an embedding as a smooth plane quartic, and conversely every smooth plane quartic has $\omega_C \cong \OO_C(1)$ and so is canonical.
The hyperelliptic curves of genus $3$ are the remaining case, a divisor in $\mathcal{M}_3$ of dimension $5$ inside $\dim \mathcal{M}_3 = 6$.
:::

::: {.example title="Genus 4"}
$\deg K = 6$ and $\abs{K}$ embeds a non-hyperelliptic $C$ in $\PP^3$ as a sextic.
That curve lies on a unique quadric surface $Q$ and is the complete intersection of $Q$ with a cubic surface.
Conversely a smooth complete intersection of a quadric and a cubic in $\PP^3$ has degree $6$ and $\omega \cong \OO(1)$, so it is the canonical curve of a genus-$4$ curve.
Whether $Q$ is smooth or a cone is the extra discrete invariant here: on a smooth $Q$ the curve is of type $(3,3)$ and carries two distinct $g^1_3$'s, on the cone it carries one.
:::

::: {.remark}
These are the cases an examiner actually asks for, and the right answer is the model, not a general theorem.
The pattern to state is: $\abs{K}$ embeds a non-hyperelliptic curve as a curve of degree $2g-2$ in $\PP^{g-1}$, and for small $g$ that image is something with a name.
Counting equations gives the unique quadric in genus $4$: $h^0(\PP^3, \OO(2)) = 10$ while $h^0(C, \OO_C(2)) = 2 \cdot 6 + 1 - 4 = 9$, so the ideal of $C$ contains a quadric, and it contains only one.
:::
