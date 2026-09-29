---
schema: qual/card@1
id: P-AGH438STRANGECURVES
kind: problem
title: Strange curves exist only in positive characteristic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.8 and independently checked both the projective
    closure of the positive-characteristic parametrization and the
    characteristic-zero projection argument. The latter was compared with
    the standard differential proof: projection from the common tangent point
    kills the tangent map generically, contradicting separability of a
    nonconstant map of curves in characteristic zero.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
We say a (singular) integral curve in $\PP^n$ is **strange** if there is a point which lies on all the tangent lines at nonsingular points of the curve.

a. There are many singular strange curves, e.g., the curve given parametrically by $x=t, y=t^p, z=t^{2p}$ over a field of characteristic $p>0$.

b. Show, however, that if $\characteristic k=0$, there aren't even any singular strange curves besides $\PP^1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

In characteristic $p>0$, the projective closure of the parametrized
curve is the image of
$$
\nu:\PP^1\longrightarrow\PP^3,
$$
$$
[u:v]
\longmapsto
\bigl[
u v^{2p-1}:
u^p v^p:
u^{2p}:
v^{2p}
\bigr].
$$

::: pf-proof

The four displayed forms are homogeneous of degree $2p$ and have no common
zero, so they define a morphism on all of $\PP^1$.
On the chart $v\ne0$, putting
$$
t=\frac uv
$$
and dividing by $v^{2p}$ gives
$$
[t:t^p:t^{2p}:1].
$$
Thus the image contains the affine parametrized curve
$$
x=t,\qquad y=t^p,\qquad z=t^{2p},
$$
and, being projective, is its projective closure.
The first affine coordinate recovers $t$, so the map is birational onto its
integral image.

:::

:::

::: {.pf-step #s2}

The affine part of this curve is nonsingular, and its unique point at
infinity is
$$
Q=[0:0:1:0].
$$

::: pf-proof

On the affine chart $w=1$, the image is the graph
$$
y=x^p,
\qquad
z=x^{2p},
$$
whose coordinate ring is
$$
k[x,y,z]/(y-x^p,z-x^{2p})
\cong
k[x].
$$
Hence the affine part is isomorphic to $\AA^1$ and is nonsingular.

The complement corresponds to $v=0$ in step [](#s1){.pf-ref}. At the unique point
$[u:v]=[1:0]$, the image is
$$
Q=[0:0:1:0].
$$
Thus $Q$ is the only point at infinity.

:::

:::

::: {.pf-step #s3}

The point $Q$ is singular.

::: pf-proof

Work on the chart $z\ne0$ around $Q$. Put
$$
s=\frac vu.
$$
Dividing the parametrization in step [](#s1){.pf-ref} by $u^{2p}$ gives
$$
\frac{x}{z}=s^{2p-1},
\qquad
\frac{y}{z}=s^p,
\qquad
\frac{w}{z}=s^{2p}.
$$
Thus the local ring of the image at $Q$ is the localization at its
origin of
$$
A=k[s^p,s^{2p-1},s^{2p}]
\subseteq
k[s].
$$
Let $\mathfrak m$ be its maximal ideal. The classes of
$$
s^p
\qquad\text{and}\qquad
s^{2p-1}
$$
are linearly independent in
$$
\mathfrak m/\mathfrak m^2:
$$
every nonzero element of $\mathfrak m^2$ has $s$-adic order at least
$2p$, whereas these two elements have orders $p$ and $2p-1$.
Therefore
$$
\dim_k\mathfrak m/\mathfrak m^2\ge2.
$$
The local ring has dimension $1$, so it is not regular. Hence $Q$ is
singular.

:::

:::

::: {.pf-step #s4}

Every tangent line at a nonsingular point of the curve passes through
the fixed point
$$
A=[1:0:0:0].
$$

::: pf-proof

By step [](#s2){.pf-ref}, every nonsingular point lies on the affine chart $w=1$ and has
the form
$$
P_t=(t,t^p,t^{2p}).
$$
Differentiating the affine parametrization gives
$$
\frac d{dt}(t,t^p,t^{2p})
=
(1,pt^{p-1},2pt^{2p-1})
=
(1,0,0),
$$
because $\operatorname{char}k=p$.
Thus the affine tangent line at $P_t$ is
$$
\lambda
\longmapsto
(t+\lambda,t^p,t^{2p}).
$$
Its projective closure contains the point at infinity in the $x$-direction,
namely
$$
A=[1:0:0:0],
$$
independently of $t$. Therefore the curve is strange. Together with
step [](#s3){.pf-ref}, this proves (a).

:::

:::

::: {.pf-step #s5}

Now assume $\operatorname{char}k=0$. Let
$$
C\subseteq\PP^n
$$
be an integral strange curve, and let
$$
A\in\PP^n
$$
lie on every tangent line at a nonsingular point of $C$. Projection from
$A$ has zero differential at every nonsingular point where it is defined.

::: pf-proof

Choose projective coordinates with
$$
A=[1:0:\cdots:0].
$$
Projection from $A$ is
$$
\pi_A:
[x_0:x_1:\cdots:x_n]
\dashrightarrow
[x_1:\cdots:x_n].
$$
It is defined on
$$
C\setminus\{A\}.
$$

Let $P$ be a nonsingular point in this open set. The differential of
$\pi_A$ kills exactly the tangent direction of the line through $A$ and
$P$: infinitesimally, moving along that line changes only the coordinate
discarded by the projection.
By strangeness, the tangent line $T_PC$ is precisely a line through $A$.
Since $T_PC$ is one-dimensional,
$$
d\pi_A|_{T_PC}=0.
$$

:::

:::

::: {.pf-step #s6}

If the projection of $C$ from $A$ were nonconstant, step [](#s5){.pf-ref} would
contradict characteristic zero.

::: pf-proof

Suppose the rational projection is nonconstant, and let
$$
Y
\subseteq
\PP^{n-1}
$$
be its integral image. Shrink to dense nonsingular opens
$$
U\subseteq C\setminus\{A\},
\qquad
V\subseteq Y,
$$
such that
$$
\pi:U\longrightarrow V
$$
is a morphism of smooth curves.
The induced extension of function fields
$$
k(Y)\subseteq k(C)
$$
is finite. Because $\operatorname{char}k=0$, it is separable.

For a finite separable extension of one-variable function fields, the map on
absolute differentials
$$
k(C)\tensor_{k(Y)}\Omega_{k(Y)/k}
\longrightarrow
\Omega_{k(C)/k}
$$
is an isomorphism. Indeed, the transitivity sequence has
$$
\Omega_{k(C)/k(Y)}=0
$$
for a finite separable extension, while both remaining vector spaces have
dimension $1$ over $k(C)$.

Hence the differential of $\pi$ at the generic point is nonzero.
On the other hand, step [](#s5){.pf-ref} says that the differential vanishes at every
nonsingular closed point of $U$. The induced morphism of line bundles
$$
\pi^*\Omega_{V/k}
\longrightarrow
\Omega_{U/k}
$$
therefore vanishes identically, and in particular vanishes at the generic
point. This is a contradiction.
Thus projection from $A$ cannot have one-dimensional image.

:::

:::

::: {.pf-step #s7}

The curve $C$ is a line.

::: pf-proof

By step [](#s6){.pf-ref}, projection from $A$ is constant on the dense open where it is
defined. A fibre of linear projection from $A$ is a line through $A$.
Therefore a dense open subset of $C$ lies on one fixed line
$$
L\subseteq\PP^n.
$$
Taking closures gives
$$
C\subseteq L.
$$
Both are integral projective curves, so
$$
C=L\cong\PP^1.
$$
Thus in characteristic zero the only strange integral curve is a line, and
in particular there are no singular strange curves. This proves (b).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove the positive-characteristic example in (a).
Steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove that in characteristic zero every strange integral
curve is a line, proving (b).

:::

:::

:::
