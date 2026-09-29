---
schema: qual/card@1
id: P-AGXVAREXNODE
kind: problem
title: The nodal cubic, its two smooth branches, and Zariski's main theorem
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nodes
  - Normalization
  - Zariski's Main Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 6.5 and Exercise 8.7 in the recorded source.
    Together they ask for the unique node, its two transverse smooth local
    branches, the affine normalization A^1, and the projective normalization
    P^1 with a disconnected two-point fiber over the node.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Restored the Exercise 6.5 assertion that the affine nodal cubic has
    normalization A^1, which the imported card had omitted, and called the
    homogeneous cubic the projective closure rather than a projectivization.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the Jacobian singular-locus computation, analytic factorization
    into two smooth transverse branches, the affine integral closure using
    t=x/y, the homogeneous P^1 parametrization, birationality, the two-point
    fiber over the node, and the resulting failure of Zariski Main without
    normality of the target.
---

::: {.problem}
Show that the nodal cubic $X = V(x^2 - y^2(y-1))$ has a unique singular point.

Show that $X$ locally has two smooth branches at zero meeting transversally.

Show that the normalization of $X$ is $\AA^1_\CC$.

Consider the projective closure
$$
\overline X=V(x^2z-y^2(y-z))\subseteq\PP^2_\CC.
$$
Show that its normalization morphism
$$
\nu:\PP^1_\CC\longrightarrow\overline X
$$
is birational, and that $\nu^{-1}([0:0:1])$ consists of two points.
Compare this to Zariski's main theorem.
:::

::: {.solution}
Put
$$
F(x,y)=x^2-y^2(y-1)=x^2+y^2-y^3.
$$

::: pf

::: {.pf-step #origin-unique-singular}
The origin is the unique singular point of $X$.

::: pf-proof
The partial derivatives are
$$
F_x=2x,
\qquad
F_y=2y-3y^2=y(2-3y).
$$
A singular point must satisfy
$$
F=F_x=F_y=0.
$$
From $F_x=0$ one gets $x=0$, and $F_y=0$ gives
$$
y=0
\qquad\text{or}\qquad
y=\frac23.
$$
The second possibility does not lie on $X$, because
$$
F\left(0,\frac23\right)
=
\frac4{27}
\neq0.
$$
Hence the unique singular point is
$$
\boxed{(0,0)}.
$$
:::

:::

::: {.pf-step #two-smooth-branches}
The germ $(X,0)$ has exactly two smooth branches, with tangent lines
$$
x+iy=0
\qquad\text{and}\qquad
x-iy=0,
$$
and the two branches meet transversally.

::: pf-proof
Let
$$
s(y)=\sqrt{1-y}\in\CC\{y\}
$$
be the convergent square root satisfying $s(0)=1$. In
$$
\CC\{x,y\}
$$
one has
$$
\begin{aligned}
F
&=x^2+y^2(1-y)\\
&=(x+iys(y))(x-iys(y)).
\end{aligned}
$$
Thus there are two local analytic branches
$$
B_+=V(x+iys(y)),
\qquad
B_-=V(x-iys(y)).
$$
Each branch is smooth at the origin because the derivative of its defining
equation with respect to $x$ is $1$.

Since
$$
s(y)=1+\text{terms of order at least }1,
$$
the linear terms of the two defining equations are
$$
x+iy
\qquad\text{and}\qquad
x-iy.
$$
These are distinct linear forms, so the tangent lines are distinct. Hence the
two smooth branches meet transversally at the origin.
:::

:::

::: {.pf-step #nu-aff-finite-birational}
The morphism
$$
\nu_{\mathrm{aff}}:\AA^1_\CC\longrightarrow X,
\qquad
t\longmapsto
\bigl(t(t^2+1),t^2+1\bigr),
$$
is finite and birational.

::: pf-proof
The image lies on $X$, because
$$
\begin{aligned}
x^2-y^2(y-1)
&=t^2(t^2+1)^2-(t^2+1)^2t^2\\
&=0.
\end{aligned}
$$

The induced inclusion of coordinate rings is
$$
A
=
\CC[x,y]/(x^2-y^2(y-1))
\hookrightarrow
\CC[t],
$$
with
$$
x\longmapsto t(t^2+1),
\qquad
y\longmapsto t^2+1.
$$
In $\CC[t]$,
$$
t^2=y-1,
$$
so $t$ is integral over $A$. Moreover
$$
\CC[t]=A[t],
$$
and therefore $\CC[t]$ is finite over $A$.

In the fraction field of $A$,
$$
t=\frac{x}{y},
$$
because $x=t(t^2+1)$ and $y=t^2+1$. Thus
$$
\Frac A=\CC(t),
$$
so the morphism is birational.
:::

:::

::: {.pf-step #normalization-a1}
The normalization of the affine nodal cubic is
$$
\boxed{X^{\operatorname{norm}}\cong\AA^1_\CC.}
$$

::: pf-proof
By step [](#nu-aff-finite-birational){.pf-ref}, $\CC[t]$ is integral over $A$ and has the same fraction field.
Let $\overline A$ be the integral closure of $A$ in that field. Then
$$
\CC[t]\subseteq\overline A.
$$
Conversely, every element of $\overline A$ is integral over $A$, hence also
integral over $\CC[t]$ because $A\subseteq\CC[t]$. The ring $\CC[t]$ is a
UFD and therefore integrally closed in $\CC(t)$, so
$$
\overline A\subseteq\CC[t].
$$
Thus
$$
\overline A=\CC[t],
$$
which proves the normalization statement.
:::

:::

::: {.pf-step #nu-extends-to-p1}
The affine normalization from step [](#nu-aff-finite-birational){.pf-ref} extends to the morphism
$$
\nu:\PP^1_\CC\longrightarrow\overline X
$$
given by
$$
\boxed{
\nu([u:v])
=
\bigl[
u(u^2+v^2):
v(u^2+v^2):
v^3
\bigr].
}
$$

::: pf-proof
The three homogeneous coordinate functions have degree $3$. They do not
vanish simultaneously: if $v=0$, then $u\neq0$ and the first coordinate is
$u^3\neq0$; if $v\neq0$ and $u^2+v^2=0$, then the third coordinate
$v^3$ is nonzero.

Put
$$
X_0=u(u^2+v^2),
\qquad
Y_0=v(u^2+v^2),
\qquad
Z_0=v^3.
$$
Then
$$
\begin{aligned}
X_0^2Z_0
&=u^2v^3(u^2+v^2)^2,\\
Y_0^2(Y_0-Z_0)
&=v^2(u^2+v^2)^2
   \bigl(v(u^2+v^2)-v^3\bigr)\\
&=u^2v^3(u^2+v^2)^2.
\end{aligned}
$$
Hence
$$
X_0^2Z_0-Y_0^2(Y_0-Z_0)=0,
$$
so the image lies in $\overline X$.

On the chart $v=1$, the formula becomes
$$
t=u
\longmapsto
[t(t^2+1):t^2+1:1],
$$
which is exactly the affine normalization from step [](#nu-aff-finite-birational){.pf-ref}.
:::

:::

::: {.pf-step #nu-is-normalization-birational}
The morphism $\nu:\PP^1_\CC\to\overline X$ is the normalization
morphism and is birational.

::: pf-proof
On the dense open set where $y\neq0$, the rational function
$$
t=\frac{x}{y}
$$
recovers the affine parameter from step [](#nu-aff-finite-birational){.pf-ref}. Thus $\nu$ induces an
isomorphism of function fields and is birational.

The source $\PP^1_\CC$ is smooth, hence normal. The morphism $\nu$ is
nonconstant between projective curves, so it is finite. Therefore it is a
finite birational morphism from a normal curve, and hence it is the
normalization of $\overline X$.
:::

:::

::: {.pf-step #fiber-over-node}
The fiber over the node
$$
P=[0:0:1]\in\overline X
$$
is
$$
\boxed{
\nu^{-1}(P)
=
\{[i:1],[-i:1]\}.
}
$$

::: pf-proof
If
$$
\nu([u:v])=[0:0:1],
$$
then $v\neq0$, so scale to $v=1$. The first two coordinates vanish exactly
when
$$
u(u^2+1)=0,
\qquad
u^2+1=0.
$$
The second equation already implies the first, and it has exactly the two
solutions
$$
u=i,
\qquad
u=-i.
$$
Thus the fiber is the displayed two-point set.
:::

:::

::: {.pf-step #zariski-main-fails}
The conclusion of Zariski's Main Theorem fails for $\nu$: the
birational morphism $\nu$ has a disconnected fiber over the node, where the
target $\overline X$ is not normal.

::: pf-proof
Zariski's Main Theorem states that a birational morphism between normal
projective varieties has connected fibers. The normalization morphism
$$
\nu:\PP^1_\CC\longrightarrow\overline X
$$
is birational and has normal source, but step [](#fiber-over-node){.pf-ref} gives a disconnected fiber
over the node. The normalization is an isomorphism over the normal locus of
$\overline X$, so $\overline X$ is not normal at $P$.
:::

:::

::: pf-qed
Steps [](#origin-unique-singular){.pf-ref} and [](#two-smooth-branches){.pf-ref} establish the nodal singularity and its two transverse
branches. Steps [](#nu-aff-finite-birational){.pf-ref} and [](#normalization-a1){.pf-ref} compute the affine normalization. Steps
[](#nu-extends-to-p1){.pf-ref}, [](#nu-is-normalization-birational){.pf-ref} and [](#fiber-over-node){.pf-ref} compute the projective normalization and the two-point fiber, and
step [](#zariski-main-fails){.pf-ref} gives the requested comparison with Zariski's Main Theorem.
:::

:::

:::
