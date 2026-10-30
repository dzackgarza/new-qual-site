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
  by: claude-opus-5-5
  date: 2026-10-29
  note: Hartshorne III.10.8 allows every t and ends "This happens in any characteristic"; in characteristic 2 the conic is the double line (x+y)^2=0, and at t=0 the cone from the vertex on C is the plane z=0, not a member of the pencil limit XZ=0. The statement now assumes char k != 2 and t != 0, says the Y_t are members of the pencil, and omits the any-characteristic sentence.
---

::: {.problem}
Let $k$ be a field of characteristic $\neq 2$.
In affine $3\dash$space with coordinates $x, y, z$, let $C$ be the conic $(x-1)^2 + y^2 = 1$ in the $xy\dash$plane, and let $P$ be the point $(0,0,t)$ on the $z\dash$axis, with $t \neq 0$.
Let $Y_t$ be the closure in $\PP^3$ of the cone over $C$ with vertex $P$.

Show that as $t$ varies, the surfaces $\theset{Y_t}$ are members of a linear system of dimension $1$, with a moving singularity at $P$.
The base locus of this linear system is the conic $C$ plus the $z\dash$axis.
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
