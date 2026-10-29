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
- Classify the curves of degree at most $7$ in $\PP^3$.
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

- $d=7$: the plane septic with $g=15$; nonspecial curves of every genus $g \leq 4$; curves of genus $5$; and curves of genus $6$, the maximum allowed by Castelnuovo's bound, which all lie on a quadric, for instance the curves of type $(3,4)$ on a smooth quadric.
:::

::: {.example title="Degree $7$ and genus $5$"}
Let $X$ have genus $5$ and $P \in X$.
Since $\abs{K}$ is base-point free, $D = K - P$ has degree $7$ and $h^0(D) = 4$.
By the very-ampleness criterion and Serre duality, $D$ is very ample exactly when $h^0(P + Q + R) = 1$ for all $Q, R \in X$.
If $X$ has no $g^1_3$ this holds for every $P$, and $\abs{K - P}$ embeds $X$ in $\PP^3$ as a curve of degree $7$; curves of genus $5$ without a $g^1_3$ exist, so $(d, g) = (7, 5)$ occurs.
The hyperplane section $K - P$ is special, in accordance with $g \geq \tfrac{1}{2} d + 1$.
[@Har10a]
:::

::: {.proposition}
For $g \geq 2$, a curve of genus $g$ has a nonspecial very ample divisor of degree $d$ exactly when $d \geq g+3$, and then it embeds in $\PP^3$.
If the hyperplane section is special and $C$ is not planar, then $d \geq 6$ and $g \geq \tfrac{1}{2}d + 1$; the only such curve with $d=6$ is the canonical genus-$4$ curve.
:::

::: {.remark}
The classification separates according to the speciality of $\OO_C(1)$.
Nonspecial hyperplane sections satisfy the degree bound $d\ge g+3$.
Special hyperplane sections first occur in the low-degree list at degree $6$ and include the named canonical examples above.

Two curves with the same $(d,g)$ can be different: for degree $9$ and genus $10$, [[FE-CRVQUAD]] separates the complete intersection of two cubics from the type-$(3,6)$ curve on a quadric by $h^0(\mci_C(2))$.
By semicontinuity of $h^0(\mci_C(2))$, in a flat family whose general member lies on a quadric every member lies on a quadric, so a type-$(3,6)$ curve does not degenerate to a complete intersection of two cubics.
:::
