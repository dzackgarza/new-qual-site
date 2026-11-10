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

::: pf

::: {.pf-step #multiplicity-at-most-d}
The multiplicity of $Y$ at $P$ is at most $d$.

::: pf-proof
By Exercise I.5.3, the multiplicity is the least index $m$ for which $f_m\ne0$.
Since $f$ has degree at most $d$ and is nonzero, such an index satisfies $m\le d$.
:::

:::

::: {.pf-step #multiplicity-d-reducible}
If the multiplicity at $P$ were $d$, then $F$ would be reducible for $d>1$.

::: pf-proof
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

Together with step [](#multiplicity-at-most-d){.pf-ref}, this proves
$$
\boxed{\mu_P(Y)\le d-1}
$$
for every point of an irreducible plane curve of degree $d>1$, proving part (a).
:::

:::

::: {.pf-step #equation-form-mult-d-minus-1}
If $\mu_P(Y)=d-1$, then the equation of $Y$ has the form
$$
F(x,y,z)=z f_{d-1}(x,y)+f_d(x,y),
$$
with $f_{d-1}\ne0$.

::: pf-proof
The multiplicity hypothesis gives
$$
f_0=\cdots=f_{d-2}=0,
\qquad f_{d-1}\ne0.
$$
Since $F$ is homogeneous of total degree $d$, the degree-$(d-1)$ affine term acquires one factor of $z$ on homogenization, while the degree-$d$ term acquires none.
This is exactly the displayed equation.
:::

:::

::: {.pf-step #projection-birational}
Projection from $P$ gives a birational map
$$
\pi:Y\dashrightarrow\PP^1,
\qquad
[x:y:z]\longmapsto[x:y].
$$

::: pf-proof
The map is defined away from $P$.
For a direction $[u:v]\in\PP^1$, the corresponding line through $P$ consists of points with $[x:y]=[u:v]$.
Substituting $x=u$, $y=v$ into step [](#equation-form-mult-d-minus-1){.pf-ref} gives
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

:::

::: {.pf-step #curve-is-rational}
The curve $Y$ is rational.

::: pf-proof
By definition, an irreducible curve is rational precisely when it is birationally equivalent to $\PP^1$.
Step [](#projection-birational){.pf-ref} supplies such a birational equivalence, proving part (b).
:::

:::

::: pf-qed
Steps [](#multiplicity-at-most-d){.pf-ref} and [](#multiplicity-d-reducible){.pf-ref} prove part (a), and steps [](#equation-form-mult-d-minus-1){.pf-ref}, [](#projection-birational){.pf-ref} and [](#curve-is-rational){.pf-ref} prove part (b).
:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 7.5, PDF p. 9: (a) "we can assume that any point $P$ of multiplicity at least $d$ is $(0,0)$. But then the equation $f(x,y)$ defining $Y$ has all terms of degree exactly $d$, so it is a product of linear factors, which is not possible if $Y$ is irreducible of degree greater than $1$"; (b) "the equation defining $Y$ is of the form $f(x,y)+g(x,y)=0$ where $f$ is homogeneous of degree $d-1$ and $g$ is homogeneous of degree $d$. If we make the substitution $t=y/x$ we find that $y=-f(t,1)/g(t,1)$, $x=yt$ gives an inverse rational map so that $Y$ is birational to $\AA^1$."
William Troiani, *Hartshorne Exercise Solutions* (October 2020), stops at §I.5 and gives no solution to 7.5.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.7.5, PDF pp. 57--58: (a) "the degree can be read off the lowest term in the equation if the point is at $(0,0)$. If all terms have degree $d$, then it can't be irreducible of degree $>1$"; (b) "assume $Y$ is defined by $f(x,y)+g(x,y)=0$, with $\deg f=d-1$, $\deg g=d$; if $t=y/x$, then $(x,y)\mapsto\left(yt,-f(t,1)/g(t,1)\right)$ which is projection from a point gives an inverse rational map to $\AA^1$".
Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, Exercise I.7.5, PDF p. 26: (a) is proved differently — "pick any line through the singular point $P$ of multiplicity $\ge d$ and any other point $Q$. Then $(C.L)=(C.L)_P+(C.L)_Q>d$, which contradicts Bezout's Theorem"; (b) the same substitution, "this is just the projection from a point and gives a birational map to $\AA^1$".
(a) agrees in all three sets and with the card. For (b) the three display the inverse as the pair $(yt,-f(t,1)/g(t,1))$, a ratio in which the two coordinates are not homogeneous of the same degree, and none checks that the parametrized point lies on $Y$. Step [](#projection-birational){.pf-ref} writes it homogeneously as $[u f_{d-1}(u,v):v f_{d-1}(u,v):-f_d(u,v)]$ and verifies $F=0$ by substitution, which is the step the printed answers leave out. Matches.
:::
