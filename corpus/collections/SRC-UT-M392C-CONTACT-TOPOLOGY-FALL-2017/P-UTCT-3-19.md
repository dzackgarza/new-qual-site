---
schema: qual/card@1
id: P-UTCT-3-19
kind: problem
title: Half-elliptic and half-hyperbolic singularities on a piecewise graph surface
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Exercise 3.19 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
---

::: {.problem}
Let $F$ be the graph of $f:\mathbb R^2\to\mathbb R$ defined by
\[
f(x,y)=\begin{cases}
0,&y\le0,\\
bxy,&y\ge0.
\end{cases}
\]
Take the contact structure $dz+x\,dy$. Show that the singularity at $0$ is half-elliptic if $-1<b<0$ and half-hyperbolic if $b<-1$ or $b>0$. Show also that $\xi$ twists right relative to $F$ if $b<-1$ and left relative to $F$ if $b>-1$.
:::

Let
\[
\alpha=dz+x\,dy,
\qquad
\xi=\ker\alpha.
\]
Parametrize the two halves of \(F\) by
\[
\Phi_-(x,y)=(x,y,0)
\qquad(y\le0)
\]
and
\[
\Phi_+(x,y)=(x,y,bxy)
\qquad(y\ge0).
\]

Choose the positive area form
\[
\omega=dx\wedge dy
\]
on the parameter plane.

## The lower half-plane

::: pf

::: pf-step

On \(y\le0\),
\[
\boxed{
\Phi_-^*\alpha
=
x\,dy}.
\]


::: pf-proof

Since
\[
z=0
\]
on the lower half,
\[
dz=0,
\]
so
\[
\Phi_-^*(dz+x\,dy)
=
x\,dy.
\]

:::

:::

::: pf-step

If
\[
v_-=P\,\partial_x+Q\,\partial_y
\]
satisfies
\[
\iota_{v_-}\omega=\Phi_-^*\alpha,
\]
then
\[
\boxed{
v_-=x\,\partial_x}.
\]


::: pf-proof

For
\[
\omega=dx\wedge dy,
\]
one has
\[
\iota_{P\partial_x+Q\partial_y}\omega
=
P\,dy-Q\,dx.
\]
Comparing with
\[
x\,dy
\]
gives
\[
P=x,
\qquad
Q=0.
\]

:::

:::

::: pf-step

Hence the lower-half singular set is
\[
\boxed{
\{x=0,\ y\le0\}}.
\]


::: pf-proof

The vector field in step <1>2 vanishes exactly when \(x=0\).

:::

:::

::: pf-step

On \(y\ge0\),
\[
dz
=
b\,y\,dx+b\,x\,dy.
\]


::: pf-proof

Differentiate
\[
z=bxy.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\Phi_+^*\alpha
=
b\,y\,dx+(b+1)x\,dy}.
\]


::: pf-proof

Using step <1>4,
\[
\begin{aligned}
\Phi_+^*\alpha
&=
dz+x\,dy\\
&=
b\,y\,dx+b\,x\,dy+x\,dy\\
&=
b\,y\,dx+(b+1)x\,dy.
\end{aligned}
\]

:::

:::

::: pf-step

If
\[
v_+=P\,\partial_x+Q\,\partial_y
\]
satisfies
\[
\iota_{v_+}\omega=\Phi_+^*\alpha,
\]
then
\[
\boxed{
v_+
=
(b+1)x\,\partial_x
-
b\,y\,\partial_y}.
\]


::: pf-proof

As in step <1>2,
\[
\iota_{v_+}\omega
=
P\,dy-Q\,dx.
\]
Comparing with step <1>5 gives
\[
P=(b+1)x,
\qquad
-Q=by,
\]
hence
\[
Q=-by.
\]

:::

:::

::: pf-step

The linearization of \(v_+\) at the origin is
\[
\boxed{
Dv_+(0)
=
\begin{pmatrix}
b+1&0\\
0&-b
\end{pmatrix}}.
\]


::: pf-proof

The vector field in step <1>6 is already linear.

:::

:::

::: pf-step

If
\[
-1<b<0,
\]
then both eigenvalues are positive:
\[
b+1>0,
\qquad
-b>0.
\]


::: pf-proof

These inequalities are immediate from the stated range.

:::

:::

::: pf-step

Hence, when
\[
-1<b<0,
\]
the origin is a source for the upper-half characteristic foliation.


::: pf-proof

The solutions of
\[
\dot x=(b+1)x,
\qquad
\dot y=-by
\]
are
\[
x(t)=x_0e^{(b+1)t},
\qquad
y(t)=y_0e^{-bt}.
\]
With both exponents positive, nonconstant trajectories move away from the
origin as \(t\to+\infty\).

:::

:::

::: pf-step

Therefore the endpoint of the lower singular curve at the origin is
\[
\boxed{\text{half-elliptic}}
\]
when
\[
\boxed{-1<b<0}.
\]


::: pf-proof

The lower half contributes the singular curve ending at the origin by step
<1>3, while the upper half has source-type elliptic dynamics by step <1>9.
This is precisely the half-elliptic local model from the notes.

:::

:::

::: pf-step

If
\[
b<-1,
\]
then
\[
b+1<0
\qquad\text{and}\qquad
-b>0.
\]


::: pf-proof

Immediate from \(b<-1\).

:::

:::

::: pf-step

If
\[
b>0,
\]
then
\[
b+1>0
\qquad\text{and}\qquad
-b<0.
\]


::: pf-proof

Immediate from \(b>0\).

:::

:::

::: pf-step

In either case
\[
b<-1
\qquad\text{or}\qquad
b>0,
\]
the origin is a saddle for the upper-half characteristic foliation.


::: pf-proof

Steps <1>11--<1>12 show that the two eigenvalues of the diagonal
linearization in step <1>7 have opposite signs.

:::

:::

::: pf-step

Therefore the origin is
\[
\boxed{\text{half-hyperbolic}}
\]
when
\[
\boxed{
b<-1
\quad\text{or}\quad
b>0}.
\]


::: pf-proof

The lower half again supplies the singular curve from step <1>3, while the
upper half has hyperbolic saddle dynamics by step <1>13. This is the
half-hyperbolic local model.

:::

:::

::: pf-step

Along \(\gamma\), the tangent vector
\[
\partial_x
\]
lies in both \(TF\) and \(\xi\).


::: pf-proof

The \(x\)-axis lies in \(F\), so \(\partial_x\in TF\). Also
\[
\alpha(\partial_x)
=
dz(\partial_x)+x\,dy(\partial_x)
=
0.
\]
Thus
\[
\partial_x\in\xi.
\]

:::

:::

::: pf-step

On the upper side of \(F\), a vector tangent to \(F\) and transverse
to \(\partial_x\) along \(\gamma\) is
\[
\boxed{
\nu_F
=
\partial_y+b x\,\partial_z}.
\]


::: pf-proof

Differentiate the graph parametrization
\[
\Phi_+(x,y)=(x,y,bxy)
\]
in the \(y\)-direction:
\[
d\Phi_+(\partial_y)
=
\partial_y+b x\,\partial_z.
\]
At \(y=0\) this is tangent to the upper side of \(F\) and linearly
independent from \(\partial_x\).

:::

:::

::: pf-step

A vector in \(\xi\) transverse to \(\partial_x\) along \(\gamma\) is
\[
\boxed{
\nu_\xi
=
\partial_y-x\,\partial_z}.
\]


::: pf-proof

Compute
\[
\alpha(\partial_y-x\,\partial_z)
=
x-x
=
0.
\]
Thus \(\nu_\xi\in\xi\), and it is clearly transverse to \(\partial_x\).

:::

:::

::: pf-step

In the oriented normal \(yz\)-plane to \(\gamma\), the slopes of the
two framing vectors are
\[
\boxed{
\operatorname{slope}(\nu_F)=bx}
\]
and
\[
\boxed{
\operatorname{slope}(\nu_\xi)=-x}.
\]


::: pf-proof

Relative to the basis
\[
(\partial_y,\partial_z),
\]
the vectors are
\[
\nu_F=(1,bx),
\qquad
\nu_\xi=(1,-x).
\]
Their vertical-over-horizontal slopes are therefore \(bx\) and \(-x\).

:::

:::

::: pf-step

The infinitesimal relative slope of the contact framing with respect
to the surface framing at the origin is
\[
\boxed{
\frac{d}{dx}
\left[
(-x)-(bx)
\right]_{x=0}
=
-(b+1)}.
\]


::: pf-proof

Subtract the two slopes in step <1>18:
\[
-x-bx
=
-(b+1)x,
\]
then differentiate with respect to \(x\).

:::

:::

::: pf-step

If
\[
b<-1,
\]
then
\[
-(b+1)>0.
\]


::: pf-proof

Since \(b+1<0\), its negative is positive.

:::

:::

::: pf-step

Thus, in the right-hand convention used in the notes,
\[
\boxed{
\xi\text{ twists right relative to }F}
\]
when
\[
\boxed{b<-1}.
\]


::: pf-proof

Step <1>19 measures the signed first-order rotation of the contact framing
relative to the surface framing in the oriented normal plane. Positive
relative rotation is the right-hand twist convention of the local model, and
step <1>20 shows that this occurs exactly for \(b<-1\).

:::

:::

::: pf-step

If
\[
b>-1,
\]
then
\[
-(b+1)<0.
\]


::: pf-proof

Now \(b+1>0\).

:::

:::

::: pf-step

Hence
\[
\boxed{
\xi\text{ twists left relative to }F}
\]
when
\[
\boxed{b>-1}.
\]


::: pf-proof

By step <1>19, the relative first-order rotation is negative in this range,
which is the left-hand twist convention.

:::

:::

::: pf-qed

Steps <1>10 and <1>14 classify the half-elliptic and half-hyperbolic
singularities, while steps <1>21 and <1>23 give the relative twisting
directions.

:::

:::
