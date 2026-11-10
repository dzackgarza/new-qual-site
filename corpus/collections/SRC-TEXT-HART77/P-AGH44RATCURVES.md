---
schema: qual/card@1
id: P-AGH44RATCURVES
kind: problem
title: Conics, the cuspidal cubic, and the nodal cubic are rational curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Maps
  - Birational Geometry
  - Plane Curves
relations:
- kind: uses
  target: P-AGH31CONICS
- kind: uses
  target: P-AGH317NORMAL
- kind: uses
  target: P-AGH314PROJPOINT
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all three parts with Hartshorne I.4.4. The projection in part (c) is [x:y]. The descriptor nodal requires characteristic different from two; in characteristic two the tangent cone at [0:0:1] is a doubled line, although the birational parametrization used here remains valid.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the function-field computation for the cusp and the explicit inverse to projection on dense opens of the cubic against the source and published solution notes.'
---

::: {.problem}
A variety $Y$ is \dfn{rational} if it is birationally equivalent to $\PP^n$ for some $n$; equivalently by (4.5), if $K(Y)$ is a purely transcendental extension of $k$.

(a) Show that any conic in $\PP^2$ is a rational curve.

(b) Show that the cuspidal cubic $y^2 = x^3$ is a rational curve.

(c) Let $Y$ be the nodal cubic curve $y^2 z = x^2(x+z)$ in $\PP^2$.
Show that the projection $\varphi$ from the point $P = (0,0,1)$ to the line $z = 0$ induces a birational map from $Y$ to $\PP^1$.
Thus $Y$ is a rational curve.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every conic in $\PP^2$ is a rational curve.

::: pf-proof

By [[P-AGH31CONICS]], every projective conic is isomorphic to $\PP^1$.
An isomorphism is in particular a birational equivalence.
Hence every conic is rational, proving (a).

:::

:::

::: {.pf-step #s2}

The cuspidal cubic
$$
C=Z(y^2-x^3)\subseteq\AA^2
$$
has function field $K(C)\cong k(t)$.

::: pf-proof

As in [[P-AGH317NORMAL]], its coordinate ring is
$$
A(C)\cong k[t^2,t^3]
$$
under
$$
x\longmapsto t^2,
\qquad
y\longmapsto t^3.
$$
Therefore
$$
K(C)=\operatorname{Frac}k[t^2,t^3].
$$
This fraction field contains
$$
t=\frac{t^3}{t^2},
$$
and conversely $t^2,t^3\in k(t)$.
Thus
$$
K(C)=k(t),
$$
a purely transcendental extension of $k$ of transcendence degree one.
Hence $C$ is rational, proving (b).

:::

:::

::: {.pf-step #s3}

Projection from
$$
P=[0:0:1]
$$
to the line $z=0$ is the rational map
$$
\varphi:Y\dashrightarrow\PP^1,
\qquad
[x:y:z]\longmapsto[x:y].
$$

::: pf-proof

This is the coordinate form of projection from a point established in [[P-AGH314PROJPOINT]].
On $Y$, the simultaneous equations $x=y=0$ give only the point $P$.
Thus the displayed formula is a morphism on $Y\setminus\{P\}$ and represents the desired rational map.

:::

:::

::: {.pf-step #s4}

On the dense open subset
$$
U=Y\cap D_+(x),
$$
the map $\varphi$ is an isomorphism onto
$$
V=\{[1:t]\in\PP^1:t^2\ne1\}.
$$

::: pf-proof

If $[x:y:z]\in U$, then $z\ne0$: otherwise the cubic equation with $z=0$ would give $x^3=0$, contradicting $x\ne0$.
Normalize to $z=1$ and put
$$
t=\frac yx.
$$
The equation
$$
y^2=x^2(x+1)
$$
then gives
$$
t^2=x+1,
$$
so
$$
x=t^2-1,
\qquad
y=t(t^2-1).
$$
Because $x\ne0$, we have $t^2\ne1$.

Conversely define
$$
\psi:V\to Y,
\qquad
[1:t]\longmapsto[t^2-1:t(t^2-1):1].
$$
Substitution gives
$$
t^2(t^2-1)^2=(t^2-1)^2((t^2-1)+1),
$$
so the image lies in $Y$; because $t^2\ne1$, it lies in $U$.
Both coordinate formulas are regular on the indicated affine opens.
Finally,
$$
\varphi(\psi([1:t]))=[t^2-1:t(t^2-1)]=[1:t],
$$
while the formulas derived above show $\psi(\varphi(Q))=Q$ for $Q\in U$.
Thus $U\cong V$.

:::

:::

::: {.pf-step #s5}

The projection $\varphi$ is birational and $Y$ is rational.

::: pf-proof

Step [](#s4){.pf-ref} gives an isomorphism between nonempty open subsets of $Y$ and $\PP^1$.
Therefore $\varphi$ is a birational map.
Hence $Y$ is a rational curve, proving (c).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a), step [](#s2){.pf-ref} proves (b), and steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (c).

:::

:::

:::

::: {.remark title="The word nodal in characteristic two"}
At $P=[0:0:1]$, use the affine chart $z=1$.
The equation is
$$
y^2=x^2(x+1),
$$
whose lowest-degree part is
$$
y^2-x^2=(y-x)(y+x).
$$
If $\operatorname{char}k\ne2$, these are two distinct tangent lines, so $P$ is an ordinary node.
If $\operatorname{char}k=2$, the tangent cone is $(y-x)^2$, so the singularity is not an ordinary node.
The birational calculation above does not divide by $2$ and remains valid in either characteristic.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 4.4, PDF p. 6: (a) by Exercise 3.1(c); (b) "the maps taking $t\in\AA^1$ to $(t^3,t^2)$ and $(x,y)$ to $y/x$ (for $x\ne0$) are inverse birational isomorphisms from the cuspidal curve to $\AA^1$"; (c) the projection $(x:y:z)\mapsto(x:y)$ off $(0:0:1)$, with inverse $(x:y)\mapsto((y^2-x^2)x:(y^2-x^2)y:x^3)$ for $(x:y)\ne(1:\pm1)$.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 4.4, PDF pp. 15--16: (a) from every conic being isomorphic to $\PP^1$; (b) by $Z(y^2-x^3)\setminus\{(0,0)\}\to\PP^1$, $(x,y)\mapsto[x:y]$, with inverse $[x:y]\mapsto((y/x)^2,(y/x)^3)$; (c) begins "This map can be given explicitly. If $[P_0:P_1:P_2]\in Y$ then its image is" and the entry ends there, so his (c) is unfinished.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.4.4, PDF p. 40: (a) by I.3.1(b); (b) $t\mapsto(t^2,t^3)$ with inverse $(x,y)\mapsto x/y$; (c) the projection $(x:y:z)\mapsto(x:y)$ with inverse $(x:y)\mapsto((y^2-x^2)x:(y^2-x^2)y:x^3)$, checked by substituting $y^2z-zx^2=z(y^2-x^2)=x^3$ on the curve.
Borcherds' (b) writes the parametrization as $(t^3,t^2)$, whose points satisfy $y^3=x^2$ rather than the curve's $y^2=x^3$; the inverse $y/x$ is the one belonging to the correct parametrization $(t^2,t^3)$, which is what Egbert writes. The proof above uses $(t^2,t^3)$ and, for (c), proves the birationality on the chart $x\ne0$ with the inverse written out and checked in both directions, which neither set does for both directions.
Agree with Egbert; Borcherds' (b) is a misprint of the parametrization and his (c) inverse is the same as the card's.
:::
