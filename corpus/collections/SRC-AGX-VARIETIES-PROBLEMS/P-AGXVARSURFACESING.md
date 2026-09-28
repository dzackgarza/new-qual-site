---
schema: qual/card@1
id: P-AGXVARSURFACESING
kind: problem
title: Singular points and tangent lines of a plane projective curve via the gradient
classification:
  areas:
  - algebraic-geometry
  topics:
  - Singularities
  - Jacobian Criterion
  - Projective Hypersurfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the corresponding clauses of Zaidenberg Exercises 8.5 in the recorded
    source. They concern a plane projective curve C=V(f) in P^2, ask that P be
    singular exactly when all three homogeneous partial derivatives vanish,
    and give the tangent-line formula at a simple point.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Corrected the card from a surface in P^3 to the source's plane curve in
    P^2. The old statement mixed a surface ambient space with a tangent-line
    formula in only three coordinates.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Applied the projective hypersurface Jacobian criterion and derived the
    tangent line by projectivizing the kernel of df_P. Euler's homogeneous
    identity verifies that the displayed line passes through P.
---

::: {.problem}
Let
$$
C=V(f)\subseteq\PP^2_\CC
$$
be a plane projective curve, where
$$
f\in\CC[x,y,z]\sm\{0\}
$$
is irreducible and homogeneous. Let
$$
P=[a:b:c]\in C.
$$

(a) Show that $P$ is singular if and only if
$$
f_x(P)=f_y(P)=f_z(P)=0.
$$

(b) If $P$ is smooth, show that the tangent line to $C$ at $P$ has equation
$$
x f_x(P)+y f_y(P)+z f_z(P)=0.
$$
:::

::: {.solution}
Let
$$
d=\deg f.
$$

<1>1. The point $P$ is smooth exactly when
$$
\rank
\begin{pmatrix}
f_x(P)&f_y(P)&f_z(P)
\end{pmatrix}
=
1.
$$

::: {.proof}
The curve $C$ is a hypersurface in the smooth surface $\PP^2_\CC$, so its
codimension is $1$. Choose a nonzero coordinate of $P$; after permuting
coordinates, assume $c\ne0$ and scale the representative so that
$$
P=[a:b:1].
$$
On the chart $z=1$, the equation is
$$
g(x,y)=f(x,y,1)=0.
$$
The Jacobian criterion [[PR-MORJAC]] says that $P$ is smooth exactly when
$$
\bigl(g_x(P),g_y(P)\bigr)
=
\bigl(f_x(P),f_y(P)\bigr)
$$
is nonzero.

Euler's identity at $P$ gives
$$
a f_x(P)+b f_y(P)+f_z(P)=d f(P)=0.
$$
Thus
$$
f_x(P)=f_y(P)=0
\quad\Longrightarrow\quad
f_z(P)=0.
$$
The converse is immediate. Hence the affine Jacobian is nonzero exactly when
the homogeneous row vector
$$
\begin{pmatrix}
f_x(P)&f_y(P)&f_z(P)
\end{pmatrix}
$$
has rank $1$.
:::

<1>2. The point $P$ is singular if and only if
$$
\boxed{
f_x(P)=f_y(P)=f_z(P)=0.
}
$$

::: {.proof}
A one-row matrix has rank less than $1$ exactly when all of its entries
vanish. By step <1>1, rank less than $1$ is exactly the singular condition.
This proves (a).
:::

<1>3. If $P$ is smooth, the kernel of the homogeneous differential
$$
df_P:\CC^3\longrightarrow\CC
$$
is the two-dimensional vector subspace
$$
\left\{
(u,v,w)\in\CC^3:
u f_x(P)+v f_y(P)+w f_z(P)=0
\right\}.
$$

::: {.proof}
The differential of the homogeneous polynomial $f$ at a representative
$(a,b,c)$ of $P$ is
$$
df_P(u,v,w)
=
u f_x(P)+v f_y(P)+w f_z(P).
$$
Since $P$ is smooth, step <1>1 says that this linear functional is nonzero.
Therefore its kernel is a vector subspace of codimension one in $\CC^3$,
hence has dimension two, with the displayed equation.
:::

<1>4. The radial vector
$$
(a,b,c)
$$
belongs to $\ker df_P$.

::: {.proof}
Euler's identity for a homogeneous polynomial of degree $d$ is
$$
x f_x+y f_y+z f_z=d f.
$$
Evaluating at $P$ gives
$$
a f_x(P)+b f_y(P)+c f_z(P)
=
d f(P)
=
0,
$$
because $P\in C=V(f)$. Hence $(a,b,c)\in\ker df_P$.
:::

<1>5. The projectivization of $\ker df_P$ is the tangent line to $C$ at
$P$.

::: {.proof}
The affine cone over $C$ is
$$
\widehat C=V(f)\subseteq\AA^3_\CC.
$$
At the nonzero representative $(a,b,c)$ of a smooth projective point, the
Zariski tangent space to the cone is
$$
T_{(a,b,c)}\widehat C
=
\ker df_P.
$$
Step <1>4 shows that this tangent plane contains the radial line through
$(a,b,c)$. The projective tangent space is the image of this plane under the
quotient by the radial direction:
$$
\PP(\ker df_P)\subseteq\PP^2_\CC.
$$
Because $\ker df_P$ is two-dimensional by step <1>3, its projectivization is
a projective line: the tangent line to $C$ at $P$.
:::

<1>6. The tangent line at a smooth point $P$ has equation
$$
\boxed{
x f_x(P)+y f_y(P)+z f_z(P)=0.
}
$$

::: {.proof}
Step <1>3 gives exactly this homogeneous linear equation for
$$
\ker df_P.
$$
Step <1>5 identifies the projectivization of that kernel with the tangent
line. Step <1>4 verifies explicitly that the line passes through $P$.
This proves (b).
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves the singularity criterion, and step <1>6 proves the
tangent-line formula.
:::
:::
