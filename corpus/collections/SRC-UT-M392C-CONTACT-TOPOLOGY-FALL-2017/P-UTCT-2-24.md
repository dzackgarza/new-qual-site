---
schema: qual/card@1
id: P-UTCT-2-24
kind: problem
title: Characteristic foliation of $dz+by\,dx+ax\,dy$ on the $xy$-plane
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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source printed alpha = dz + a dx + b dy with constant a, b, which is closed and has straight-line leaves instead of x^b y^a = c; the statement now uses alpha = dz + by dx + ax dy with a different from b, whose leaves are |x|^b |y|^a = c on each quadrant.
---

::: {.problem}
For a surface $F$ in a $3$-manifold with a plane field $\xi = \ker(\alpha)$, the characteristic foliation $\mathcal{F}$ of $F$ is cut out by a vector field $v$ with $\iota_v \omega = \alpha|_F$ for a positive area form $\omega$ on $F$, where $\operatorname{div}_\omega v$ is defined by $\mathcal{L}_v \omega = (\operatorname{div}_\omega v)\,\omega$, and $\operatorname{sign}(\xi) = \operatorname{sign}(\alpha \wedge d\alpha)$.

Let $M = \RR^3$ and let $\alpha = dz + b y\,dx + a x\,dy$ for real numbers $a \neq b$.
Determine $\operatorname{sign}(\xi)$ and $\operatorname{div}_\omega v$ for $\mathcal{F}$ on the $x$-$y$ plane.
Check that on each open quadrant the characteristic foliation is given by $|x|^b |y|^a = c$.
Draw a picture and observe how these vary with $a$ and $b$.
How is $\operatorname{sign}(\operatorname{div}_\omega \mathcal{F})$ visible?
:::

::: {.remark}
The first paragraph restates the definitions of Section 2 of the source (Definition 2.20, Theorem 2.23).
:::

::: {.solution}

Take the positive area form
\[
\omega=dx\wedge dy
\]
on the $xy$-plane.

::: pf

::: {.pf-step #s1-1}

On each open quadrant, the leaves of the characteristic foliation of
\[
\alpha
=
dz+b y\,dx+a x\,dy
\]
on the $xy$-plane are the curves $|x|^b|y|^a=c$.


::: pf-proof

Restricting to the $xy$-plane gives
\[
\alpha|_F
=
b y\,dx+a x\,dy.
\]
The level curves of
\[
\Phi(x,y)
=
|x|^b |y|^a
\]
on an open quadrant, where $\Phi$ is smooth and positive, satisfy
\[
d\log\Phi
=
b\frac{dx}{x}
+
a\frac{dy}{y}.
\]
Multiplying by $xy$ gives the proportional $1$-form
\[
b y\,dx+a x\,dy.
\]
Thus its kernel is exactly tangent to the level curves $|x|^b|y|^a=c$, and these are the leaves.

:::

:::

::: {.pf-step #s1-2}

The characteristic vector field is
\[
\boxed{
v
=
a x\frac{\partial}{\partial x}
-
b y\frac{\partial}{\partial y}.
}
\]


::: pf-proof

For
\[
\omega=dx\wedge dy
\]
and any vector field $P\partial_x+Q\partial_y$,
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

::: {.pf-step #s1-3}

The divergence is
\[
\boxed{
\operatorname{div}_\omega v
=
a-b.
}
\]


::: pf-proof

Differentiate the components from step [](#s1-2){.pf-ref}:
\[
\operatorname{div}_\omega v
=
\partial_x(a x)
+
\partial_y(-b y)
=
a-b.
\]

:::

:::

::: {.pf-step #s1-4}

The contact sign is governed by the same quantity:
\[
\alpha\wedge d\alpha
=
(a-b)
\,dx\wedge dy\wedge dz.
\]
Hence, relative to the standard orientation,
\[
\boxed{
\operatorname{sign}(\xi)
=
\operatorname{sign}(a-b).
}
\]


::: pf-proof

Compute
\[
\begin{aligned}
d\alpha
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
\alpha\wedge
d\alpha
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

::: {.pf-step #s1-5}

The sign of the divergence is visible in the phase portrait:

- if $a-b>0$, area expands infinitesimally along the characteristic flow;
- if $a-b<0$, area contracts.


::: pf-proof

By definition,
\[
\mathcal L_{v}\omega
=
(\operatorname{div}_\omega v)\omega.
\]
Using step [](#s1-3){.pf-ref},
\[
\mathcal L_{v}\omega
=
(a-b)\omega.
\]
Positive coefficient means local area expansion, and negative coefficient means
local contraction.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} identifies the leaves, step [](#s1-4){.pf-ref} gives $\operatorname{sign}(\xi)$,
steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} give the characteristic field and its divergence, and
step [](#s1-5){.pf-ref} describes how the sign of the divergence is visible.

:::

:::

:::
