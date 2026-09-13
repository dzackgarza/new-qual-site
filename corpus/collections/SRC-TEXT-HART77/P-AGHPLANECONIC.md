---
schema: qual/card@1
id: P-AGHPLANECONIC
kind: problem
title: Coordinate rings of the parabola, the hyperbola, and any conic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coordinate Rings
  - Plane Curves
  - Conics
relations:
- kind: uses
  target: PR-7OT2Z
review: draft
---

::: problem
(a) Let $Y$ be the plane curve $y = x^2$, the zero set of $f = y - x^2$.
Show that $A(Y)$ is isomorphic to a polynomial ring in one variable over $k$.

(b) Let $Z$ be the plane curve $xy = 1$.
Show that $A(Z)$ is not isomorphic to a polynomial ring in one variable over $k$.

(c) Let $f$ be any irreducible quadratic polynomial in $k[x,y]$, and let $W$ be the conic it defines.
Show that $A(W)$ is isomorphic to $A(Y)$ or to $A(Z)$.
Which one, and when?
:::

::: solution
**(a)** $A(Y) = k[x,y]/\gens{y-x^2} \cong k[t,t^2] \cong k[t]$.

**(b)** $A(Z) = k[x,y]/\gens{xy-1} \cong k[x^{\pm 1}]$.
This is not a polynomial ring: it contains the unit $x\inv \notin k$, while the units of $k[t]$ are exactly $k^*$.

**(c)** An affine change of coordinates reduces $F$ to one of the two cases above.
Write the conic as
\[
F(x,y) = \tv{x, y, 1}^t
\begin{pmatrix}
A & B/2 & D/2 \\
B/2 & C & E/2 \\
D/2 & E/2 & F
\end{pmatrix}
\tv{x, y, 1} .
\]
The matrix is symmetric, so it diagonalises, and the corresponding affine change of coordinates puts $F$ in the form $\lambda_1 x^2 + \lambda_2 y^2 + \lambda_3$.

Which case appears is decided by whether the conic is degenerate at infinity: the parabola $y = x^2$ meets the line at infinity in one point, the hyperbola $xy = 1$ in two.
So $A(W) \cong A(Y)$ when the conic is tangent to the line at infinity, and $A(W) \cong A(Z)$ otherwise.
:::
