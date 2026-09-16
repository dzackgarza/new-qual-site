---
schema: qual/card@1
id: D-MORFLAT
kind: definition
title: Flat morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flatness
  - Families
  - Local Rings
relations:
- kind: uses
  target: D-MORFIB
review: draft
prompts:
- What is a flat morphism?
- What is a faithfully flat morphism?
- What is flatness for a sheaf rather than a morphism?
---

::: {.definition title="Flat"}
$f : X \to Y$ is \dfn{flat at} $x$ if $\OO_{X,x}$ is a flat module over $\OO_{Y,f(x)}$, and \dfn{flat} if it is flat at every point.
More generally $\mcf \in \mods{\OO_X}$ is \dfn{flat over $Y$ at $x$} if $\mcf_x$ is a flat $\OO_{Y,f(x)}$-module, and $f$ is flat exactly when $\OO_X$ is.
$f$ is \dfn{faithfully flat} if it is flat and surjective.
:::

::: {.remark}
Flatness is a condition on stalks and therefore checkable on affines, where it is the ordinary flatness of $B \to A$.
The geometric meaning is that $f$ is a family without jumps, and the way to say that precisely is that $\wait \tensor_B A$ is exact, so no relation among the fibres is created or destroyed.

Over a discrete valuation ring, and more generally over a Dedekind domain, flat means torsion-free, which is the reason flatness is invisible for curves: any dominant morphism from an integral scheme to a smooth curve is flat.
Over a regular local ring of higher dimension this fails, and the blowup is the standard witness.

Faithful flatness is the descent hypothesis: a faithfully flat map reflects as well as preserves, so a module is zero exactly when its base change is, and this is what makes flat descent work.
:::

::: {.remark}
A flat morphism $f \colon X \to T$ is regarded as the family of schemes $X_t = X \times_T \Spec \kappa(t)$ parametrized by the points $t \in T$ ([[D-MORFIB]]).
For $f$ flat and projective over a connected Noetherian base, the Hilbert polynomials of the fibres are constant ([[T-COHFLATCHI]]).
:::
