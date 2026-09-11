---
schema: qual/card@1
id: P-AGH73DUALCURVE
kind: problem
title: The dual curve $Y\dual \subseteq (\PP^2)\dual$ of a plane curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Intersection Theory
  - Morphisms
relations: []
review: draft
---

::: problem
Let $Y \subseteq \PP^2$ be a curve.
Regard the set of lines in $\PP^2$ as another projective space $(\PP^2)\dual$, taking $(a_0, a_1, a_2)$ as homogeneous coordinates of the line
$$
L: a_0 x_0 + a_1 x_1 + a_2 x_2 = 0.
$$

For each nonsingular point $P \in Y$, show that there is a unique line $T_P(Y)$ whose intersection multiplicity with $Y$ at $P$ is $> 1$.
This is the *tangent line* to $Y$ at $P$.

Show that the map $P \mapsto T_P(Y)$ defines a morphism from $\Reg Y$, the set of nonsingular points of $Y$, into $(\PP^2)\dual$.
The closure of the image of this morphism is called the *dual curve* $Y\dual \subseteq (\PP^2)\dual$ of $Y$.
:::
