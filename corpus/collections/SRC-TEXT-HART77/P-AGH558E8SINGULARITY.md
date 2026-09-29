---
schema: qual/card@1
id: P-AGH558E8SINGULARITY
kind: problem
title: The $E_8$ surface singularity $x^2+y^3+z^5=0$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Hartshorne V.5.8 transcription and collection context,
    and checked the target exceptional configuration against the local ADE
    surface-singularity card D-SRFADE. The retained Hartshorne solution
    attachment stops in Chapter IV, so there is no retained V.5.8 source
    solution to import. The proof below is therefore an independent chart
    calculation. For part (a), it checks t=-(u^2+v^3), identifies A[z^-1]
    with a localization of k[u,v], and supplies the prime-element argument
    needed to descend unique factorization across z. For part (b), it
    follows the singular points through all eight ordinary point blowups.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Recomputed every blowup chart and the exceptional-curve incidence.
    After the first two blowups the unique remaining singular point is the
    intersection of the first two exceptional lines. The third blowup
    separates them and produces one ordinary double point and one point
    with local equation X^2+zY(Y+z)=0. One blowup resolves the ordinary
    double point; blowing up the second point produces three ordinary
    double points, each resolved by one further blowup. Thus the count is
    3+1+1+3=8. Tracking the strict transforms gives final edges
    E1-E4-E3-E7-E5-E6-E2 and E5-E8, the displayed E8 diagram.
---

::: {.problem}
Let $k$ be an algebraically closed field, and let $X$ be the surface in $\AA_k^3$ defined by the equation $x^2+y^3+z^5=0$.
It has an isolated singularity at the origin $P=(0,0,0)$.

a. Show that the affine ring $A=k[x, y, z] /\left(x^2+y^3+z^5\right)$ of $X$ is a unique factorization domain, as follows.
Let $t=z^{-1}$; $u=t^3 x$, and $v=t^2 y$.
Show that $z$ is irreducible in $A$; $t \in k[u, v]$, and $A\left[z^{-1}\right]=k\left[u, v, t^{-1}\right]$.
Conclude that $A$ is a UFD.

b. Show that the singularity at $P$ can be resolved by eight successive blowings-up.
If $\tilde{X}$ is the resulting nonsingular surface, then the inverse image of $P$ is a union of eight projective lines, which intersect each other according to the Dynkin diagram $\mathbf{E}_8$:

\begin{tikzcd}
	\circ & \circ & \circ & \circ & \circ & \circ & \circ \\
	&&&& \circ
	\arrow[dash, from=1-1, to=1-2]
	\arrow[dash, from=1-2, to=1-3]
	\arrow[dash, from=1-3, to=1-4]
	\arrow[dash, from=1-4, to=1-5]
	\arrow[dash, from=1-5, to=1-6]
	\arrow[dash, from=1-6, to=1-7]
	\arrow[dash, from=1-5, to=2-5]
\end{tikzcd}
:::

::: {.solution}
::: pf

::: {.pf-step #z-is-prime}
Part (a): $A$ is a noetherian domain, and $z$ is a prime element of
$A$.

::: pf-proof
Put
$$
F=x^2+y^3+z^5.
$$
Regard $F$ as a polynomial in $x$ over
$$
K=k(y,z).
$$
If $F$ were reducible over $K$, then, since it has degree $2$ in $x$, it
would have a root in $K$. Thus
$$
-(y^3+z^5)
$$
would be a square in $K$.

The polynomial
$$
y^3+z^5\in k[y,z]
$$
is squarefree in every characteristic. Indeed, a repeated irreducible
factor would divide both partial derivatives whenever both are nonzero. In
characteristic $3$ the $z$-derivative is $5z^4\neq0$, and in
characteristic $5$ the $y$-derivative is $3y^2\neq0$; in all other
characteristics the two derivatives have no common nonconstant divisor
with $y^3+z^5$. Hence some irreducible factor of $y^3+z^5$ occurs with
valuation $1$, whereas every square in $K$ has even valuation at every
irreducible polynomial. Therefore $-(y^3+z^5)$ is not a square in $K$.

So $F$ is irreducible over $K$. By Gauss's lemma it is irreducible in the
UFD $k[x,y,z]$, hence prime there. Consequently
$$
A=k[x,y,z]/(F)
$$
is a domain. It is noetherian because it is a finitely generated
$k$-algebra.

Moreover,
$$
A/(z)\cong k[x,y]/(x^2+y^3).
$$
The polynomial $x^2+y^3$ is irreducible in $k[x,y]$: over $k(y)$ a
factorization would give a root, hence would make $-y^3$ a square, which
is impossible because its $y$-adic valuation is $3$. Thus $A/(z)$ is a
domain, so $(z)$ is prime in $A$. In particular $z$ is irreducible.
:::

:::

::: {.pf-step #coordinate-change-ufd}
Part (a): with
$$
t=z^{-1},
\qquad
u=t^3x,
\qquad
v=t^2y,
$$
one has
$$
\boxed{t=-(u^2+v^3)}
$$
and
$$
\boxed{A[z^{-1}]=k[u,v,t^{-1}].}
$$

::: pf-proof
In $A[z^{-1}]$ the defining equation gives
$$
u^2+v^3
=
t^6(x^2+y^3)
=
-t^6z^5
=
-t.
$$
Hence
$$
t=-(u^2+v^3)\in k[u,v].
$$

Certainly
$$
u,\ v,\ t^{-1}=z
$$
belong to $A[z^{-1}]$, so
$$
k[u,v,t^{-1}]\subseteq A[z^{-1}].
$$
Conversely,
$$
z=t^{-1},
\qquad
x=t^{-3}u=(t^{-1})^3u,
\qquad
y=t^{-2}v=(t^{-1})^2v,
$$
and $t\in k[u,v]$ by the preceding calculation. Thus every generator of
$A[z^{-1}]$ belongs to $k[u,v,t^{-1}]$, proving equality.

Equivalently,
$$
A[z^{-1}]
\cong
k[u,v,(u^2+v^3)^{-1}],
$$
via
$$
t=-(u^2+v^3).
$$
Indeed, starting with independent variables $U,V$ and putting
$$
T=-(U^2+V^3),
\qquad
z=T^{-1},
\qquad
x=T^{-3}U,
\qquad
y=T^{-2}V,
$$
gives
$$
x^2+y^3+z^5
=
T^{-6}(U^2+V^3+T)
=0.
$$
This defines an inverse to the map sending $U,V$ to $u,v$, so the
displayed isomorphism is genuine and in particular $u,v$ are
algebraically independent.
This is a localization of the polynomial UFD $k[u,v]$, hence is a UFD.
:::

:::

::: {.pf-step #a-is-ufd}
Part (a): $A$ is a unique factorization domain.

::: pf-proof
We use the prime element $z$ from step [](#z-is-prime){.pf-ref} and the UFD
$$
A[z^{-1}]
$$
from step [](#coordinate-change-ufd){.pf-ref}.

Because $A$ is noetherian, every nonzero nonunit of $A$ factors into
irreducibles. It remains to prove that every irreducible of $A$ is prime.
Let $p\in A$ be irreducible.

If $p$ is associate to $z$, then $p$ is prime because $z$ is prime.
Assume therefore that $p$ is not associate to $z$.

First, $p$ remains irreducible in $A[z^{-1}]$. Suppose
$$
p=\frac{a}{z^m}\frac{b}{z^n}
$$
in $A[z^{-1}]$. Since $A$ is a domain,
$$
z^{m+n}p=ab.
$$
As long as a factor $z$ remains on the left, primality of $z$ implies
that $z$ divides $a$ or $b$; cancel such a factor. After $m+n$
cancellations we obtain
$$
p=a'b'
$$
with $a',b'\in A$. Irreducibility of $p$ makes one of $a',b'$ a unit in
$A$. The corresponding factor $a/z^m$ or $b/z^n$ is therefore a unit in
$A[z^{-1}]$. Hence $p$ is irreducible in $A[z^{-1}]$.

Since $A[z^{-1}]$ is a UFD, $p$ is prime there. Now suppose
$$
p\mid ab
$$
in $A$. In $A[z^{-1}]$, primality gives
$$
p\mid a
\qquad\text{or}\qquad
p\mid b.
$$
Assume the first. Then for some $c\in A$ and $n\geq0$,
$$
z^na=pc.
$$
If $n>0$, the left side is divisible by $z$. Since $z$ is prime and
$z\nmid p$ (otherwise irreducibility of $p$ would make $p$ associate to
$z$), one has $z\mid c$. Cancel one factor of $z$ and repeat. After $n$
steps,
$$
a=pc'
$$
for some $c'\in A$. Thus $p\mid a$ already in $A$. The same argument
applies if $p\mid b$ in the localization.

Therefore every irreducible of $A$ is prime. Since $A$ is atomic, $A$ is
a UFD.
:::

:::

::: {.pf-step #first-blowup-singular-locus}
Part (b): after the first blowup, the only singular point of the
strict transform lies on one exceptional line $E_1$.

::: pf-proof
Blow up the origin of
$$
X:\quad x^2+y^3+z^5=0.
$$
The origin is the only singular point of $X$. In characteristics different
from $2,3,5$ this follows immediately from the three partial derivatives.
In characteristic $2$, the $y$- and $z$-derivatives force $y=z=0$, and
then the equation forces $x=0$; in characteristic $3$, the $x$- and
$z$-derivatives force $x=z=0$ and then $y=0$; in characteristic $5$, the
$x$- and $y$-derivatives force $x=y=0$ and then $z=0$.

In the $x$-chart, with
$$
y=xy_1,
\qquad
z=xz_1,
$$
the strict transform is
$$
1+xy_1^3+x^3z_1^5=0,
$$
so it does not meet the exceptional divisor.

In the $y$-chart, with
$$
x=yx_1,
\qquad
z=yz_1,
$$
the strict transform is
$$
x_1^2+y+y^3z_1^5=0.
$$
Along the exceptional divisor $y=0$ its derivative with respect to $y$
is $1$, so this chart is nonsingular along the exceptional locus.

In the $z$-chart, with
$$
x=zx_1,
\qquad
y=zy_1,
$$
the strict transform is
$$
X_1:\quad x_1^2+zy_1^3+z^3=0.
$$
Its reduced exceptional curve is
$$
E_1:\quad z=x_1=0,
$$
in this affine chart; together with its piece in the $y$-chart it is the
projective line $E_1\cong\PP^1$. Along $E_1$, the derivative with respect to $z$ is
$y_1^3$, so the only singular point on $E_1$ is
$$
x_1=y_1=z=0.
$$
Away from the exceptional divisor the blowup is an isomorphism, so this
is the only singular point of the first strict transform.
:::

:::

::: {.pf-step #second-blowup-singular-locus}
After the second blowup, the reduced exceptional locus is
$$
E_1\cup E_2,
$$
and its unique singular point is $E_1\cap E_2$.

::: pf-proof
Rename the coordinates in the singular chart of step [](#first-blowup-singular-locus){.pf-ref} as
$$
x,y,z,
$$
so the equation is
$$
x^2+zy^3+z^3=0.
$$
Blow up its origin.

The $x$-chart again misses the exceptional locus of the strict transform.
In the $z$-chart the strict transform is
$$
x_2^2+z+z^2y_2^3=0,
$$
which is nonsingular along $z=0$ because the $z$-derivative is $1$ there.

In the $y$-chart, with
$$
x=yx_2,
\qquad
z=yz_2,
$$
the strict transform is
$$
X_2:\quad x_2^2+y^2z_2+yz_2^3=0.
$$
The new reduced exceptional curve is
$$
E_2:\quad y=x_2=0,
$$
in this affine chart; globally it is a projective line
$E_2\cong\PP^1$.
and the strict transform of $E_1$ is
$$
E_1:\quad z_2=x_2=0.
$$
They meet at the origin. Along $E_2$, the derivative of the equation
with respect to $y$ is $z_2^3$ at $y=0$, so the only singular point there
is $z_2=0$. Thus the unique remaining singular point is precisely
$$
E_1\cap E_2.
$$
:::

:::

::: {.pf-step #third-blowup-two-points}
The third blowup separates $E_1$ and $E_2$, introduces a projective
line $E_3$, and leaves exactly two singular points: an ordinary double
point at $E_1\cap E_3$ and a point with local equation
$X^2+zY(Y+z)=0$ at $E_2\cap E_3$.

::: pf-proof
Rename the coordinates in step [](#second-blowup-singular-locus){.pf-ref} as $x,y,z$, so
$$
X_2:\quad x^2+y^2z+yz^3=0.
$$
Blow up the origin.

In the $y$-chart,
$$
x=yX,
\qquad
z=yZ,
$$
and the strict transform is
$$
X^2+yZ+y^2Z^3=0.
$$
The only singular point on the exceptional curve $y=X=0$ is the origin.
Its quadratic tangent cone is
$$
X^2+yZ=0,
$$
which is a nonsingular conic in $\PP^2$. Hence this is an ordinary double
point. This point is the intersection of the strict transform of $E_1$
with the new exceptional line $E_3$.

In the $z$-chart,
$$
x=zX,
\qquad
y=zY,
$$
and the strict transform is
$$
X^2+zY^2+z^2Y
=
X^2+zY(Y+z)
=0.
$$
Again the only singular point on the exceptional curve $z=X=0$ is the
origin, with exact local equation
$$
X^2+zY(Y+z)=0.
$$
It is the intersection of the strict transform of $E_2$ with $E_3$.

Thus after the third blowup the incidence graph of the old exceptional
curves is
$$
E_1-E_3-E_2,
$$
with the two displayed intersection points still singular.
:::

:::

::: {.pf-step #resolve-ordinary-double-point-e1e3}
Blowing up the ordinary double point $E_1\cap E_3$ once resolves
that point and inserts a projective line $E_4$ between $E_1$ and $E_3$.

::: pf-proof
At this point the local equation has quadratic tangent cone
$$
X^2+yZ=0,
$$
a nonsingular conic in $\PP^2$. The blowup of an ordinary double point
with nonsingular projectivized tangent cone is nonsingular, and its
exceptional curve is exactly that conic. Hence the fourth blowup resolves
this singularity and introduces
$$
E_4\cong\PP^1.
$$

The strict transforms of $E_1$ and $E_3$ meet the conic in the two
distinct tangent directions
$$
[0:1:0]
\qquad\text{and}\qquad
[0:0:1].
$$
Thus this blowup replaces the edge $E_1-E_3$ by
$$
E_1-E_4-E_3.
$$
:::

:::

::: {.pf-step #e5-three-double-points}
Blowing up the point $E_2\cap E_3$ with local equation
$X^2+zY(Y+z)=0$ introduces a projective line $E_5$ carrying exactly
three ordinary double points.

::: pf-proof
Use the exact local equation from step [](#third-blowup-two-points){.pf-ref}:
$$
X^2+zY(Y+z)=0.
$$
Blow up its origin.

In the $Y$-chart, with
$$
X=YU,
\qquad
z=YZ,
$$
the strict transform is
$$
U^2+YZ(1+Z)=0.
$$
Along the exceptional line $Y=U=0$, singular points occur exactly when
$$
Z(1+Z)=0,
$$
namely at
$$
Z=0
\qquad\text{and}\qquad
Z=-1.
$$

In the $z$-chart, with
$$
X=zU,
\qquad
Y=zV,
$$
the strict transform is
$$
U^2+zV(1+V)=0.
$$
Along the exceptional line $z=U=0$, singular points occur at
$$
V=0
\qquad\text{and}\qquad
V=-1.
$$
The points $Z=-1$ and $V=-1$ are the same point on the overlap. Hence
there are exactly three singular points on the new exceptional line
$$
E_5\cong\PP^1.
$$

Near each of them the factor multiplying the transverse coordinate is a
unit times a local parameter, so the quadratic tangent cone is
$$
U^2+ab=0.
$$
Thus all three are ordinary double points.

The point $Z=0$ is where the strict transform of $E_3$ meets $E_5$, the
point $V=0$ is where the strict transform of $E_2$ meets $E_5$, and the
third point is a free point of $E_5$.
:::

:::

::: {.pf-step #resolve-remaining-three-points}
Three further blowups resolve the three ordinary double points on
$E_5$ and produce projective lines $E_6,E_7,E_8$.

::: pf-proof
Blow up the ordinary double point
$$
E_2\cap E_5.
$$
As in step [](#resolve-ordinary-double-point-e1e3){.pf-ref}, this resolves that point and inserts a smooth conic
$$
E_6\cong\PP^1
$$
between $E_2$ and $E_5$.

Next blow up
$$
E_3\cap E_5.
$$
This inserts
$$
E_7\cong\PP^1
$$
between $E_3$ and $E_5$.

Finally blow up the third ordinary double point, which lies only on
$E_5$. This introduces
$$
E_8\cong\PP^1
$$
meeting $E_5$ once.

Each ordinary double point is resolved by its single blowup, and the
three points are distinct. Therefore after these three blowups the strict
transform is nonsingular.
:::

:::

::: {.pf-step #eight-blowups-e8-diagram}
The resolution uses exactly eight successive point blowups, and
the reduced inverse image of $P$ has dual graph $\mathbf E_8$.

::: pf-proof
The number of blowups is
$$
3+1+1+3=8:
$$
three blowups reach the two remaining singular points, one resolves the
ordinary double point, one blows up the point with equation
$X^2+zY(Y+z)=0$, and three resolve the resulting ordinary double points.

Tracking incidences through the blowups gives precisely the edges
$$
E_1-E_4-E_3-E_7-E_5-E_6-E_2
$$
and the additional edge
$$
E_5-E_8.
$$
Thus the seven curves
$$
E_1,E_4,E_3,E_7,E_5,E_6,E_2
$$
form a chain, and $E_8$ meets the fifth curve $E_5$ in that chain. There
are no other intersections. Hence the reduced inverse image of $P$ is a
union of eight projective lines with incidence diagram
$$
\begin{tikzcd}
\circ & \circ & \circ & \circ & \circ & \circ & \circ \\
&&&& \circ
\arrow[dash, from=1-1, to=1-2]
\arrow[dash, from=1-2, to=1-3]
\arrow[dash, from=1-3, to=1-4]
\arrow[dash, from=1-4, to=1-5]
\arrow[dash, from=1-5, to=1-6]
\arrow[dash, from=1-6, to=1-7]
\arrow[dash, from=1-5, to=2-5]
\end{tikzcd}
$$
which is the Dynkin diagram $\mathbf E_8$.
:::

:::

::: pf-qed
Steps [](#z-is-prime){.pf-ref}, [](#coordinate-change-ufd){.pf-ref} and [](#a-is-ufd){.pf-ref} prove part (a). Steps [](#first-blowup-singular-locus){.pf-ref}, [](#second-blowup-singular-locus){.pf-ref}, [](#third-blowup-two-points){.pf-ref}, [](#resolve-ordinary-double-point-e1e3){.pf-ref}, [](#e5-three-double-points){.pf-ref}, [](#resolve-remaining-three-points){.pf-ref} and [](#eight-blowups-e8-diagram){.pf-ref} give the eight
successive blowups, prove smoothness after the eighth, and identify the
exceptional incidence graph required in part (b).
:::

:::
:::
