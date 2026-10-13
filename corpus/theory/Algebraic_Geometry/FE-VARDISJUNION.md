---
schema: qual/card@1
id: FE-VARDISJUNION
kind: example
title: The coordinate ring of a plane and a disjoint line
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coordinate Rings
  - Irreducibility
  - Chinese Remainder Theorem
relations:
- kind: uses
  target: PR-7OT2Z
review: draft
prompts:
- Compute the ideal and the coordinate ring of the union of a plane and a line disjoint from it.
---

::: {.example}
In $\AA^3_\CC$ with coordinates $x, y, z$, let $X_1 = V(x, z-1)$ be the line through $(0,0,1)$ parallel to the $y$-axis, let $X_2 = V(z)$ be the $xy$-plane, and let $X = X_1 \cup X_2$.

![The line $X_1 = V(x, z-1)$ through $(0,0,1)$ and the plane $X_2 = V(z)$.](../../../assets/algebraic-geometry/varieties/plane-and-disjoint-parallel-line.png){width=350px}

The two ideals are comaximal:
$$
I(X_1)+I(X_2)=(x,z-1)+(z)=(1).
$$
Thus the Chinese remainder theorem gives $I(X)=I(X_1)\cap I(X_2)=I(X_1)I(X_2)$, so
$$
I(X)=(x,z-1)(z)=(xz,z^2-z).
$$
The coordinate ring decomposes as
$$
\CC[X]=\frac{\CC[x,y,z]}{(xz,z^2-z)}
\cong\frac{\CC[x,y,z]}{(x,z-1)}\times\frac{\CC[x,y,z]}{(z)}
\cong\CC[y]\times\CC[x,y].
$$
:::
