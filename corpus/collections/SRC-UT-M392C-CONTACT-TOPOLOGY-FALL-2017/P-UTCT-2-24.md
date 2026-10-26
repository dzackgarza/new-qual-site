---
schema: qual/card@1
id: P-UTCT-2-24
kind: problem
title: Characteristic foliation of $dz+a\,dx+b\,dy$ on the $xy$-plane
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
  note: Checked against Exercise 2.24 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Recovered the foliation equation x^b y^a = c from p. 20 of Gompf Contact Topology.pdf, stated the definitions of sign and divergence, and noted that the printed form with constant a, b does not give that foliation.
---

::: {.problem}
For a surface $F$ in a $3$-manifold with a plane field $\xi = \ker(\alpha)$, the characteristic foliation $\mathcal{F}$ of $F$ is cut out by a vector field $v$ with $\iota_v \omega = \alpha|_F$ for a positive area form $\omega$ on $F$, where $\operatorname{div}_\omega v$ is defined by $\mathcal{L}_v \omega = (\operatorname{div}_\omega v)\,\omega$, and $\operatorname{sign}(\xi) = \operatorname{sign}(\alpha \wedge d\alpha)$.

Let $M = \mathbb{R}^3$ and let $\alpha = dz + a\,dx + b\,dy$ for $(a, b) \in \mathbb{R}^2 - \{0\}$.
Determine $\operatorname{sign}(\xi)$ and $\operatorname{div}_\omega v$ for $\mathcal{F}$ on the $x$-$y$ plane.
Check that the characteristic foliation is given by $x^b y^a = c$.
Draw a picture and observe how these vary with $a$ and $b$.
How is $\operatorname{sign}(\operatorname{div}_\omega \mathcal{F})$ visible?
:::

::: {.remark}
The first paragraph restates the definitions of Section 2 of the source (Definition 2.20, Theorem 2.23).
As printed, with $a$ and $b$ constants, $d\alpha = 0$, and $\alpha|_{xy\text{-plane}} = a\,dx + b\,dy$ has the lines $ax + by = c$ as leaves rather than the curves $x^b y^a = c$; the source does not say how $a$ and $b$ are meant to vary.
:::

Take the positive area form
\[
\omega=dx\wedge dy
\]
on the $xy$-plane.

::: pf

::: pf-step

For the printed form
\[
\alpha
=
dz+a\,dx+b\,dy
\]
with constant $a,b$, one has
\[
d\alpha=0.
\]


::: pf-proof

The functions $a$ and $b$ are constants, so
\[
d(a\,dx)=0,
\qquad
d(b\,dy)=0,
\]
and of course
\[
d(dz)=0.
\]
Therefore
\[
d\alpha=0.
\]

:::

:::

::: pf-step

Consequently
\[
\alpha\wedge d\alpha=0.
\]
Thus the printed plane field
\[
\xi=\ker\alpha
\]
is not a contact structure.


::: pf-proof

By step <1>1,
\[
\alpha\wedge d\alpha
=
\alpha\wedge0
=
0.
\]
A contact form on a $3$-manifold must satisfy
\[
\alpha\wedge d\alpha\ne0
\]
everywhere. Hence the printed $\alpha$ is not contact. In particular the
usual positive/negative contact sign is not defined as a nonzero sign; the
displayed $3$-form has value zero.

:::

:::

::: pf-step

On the $xy$-plane,
\[
\alpha|_F
=
a\,dx+b\,dy.
\]
The characteristic vector field determined by
\[
\iota_v\omega
=
\alpha|_F
\]
is
\[
\boxed{
v
=
b\frac{\partial}{\partial x}
-
a\frac{\partial}{\partial y}.
}
\]


::: pf-proof

Write
\[
v=P\frac{\partial}{\partial x}
+Q\frac{\partial}{\partial y}.
\]
For
\[
\omega=dx\wedge dy,
\]
one has
\[
\iota_v\omega
=
P\,dy-Q\,dx.
\]
Equating this with
\[
a\,dx+b\,dy
\]
gives
\[
P=b,
\qquad
-Q=a.
\]
Hence
\[
Q=-a.
\]

:::

:::

::: pf-step

The divergence of the printed characteristic field is
\[
\boxed{
\operatorname{div}_\omega v=0.
}
\]


::: pf-proof

For the standard area form,
\[
\operatorname{div}_\omega
\left(
P\partial_x+Q\partial_y
\right)
=
\partial_xP+\partial_yQ.
\]
Here
\[
P=b,
\qquad
Q=-a
\]
are constant, so
\[
\operatorname{div}_\omega v
=
0+0
=
0.
\]
Equivalently,
\[
\mathcal L_v\omega
=
d(\iota_v\omega)
=
d(\alpha|_F)
=
0.
\]

:::

:::

::: pf-step

The leaves of the printed characteristic foliation are
\[
\boxed{
ax+by=c.
}
\]


::: pf-proof

Along an integral curve
\[
(x(t),y(t))
\]
of $v$,
\[
x'(t)=b,
\qquad
y'(t)=-a.
\]
Therefore
\[
\frac{d}{dt}
\bigl(
ax(t)+by(t)
\bigr)
=
a b+b(-a)
=
0.
\]
Thus
\[
ax+by
\]
is constant on every leaf.

Conversely, the tangent direction to a level line
\[
ax+by=c
\]
is annihilated by
\[
a\,dx+b\,dy,
\]
so these are exactly the leaves.

:::

:::

::: pf-step

Hence the source claim
\[
x^b y^a=c
\]
does not follow from the printed $1$-form.


::: pf-proof

Step <1>5 gives the actual first integral of the printed characteristic line
field. Except in degenerate special cases, its leaves are affine lines, not
the monomial curves requested by the source.

:::

:::

::: pf-step

A natural corrected form producing the advertised monomial leaves is
\[
\widetilde\alpha
=
dz+b y\,dx+a x\,dy.
\]


::: pf-proof

Restricting to the $xy$-plane gives
\[
\widetilde\alpha|_F
=
b y\,dx+a x\,dy.
\]
The level curves of
\[
\Phi(x,y)
=
x^b y^a
\]
on any quadrant where this expression is real and smooth satisfy
\[
d\log|\Phi|
=
b\frac{dx}{x}
+
a\frac{dy}{y}.
\]
Multiplying by $xy$ gives the proportional $1$-form
\[
b y\,dx+a x\,dy.
\]
Thus its kernel is exactly tangent to the advertised level curves.

:::

:::

::: pf-step

For the corrected form, the characteristic vector field is
\[
\boxed{
\widetilde v
=
a x\frac{\partial}{\partial x}
-
b y\frac{\partial}{\partial y}.
}
\]


::: pf-proof

As in step <1>3,
\[
\iota_{P\partial_x+Q\partial_y}
(dx\wedge dy)
=
P\,dy-Q\,dx.
\]
Set this equal to
\[
b y\,dx+a x\,dy.
\]
Then
\[
P=a x,
\qquad
-Q=b y,
\]
so
\[
Q=-b y.
\]

:::

:::

::: pf-step

The corrected divergence is
\[
\boxed{
\operatorname{div}_\omega\widetilde v
=
a-b.
}
\]


::: pf-proof

Differentiate the components from step <1>8:
\[
\operatorname{div}_\omega\widetilde v
=
\partial_x(a x)
+
\partial_y(-b y)
=
a-b.
\]

:::

:::

::: pf-step

The corrected contact sign is governed by the same quantity:
\[
\widetilde\alpha\wedge d\widetilde\alpha
=
(a-b)
\,dx\wedge dy\wedge dz.
\]
Hence, relative to the standard orientation,
\[
\boxed{
\operatorname{sign}(\widetilde\xi)
=
\operatorname{sign}(a-b)
}
\]
when $a\ne b$.


::: pf-proof

Compute
\[
\begin{aligned}
d\widetilde\alpha
&=
d(b y\,dx)
+
d(a x\,dy)\\
&=
b\,dy\wedge dx
+
a\,dx\wedge dy\\
&=
(a-b)\,dx\wedge dy.
\end{aligned}
\]
Therefore
\[
\begin{aligned}
\widetilde\alpha\wedge
d\widetilde\alpha
&=
\bigl(
dz+b y\,dx+a x\,dy
\bigr)
\wedge
(a-b)\,dx\wedge dy\\
&=
(a-b)
\,dz\wedge dx\wedge dy.
\end{aligned}
\]
The permutation
\[
(dz,dx,dy)
\longmapsto
(dx,dy,dz)
\]
is even, so
\[
dz\wedge dx\wedge dy
=
dx\wedge dy\wedge dz.
\]
Thus the sign is the sign of $a-b$.

:::

:::

::: pf-step

For the corrected problem, the sign of the divergence is visible in
the phase portrait:

- if $a-b>0$, area expands infinitesimally along the characteristic flow;
- if $a-b<0$, area contracts;
- if $a=b$, the divergence vanishes and the corrected form is again not
  contact.


::: pf-proof

By definition,
\[
\mathcal L_{\widetilde v}\omega
=
(\operatorname{div}_\omega\widetilde v)\omega.
\]
Using step <1>9,
\[
\mathcal L_{\widetilde v}\omega
=
(a-b)\omega.
\]
Positive coefficient means local area expansion, negative coefficient means
local contraction, and zero means infinitesimal area preservation.

:::

:::

::: pf-qed

Steps <1>1--<1>6 give the exact answer for the $1$-form printed in the
source. Steps <1>7--<1>11 give the natural corrected calculation that
produces the advertised leaves
\[
x^b y^a=c
\]
and the intended nonzero divergence/contact-sign discussion.

:::

:::
