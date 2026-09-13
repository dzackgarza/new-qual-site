---
schema: qual/card@1
id: FE-CRVDEGS
kind: example
title: Curves of low degree in $\PP^3$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Space Curves
  - Genus
  - Complete Intersections
relations:
- kind: uses
  target: T-CRVCAST
- kind: uses
  target: FE-CRVQUAD
review: draft
prompts:
- Classify the curves of degree at most $5$ in $\PP^3$.
- Which pairs $(d,g)$ occur for curves in $\PP^3$?
---

::: {.example}
By degree, for smooth curves in $\PP^3$:

- $d=1$: a line, $g=0$.

- $d=2$: a plane conic, $g=0$.

- $d=3$: the plane cubic with $g=1$, and the twisted cubic with $g=0$.

- $d=4$: the plane quartic with $g=3$; the rational quartic with $g=0$; and the elliptic quartic with $g=1$, which is the complete intersection of two quadrics.

- $d=5$: the plane quintic with $g=6$, and curves with nonspecial hyperplane section of genus $0, 1, 2$.

- $d=6$: the plane sextic with $g=10$; nonspecial curves of genus $0,1,2,3$; and the canonical curve of genus $4$, the complete intersection of a quadric and a cubic.
:::

::: {.proposition}
For $g \geq 2$, a curve of genus $g$ has a nonspecial very ample divisor of degree $d$ exactly when $d \geq g+3$, and then it embeds in $\PP^3$.
If the hyperplane section is special and $C$ is not planar, then $d \geq 6$ and $g \geq \tfrac{1}{2}d + 1$; the only such curve with $d=6$ is the canonical genus-$4$ curve.
:::

::: {.remark}
The useful way to organise this is by the speciality of $\OO_C(1)$.
Nonspecial hyperplane sections are the generic, well-understood case and are governed entirely by the degree bound $d \geq g+3$.
The special ones are rare, start at degree $6$, and are where the named curves sit.

That two curves with the same $(d,g)$ can be genuinely different is worth having an example for: degree $9$ and genus $10$ admits both the complete intersection of two cubics and the type-$(3,6)$ curve on a quadric.
They are distinguished by $h^0(\mci_C(2))$, which is $0$ for the first and $1$ for the second, and semicontinuity shows neither degenerates to the other.
Whether $\dim M^d_g$ is even known in general is a fair thing to admit: it is not.
:::
