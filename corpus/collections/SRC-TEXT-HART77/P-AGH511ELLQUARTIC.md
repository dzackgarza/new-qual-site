---
schema: qual/card@1
id: P-AGH511ELLQUARTIC
kind: problem
title: The elliptic quartic curve in $\PP^3$ projects to a plane cubic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Complete Intersections
  - Elliptic Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the two quadrics, projection, target cubic and omitted point with the retained Hartshorne I.5.11 transcription. Direct calculation shows the source needs characteristic different from 2: in characteristic 2 the fibre over the omitted cubic point is an entire line. The card states the intended hypothesis and records the counterexample.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Assume $\operatorname{char}k\ne2$.
Let $Y$ be the algebraic set in $\PP^3$ defined by the equations
$$
x^2 - xz - yw = 0, \qquad yz - xw - zw = 0.
$$
Let $P$ be the point $(x,y,z,w) = (0,0,0,1)$, and let $\varphi$ denote the projection from $P$ to the plane $w = 0$.
Show that $\varphi$ induces an isomorphism of $Y \sm\ts{P}$ with the plane cubic curve $y^2 z - x^3 + x z^2 = 0$ minus the point $(1,0,-1)$.
Then show that $Y$ is an irreducible nonsingular curve.

This $Y$ is called the *elliptic quartic curve* in $\PP^3$.
Since it is defined by two equations it is another example of a complete intersection.
:::

::: {.solution}
Put
$$
F_1=x^2-xz-yw,\qquad
F_2=yz-xw-zw,
$$
and let
$$
C=V(H)\subseteq\PP^2_{[x:y:z]},
\qquad
H=y^2z-x^3+xz^2.
$$
The projection from
$$
P=[0:0:0:1]
$$
is
$$
\varphi([x:y:z:w])=[x:y:z].
$$

<1>1. Projection maps $Y\setminus\{P\}$ into $C$.

::: {.proof}
On $Y$ the two equations can be rewritten
$$
yw=x(x-z),\qquad
(x+z)w=yz.
$$
Multiply the second equation by $y$ and use the first:
$$
y^2z
=yw(x+z)
=x(x-z)(x+z)
=x^3-xz^2.
$$
Thus
$$
H(x,y,z)=0.
$$
The only point of $\PP^3$ where the three projection coordinates vanish is $P$, so the projection is defined on $Y\setminus\{P\}$ and lands in $C$.
:::

<1>2. On the cubic $C$, the simultaneous equations
$$
y=0,\qquad x+z=0
$$
define the single point
$$
Q=[1:0:-1].
$$
For every point of $C\setminus\{Q\}$ there is a unique $w$ satisfying the two equations of $Y$.

::: {.proof}
The first assertion is immediate in projective coordinates.
For a point $q=[x:y:z]\in C$, the required $w$ must satisfy
$$
yw=x(x-z),\qquad
(x+z)w=yz.
$$
The compatibility determinant of these two linear equations in $w$ is
$$
y(yz)-(x+z)x(x-z)
=y^2z-x^3+xz^2
=H,
$$
so they are compatible on $C$.
Away from $Q$, the two coefficients $y$ and $x+z$ are not both zero, so the compatible system has a unique solution.

At $Q$, one has
$$
x(x-z)=1(1-(-1))=2\ne0,
$$
using $\operatorname{char}k\ne2$.
Thus no $w$ solves the first equation there.
Hence $Q$ has no preimage and every other point has exactly one.
:::

<1>3. The inverse to projection on $C\setminus\{Q\}$ is a morphism.

::: {.proof}
The opens
$$
D_+(y),\qquad D_+(x+z)
$$
cover $C\setminus\{Q\}$.
On the first define
$$
w=\frac{x(x-z)}{y},
$$
and on the second define
$$
w=\frac{yz}{x+z}.
$$
These are homogeneous degree-one expressions in the sense that scaling $[x:y:z]$ by $\lambda$ scales the resulting $w$ by $\lambda$.
Thus they define morphisms to $\PP^3$.
On the overlap they agree because the compatibility equation in step <1>2 is exactly
$$
\frac{x(x-z)}y=\frac{yz}{x+z}.
$$
The two local morphisms therefore glue to
$$
\psi:C\setminus\{Q\}\longrightarrow Y\setminus\{P\}.
$$
By construction $\varphi\psi$ is the identity.
For a point of $Y\setminus\{P\}$, its $w$ already satisfies the same two linear equations, whose solution is unique by step <1>2, so $\psi\varphi$ is also the identity.
Consequently
$$
\boxed{Y\setminus\{P\}\cong C\setminus\{Q\}.}
$$
:::

<1>4. The plane cubic $C$ is nonsingular and irreducible.

::: {.proof}
Its partial derivatives are
$$
H_x=-3x^2+z^2,\qquad
H_y=2yz,\qquad
H_z=y^2+2xz.
$$
Suppose all three vanish at a projective point of $C$.
Because $2\ne0$, the equation $H_y=0$ gives $y=0$ or $z=0$.

If $y=0$, then $H_z=2xz=0$.
If $x=0$, then $H_x=z^2$ forces $z=0$.
If $z=0$, then the cubic equation $H=-x^3=0$ forces $x=0$.
Either way there is no projective point.

If $z=0$, then $H_z=y^2$ forces $y=0$, and again $H=-x^3=0$ forces $x=0$.
This also covers characteristic $3$.
Hence $C$ has no singular point.

By [[P-AGH59NONVANISHIRRED]], a positive-degree homogeneous plane equation with nowhere-vanishing gradient on its zero set is irreducible.
Thus $C$ is a nonsingular irreducible cubic curve.
:::

<1>5. The algebraic set $Y$ is irreducible of dimension one.

::: {.proof}
By steps <1>3--<1>4, the open subset
$$
Y\setminus\{P\}
$$
is irreducible and one-dimensional.
Its closure is therefore an irreducible component $Y_0$ of $Y$.

Any other irreducible component would have empty intersection with $Y\setminus\{P\}$, hence would be contained in the singleton $\{P\}$.
But $\{P\}$ cannot be an irreducible component of an algebraic set cut out by two homogeneous equations in $\PP^3$.
Indeed, its affine-cone prime has height three in $k[x,y,z,w]$, whereas Krull's height theorem says that a minimal prime over an ideal generated by two elements has height at most two.
Thus no second component exists and
$$
Y=Y_0.
$$
Hence $Y$ is irreducible, and since the dense open subset $Y\setminus\{P\}$ is a curve, $\dim Y=1$.
:::

<1>6. The point $P$ is nonsingular on $Y$.

::: {.proof}
The Jacobian matrix of the two defining quadrics is
$$
\begin{pmatrix}
2x-z&-w&-x&-y\\
-w&z&y-w&-x-z
\end{pmatrix}.
$$
At
$$
P=[0:0:0:1]
$$
this becomes
$$
\begin{pmatrix}
0&-1&0&0\\
-1&0&-1&0
\end{pmatrix},
$$
which has rank two.
By step <1>5, $Y$ is a projective variety of dimension one.
The projective Jacobian criterion [[P-AGH58JACOBIANRANK]] requires rank
$$
3-1=2
$$
for nonsingularity.
Thus $P$ is nonsingular.
:::

<1>7. The projective curve $Y$ is nonsingular.

::: {.proof}
On $Y\setminus\{P\}$, step <1>3 identifies $Y$ with the open subset $C\setminus\{Q\}$ of the nonsingular cubic from step <1>4.
Thus every point away from $P$ is nonsingular.
Step <1>6 proves nonsingularity at $P$.
Therefore
$$
\boxed{Y\text{ is an irreducible nonsingular projective curve}.}
$$
This proves the asserted elliptic-quartic properties required in the exercise.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 establish the stated projection isomorphism, and steps <1>4--<1>7 prove that $Y$ is an irreducible nonsingular curve.
:::
:::

::: {.remark title="Characteristic two"}
The source does not exclude characteristic $2$, but the stated conclusion fails there.
At the target point
$$
Q=[1:0:-1]=[1:0:1]
$$
the two equations for $w$ become identities in characteristic $2$.
Consequently every point
$$
[1:0:1:w]\in\PP^3
$$
lies on $Y$, so the fibre over $Q$ is a whole line rather than being empty.
Thus the projection isomorphism and the irreducible elliptic-quartic conclusion require $\operatorname{char}k\ne2$ for these equations.
:::
