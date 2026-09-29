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
Work over an algebraically closed field $k$ of characteristic different from $3$, for instance of characteristic $0$.  Write
\[
c=C\in k
\]
and
\[
F=X^3+Y^3+Z^3-3cXYZ.
\]

::: pf

::: {.pf-step #singularity-equations}
A point $[X:Y:Z]\in V(F)$ is singular exactly when
\[
X^2=cYZ,
\qquad
Y^2=cXZ,
\qquad
Z^2=cXY.
\]

::: pf-proof
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

:::

::: {.pf-step #nonvanishing-coordinates}
At a singular point none of $X,Y,Z$ can vanish.

::: pf-proof
Suppose, for example, that $X=0$.  Then the equations in step [](#singularity-equations){.pf-ref} give
\[
Y^2=0,
\qquad
Z^2=0,
\]
so $Y=Z=0$, impossible in projective space.  The same argument applies cyclically.
:::

:::

::: {.pf-step #c-cubed-one}
If the cubic is singular, then
\[
\boxed{c^3=1.}
\]

::: pf-proof
Multiply the three equations in step [](#singularity-equations){.pf-ref}:
\[
X^2Y^2Z^2
=c^3X^2Y^2Z^2.
\]
By step [](#nonvanishing-coordinates){.pf-ref} the product $XYZ$ is nonzero, so cancellation gives $c^3=1$.
:::

:::

::: {.pf-step #smooth-case}
If $c^3\ne1$, the cubic is smooth.

::: pf-proof
Step [](#c-cubed-one){.pf-ref} shows that a singular point would force $c^3=1$.  Therefore no singular point exists when $c^3\ne1$.
:::

:::

::: {.pf-step #singular-points-list}
Assume $c^3=1$.  The singular points are exactly
\[
\boxed{
P_\rho=
\left[1:\rho:\frac{\rho^2}{c}\right],
\qquad
\rho^3=1.
}
\]
Thus there are exactly three of them.

::: pf-proof
By step [](#nonvanishing-coordinates){.pf-ref} we may normalize $X=1$.  Put
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
Conversely, if $\rho^3=1$ and $c^3=1$, direct substitution verifies all three equations in step [](#singularity-equations){.pf-ref}, so every displayed point is singular.
:::

:::

::: {.pf-step #line-factorization}
When $c^3=1$, the cubic factors as three distinct lines:
\[
\boxed{
F=
(X+Y+cZ)
(X+\omega Y+\omega^2cZ)
(X+\omega^2Y+\omega cZ),
}
\]
and $\omega$ is a primitive cube root of unity.

::: pf-proof
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

:::

::: {.pf-step #nodal-singularities}
The three singularities in step [](#singular-points-list){.pf-ref} are ordinary nodes, namely the three pairwise intersections of the lines in step [](#line-factorization){.pf-ref}.

::: pf-proof
The three distinct lines in step [](#line-factorization){.pf-ref} have no common point: their coefficient matrix is a nonzero scalar multiple of the $3\times3$ Fourier matrix, whose determinant is nonzero because $1,\omega,\omega^2$ are distinct.

Hence each singular point lies on exactly two of the three components, and those two distinct lines meet transversely in $\mathbb P^2$.  Therefore each singularity is an ordinary double point.  There are three pairwise intersections, agreeing with the three points found in step [](#singular-points-list){.pf-ref}.
:::

:::

::: {.pf-step #classification-summary}
Therefore
\[
\boxed{
\begin{cases}
c^3\ne1 &: V(F)\text{ is smooth},\\
c^3=1 &: V(F)\text{ is a union of three lines with three nodal singularities }P_\rho.
\end{cases}
}
\]

::: pf-proof
Combine steps [](#smooth-case){.pf-ref}, [](#singular-points-list){.pf-ref}, [](#line-factorization){.pf-ref} and [](#nodal-singularities){.pf-ref}.
:::

:::

::: pf-qed
Step [](#classification-summary){.pf-ref} gives the complete singularity classification in characteristic different from $3$.
:::

:::
:::

::: {.remark}
In characteristic $3$, the equation becomes
\[
X^3+Y^3+Z^3=(X+Y+Z)^3,
\]
independently of $c$, so the curve is the line $X+Y+Z=0$ with multiplicity three, and every point of it is singular.
:::
