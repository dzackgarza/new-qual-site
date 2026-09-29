---
schema: qual/card@1
id: P-AGH4311PROJECTIONCLOSEDIMMERSION
kind: problem
title: Projection embeds a smooth $r$-fold into $\PP^{n-1}$ when $n>2r+1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Very Ample Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.11 together with the projection/linear-system
    criterion II.7.3 and the Veronese construction II.7.7. Part (a) uses
    separate secant and embedded-tangent-space incidence bounds. Part (b)
    reduces each secant to the plane conic obtained from the corresponding
    line in P^2 and checks the lower dimension bound for the secant variety by
    an explicit four-rank local parametrization, valid in every
    characteristic.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
a. If $X$ is a nonsingular variety of dimension $r$ in $\PP^n$, and if $n>2r+1$, show that there is a point $O \notin X$, such that the projection from $O$ induces a closed immersion of $X$ into $\PP^{n-1}$.

b. If $X$ is the Veronese surface in $\PP^5$, which is the 2-uple embedding of $\PP^2$ (I, Ex.
2.13), show that each point of every secant line of $X$ lies on infinitely many secant lines.
Therefore, the secant variety of $X$ has dimension 4, and so in this case there is a projection which gives a closed immersion of $X$ into $\PP^4$ (II, Ex.
7.7).

A theorem of Severi states that the Veronese surface is the only surface in $\PP^5$ for which there is a projection giving a closed immersion into $\PP^4$.
Usually one obtains a finite number of double points with transversal tangent planes.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let
$$
\Sigma_{\mathrm{sec}}
$$
be the union of secant lines
$$
\overline{PQ},
\qquad
P,Q\in X,\quad P\ne Q.
$$
Its closure in $\PP^n$ has dimension at most
$$
2r+1.
$$

::: pf-proof

Over
$$
(X\times X)\setminus\Delta
$$
consider the incidence variety
$$
\mathcal S
=
\{(P,Q,O):O\in\overline{PQ}\}.
$$
For every ordered pair $(P,Q)$, the fibre is the projective line
$\overline{PQ}$. Hence
$$
\dim\mathcal S
=
2r+1.
$$
The image of $\mathcal S$ is the union of secant lines, so the dimension of
its closure satisfies
$$
\dim\overline{\Sigma_{\mathrm{sec}}}
\le
2r+1.
$$

:::

:::

::: {.pf-step #s2}

Let
$$
\Sigma_{\mathrm{tan}}
=
\bigcup_{P\in X}T_PX
$$
be the union of the embedded projective tangent spaces. Then
$$
\dim\overline{\Sigma_{\mathrm{tan}}}\le2r.
$$

::: pf-proof

Since $X$ is nonsingular of dimension $r$, each embedded tangent space
$$
T_PX
\subseteq
\PP^n
$$
is a projective $r$-plane.
The tangent-space incidence
$$
\mathcal T
=
\{(P,O)\in X\times\PP^n:O\in T_PX\}
$$
is the projectivization of a rank-$(r+1)$ vector bundle over $X$ and hence
has dimension
$$
r+r=2r.
$$
Its image is $\Sigma_{\mathrm{tan}}$, giving the stated bound.

:::

:::

::: {.pf-step #s3}

There is a point
$$
O\in\PP^n
\setminus
\left(
X
\cup
\overline{\Sigma_{\mathrm{sec}}}
\cup
\overline{\Sigma_{\mathrm{tan}}}
\right).
$$

::: pf-proof

By hypothesis
$$
n>2r+1.
$$
Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} show that the two closed secant and tangent loci have
dimension strictly smaller than $n$, and
$$
\dim X=r<n.
$$
Their finite union is therefore a proper closed subset of the irreducible
space $\PP^n$. Choose $O$ in its complement.

:::

:::

::: {.pf-step #s4}

Projection from the point $O$ in step [](#s3){.pf-ref} separates points of $X$.

::: pf-proof

Let
$$
\pi_O:X\longrightarrow\PP^{n-1}
$$
be the projection from $O$. It is defined everywhere because $O\notin X$.

If distinct points
$$
P,Q\in X
$$
had the same image, then $O,P,Q$ would lie on one line, so
$$
O\in\overline{PQ}\subseteq\Sigma_{\mathrm{sec}},
$$
contrary to step [](#s3){.pf-ref}. Hence $\pi_O$ is injective on closed points, which is
the point-separation condition for the corresponding subsystem of
$H^0(X,\mco_X(1))$.

:::

:::

::: {.pf-step #s5}

Projection from $O$ separates tangent vectors of $X$.

::: pf-proof

Fix
$$
P\in X.
$$
The differential of linear projection
$$
d\pi_O:T_PX_{\mathrm{aff}}\longrightarrow
T_{\pi_O(P)}\PP^{n-1}
$$
has a nonzero kernel exactly when the projective center $O$ lies in the
embedded projective tangent space
$$
T_PX.
$$
Indeed, the kernel direction is the infinitesimal direction of the line from
$P$ toward the center of projection.

Step [](#s3){.pf-ref} gives
$$
O\notin T_PX
$$
for every $P$. Thus every tangent map is injective, so the projected linear
system separates tangent vectors.

:::

:::

::: {.pf-step #s6}

The projection
$$
\pi_O:X\longrightarrow\PP^{n-1}
$$
is a closed immersion.

::: pf-proof

Projection from $O$ is the morphism defined by the base-point-free
codimension-one subsystem of hyperplane sections consisting of hyperplanes
through $O$.
Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} show that this system separates points and tangent vectors.
The [[T-DIVMAPPN|closed-immersion criterion for a linear system]]
therefore gives
$$
\boxed{\pi_O\text{ is a closed immersion}.}
$$
This proves (a).

:::

:::

::: {.pf-step #s7}

Now let
$$
\nu_2:\PP^2\longrightarrow X\subseteq\PP^5
$$
be the quadratic Veronese embedding. Every secant line to $X$ is contained
in the plane of a Veronese conic.

::: pf-proof

Let a secant line join the two distinct points
$$
\nu_2(P),\nu_2(Q),
\qquad
P,Q\in\PP^2.
$$
Let
$$
\ell=\overline{PQ}\subseteq\PP^2.
$$
The restriction
$$
\nu_2|_\ell:\ell\cong\PP^1\longrightarrow\PP^5
$$
is the complete quadratic Veronese embedding of $\PP^1$.
Its image
$$
C=\nu_2(\ell)
$$
is a nonsingular plane conic spanning a plane
$$
\Pi\cong\PP^2.
$$
Both endpoints of the secant lie on $C$, so their joining line lies in
$\Pi$.

:::

:::

::: {.pf-step #s8}

Every point of every secant line of $X$ lies on infinitely many
secant lines of $X$.

::: pf-proof

Let
$$
O
$$
be a point of the secant line in step [](#s7){.pf-ref}. Then
$$
O\in\Pi.
$$
Consider the pencil of all lines in $\Pi$ through $O$.

If $O\in C$, every member except the unique tangent line at the smooth point
$O$ meets $C$ in $O$ and one further distinct point.

Suppose $O\notin C$. Projection from $O$ gives a finite morphism
$$
C\longrightarrow\PP^1
$$
of degree $2$, where the target is the pencil of lines through $O$.
The original secant line from step [](#s7){.pf-ref} is one fibre containing two distinct
points. Hence this degree-two morphism is generically separable: a purely
inseparable degree-two map would be radicial and could not have such a
fibre. Therefore the geometric generic fibre consists of two distinct
points, and the same holds over a nonempty open subset of the pencil.

In either case infinitely many lines through $O$ are secants of the conic
$C$. Since
$$
C\subseteq X,
$$
they are also secant lines of the Veronese surface $X$.

:::

:::

::: {.pf-step #s9}

The secant variety of the Veronese surface has dimension at most $4$.

::: pf-proof

Let
$$
\mathcal J
=
\{(P,Q,O):
P,Q\in X,\ P\ne Q,\ O\in\overline{PQ}\}.
$$
Since
$$
\dim X=2,
$$
one has
$$
\dim\mathcal J=2+2+1=5.
$$
Its image in $\PP^5$ is dense in the secant variety
$$
\operatorname{Sec}(X).
$$

By step [](#s8){.pf-ref}, every point of this image lies on infinitely many secant lines.
Thus every fibre of
$$
\mathcal J\longrightarrow\operatorname{Sec}(X)
$$
over a point of the dense image has infinitely many closed points.
A zero-dimensional finite-type scheme over an algebraically closed field has
only finitely many closed points, so these fibres have dimension at least
$1$.
The fibre-dimension inequality therefore gives
$$
\dim\operatorname{Sec}(X)
\le
5-1
=4.
$$

:::

:::

::: {.pf-step #s10}

The secant variety has dimension at least $4$.

::: pf-proof

Use the standard coordinates
$$
\nu_2([x:y:z])
=
[x^2:y^2:z^2:xy:xz:yz].
$$
Near
$$
P_0=[1:0:0],
\qquad
Q_0=[0:1:0],
$$
write
$$
P(a,b)=[1:a:b],
\qquad
Q(c,d)=[c:1:d].
$$
Restrict to the four-parameter family with $c=0$ and consider
$$
\Psi(a,b,d,t)
=
[\nu_2(P(a,b))+t\,\nu_2(Q(0,d))].
$$
On the target chart where the $x^2$-coordinate is nonzero, normalize that
coordinate to $1$. The image coordinates are then
$$
\begin{aligned}
A&=a^2+t,\\
B&=b^2+td^2,\\
C&=a,\\
D&=b,\\
E&=ab+td.
\end{aligned}
$$
On the open subset
$$
t\ne0,
$$
these equations recover the four parameters rationally:
$$
a=C,
\qquad
b=D,
\qquad
t=A-C^2,
\qquad
d=\frac{E-CD}{A-C^2}.
$$
Thus $\Psi$ is generically one-to-one onto its image on this four-dimensional
open set. Its image therefore has dimension $4$.
Since that image is contained in the secant variety,
$$
\dim\operatorname{Sec}(X)\ge4.
$$

:::

:::

::: {.pf-step #s11}

The secant variety of the Veronese surface has dimension exactly
$$
\boxed{4}.
$$

::: pf-proof

Steps [](#s9){.pf-ref} and [](#s10){.pf-ref} give the opposite inequalities
$$
\dim\operatorname{Sec}(X)\le4
\qquad\text{and}\qquad
\dim\operatorname{Sec}(X)\ge4.
$$
Therefore equality holds.

:::

:::

::: {.pf-step #s12}

There is a projection
$$
X\hookrightarrow\PP^4
$$
which is a closed immersion.

::: pf-proof

By step [](#s11){.pf-ref},
$$
\operatorname{Sec}(X)
\subsetneq
\PP^5.
$$
Choose
$$
O\in\PP^5\setminus\operatorname{Sec}(X).
$$
The closure of the secant variety contains the embedded tangent spaces of
the smooth surface $X$: every tangent direction is a limit of secant
directions, and the projective tangent plane is the union of its tangent
lines through the point.
Thus $O$ lies on neither a secant line nor an embedded tangent plane of $X$.

The point- and tangent-separation argument of steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} therefore
applies to projection from $O$ and gives a closed immersion
$$
\boxed{X\hookrightarrow\PP^4}.
$$
This is the projection asserted in (b).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove (a). Steps [](#s7){.pf-ref} and [](#s8){.pf-ref} prove that each point on every
secant line lies on infinitely many secants; steps [](#s9){.pf-ref}, [](#s10){.pf-ref} and [](#s11){.pf-ref} compute the
secant-variety dimension; and step [](#s12){.pf-ref} gives the closed immersion into
$\PP^4$ required in (b).

:::

:::

:::
