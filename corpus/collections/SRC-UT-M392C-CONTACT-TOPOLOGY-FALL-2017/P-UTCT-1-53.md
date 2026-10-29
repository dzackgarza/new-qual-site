---
schema: qual/card@1
id: P-UTCT-1-53
kind: problem
title: Contactomorphism from the cylindrically symmetric to the standard contact structure on $\RR^3$
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
On $\RR^3$ let $\alpha = dz + x\,dy$ be the standard contact form, and let $\xi' = \ker(\alpha')$, where
$$
\alpha' = dz + \tfrac{1}{2} r^2\, d\theta = dz + \frac{x\,dy - y\,dx}{2}
$$
is the cylindrically symmetric contact form.
Let $\phi : \RR^3 \to \RR^3$ be
$$
\phi(x, y, z) = (x, y, z + xy/2).
$$
Show that $\phi^*\alpha' = \alpha$, where $\alpha'$ is from the example above and $\alpha$ is the standard contact structure.
This is an example of a contactomorphism.
:::

::: {.remark}
Example 1.52 of the source prints $\alpha' = dx + \frac{1}{2} r^2 d\theta$ and gives its rectangular form as $\frac{x\,dy - y\,dx}{2}$; both omit $dz$, which is needed for $\alpha'$ to be a contact form and for $\phi^*\alpha' = \alpha$ to hold.
:::

::: {.solution}

Write the target coordinates of \(\phi\) as
\[
(X,Y,Z)
=
\left(
x,\ y,\ z+\frac{xy}{2}
\right).
\]

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

One has
\[
\boxed{
\phi^*dZ
=
dz+\frac12(x\,dy+y\,dx)}.
\]


::: pf-proof

By step [](#s1-1){.pf-ref},
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

::: {.pf-step #s1-4}

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

::: {.pf-step #s1-5}

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

Using steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
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

::: {.pf-step #s1-6}

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

Apply linearity of pullback to the decomposition in step [](#s1-4){.pf-ref}, then use
steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

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

In step [](#s1-6){.pf-ref},
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

By step [](#s1-7){.pf-ref},
\[
\phi^*\alpha'=\alpha,
\]
which is stronger than merely preserving the kernel distribution.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves the required pullback identity.

:::

:::

:::
