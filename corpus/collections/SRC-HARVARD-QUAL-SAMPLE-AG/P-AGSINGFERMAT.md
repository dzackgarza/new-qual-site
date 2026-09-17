---
schema: qual/card@1
id: P-AGSINGFERMAT
kind: problem
title: Singularities of $X^3+Y^3+Z^3 = 3CXYZ$ in $\PP^2$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Singularities
  - Plane Curves
  - Hesse Pencil
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's question on the Hesse cubic X^3+Y^3+Z^3=3CXYZ.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Find the singularities, if any, of the curve in $\PP^2$ defined by
\[
X^3 + Y^3 + Z^3 = 3CXYZ .
\]
:::

::: {.solution}
Work over an algebraically closed field $k$ of characteristic different from $3$; in particular this covers the source's characteristic-zero setting.  Write
\[
c=C\in k
\]
and
\[
F=X^3+Y^3+Z^3-3cXYZ.
\]

<1>1. A point $[X:Y:Z]\in V(F)$ is singular exactly when
\[
X^2=cYZ,
\qquad
Y^2=cXZ,
\qquad
Z^2=cXY.
\]
::: {.proof}
Since $\operatorname{char}k\ne3$,
\[
\frac{\partial F}{\partial X}=3(X^2-cYZ),
\quad
\frac{\partial F}{\partial Y}=3(Y^2-cXZ),
\quad
\frac{\partial F}{\partial Z}=3(Z^2-cXY).
\]
The Jacobian criterion for a plane hypersurface gives precisely the displayed system.
:::

<1>2. At a singular point none of $X,Y,Z$ can vanish.
::: {.proof}
Suppose, for example, that $X=0$.  Then the equations in <1>1 give
\[
Y^2=0,
\qquad
Z^2=0,
\]
so $Y=Z=0$, impossible in projective space.  The same argument applies cyclically.
:::

<1>3. If the cubic is singular, then
\[
\boxed{c^3=1.}
\]
::: {.proof}
Multiply the three equations in <1>1:
\[
X^2Y^2Z^2
=c^3X^2Y^2Z^2.
\]
By <1>2 the product $XYZ$ is nonzero, so cancellation gives $c^3=1$.
:::

<1>4. If $c^3\ne1$, the cubic is smooth.
::: {.proof}
Step <1>3 shows that a singular point would force $c^3=1$.  Therefore no singular point exists when $c^3\ne1$.
:::

<1>5. Assume $c^3=1$.  The singular points are exactly
\[
\boxed{
P_\rho=
\left[1:\rho:\frac{\rho^2}{c}\right],
\qquad
\rho^3=1.
}
\]
Thus there are exactly three of them.
::: {.proof}
By <1>2 we may normalize $X=1$.  Put
\[
y=Y/X,
\qquad
z=Z/X.
\]
The singularity equations become
\[
1=cyz,
\qquad
y^2=cz,
\qquad
z^2=cy.
\]
Substituting $z=y^2/c$ into the first equation gives
\[
y^3=1.
\]
Thus $y=\rho$ for one of the three cube roots of unity and
\[
z=\frac{\rho^2}{c}.
\]
Conversely, if $\rho^3=1$ and $c^3=1$, direct substitution verifies all three equations in <1>1, so every displayed point is singular.
:::

<1>6. When $c^3=1$, the cubic factors as three distinct lines:
\[
\boxed{
F=
(X+Y+cZ)
(X+\omega Y+\omega^2cZ)
(X+\omega^2Y+\omega cZ),
}
\]
and $\omega$ is a primitive cube root of unity.
::: {.proof}
Because $c^3=1$, putting
\[
W=cZ
\]
gives
\[
F=X^3+Y^3+W^3-3XYW.
\]
The standard identity
\[
a^3+b^3+d^3-3abd
=(a+b+d)(a+\omega b+\omega^2d)(a+\omega^2b+\omega d)
\]
gives the factorization after substituting $d=W=cZ$.

The three linear forms are distinct because $1,\omega,\omega^2$ are distinct.
:::

<1>7. The three singularities in <1>5 are ordinary nodes, namely the three pairwise intersections of the lines in <1>6.
::: {.proof}
The three distinct lines in <1>6 have no common point: their coefficient matrix is a nonzero scalar multiple of the $3\times3$ Fourier matrix, whose determinant is nonzero because $1,\omega,\omega^2$ are distinct.

Hence each singular point lies on exactly two of the three components, and those two distinct lines meet transversely in $\mathbb P^2$.  Therefore each singularity is an ordinary double point.  There are three pairwise intersections, agreeing with the three points found in <1>5.
:::

<1>8. Therefore
\[
\boxed{
\begin{cases}
c^3\ne1 &: V(F)\text{ is smooth},\\
c^3=1 &: V(F)\text{ is a union of three lines with three nodal singularities }P_\rho.
\end{cases}
}
\]
::: {.proof}
Combine <1>4--<1>7.
:::

<1>9. Q.E.D.
::: {.proof}
Step <1>8 gives the complete singularity classification in characteristic different from $3$.
:::
:::

::: {.remark}
In characteristic $3$, the equation becomes
\[
X^3+Y^3+Z^3=(X+Y+Z)^3,
\]
independently of $c$, so the curve is a nonreduced triple line; this is why the characteristic assumption matters.
:::
