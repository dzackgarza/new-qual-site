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
- What is an associated point?
- How can one check that a morphism to a regular curve is flat?
- What properties are not preserved in a flat family?
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

::: {.definition title="Associated points"}
A point $x$ of a Noetherian scheme $X$ is an \dfn{associated point} if $\mfm_x$ is an associated prime of $0$ in $\OO_{X,x}$, equivalently if every element of $\mfm_x$ is a zero divisor in $\OO_{X,x}$.
The generic points of the irreducible components are associated points, and when $X$ is reduced they are the only ones.
:::

::: {.proposition title="Flatness over a regular curve"}
Let $f \colon X \to Y$ be a morphism with $X$ Noetherian and $Y$ integral, regular and of dimension one.
Then $f$ is flat if and only if every associated point of $X$ maps to the generic point of $Y$.
In particular, if $X$ is reduced, $f$ is flat if and only if every irreducible component of $X$ dominates $Y$.
[@Har10a]
:::

::: {.proposition title="Flat limits"}
Let $Y$ be integral, regular and of dimension one, $P \in Y$ a closed point, and $X^\circ \subseteq \PP^n_{Y \sm P}$ a closed subscheme flat over $Y \sm P$.
Then there is a unique closed subscheme $X \subseteq \PP^n_Y$, flat over $Y$, whose restriction to $\PP^n_{Y \sm P}$ is $X^\circ$: the scheme-theoretic closure of $X^\circ$.
[@Har10a]
:::

::: {.example title="What a flat family does not preserve"}
The family $V(xy - t) \subseteq \AA^2 \times \AA^1_t \to \AA^1_t$ is flat, since its total space is integral and dominates the line; its fibres are smooth irreducible hyperbolas for $t \neq 0$ and the reducible pair of axes at $t = 0$.
The family $V(y^2 - tx) \to \AA^1_t$ is flat for the same reason; its fibres are reduced parabolas for $t \neq 0$ and the nonreduced double line $y^2 = 0$ at $t = 0$.
So irreducibility, reducedness and smoothness can all fail in the special fibre, while the Hilbert polynomial of a flat projective family cannot change.
:::
