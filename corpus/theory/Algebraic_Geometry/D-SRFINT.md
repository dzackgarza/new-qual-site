---
schema: qual/card@1
id: D-SRFINT
kind: definition
title: The intersection pairing on a surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Intersection Theory
  - Surfaces
  - Divisors
relations:
- kind: uses
  target: D-VARDEG
review: draft
prompts:
- Define the intersection pairing on a surface.
- How is the degree of a curve on a surface defined?
- What is the self-intersection of a divisor?
---

::: {.definition}
Let $X$ be a smooth projective surface.
There is a unique symmetric bilinear pairing
\[
\Div(X) \times \Div(X) \to \ZZ , \qquad (C,D) \mapsto C \cdot D ,
\]
which counts points for transverse smooth curves and depends only on linear equivalence classes.
$C^2 = C \cdot C$ is the \dfn{self-intersection}. Fixing an ample $H$, the **degree** of a curve $C$ in the embedding determined by $H$ is $C \cdot H$.
:::

::: {.remark}
Uniqueness plus the transverse case is the working definition: one moves the divisors into general position and counts, and linear invariance is what makes the count well defined even for a curve against itself.
Self-intersection is where the geometry is, because a curve cannot be moved off itself; the answer is read from the normal bundle, $C^2 = \deg \OO_X(C)\vert_C$.

Two computations to have ready.
On $\PP^2$, $\Pic = \ZZ H$ with $H^2 = 1$, so a curve of degree $d$ and one of degree $e$ meet in $de$ points, which is Bézout.
On $\PP^1 \times \PP^1$ the two rulings satisfy $A^2 = B^2 = 0$ and $A \cdot B = 1$.

For a curve $C$ inside a surface $S$ the ideal sheaf is $\mci_C = \OO_S(-C)$ and the conormal sheaf is $\mci_C/\mci_C^2 = \OO_S(-C)\vert_C$, which is the bookkeeping behind both self-intersection and adjunction.
:::
