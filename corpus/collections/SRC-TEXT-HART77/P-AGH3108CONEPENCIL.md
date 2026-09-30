---
schema: qual/card@1
id: P-AGH3108CONEPENCIL
kind: problem
title: A pencil of cones with a moving singularity in the base locus
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Bertini's Theorem
  - Base Loci
  - Quadric Cones
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.10.8 and derived the cone equation by eliminating the
    line parameter. The printed model has two genuine degeneracies: in
    characteristic two its conic is the double line (X+Y)^2=0 and its pencil
    collapses; at t=0 the literal cone from the vertex lying on C is the plane
    Z=0, whereas the pencil limit of the t!=0 cones is XZ=0. The proof below
    records the correct characteristic-not-two/nonzero-vertex calculation and
    gives a replacement smooth conic exhibiting the intended phenomenon in
    every characteristic.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
In affine $3\dash$space with coordinates $x, y, z$, let $C$ be the conic $(x-1)^2 + y^2 = 1$ in the $xy\dash$plane, and let $P$ be the point $(0,0,t)$ on the $z\dash$axis.
Let $Y_t$ be the closure in $\PP^3$ of the cone over $C$ with vertex $P$.

Show that as $t$ varies, the surfaces $\theset{Y_t}$ form a linear system of dimension $1$, with a moving singularity at $P$.
The base locus of this linear system is the conic $C$ plus the $z\dash$axis.

This happens in any characteristic.
:::

::: {.remark title="Erratum to the printed all-characteristic statement"}
There are two literal defects in the printed model.

First, in characteristic $2$,
$$
(x-1)^2+y^2=1
$$
reduces to
$$
(x+y)^2=0,
$$
so the displayed $C$ is a doubled line, not a nonsingular conic. The pencil
equation below also loses its second generator because its coefficient is
$2$.

Second, the origin $O=(0,0,0)$ lies on $C$. Thus the literal union of lines
joining $O$ to $C$ is just the plane $z=0$. It is not the $t=0$ member
$XZ=0$ of the pencil obtained as the flat/projective limit of the cones with
$t\ne0$.

Accordingly, the printed equations prove the intended moving-singularity
phenomenon for $\operatorname{char}k\ne2$ and $t\ne0$, with the complete
pencil obtained by projective closure in the parameter. The phenomenon itself
does occur in every characteristic: one may replace $C$ by the smooth conic
$$
xy+x+y=0,
$$
which gives the characteristic-free pencil constructed in step [](#s6){.pf-ref} below.
:::

::: {.solution}
Use homogeneous coordinates
$$
[X:Y:Z:W]
$$
on $\PP^3$, with affine chart $W=1$ carrying the coordinates $x,y,z$.
Let
$$
L=V(X,Y)
$$
be the projective $z$-axis.

::: pf

::: {.pf-step #s1}
Assume first that $\operatorname{char}k\ne2$. The projective closure of the printed conic is
$$
C=V(Z,Q),
\qquad
Q=X^2+Y^2-2XW.
$$

::: pf-proof
Homogenizing
$$
(x-1)^2+y^2=1
$$
gives
$$
X^2+Y^2-2XW=0
$$
in the plane $Z=0$.

Its gradient in that plane is
$$
(2X-2W,\ 2Y,\ -2X).
$$
Because $2\ne0$, these derivatives have no common projective zero on $Q=0$.
Thus $C$ is a nonsingular conic.
:::

:::

::: {.pf-step #s2}
For $t\ne0$, the cone over $C$ with vertex
$$
P_t=[0:0:t:1]
$$
is the quadric surface
$$
Y_t=V(F_t),
\qquad
F_t=tQ+2XZ.
$$

::: pf-proof
Take a point
$$
Q_0=(u,v,0)\in C
$$
on the affine chart. A point on the line joining $P_t$ to $Q_0$ has the form
$$
(x,y,z)=(\lambda u,\lambda v,(1-\lambda)t).
$$
Since $t\ne0$,
$$
\lambda=1-\frac zt.
$$
The conic equation
$$
u^2+v^2-2u=0
$$
therefore becomes
$$
\begin{aligned}
0
&=\lambda^2(u^2+v^2)-2\lambda^2u\\
&=x^2+y^2-2x\left(1-\frac zt\right).
\end{aligned}
$$
Multiplying by $t$ gives
$$
t(x^2+y^2-2x)+2xz=0,
$$
whose homogenization is precisely
$$
F_t=t(X^2+Y^2-2XW)+2XZ.
$$

Conversely, $V(F_t)$ contains $C$ and $P_t$, and the displayed calculation
shows every line $\overline{P_tQ_0}$ is contained in it. Both the union of
these lines and $V(F_t)$ are irreducible surfaces of degree two for $t\ne0$,
so they are equal.
:::

:::

::: {.pf-step #s3}
The nonzero-vertex cones lie in the pencil
$$
\Lambda=\PP\langle Q,\,XZ\rangle.
$$

::: pf-proof
Step [](#s2){.pf-ref} gives
$$
F_t=tQ+2XZ.
$$
Thus every $Y_t$ with $t\ne0$ is a member of the projective line of quadrics
spanned by $Q$ and $XZ$.
The two quadrics are linearly independent, so
$$
\boxed{\dim\Lambda=1}.
$$

As $t$ ranges through $k^\times$, the coefficient ratio $[t:2]$ ranges
through the open subset of $\Lambda$ where both coordinates are nonzero. Its
closure is the whole pencil. The missing boundary members are the expected
projective limits $Q=0$ and $XZ=0$.
:::

:::

::: {.pf-step #s4}
The set-theoretic base locus of the pencil is exactly
$$
C\cup L.
$$

::: pf-proof
The base locus is
$$
V(Q,XZ).
$$
If $Z=0$, the equation $Q=0$ cuts out precisely $C$.
If $X=0$, then
$$
Q=Y^2,
$$
so set-theoretically $Y=0$, giving the $z$-axis
$$
L=V(X,Y).
$$
Thus
$$
\boxed{|\operatorname{Bs}\Lambda|=C\cup L}.
$$
Every nonzero-vertex cone contains both: it contains $C$ by construction, and
it contains $L$ because $O=(0,0,0)\in C$ and the line joining $O$ to
$P_t$ is $L$.
:::

:::

::: {.pf-step #s5}
For $t\ne0$, the point $P_t$ is the unique singular point of $Y_t$.

::: pf-proof
The four partial derivatives of
$$
F_t=t(X^2+Y^2-2XW)+2XZ
$$
are
$$
(F_t)_X=2tX-2tW+2Z,
$$
$$
(F_t)_Y=2tY,
\qquad
(F_t)_Z=2X,
\qquad
(F_t)_W=-2tX.
$$
Since $2t\ne0$, simultaneous vanishing forces
$$
X=Y=0,
\qquad
Z=tW.
$$
Hence the only singular point is
$$
[0:0:t:1]=P_t.
$$
As $t$ varies through $k^\times$, this singular point moves along the
punctured affine part of the base line $L$.
:::

:::

::: {.pf-step #s6}
The intended phenomenon has an all-characteristic model.

::: pf-proof
Replace the printed conic by
$$
C'=V(Z,Q'),
\qquad
Q'=XY+XW+YW.
$$
On the affine chart $W=1$ this is
$$
xy+x+y=0.
$$

This conic is smooth in every characteristic. Indeed,
$$
(Q'_X,Q'_Y,Q'_W)=(Y+W,\ X+W,\ X+Y).
$$
If these three derivatives vanish, then $X=Y=-W$; substituting into $Q'$
gives $Q'=-W^2$ (which is $W^2$ in characteristic $2$), so no projective
point of $C'$ has all derivatives zero.

For $t\ne0$, the same line-parameter elimination as in step [](#s2){.pf-ref} gives the
cone with vertex $P_t$:
$$
Y'_t
=V\bigl(tQ'-Z(X+Y)\bigr).
$$
Thus the cones lie in the pencil
$$
\Lambda'=\PP\langle Q',\,Z(X+Y)\rangle,
$$
which has dimension one in every characteristic.

Its base locus is
$$
V(Q',Z(X+Y)).
$$
The component $Z=0$ gives $C'$. If $X+Y=0$, then
$$
Q'=XY=-X^2,
$$
so set-theoretically $X=Y=0$, giving again the axis $L$.
Hence
$$
|\operatorname{Bs}\Lambda'|=C'\cup L.
$$

Finally put
$$
F'_t=tQ'-Z(X+Y).
$$
Its derivatives are
$$
(F'_t)_X=t(Y+W)-Z,
$$
$$
(F'_t)_Y=t(X+W)-Z,
$$
$$
(F'_t)_Z=-(X+Y),
\qquad
(F'_t)_W=t(X+Y).
$$
At $P_t=[0:0:t:1]$ they all vanish.
Conversely, if all derivatives vanish, then $X+Y=0$ and
$$
Z=t(X+W)=t(Y+W).
$$
If $\operatorname{char}k\ne2$, these equations force $X=Y=0$.
If $\operatorname{char}k=2$, substituting $Y=X$ into $F'_t=0$ gives
$$
tX^2=0,
$$
so again $X=Y=0$ because $t\ne0$.
Then $Z=tW$, and the unique singular point is $P_t$.

Thus in every characteristic the pencil $\Lambda'$ has a singular point that
moves along the fixed base line $L$.
:::

:::

::: {.pf-step #s7}
The $t=0$ discrepancy in the printed model is exactly the pencil limit.

::: pf-proof
The origin
$$
O=[0:0:0:1]
$$
lies on the printed conic $C$. The literal geometric cone obtained by joining
$O$ to all points of $C$ lies entirely in the plane $Z=0$; since the secant
lines through a point of a nonsingular plane conic sweep the whole plane, that
cone is simply
$$
V(Z).
$$

By contrast, the $t\to0$ member of the pencil from step [](#s3){.pf-ref} is
$$
V(XZ)=V(X)\cup V(Z).
$$
Thus the pencil is the projective closure of the family of cones with
$t\ne0$, but its special member at parameter $t=0$ is not the literal cone
with vertex $O$. This is precisely the second defect stated in the erratum.
:::

:::

::: pf-qed
for the corrected statement.

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, and [](#s5){.pf-ref} prove the intended pencil, base-locus, and moving-singularity
claims for the printed model where that model is valid
($\operatorname{char}k\ne2$, $t\ne0$). Step [](#s6){.pf-ref} gives an explicit version
valid in every characteristic, and step [](#s7){.pf-ref} identifies the special
$t=0$ degeneration that prevents the literal printed family from being the
whole pencil.
:::

:::
:::
