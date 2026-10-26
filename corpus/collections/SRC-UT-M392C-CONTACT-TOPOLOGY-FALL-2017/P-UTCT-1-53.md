---
schema: qual/card@1
id: P-UTCT-1-53
kind: problem
title: Contactomorphism from the cylindrically symmetric to the standard contact structure on $\mathbb R^3$
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
  note: Checked against Exercise 1.53 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the forms alpha (Example 1.48) and alpha-prime (Example 1.52) from p. 12 of Gompf Contact Topology.pdf, with a remark on the missing dz in the source.
---

::: {.problem}
On $\mathbb{R}^3$ let $\alpha = dz + x\,dy$ be the standard contact form, and let $\xi' = \ker(\alpha')$, where
$$
\alpha' = dz + \tfrac{1}{2} r^2\, d\theta = dz + \frac{x\,dy - y\,dx}{2}
$$
is the cylindrically symmetric contact form.
Let $\phi : \mathbb{R}^3 \to \mathbb{R}^3$ be
$$
\phi(x, y, z) = (x, y, z + xy/2).
$$
Show that $\phi^*\alpha' = \alpha$, where $\alpha'$ is from the example above and $\alpha$ is the standard contact structure.
This is an example of a contactomorphism.
:::

::: {.remark}
Example 1.52 of the source prints $\alpha' = dx + \frac{1}{2} r^2 d\theta$ and gives its rectangular form as $\frac{x\,dy - y\,dx}{2}$; both omit $dz$, which is needed for $\alpha'$ to be a contact form and for $\phi^*\alpha' = \alpha$ to hold.
:::

Write the target coordinates of \(\phi\) as
\[
(X,Y,Z)
=
\left(
x,\ y,\ z+\frac{xy}{2}
\right).
\]

::: pf

::: pf-step

The pullbacks of the coordinate functions are
\[
\boxed{
\phi^*X=x,
\qquad
\phi^*Y=y,
\qquad
\phi^*Z=z+\frac{xy}{2}}.
\]


::: pf-proof

This is the definition of the map
\[
\phi(x,y,z)
=
\left(
x,y,z+\frac{xy}{2}
\right).
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\phi^*dX=dx}
\]
and
\[
\boxed{
\phi^*dY=dy}.
\]


::: pf-proof

Pullback commutes with exterior differentiation:
\[
\phi^*(dX)
=
d(\phi^*X)
=
dx,
\]
and similarly for \(Y\).

:::

:::

::: pf-step

One has
\[
\boxed{
\phi^*dZ
=
dz+\frac12(x\,dy+y\,dx)}.
\]


::: pf-proof

By step <1>1,
\[
\phi^*Z
=
z+\frac{xy}{2}.
\]
Differentiate:
\[
d\left(
z+\frac{xy}{2}
\right)
=
dz+\frac12\,d(xy)
=
dz+\frac12(x\,dy+y\,dx).
\]

:::

:::

::: pf-step

The cylindrically symmetric contact form is
\[
\alpha'
=
dZ+\frac12(X\,dY-Y\,dX).
\]


::: pf-proof

This is the rectangular-coordinate expression stated in the problem.

:::

:::

::: pf-step

Pulling back the skew term gives
\[
\boxed{
\phi^*\!\left(
\frac12(X\,dY-Y\,dX)
\right)
=
\frac12(x\,dy-y\,dx)}.
\]


::: pf-proof

Using steps <1>1--<1>2,
\[
\begin{aligned}
\phi^*(X\,dY-Y\,dX)
&=
(\phi^*X)(\phi^*dY)
-
(\phi^*Y)(\phi^*dX)\\
&=
x\,dy-y\,dx.
\end{aligned}
\]
Multiply by \(1/2\).

:::

:::

::: pf-step

Hence
\[
\begin{aligned}
\phi^*\alpha'
&=
\phi^*dZ
+
\phi^*\!\left(
\frac12(X\,dY-Y\,dX)
\right)\\
&=
dz+\frac12(x\,dy+y\,dx)
+
\frac12(x\,dy-y\,dx).
\end{aligned}
\]


::: pf-proof

Apply linearity of pullback to the decomposition in step <1>4, then use
steps <1>3 and <1>5.

:::

:::

::: pf-step

The \(y\,dx\)-terms cancel, so
\[
\boxed{
\phi^*\alpha'
=
dz+x\,dy
=
\alpha}.
\]


::: pf-proof

In step <1>6,
\[
\frac12y\,dx-\frac12y\,dx=0,
\]
while
\[
\frac12x\,dy+\frac12x\,dy=x\,dy.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\phi_*(\ker\alpha)
=
\ker\alpha'}.
\]


::: pf-proof

For any tangent vector \(v\),
\[
\alpha(v)=0
\iff
(\phi^*\alpha')(v)=0
\iff
\alpha'(d\phi(v))=0.
\]
Since \(\phi\) is a diffeomorphism, this identifies the two contact
hyperplane fields.

:::

:::

::: pf-step

Hence \(\phi\) is a contactomorphism from the standard contact
structure to the cylindrically symmetric one.


::: pf-proof

By step <1>7,
\[
\phi^*\alpha'=\alpha,
\]
which is stronger than merely preserving the kernel distribution.

:::

:::

::: pf-qed

Step <1>7 proves the required pullback identity.

:::

:::
