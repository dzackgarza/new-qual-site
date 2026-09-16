---
schema: qual/card@1
id: P-AGHTHREECOMP
kind: problem
title: Decomposing $V(x^2-yz,\ xz-x)$ into irreducible components
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Prime Ideals
  - Varieties
relations:
- kind: uses
  target: PR-TNVSI
review: draft
---

::: {.problem}
Let $Y$ be the algebraic set in $\AA^3$ defined by the two polynomials $x^2 - yz$ and $xz - x$.
Show that $Y$ is a union of three irreducible components.
Describe them and find their prime ideals.
:::

::: {.solution}
Factor the second equation:
\[
Y = V(x^2 - yz) \intersect V(xz - x) = V(x^2-yz) \intersect \left( V(x) \union V(z-1) \right) .
\]
So a point of $Y$ has $x = 0$ or $z = 1$.

**Case $x = 0$.** Then $yz = 0$, so $y = 0$ or $z = 0$, giving the two lines
\[
V(x, y) \quad \text{and} \quad V(x, z) .
\]

**Case $z = 1$.** Then $x^2 = y$, giving the parabola $V(z - 1,\ x^2 - y)$.

Hence
\[
Y = V(x,y) \union V(x,z) \union V(z-1,\ x^2-y) ,
\]
two lines and a parabola.
Each is irreducible because its ideal is prime: the quotients are $k[z]$, $k[y]$ and $k[x]$ respectively, all domains.
None contains another, so these are the irreducible components.
:::
