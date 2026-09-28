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
$$
\Div(X) \times \Div(X) \to \ZZ , \qquad (C,D) \mapsto C \cdot D ,
$$
which counts points for transverse smooth curves and depends only on linear equivalence classes.
$C^2 = C \cdot C$ is the \dfn{self-intersection}. Fixing a very ample $H$, the \dfn{degree} of a curve $C$ in the embedding determined by $H$ is $C \cdot H$.
:::

::: {.remark}
To compute $C\cdot D$, replace $C$ and $D$ by linearly equivalent divisors that are differences of nonsingular curves meeting transversally, and count intersection points [@Har10a, Theorem V.1.1].
For $C$ an irreducible nonsingular curve and any divisor $D$, $C\cdot D=\deg_C\OO_X(D)\vert_C$; in particular $C^2 = \deg_C \OO_X(C)\vert_C=\deg_C\mcn_{C/X}$.

On $\PP^2$, $\Pic = \ZZ H$ with $H^2 = 1$, so curves of degrees $d$ and $e$ with no common component meet in $de$ points counted with multiplicity, which is Bézout's theorem.
On $\PP^1 \times \PP^1$ the two rulings satisfy $A^2 = B^2 = 0$ and $A \cdot B = 1$.

For a curve $C$ on a surface $S$, the ideal sheaf is $\mci_C = \OO_S(-C)$ and the conormal sheaf is $\mci_C/\mci_C^2 = \OO_S(-C)\vert_C$.
For $C$ nonsingular of genus $g$, the adjunction formula gives $2g-2=C\cdot(C+K_S)$ [@Har10a, Proposition V.1.5].
:::
