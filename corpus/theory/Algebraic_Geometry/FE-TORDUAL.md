---
schema: qual/card@1
id: FE-TORDUAL
kind: example
title: The affine toric variety of the cone on (2,1) and (1,4)
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Cones
  - Affine Varieties
relations:
- kind: uses
  target: D-Q7Q2N
review: draft
prompts:
- Compute the dual of a two-dimensional cone by rotating its ray generators.
- Compute the affine toric variety of the cone spanned by (2,1) and (1,4), with its equations.
---

::: {.example title="Dualising a plane cone"}
In the plane the dual of $\sigma = \Cone(v_1, v_2)$ is found by rotating each generator a quarter turn and orienting the result inwards.
Rotation by $\pi/2$ is
\[
e_1 \mapsto e_2, \quad e_2 \mapsto -e_1, \qquad R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} .
\]
For $v_1 = (2,1)$ and $v_2 = (1,4)$ this gives $R v_1 = (-1,2)$ and $R v_2 = (-4,1)$.
The second normal points out of the cone, so flip it to $(4,-1)$, and
\[
\sigma\dual = \Cone\big( (4,-1),\ (-1,2) \big) .
\]
Check the two pairings that must vanish: $\inp{(4,-1)}{(1,4)} = 4 - 4 = 0$ and $\inp{(-1,2)}{(2,1)} = -2 + 2 = 0$, so each of these is the inward normal to one wall.
:::

::: {.example title="The semigroup and its equations"}
The Hilbert basis of $S_\sigma = \sigma\dual \intersect M$ is
\[
(4,-1), \quad (1,0), \quad (0,1), \quad (-1,2) ,
\]
found by walking from one extremal ray to the other and keeping the lattice points that are not sums of earlier ones.
Write $u = x^4 y\inv$, $v = x$, $w = y$, $t = x\inv y^2$ for the corresponding characters.

Now read the additive relations straight off the exponent vectors:
\[
(4,-1) + (0,1) = (4,0) , \qquad (1,0) + (-1,2) = (0,2) , \qquad (4,-1) + (-1,2) = (3,1) ,
\]
that is $uw = v^4$, $vt = w^2$, and $ut = v^3 w$.
Hence
\[
X_\sigma = \Spec k[x^4 y\inv, x, y, x\inv y^2] = \Spec \frac{k[u,v,w,t]}{(uw - v^4,\ vt - w^2,\ ut - v^3 w)} ,
\]
a surface in $\AA^4$.
The three equations are the $2 \times 2$ minors of
\[
\begin{bmatrix} v & w & u \\ w & t & v^3 \end{bmatrix} ,
\]
so the singularity is determinantal, as every two-dimensional toric singularity is.
:::

::: {.remark}
The index $\abs{\det \begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix}} = 7$ is the whole story: $v_1, v_2$ generate a sublattice of index $7$ in $N$, so $X_\sigma$ is the cyclic quotient singularity $\AA^2 / \mu_7$ and $\Cl(X_\sigma) = \ZZ/7$.
An examiner asking for "a computation" wants the two steps above and nothing else: rotate to get $\sigma\dual$, list the lattice points, read the relations.
:::
