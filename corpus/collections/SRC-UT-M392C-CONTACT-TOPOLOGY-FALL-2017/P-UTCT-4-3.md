---
schema: qual/card@1
id: P-UTCT-4-3
kind: problem
title: The standard contact form on $S^3$
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
  note: Checked against Exercise 4.3 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the construction of the standard contact form on S^3 preceding the exercise, from p. 32 of Gompf Contact Topology.pdf.
---

::: {.problem}
Write $S^3 = \partial B^4 \subset \CC^2$ as the preimage of $1$ of the function $r^2$, so that $\ker(d(r^2))$ along $S^3$ is $TS^3$.
There is a complex structure $J$ on $TS^3$ inherited from $\CC^2$.
Write $\alpha = d(r^2) \circ J$, and let $\xi = \ker(\alpha|_{S^3})$, the standard structure on $S^3$.

Verify that this is a positive contact form by showing that
$$
d(r^2) \wedge \alpha \wedge d\alpha
$$
is a positive volume form on $\CC^2$, and therefore $\alpha \wedge d\alpha$ is a positive volume form on $S^3$.
Do this by showing that
$$
\alpha = x_1\,dy_1 - y_1\,dx_1 + x_2\,dy_2 - y_2\,dx_2
$$
and computing $\alpha \wedge d\alpha$.
Can you show that this form restricted to $S^3 - \{*\}$ is contactomorphic to $(\RR^3, dz + x\,dy)$?
:::

::: {.solution}

Write
$$
z_j=x_j+iy_j
\qquad(j=1,2)
$$
on $\CC^2$, and use the standard complex orientation
$$
\Omega
=
dx_1\wedge dy_1\wedge dx_2\wedge dy_2.
$$

## The contact condition

::: pf

::: {.pf-step #s1-1}

With the normalization used in the notes,
$$
\boxed{
\alpha
=
x_1\,dy_1-y_1\,dx_1
+
x_2\,dy_2-y_2\,dx_2}.
$$


::: pf-proof

For the standard complex structure with
$$
J(\partial_{x_j})=-\partial_{y_j},
\qquad
J(\partial_{y_j})=\partial_{x_j},
$$
the form
$$
d(r^2)\circ J
$$
is a positive constant multiple of the displayed form. Multiplying a
defining contact form by a positive constant does not change its kernel or
its contact orientation, so the source adopts the displayed normalization.

:::

:::

::: {.pf-step #s1-2}

Its exterior derivative is
$$
\boxed{
d\alpha
=
2\,dx_1\wedge dy_1
+
2\,dx_2\wedge dy_2}.
$$


::: pf-proof

For each $j$,
$$
d(x_j\,dy_j-y_j\,dx_j)
=
dx_j\wedge dy_j-dy_j\wedge dx_j
=
2\,dx_j\wedge dy_j.
$$
Sum over $j=1,2$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{
\begin{aligned}
\alpha\wedge d\alpha
=
2\bigl(&
-y_1\,dx_1\wedge dx_2\wedge dy_2
+x_1\,dy_1\wedge dx_2\wedge dy_2\\
&-y_2\,dx_1\wedge dy_1\wedge dx_2
+x_2\,dx_1\wedge dy_1\wedge dy_2
\bigr).
\end{aligned}}
$$


::: pf-proof

Expand
$$
\alpha\wedge
2(dx_1\wedge dy_1+dx_2\wedge dy_2).
$$
The terms from the $j=1$ part of $\alpha$ vanish when wedged with
$dx_1\wedge dy_1$, and similarly for $j=2$. Reordering the surviving
terms into the displayed coordinate order gives the formula.

:::

:::

::: {.pf-step #s1-4}

The differential of the squared radius is
$$
\boxed{
d(r^2)
=
2(x_1\,dx_1+y_1\,dy_1+x_2\,dx_2+y_2\,dy_2)}.
$$


::: pf-proof

Differentiate
$$
r^2=x_1^2+y_1^2+x_2^2+y_2^2.
$$

:::

:::

::: {.pf-step #s1-5}

Wedge multiplication gives
$$
\boxed{
d(r^2)\wedge\alpha\wedge d\alpha
=
4r^2\,\Omega}.
$$


::: pf-proof

Using step [](#s1-3){.pf-ref}, only one term of $d(r^2)$ can complete each displayed
$3$-form to the ordered $4$-form $\Omega$:

$$
2x_1dx_1
$$
pairs with
$$
2x_1dy_1\wedge dx_2\wedge dy_2,
$$

$$
2y_1dy_1
$$
pairs with
$$
-2y_1dx_1\wedge dx_2\wedge dy_2,
$$

$$
2x_2dx_2
$$
pairs with
$$
2x_2dx_1\wedge dy_1\wedge dy_2,
$$

and

$$
2y_2dy_2
$$
pairs with
$$
-2y_2dx_1\wedge dy_1\wedge dx_2.
$$

After reordering, all four contributions have positive sign. Their sum is
$$
4(x_1^2+y_1^2+x_2^2+y_2^2)\Omega
=
4r^2\Omega.
$$

:::

:::

::: {.pf-step #s1-6}

On
$$
\CC^2-\{0\},
$$
the $4$-form in step [](#s1-5){.pf-ref} is positive.


::: pf-proof

For $r>0$,
$$
4r^2>0,
$$
and $\Omega$ is the chosen positive volume form.

:::

:::

::: {.pf-step #s1-7}

In particular, along
$$
S^3=\{r^2=1\},
$$
the $3$-form
$$
\boxed{
\alpha\wedge d\alpha}
$$
is a positive volume form on the outward-oriented sphere.


::: pf-proof

The outward normal is positively paired with $d(r^2)$. By step [](#s1-5){.pf-ref},
$$
d(r^2)\wedge\alpha\wedge d\alpha
$$
is positive in the ambient orientation. This is exactly the criterion that
the restriction of
$$
\alpha\wedge d\alpha
$$
to the oriented level set $S^3$ be positive.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\xi=\ker(\alpha|_{S^3})}
$$
is a positive contact structure on $S^3$.


::: pf-proof

A $1$-form on an oriented $3$-manifold is a positive contact form exactly
when
$$
\alpha\wedge d\alpha
$$
is a positive volume form. Apply step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Define
$$
\boxed{
\mathcal C(\zeta,t)
=
\left(
\frac{2\zeta}{D},
\frac{1-|\zeta|^2+it}{D}
\right)}.
$$


::: pf-proof

This is the standard Cayley transform from the Heisenberg model to the
sphere.

:::

:::

::: {.pf-step #s1-10}

The image of $\mathcal C$ lies in $S^3$.


::: pf-proof

Let
$$
w_1=\frac{2\zeta}{D},
\qquad
w_2=\frac{1-|\zeta|^2+it}{D}.
$$
Since
$$
|D|^2
=
(1+|\zeta|^2)^2+t^2,
$$
one has
$$
\begin{aligned}
|w_1|^2+|w_2|^2
&=
\frac{
4|\zeta|^2
+
(1-|\zeta|^2)^2+t^2
}{
(1+|\zeta|^2)^2+t^2
}\\
&=
\frac{
1+2|\zeta|^2+|\zeta|^4+t^2
}{
(1+|\zeta|^2)^2+t^2
}\\
&=
1.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-11}

The point
$$
(0,-1)\in S^3
$$
is not in the image of $\mathcal C$.


::: pf-proof

If $w_1=0$, then $\zeta=0$. In that case
$$
w_2
=
\frac{1+it}{1-it}.
$$
For finite $t$, this cannot equal $-1$, since
$$
1+it
=
-(1-it)
$$
would imply $1=-1$.

:::

:::

::: {.pf-step #s1-12}

The map $\mathcal C$ is a diffeomorphism
$$
\boxed{
\CC\times\RR
\xrightarrow{\sim}
S^3-\{(0,-1)\}}.
$$


::: pf-proof

For a point
$$
(w_1,w_2)\in S^3
$$
with $w_2\ne-1$, the defining formulas give
$$
1+w_2
=
\frac{2}{D}.
$$
Hence
$$
\boxed{
\zeta
=
\frac{w_1}{1+w_2}}.
$$
Then
$$
D
=
\frac{2}{1+w_2},
$$
and since
$$
D=1+|\zeta|^2-it,
$$
one recovers
$$
\boxed{
t
=
-\operatorname{Im}
\left(
\frac{2}{1+w_2}
\right)}.
$$
These formulas define a smooth inverse on
$$
S^3-\{(0,-1)\}.
$$

:::

:::

::: {.pf-step #s1-13}

On $\CC\times\RR$, define the Heisenberg contact form
$$
\boxed{
\beta
=
dt+2\,\operatorname{Im}(\overline\zeta\,d\zeta)}.
$$


::: pf-proof

This is the standard contact form in complex notation.

:::

:::

::: {.pf-step #s1-14}

Writing $\zeta=u+iv$,
$$
\boxed{
\beta
=
dt+2(u\,dv-v\,du)}.
$$


::: pf-proof

Compute
$$
\overline\zeta\,d\zeta
=
(u-iv)(du+i\,dv)
=
u\,du+v\,dv
+
i(u\,dv-v\,du).
$$
Take the imaginary part.

:::

:::

::: {.pf-step #s1-15}

A direct differentiation of the Cayley transform gives
$$
\boxed{
\mathcal C^*(\alpha|_{S^3})
=
\frac{
2
}{
(1+|\zeta|^2)^2+t^2
}
\,\beta}.
$$


::: pf-proof

Substitute the two component functions from step [](#s1-9){.pf-ref} into
$$
\alpha
=
\operatorname{Im}
\left(
\overline w_1\,dw_1
+
\overline w_2\,dw_2
\right),
$$
which is equivalent to the real-coordinate expression in step [](#s1-1){.pf-ref}.
Differentiating
$$
w_1=\frac{2\zeta}{D},
\qquad
w_2=\frac{1-|\zeta|^2+it}{D},
$$
collecting the terms in $dt$ and
$\operatorname{Im}(\overline\zeta\,d\zeta)$, and using
$$
|D|^2
=
(1+|\zeta|^2)^2+t^2
$$
yields the displayed formula.

:::

:::

::: {.pf-step #s1-16}

The scalar factor in step [](#s1-15){.pf-ref} is everywhere positive.


::: pf-proof

Its denominator is a sum of squares and its numerator is $2>0$.

:::

:::

::: {.pf-step #s1-17}

Hence $\mathcal C$ is a contactomorphism from
$$
(\CC\times\RR,\ker\beta)
$$
to
$$
(S^3-\{(0,-1)\},\ker\alpha).
$$


::: pf-proof

By steps [](#s1-15){.pf-ref} through [](#s1-16){.pf-ref},
$$
\mathcal C^*\alpha
=
g\beta
$$
for a positive function $g$. Multiplication by a nowhere-zero function
does not change the kernel, so
$$
d\mathcal C(\ker\beta)
=
\ker\alpha.
$$
Step [](#s1-12){.pf-ref} gives the diffeomorphism.

:::

:::

::: {.pf-step #s1-18}

Under $\Phi$,
$$
2\,\operatorname{Im}(\overline\zeta\,d\zeta)
=
\frac12(x\,dy-y\,dx).
$$


::: pf-proof

Since
$$
\zeta=\frac{x+iy}{2},
$$
one has
$$
d\zeta=\frac{dx+i\,dy}{2}.
$$
Thus
$$
\operatorname{Im}(\overline\zeta\,d\zeta)
=
\frac14(x\,dy-y\,dx).
$$
Multiply by $2$.

:::

:::

::: {.pf-step #s1-19}

Also
$$
dt
=
dz+\frac12(x\,dy+y\,dx).
$$


::: pf-proof

Differentiate
$$
t=z+\frac{xy}{2}.
$$

:::

:::

::: {.pf-step #s1-20}

Therefore
$$
\boxed{
\Phi^*\beta
=
dz+x\,dy}.
$$


::: pf-proof

Using steps [](#s1-18){.pf-ref} through [](#s1-19){.pf-ref},
$$
\begin{aligned}
\Phi^*\beta
&=
dt
+
2\operatorname{Im}(\overline\zeta\,d\zeta)\\
&=
dz+\frac12(x\,dy+y\,dx)
+
\frac12(x\,dy-y\,dx)\\
&=
dz+x\,dy.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-21}

The composite
$$
\boxed{
\Psi
=
\mathcal C\circ\Phi:
\RR^3
\longrightarrow
S^3-\{(0,-1)\}}
$$
is a contactomorphism from
$$
(\RR^3,\ker(dz+x\,dy))
$$
onto the punctured standard contact sphere.


::: pf-proof

The map $\Phi$ is a diffeomorphism from $\RR^3$ to
$\CC\times\RR$. By step [](#s1-20){.pf-ref}, it is a strict
contactomorphism from
$$
dz+x\,dy
$$
to $\beta$. Step [](#s1-17){.pf-ref} says $\mathcal C$ is a contactomorphism from
$\ker\beta$ to the punctured sphere. Their composite is therefore a
contactomorphism.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-8){.pf-ref} verify the positive contact form on $S^3$, and steps
[](#s1-9){.pf-ref} through [](#s1-21){.pf-ref} give the explicit contactomorphism with standard
$\RR^3$ after deleting one point.

:::

:::

:::
