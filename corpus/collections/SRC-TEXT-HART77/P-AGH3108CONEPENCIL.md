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
- event: source-checked
  by: claude
  date: 2026-11-09
  note: 'Read III.10.8 against Hartshorne p. 276 and Dongryul Kim, Solutions to Hartshorne, p. 203. Both printed defects are now recorded in the solution rather than in the statement: the statement is kept as printed, including "any characteristic" and every t, and the solution states that characteristic 2 makes C the double line and that at t=0 the cone is the plane z=0, which is not a member of the pencil <Q, XZ>. The earlier note on this card mentions a replacement smooth conic exhibiting the phenomenon in every characteristic; no such conic is part of the current solution.'
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Hartshorne III.10.8 allows every t and ends "This happens in any characteristic"; in characteristic 2 the conic is the double line (x+y)^2=0, and at t=0 the cone from the vertex on C is the plane z=0, not a member of the pencil limit XZ=0.'
---

::: {.problem}
A linear system with moving singularities contained in the base locus (any characteristic).

In affine $3\dash$space with coordinates $x, y, z$, let $C$ be the conic $(x-1)^2 + y^2 = 1$ in the $xy\dash$plane, and let $P$ be the point $(0,0,t)$ on the $z\dash$axis.
Let $Y_t$ be the closure in $\PP^3$ of the cone over $C$ with vertex $P$.
Show that as $t$ varies, the surfaces $\theset{Y_t}$ form a linear system of dimension $1$, with a moving singularity at $P$.
The base locus of this linear system is the conic $C$ plus the $z\dash$axis.
:::

::: {.solution}
Two hypotheses must be read into the printed statement.

First, in characteristic $2$ the equation $(x-1)^2+y^2=1$ becomes
$x^2+y^2=0$, that is $(x+y)^2=0$: the "conic" is a double line, and the cones over
it form a constant family, not a pencil. The computation below therefore assumes
$\operatorname{char}k\neq2$, as does the identification of $C$ with a nonsingular
conic in step [](#s1){.pf-ref}.

Second, at $t=0$ the vertex $P=(0,0,0)$ lies on $C$, so the cone with vertex $P$
over $C$ is the plane $z=0$ (the union of the lines joining $P$ to the points of
$C$), and a plane is not a member of the pencil $\Lambda$ of step [](#s3){.pf-ref},
whose members are the quadrics $tQ+2XZ$; the plane $Z=0$ arises there only in
combination with $X=0$, as the reducible quadric $XZ$. The pencil statement below
is therefore proved for $t\neq0$, and the parameter $t$ then identifies
$\GG_{m,k}$ with a dense open subset of $\Lambda$ whose closure is $\PP^1$.

With these two conventions the printed assertions hold, and the singular point
$P_t$ of $Y_t$ moves with $t$ inside the base locus.
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
The projective closure of the conic is
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

The parameter morphism $\GG_{m,k}\to\Lambda$ sends $t$ to $[t:2]$ and
identifies $\GG_{m,k}$ with the open subset where both coefficients are
nonzero. Its scheme-theoretic closure is the whole pencil. The two boundary
members are the projective limits $Q=0$ and $XZ=0$.
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
\boxed{\underlyingspace{\operatorname{Bs}\Lambda}=C\cup L}.
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

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, and [](#s5){.pf-ref} prove the pencil, base-locus, and moving-singularity
claims.
:::

:::
:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter III §10, Exercise 10.8, PDF p. 203, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he eliminates the line parameter to get $x^2-2x(w-t^{-1}z)+y^2=0$, i.e. the members $t(x^2+y^2-2xw)+2xz=0$ of the pencil $\langle x^2-2xw+y^2,\ -2xz\rangle$, identifies the base locus as the conic plus the $z$-axis, and remarks that characteristic $\neq2$ is needed "otherwise $(x-1)^2+y^2=1$ is $(x+y)^2=0$, so this is a constant linear system". The pencil, the base locus and the moving singularity agree with the proof above, which derives $F_t=tQ+2XZ$ and the singular point $[0:0:t:1]$ directly. Kim's remark is the first of the two conventions stated in the erratum at the start of the solution; the second, that at $t=0$ the cone degenerates to the plane $Z=0$ and so is not a member of the pencil, is not in his note.
:::
