---
schema: qual/card@1
id: P-AGH75MULTBOUND
kind: problem
title: An irreducible plane curve of degree $d$ has no point of multiplicity $\geq d$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Multiplicity
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.7.5 together with the multiplicity definition in I.5.3 and the rational-curve definition used in I.6.1. The proof puts the high-multiplicity point at [0:0:1], reads the homogeneous equation degree by degree, and constructs an explicit birational inverse to projection from a point of multiplicity d-1.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
(a) Show that an irreducible curve $Y$ of degree $d > 1$ in $\PP^2$ cannot have a point of multiplicity $\geq d$.

(b) If $Y$ is an irreducible curve of degree $d > 1$ having a point of multiplicity $d - 1$, show that $Y$ is a rational curve.
:::

::: {.solution}
After a projective linear change of coordinates, put the point under consideration at
$$
P=[0:0:1].
$$
Let $F(x,y,z)$ be an irreducible homogeneous equation of degree $d$ for $Y$, and write
$$
f(x,y)=F(x,y,1)=f_0+f_1+\cdots+f_d
$$
with each $f_i$ homogeneous of degree $i$ in $x,y$.

<1>1. The multiplicity of $Y$ at $P$ is at most $d$.

::: {.proof}
By Exercise I.5.3, the multiplicity is the least index $m$ for which $f_m\ne0$.
Since $f$ has degree at most $d$ and is nonzero, such an index satisfies $m\le d$.
:::

<1>2. If the multiplicity at $P$ were $d$, then $F$ would be reducible for $d>1$.

::: {.proof}
Multiplicity $d$ means
$$
f_0=f_1=\cdots=f_{d-1}=0,
$$
so $f=f_d$ is homogeneous of degree $d$.
Homogenizing back to degree $d$ gives
$$
F(x,y,z)=f_d(x,y),
$$
which is independent of $z$.
Over the algebraically closed field $k$, the binary homogeneous form $f_d(x,y)$ factors into $d$ linear forms, counted with multiplicity.
For $d>1$ this contradicts irreducibility of $F$.

Together with step <1>1, this proves
$$
\boxed{\mu_P(Y)\le d-1}
$$
for every point of an irreducible plane curve of degree $d>1$, proving part (a).
:::

<1>3. If $\mu_P(Y)=d-1$, then the equation of $Y$ has the form
$$
F(x,y,z)=z f_{d-1}(x,y)+f_d(x,y),
$$
with $f_{d-1}\ne0$.

::: {.proof}
The multiplicity hypothesis gives
$$
f_0=\cdots=f_{d-2}=0,
\qquad f_{d-1}\ne0.
$$
Since $F$ is homogeneous of total degree $d$, the degree-$(d-1)$ affine term acquires one factor of $z$ on homogenization, while the degree-$d$ term acquires none.
This is exactly the displayed equation.
:::

<1>4. Projection from $P$ gives a birational map
$$
\pi:Y\dashrightarrow\PP^1,
\qquad
[x:y:z]\longmapsto[x:y].
$$

::: {.proof}
The map is defined away from $P$.
For a direction $[u:v]\in\PP^1$, the corresponding line through $P$ consists of points with $[x:y]=[u:v]$.
Substituting $x=u$, $y=v$ into step <1>3 gives
$$
z f_{d-1}(u,v)+f_d(u,v)=0.
$$
On the nonempty open subset
$$
W=\{[u:v]:f_{d-1}(u,v)\ne0\}\subseteq\PP^1,
$$
there is therefore exactly one residual point of $Y$ on that line, namely
$$
\rho([u:v])
=
[u f_{d-1}(u,v):v f_{d-1}(u,v):-f_d(u,v)].
$$
The three displayed coordinates are homogeneous of the same degree $d$, and on $W$ the first two do not vanish simultaneously, so $\rho$ is a morphism there.
Direct substitution gives $F(\rho([u:v]))=0$.
Moreover
$$
\pi\rho([u:v])=[u:v]
$$
on $W$.

Conversely, on the dense open subset of $Y$ where $(x,y)\ne(0,0)$ and $f_{d-1}(x,y)\ne0$, the equation
$$
z f_{d-1}(x,y)+f_d(x,y)=0
$$
forces the $z$-coordinate to be the one in the formula for $\rho$ up to projective scaling.
Thus $\rho\pi$ is the identity there.
Hence $Y$ and $\PP^1$ are birational.
:::

<1>5. The curve $Y$ is rational.

::: {.proof}
By definition, an irreducible curve is rational precisely when it is birationally equivalent to $\PP^1$.
Step <1>4 supplies such a birational equivalence, proving part (b).
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove part (a), and steps <1>3--<1>5 prove part (b).
:::
:::
