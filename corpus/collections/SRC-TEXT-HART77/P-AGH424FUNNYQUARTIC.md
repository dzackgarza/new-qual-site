---
schema: qual/card@1
id: P-AGH424FUNNYQUARTIC
kind: problem
title: The quartic $x^3 y+y^3 z+z^3 x=0$ in characteristic $3$ is self-dual with inseparable dual map
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Embeddings
  - Genus
relations: []
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.2.4. The proof below checks smoothness from the
    characteristic-three gradient, proves the flex statement directly from
    the Taylor expansion rather than a Hessian criterion, and identifies the
    Gauss map with a cyclic coordinate permutation after the cube map.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
review: draft
---

::: {.problem}
Let $X$ be the plane quartic curve $x^3 y+y^3 z+ z^3 x = 0$ over a field of characteristic 3. Show that $X$ is nonsingular, every point of $X$ is an inflection point, the dual curve $X^*$ is isomorphic to $X$, but the natural map $X \to X^*$ is purely inseparable.
:::

::: {.solution}
Put
$$
F(x,y,z)=x^3y+y^3z+z^3x.
$$

::: pf

::: {.pf-step #s1}

The plane quartic
$$
X=V(F)\subset\PP^2
$$
is nonsingular.

::: pf-proof

In characteristic $3$,
$$
F_x=z^3,
\qquad
F_y=x^3,
\qquad
F_z=y^3.
$$
Thus the three partial derivatives vanish simultaneously only when
$$
x=y=z=0,
$$
which is not a point of $\PP^2$.  The projective Jacobian criterion therefore
shows that $X$ is nonsingular.

:::

:::

::: {.pf-step #s2}

If
$$
P=[a:b:c]\in X,
$$
then the tangent line at $P$ is
$$
T_P(X)=V(c^3x+a^3y+b^3z).
$$

::: pf-proof

For a nonsingular projective plane curve, the tangent line at $P$ is defined
by
$$
F_x(P)x+F_y(P)y+F_z(P)z=0.
$$
Step [](#s1){.pf-ref} gives
$$
F_x(P)=c^3,
\qquad
F_y(P)=a^3,
\qquad
F_z(P)=b^3,
$$
which yields the displayed equation.

:::

:::

::: {.pf-step #s3}

Every point of $X$ is an inflection point.

::: pf-proof

Fix $P=[a:b:c]\in X$ and choose a standard affine chart containing $P$.
After fixing the nonzero homogeneous coordinate defining that chart, write a
nearby lift as
$$
(a+u,b+v,c+w).
$$
Here the increment of the fixed chart coordinate is $0$, so only two of
$u,v,w$ are independent local coordinates.
Because $(r+s)^3=r^3+s^3$ in characteristic $3$, direct expansion gives
$$
\begin{aligned}
F(a+u,b+v,c+w)
={}&F(a,b,c)\\
&+(c^3u+a^3v+b^3w)\\
&+(b u^3+c v^3+a w^3)\\
&+(u^3v+v^3w+w^3u).
\end{aligned}
$$
There are no terms of total degree $2$ in the local increments.

The constant term vanishes because $P\in X$, and by step [](#s2){.pf-ref} the linear
term is an equation for the tangent line.  After restricting to
$T_P(X)$, the local equation therefore has order at least $3$.  Hence
$$
I_P\bigl(X,T_P(X)\bigr)\ge3,
$$
so $P$ is an inflection point.  Since $P$ was arbitrary, every point of $X$
is an inflection point.

:::

:::

::: {.pf-step #s4}

In dual homogeneous coordinates $[U:V:W]$, the Gauss map is
$$
\gamma:X\longrightarrow(\PP^2)^*,
\qquad
[a:b:c]\longmapsto[c^3:a^3:b^3],
$$
and its image is the quartic
$$
Y=V(U^3V+V^3W+W^3U).
$$

::: pf-proof

The formula for $\gamma$ is exactly the tangent-line formula of step [](#s2){.pf-ref}.
For a point in its image,
$$
(U,V,W)=(c^3,a^3,b^3),
$$
and therefore
$$
\begin{aligned}
U^3V+V^3W+W^3U
&=c^9a^3+a^9b^3+b^9c^3\\
&=(c^3a+a^3b+b^3c)^3\\
&=F(a,b,c)^3\\
&=0.
\end{aligned}
$$
Thus $\gamma(X)\subseteq Y$.

The same Jacobian calculation as in step [](#s1){.pf-ref} shows that $Y$ is nonsingular.
Moreover it is geometrically integral: if its defining quartic factored over
an algebraic closure, two positive-degree components would meet in
$\PP^2$ by Bézout, producing a singular point.  The map $\gamma$ is
nonconstant: if all tangent lines were equal, the nonsingular plane quartic
would have one fixed tangent line at every point, which is impossible since
that line meets $X$ in only finitely many points.  Hence the image of the
projective curve $X$ is a closed irreducible curve contained in $Y$, and must
equal $Y$.

By definition the closure of the Gauss image is the dual curve.  Therefore
$$
X^*=Y.
$$

:::

:::

::: {.pf-step #s5}

The dual curve $X^*$ is isomorphic to $X$.

::: pf-proof

The equation found in step [](#s4){.pf-ref},
$$
U^3V+V^3W+W^3U=0,
$$
has exactly the same form as
$$
x^3y+y^3z+z^3x=0.
$$
The projective linear identification
$$
[x:y:z]\longmapsto[U:V:W]=[x:y:z]
$$
therefore restricts to an isomorphism
$$
X\xrightarrow{\sim}X^*.
$$

:::

:::

::: {.pf-step #s6}

Under the identification in step [](#s5){.pf-ref}, the Gauss map is
$$
\gamma([x:y:z])=[z^3:x^3:y^3].
$$
It is a purely inseparable morphism of degree $3$.

::: pf-proof

Let
$$
q:X\longrightarrow X,
\qquad
[x:y:z]\longmapsto[x^3:y^3:z^3],
$$
and let
$$
\rho([x:y:z])=[z:x:y].
$$
The cyclic permutation $\rho$ preserves the equation $F=0$, so it is an
automorphism of $X$.  Step [](#s4){.pf-ref} gives
$$
\gamma=\rho\circ q.
$$

Let $K=k(X)$.  On function fields, $q^*K$ contains the cube of every element
of $K$.  Indeed, if
$$
f=\sum_m a_m m
$$
is a homogeneous polynomial written as a sum of monomials, define
$$
f^{[3]}=\sum_m a_m^3m.
$$
Then
$$
q^*f^{[3]}=f^3.
$$
Consequently, if $r=f/g\in K$, then
$$
r^3=\frac{f^3}{g^3}
$$
lies in $q^*K$.  Thus every element of $K$ has third power in $q^*K$, so
$$
K/q^*K
$$
is purely inseparable.  Composing with the automorphism $\rho$ does not
change this property; hence the natural map
$$
X\longrightarrow X^*
$$
is purely inseparable.

It is nontrivial and has degree $3$.  Indeed, $\gamma$ is a nonconstant map
of projective curves, hence finite, and its coordinate functions have degree
$3$.  Therefore
$$
\gamma^*\OO_{X^*}(1)\cong\OO_X(3).
$$
Since both $X$ and $X^*$ are plane quartics,
$$
\deg\OO_X(3)=12,
\qquad
\deg\OO_{X^*}(1)=4.
$$
For a finite morphism of curves,
$$
\deg\gamma^*L=(\deg\gamma)(\deg L),
$$
so
$$
12=4\deg\gamma
$$
and consequently
$$
\deg\gamma=3.
$$

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves nonsingularity, step [](#s3){.pf-ref} proves that every point is an
inflection point, steps [](#s4){.pf-ref} and [](#s5){.pf-ref} identify the dual curve with $X$, and step
[](#s6){.pf-ref} proves that the natural map to the dual is purely inseparable.

:::

:::

:::
