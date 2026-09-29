---
schema: qual/card@1
id: P-AGH529QUADCONE
kind: problem
title: Degree and genus of nonsingular curves on a quadric cone
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.9, the retained Egbert companion calculation, the
    ruled-surface model referenced by the hint, and the repository's
    Hirzebruch-surface and quadric-cone material. The blowup of the vertex is
    the Hirzebruch surface F_2 with exceptional section C_0^2=-2; the pullback
    of a hyperplane is C_0+2f. For a nonsingular curve through the vertex, its
    strict transform meets C_0 once and transversely, while a curve avoiding
    the vertex is disjoint from C_0. These two intersection numbers give the
    even/odd dichotomy used below.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y$ be a nonsingular curve on a quadric cone $X_0$ in $\PP^3$.
Show that either

- $Y$ is a complete intersection of $X_0$ with a surface of degree $a \geqslant 1$, in which case $\deg Y=2 a$, $g(Y)=(a-1)^2$, or,

- $\deg Y$ is odd, say $2 a+1$, and $g(Y)=a^2-a$.

Cf.
(V, 6.4.1). Hint: Use (2.11.4).
:::

::: {.solution}
Let
$$
v\in X_0
$$
be the vertex, and let
$$
\pi:\widetilde X_0\longrightarrow X_0
$$
be the blowup of $v$.

::: pf

::: {.pf-step #s1}

The resolution $\widetilde X_0$ is the Hirzebruch surface $\FF_2$.
If $C_0$ is its exceptional section and $f$ a ruling fibre, then
$$
C_0^2=-2,
\qquad
C_0\cdot f=1,
\qquad
f^2=0,
$$
and
$$
K_{\FF_2}=-2C_0-4f.
$$
Moreover, if $H$ denotes the pullback of the hyperplane class of
$X_0\subseteq\PP^3$, then
$$
\boxed{H\sim C_0+2f}.
$$

::: pf-proof

The ruled-surface model referred to in the hint identifies the blowup of the
vertex of the quadric cone with $\FF_2$; equivalently, the quadric cone is
obtained by contracting the negative section of $\FF_2$.  The intersection
numbers and
$$
K_{\FF_2}=-2C_0-4f
$$
are the standard Hirzebruch-surface formulas recorded in [[FE-TORHIRZ]].

Write
$$
H\sim rC_0+sf.
$$
A ruling fibre maps isomorphically to a ruling line of the cone, so
$$
H\cdot f=1.
$$
Hence $r=1$.  Since $C_0$ is contracted to the vertex,
$$
H\cdot C_0=0.
$$
Thus
$$
0=(C_0+sf)\cdot C_0=-2+s,
$$
so $s=2$ and $H\sim C_0+2f$.

:::

:::

::: {.pf-step #s2}

Let $D\subseteq\FF_2$ be the strict transform of $Y$.  Then
$$
D\cong Y,
$$
and
$$
D\cdot C_0=
\begin{cases}
0,&v\notin Y,\\
1,&v\in Y.
\end{cases}
$$

::: pf-proof

Away from $v$, the morphism $\pi$ is an isomorphism, so if $v\notin Y$ the
strict transform is isomorphic to $Y$ and is disjoint from $C_0$.

Assume now that $v\in Y$.  Work in an affine chart of $\PP^3$ centered at
$v$.  Since the curve $Y$ is nonsingular at $v$, choose a local parameter
$t$ on $Y$ at $v$.  Among the ambient affine coordinates, at least one,
say $x$, restricts to
$$
x=t u
$$
with $u$ a unit at $v$; every other ambient coordinate restricts to a
multiple of $t$.  In the $x$-chart of the blowup, the strict transform of
$Y$ is therefore still parametrized by $t$, and the exceptional divisor is
cut on it by $t=0$.  Hence the strict transform is nonsingular, the map
$D\to Y$ is an isomorphism, and $D$ meets the exceptional curve once and
transversely.  Thus
$$
D\cdot C_0=1.
$$

:::

:::

::: {.pf-step #s3}

Write
$$
D\sim aC_0+bf.
$$
Then
$$
\boxed{
D\sim
\begin{cases}
aH,&v\notin Y,\\
aH+f,&v\in Y,
\end{cases}}
$$
for an integer $a\ge0$; in the first case $a\ge1$.

::: pf-proof

Since
$$
\Pic(\FF_2)=\ZZ C_0\oplus\ZZ f,
$$
such integers $a,b$ exist.  Intersecting with a fibre gives
$$
D\cdot f=a,
$$
so $a\ge0$ because $D$ is an effective curve distinct from $C_0$.

By step [](#s2){.pf-ref},
$$
b-2a
=
D\cdot C_0
\in\{0,1\}.
$$
Thus
$$
b=2a
$$
when $Y$ avoids the vertex, and
$$
b=2a+1
$$
when $Y$ passes through it.  Using $H=C_0+2f$ from step [](#s1){.pf-ref} gives the two
displayed classes.  In the first case $a=0$ would make $D\sim0$, impossible
for a nonempty effective curve, so $a\ge1$ there.

:::

:::

::: {.pf-step #s4}

The degree of $Y$ is
$$
\boxed{
\deg Y=
\begin{cases}
2a,&v\notin Y,\\
2a+1,&v\in Y.
\end{cases}}
$$

::: pf-proof

The degree is intersection with a hyperplane.  Pulling the hyperplane class
back to $\FF_2$ therefore gives
$$
\deg Y=D\cdot H.
$$
From step [](#s1){.pf-ref},
$$
H^2=(C_0+2f)^2=-2+4=2,
\qquad
H\cdot f=1.
$$
Using the two classes from step [](#s3){.pf-ref} gives
$$
(aH)\cdot H=2a
$$
and
$$
(aH+f)\cdot H=2a+1.
$$

:::

:::

::: {.pf-step #s5}

The genus of $Y$ is
$$
\boxed{
g(Y)=
\begin{cases}
(a-1)^2,&v\notin Y,\\
a^2-a,&v\in Y.
\end{cases}}
$$

::: pf-proof

By step [](#s2){.pf-ref}, $D\cong Y$, so it is enough to compute the genus of $D$ on
the nonsingular surface $\FF_2$.  Step [](#s1){.pf-ref} gives
$$
K_{\FF_2}=-2C_0-4f=-2H.
$$

If $D=aH$, then
$$
D^2=2a^2,
\qquad
D\cdot K_{\FF_2}=-4a.
$$
Adjunction gives
$$
g(Y)
=
1+\frac12D\cdot(D+K_{\FF_2})
=
1+a^2-2a
=
(a-1)^2.
$$

If $D=aH+f$, then
$$
D^2=2a^2+2a,
$$
while
$$
D\cdot K_{\FF_2}
=
-2D\cdot H
=
-4a-2.
$$
Hence
$$
g(Y)
=
1+\frac12(2a^2+2a-4a-2)
=
a^2-a.
$$

:::

:::

::: {.pf-step #s6}

If $v\notin Y$, then $Y$ is the scheme-theoretic complete
intersection of $X_0$ with a surface of degree $a$.

::: pf-proof

In this case $Y$ lies in the nonsingular locus of the normal surface $X_0$,
so it is an effective Cartier divisor on $X_0$.  Since it avoids the center
of the blowup, its total transform is its strict transform:
$$
\pi^*Y=D.
$$
By step [](#s3){.pf-ref},
$$
\OO_{\FF_2}(D)
\cong
\OO_{\FF_2}(aH)
\cong
\pi^*\OO_{X_0}(a).
$$
Thus
$$
\pi^*\OO_{X_0}(Y)
\cong
\pi^*\OO_{X_0}(a).
$$

The pullback
$$
\pi^*:\Pic(X_0)\longrightarrow\Pic(\FF_2)
$$
is injective.  Indeed, $X_0$ is normal and $\pi$ is proper birational, so
$$
\pi_*\OO_{\FF_2}=\OO_{X_0}.
$$
If $\pi^*L$ is trivial, the projection formula gives
$$
L
\cong
L\tensor\pi_*\OO_{\FF_2}
\cong
\pi_*\pi^*L
\cong
\OO_{X_0}.
$$
Therefore
$$
\OO_{X_0}(Y)\cong\OO_{X_0}(a).
$$

The canonical section cutting out $Y$ is consequently a section of
$\OO_{X_0}(a)$.  From the hypersurface sequence of the quadric cone,
$$
0
\longrightarrow
\OO_{\PP^3}(a-2)
\longrightarrow
\OO_{\PP^3}(a)
\longrightarrow
\OO_{X_0}(a)
\longrightarrow0,
$$
and the standard vanishing
$$
H^1(\PP^3,\OO_{\PP^3}(a-2))=0,
$$
the restriction map
$$
H^0(\PP^3,\OO_{\PP^3}(a))
\longrightarrow
H^0(X_0,\OO_{X_0}(a))
$$
is surjective.  Lift the section defining $Y$ to a degree-$a$ homogeneous
form $F$.  Then
$$
Y=X_0\cap V(F)
$$
scheme-theoretically.  Hence $Y$ is a complete intersection of the quadric
cone with a surface of degree $a$.

:::

:::

::: {.pf-step #s7}

The two alternatives in the statement are exhaustive.

::: pf-proof

If $Y$ avoids the vertex, steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} give
$$
\deg Y=2a,
\qquad
g(Y)=(a-1)^2,
$$
with $a\ge1$, and show that $Y$ is the required complete intersection.

If $Y$ passes through the vertex, steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give
$$
\deg Y=2a+1,
\qquad
g(Y)=a^2-a.
$$
These are exactly the two cases asserted.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} proves the required classification.

:::

:::

:::
