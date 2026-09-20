---
schema: qual/card@1
id: P-AGXVAREXCUSP
kind: problem
title: The cuspidal cubic, its unique singular point, and its normalization
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cusps
  - Normalization
  - Plane Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 6.5 in the recorded source. It asks that the
    cuspidal cubic x^3-y^2=0 have a unique singular point, that its germ at
    the origin be unibranch, and that its normalization be A^1 via
    t -> (t^2,t^3).
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced the imported request for irreducibility only in C[x,y] by the
    source's stronger local analytic statement: irreducibility in C{x,y},
    equivalently one analytic branch at the cusp.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the Jacobian singular-locus computation, the coordinate-ring
    embedding C[t^2,t^3] in C[t], finiteness and birationality of the
    parametrization, identification of C[t] with the integral closure, and
    analytic irreducibility by Weierstrass preparation and the x-adic order.
---

::: {.problem}
Let
$$
X=V(x^3-y^2)\subseteq\AA^2_\CC.
$$
Show that $X$ has a unique singular point, namely the origin.

Show that the germ $(X,0)$ is unibranch.

Show that the normalization of $X$ is $\AA^1_\CC$, using the morphism
$$
\nu:\AA^1_\CC\longrightarrow X,
\qquad
t\longmapsto(t^2,t^3).
$$
:::

::: {.solution}
<1>1. The coordinate ring of $X$ is
$$
\boxed{
A(X)\cong\CC[t^2,t^3]\subseteq\CC[t].
}
$$

::: {.proof}
Consider the homomorphism
$$
\phi:\CC[x,y]\longrightarrow\CC[t],
\qquad
x\longmapsto t^2,
\qquad
y\longmapsto t^3.
$$
Certainly
$$
x^3-y^2\in\ker\phi.
$$
Conversely, divide any
$$
p(x,y)\in\CC[x,y]
$$
by the monic polynomial $y^2-x^3$ as a polynomial in $y$ over $\CC[x]$:
$$
p=q(y^2-x^3)+a(x)+yb(x)
$$
for unique
$$
q\in\CC[x,y],
\qquad
a,b\in\CC[x].
$$
If $p\in\ker\phi$, then
$$
a(t^2)+t^3b(t^2)=0.
$$
The first summand contains only even powers of $t$, while the second contains
only odd powers of degree at least $3$. Hence both summands vanish, so
$$
a=b=0.
$$
Thus
$$
\ker\phi=(y^2-x^3)=(x^3-y^2),
$$
and the induced map identifies
$$
\CC[x,y]/(x^3-y^2)
\cong
\CC[t^2,t^3].
$$
:::

<1>2. The origin is the unique singular point of $X$.

::: {.proof}
Let
$$
F(x,y)=x^3-y^2.
$$
Then
$$
F_x=3x^2,
\qquad
F_y=-2y.
$$
Since the base field has characteristic $0$, a point of the plane curve is
singular exactly when
$$
F=F_x=F_y=0.
$$
The equations
$$
3x^2=0,
\qquad
-2y=0
$$
force
$$
x=y=0.
$$
The origin lies on $X$, so it is the unique singular point.
:::

<1>3. The morphism
$$
\nu:\AA^1_\CC\longrightarrow X,
\qquad
t\longmapsto(t^2,t^3),
$$
is finite and birational.

::: {.proof}
By step <1>1, the comorphism of $\nu$ is the inclusion
$$
\CC[t^2,t^3]\hookrightarrow\CC[t].
$$
The element $t$ is integral over $\CC[t^2,t^3]$, because it satisfies
$$
T^2-t^2=0
$$
with coefficient $t^2\in\CC[t^2,t^3]$. Moreover,
$$
\CC[t]
=
\CC[t^2,t^3][t].
$$
Hence $\CC[t]$ is finite over $\CC[t^2,t^3]$, so $\nu$ is finite.

The two rings have the same fraction field, because
$$
t=\frac{t^3}{t^2}
$$
in their common fraction field. Thus
$$
\Frac\CC[t^2,t^3]=\CC(t)=\Frac\CC[t],
$$
and $\nu$ is birational.
:::

<1>4. The normalization of $X$ is $\AA^1_\CC$.

::: {.proof}
Let
$$
A=\CC[t^2,t^3]
\subseteq
K=\CC(t),
$$
and let $\overline A$ be the integral closure of $A$ in $K$.

Step <1>3 shows that $\CC[t]$ is integral over $A$, so
$$
\CC[t]\subseteq\overline A.
$$
Conversely, if
$$
u\in\overline A,
$$
then $u$ satisfies a monic polynomial with coefficients in $A$, hence also a
monic polynomial with coefficients in $\CC[t]$. Since $\CC[t]$ is a UFD, it
is integrally closed in $\CC(t)$, so
$$
u\in\CC[t].
$$
Therefore
$$
\overline A=\CC[t].
$$
Taking spectra gives
$$
X^{\operatorname{norm}}\cong\Spec\CC[t]=\AA^1_\CC,
$$
and the normalization morphism is precisely $\nu$.
:::

<1>5. The germ $(X,0)$ is unibranch.

::: {.proof}
The source defines the analytic branches at the origin by the irreducible
factors of
$$
y^2-x^3
$$
in the convergent power-series ring
$$
\CC\{x,y\}.
$$
It therefore suffices to prove that this germ is irreducible there.

Regard $y^2-x^3$ as a Weierstrass polynomial in $y$. If it factored into two
nonunits in $\CC\{x,y\}$, the Weierstrass preparation theorem would, after
absorbing units into the factors, give a factorization into monic
Weierstrass polynomials in $y$. Since the degree in $y$ is $2$, the only
possibility is
$$
y^2-x^3=(y-a(x))(y-b(x))
$$
with
$$
a(x),b(x)\in\CC\{x\}.
$$
Comparing the coefficient of $y$ gives
$$
b=-a,
$$
and comparing constant terms gives
$$
a(x)^2=x^3.
$$
This is impossible: the $x$-adic order of a square is even, whereas
$$
\operatorname{ord}_x(x^3)=3.
$$
Hence $y^2-x^3$ is irreducible in $\CC\{x,y\}$, so the germ has exactly one
analytic branch. Thus $(X,0)$ is unibranch.
:::

<1>6. The normalization has exactly one point over the cusp:
$$
\boxed{\nu^{-1}(0,0)=\{0\}.}
$$

::: {.proof}
The equations
$$
t^2=0,
\qquad
t^3=0
$$
hold simultaneously exactly when $t=0$. Thus the unique point of the
normalization lying over the singularity is the origin of $\AA^1$.
This agrees with the unibranch computation in step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves the singular-point claim, step <1>5 proves the unibranch
claim, and steps <1>3--<1>4 identify the normalization and its morphism.
:::
:::
