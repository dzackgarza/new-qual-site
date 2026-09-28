---
schema: qual/card@1
id: P-AGH57CONEBLOWUP
kind: problem
title: Blowing up the vertex of the cone over a nonsingular plane curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowing Up
  - Singularities
  - Cones
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all three parts with the retained Hartshorne I.5.7 transcription. The proof uses homogeneity to identify each affine blowup chart with an affine-line product of the corresponding standard affine chart of Y; the same equations identify the exceptional fibre with Y.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $Y \subseteq \PP^2$ be a nonsingular plane curve of degree $> 1$, defined by the equation $f(x,y,z) = 0$.
Let $X \subseteq \AA^3$ be the affine variety defined by $f$; this is the cone over $Y$.
Let $P = (0,0,0)$ be the vertex of the cone, and let $\varphi: \tilde{X} \to X$ be the blowing-up of $X$ at $P$.

1. Show that $X$ has just one singular point, namely $P$.

2. Show that $\tilde{X}$ is nonsingular, by covering it with open affines.

3. Show that $\varphi^{-1}(P)$ is isomorphic to $Y$.
:::

::: {.solution}
Let $d>1$ be the degree of the homogeneous irreducible polynomial
$$
f(x,y,z).
$$
The affine cone is
$$
X=V(f)\subseteq\AA_k^3,
$$
and its vertex is $P=(0,0,0)$.

<1>1. The vertex $P$ is singular on $X$.

::: {.proof}
Every first partial derivative of the degree-$d$ homogeneous polynomial $f$ is homogeneous of degree $d-1>0$.
Hence
$$
f_x(P)=f_y(P)=f_z(P)=0.
$$
Since $f(P)=0$, the Jacobian criterion makes $P$ singular.
:::

<1>2. Every nonzero point of $X$ is nonsingular.

::: {.proof}
Let $Q=(a,b,c)\in X\setminus\{P\}$ and let
$$
q=[a:b:c]\in Y\subseteq\PP^2.
$$
The nonsingularity of the projective plane curve $Y$ means that the three homogeneous partial derivatives
$$
f_x,\qquad f_y,\qquad f_z
$$
do not vanish simultaneously at any representative of $q$ [@Har10a, Chapter I, §5].
Thus at least one of
$$
f_x(Q),\quad f_y(Q),\quad f_z(Q)
$$
is nonzero.
The affine Jacobian criterion therefore makes $Q$ nonsingular on $X$.
Combined with step <1>1, this proves
$$
\boxed{\Sing X=\{P\}.}
$$
:::

<1>3. On the blowup chart corresponding to the $x$-direction, the strict transform is
$$
\widetilde X_x
\cong
\Spec k[x,u,v]/(f(1,u,v))
\cong
\AA_x^1\times\bigl(Y\cap D_+(x)\bigr).
$$

::: {.proof}
The blowup of $\AA^3$ at the origin is the closed subvariety of
$$
\AA^3\times\PP^2_{[U:V:W]}
$$
defined by the proportionality relations
$$
xV=yU,\qquad xW=zU,\qquad yW=zV.
$$
On the chart $U\ne0$, put
$$
u=V/U,\qquad v=W/U.
$$
Then
$$
y=xu,\qquad z=xv,
$$
so this blowup chart is $\Spec k[x,u,v]$.

By homogeneity,
$$
f(x,xu,xv)=x^d f(1,u,v).
$$
Away from the exceptional divisor $x=0$, the inverse image of $X\setminus\{P\}$ is therefore cut out by $f(1,u,v)=0$.
Its closure is the same hypersurface, so this is precisely the strict transform.

The standard affine chart $Y\cap D_+(x)$ has coordinates $u=y/x$, $v=z/x$ and equation $f(1,u,v)=0$.
The displayed product decomposition follows because the strict-transform equation is independent of the coordinate $x$.
:::

<1>4. The strict transform $\widetilde X$ is nonsingular.

::: {.proof}
The three blowup charts $U\ne0$, $V\ne0$, $W\ne0$ cover the blowup.
Step <1>3 gives
$$
\widetilde X_x\cong\AA^1\times(Y\cap D_+(x)).
$$
By the same calculation after cyclically permuting the coordinates,
$$
\widetilde X_y\cong\AA^1\times(Y\cap D_+(y)),
\qquad
\widetilde X_z\cong\AA^1\times(Y\cap D_+(z)).
$$
The three standard affine pieces of $Y$ are nonsingular because $Y$ is nonsingular.
Their products with $\AA^1$ are nonsingular: on the $x$-chart, for example, the equation is $f(1,u,v)=0$, and its two derivatives with respect to $u,v$ cannot vanish simultaneously there.
Indeed, if they did, then $f_y=f_z=0$ at the corresponding projective point, and Euler's homogeneous identity
$$
x f_x+y f_y+z f_z=d f
$$
would also give $f_x=0$ because $x\ne0$ and $f=0$, contradicting nonsingularity of $Y$.
The extra coordinate $x$ contributes a free affine-line direction.
Thus every point of every blowup chart is nonsingular, proving
$$
\boxed{\widetilde X\text{ is nonsingular}.}
$$
:::

<1>5. The exceptional fibre is naturally isomorphic to $Y$.

::: {.proof}
On the $x$-chart, the exceptional divisor is given by $x=0$.
Intersecting with the strict-transform equation from step <1>3 gives
$$
\varphi^{-1}(P)\cap\widetilde X_x
=
\Spec k[u,v]/(f(1,u,v)),
$$
which is exactly the standard affine chart $Y\cap D_+(x)$.
The analogous calculations on the other two charts give $Y\cap D_+(y)$ and $Y\cap D_+(z)$.

On overlaps, the transition functions are the ordinary projective coordinate-ratio changes, since the exceptional divisor of the blowup is the projective space of directions through the origin.
Thus these three affine pieces glue by exactly the same transition maps as the standard affine cover of $Y$.
Consequently
$$
\boxed{\varphi^{-1}(P)\cong Y.}
$$
Concretely, the isomorphism sends a point of the exceptional fibre represented by the direction $[U:V:W]$ to the point $[U:V:W]\in Y$; the equation $f(U,V,W)=0$ follows from the strict-transform equations.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove part (1), steps <1>3--<1>4 prove part (2), and step <1>5 proves part (3).
:::
:::
