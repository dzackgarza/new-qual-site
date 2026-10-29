---
schema: qual/card@1
id: P-UGAP13F-05
kind: problem
title: Path dependence of a plane integral and an inward-pointing gradient
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
(a) Let $C$ be a path from $(0,1)$ to $(1,2)$. Explain whether
\[
\int_C y e^x\,dx+x e^y\,dy
\]
depends on the choice of $C$.

(b) Give an example of a function defined on the plane whose gradient always points toward the origin.
:::

::: {.solution}

::: pf

::: pf-step

Consider first the path $C_1$ that goes horizontally from
\[
(0,1)
\]
to
\[
(1,1)
\]
and then vertically to
\[
(1,2).
\]
Along the horizontal segment,
\[
y=1,
\qquad
dy=0.
\]
Therefore
\[
\int_{C_{1,mathrm{hor}}}
y e^x\,dx+x e^y\,dy
=
\int_0^1 e^x\,dx
=
e-1.
\]


::: pf-proof

On this segment,
\[
y e^x\,dx
=
e^x\,dx
\]
and the second term vanishes.

:::

:::

::: pf-step

Along the vertical segment of $C_1$,
\[
x=1,
\qquad
dx=0.
\]
Hence
\[
\int_{C_{1,mathrm{vert}}}
y e^x\,dx+x e^y\,dy
=
\int_1^2 e^y\,dy
=
e^2-e.
\]


::: pf-proof

The first term vanishes because
\[
dx=0,
\]
and
\[
x e^y\,dy
=
e^y\,dy.
\]

:::

:::

::: {.pf-step #s1-3}

Thus
\[
\int_{C_1}
y e^x\,dx+x e^y\,dy
=
\boxed{
e^2-1
}.
\]


::: pf-proof

Add the two segment integrals:
\[
(e-1)+(e^2-e)
=
e^2-1.
\]

:::

:::

::: {.pf-step #s1-4}

Now let $C_2$ go vertically from
\[
(0,1)
\]
to
\[
(0,2)
\]
and then horizontally to
\[
(1,2).
\]
The vertical segment contributes
\[
0.
\]


::: pf-proof

Along this segment,
\[
x=0,
\qquad
dx=0.
\]
Hence both
\[
y e^x\,dx
\]
and
\[
x e^y\,dy
\]
vanish.

:::

:::

::: {.pf-step #s1-5}

Along the horizontal segment of $C_2$,
\[
y=2,
\qquad
dy=0,
\]
so
\[
\int_{C_{2,mathrm{hor}}}
y e^x\,dx+x e^y\,dy
=
\int_0^1
2e^x\,dx
=
2e-2.
\]


::: pf-proof

Only the first term survives and
\[
y=2.
\]

:::

:::

::: {.pf-step #s1-6}

Therefore
\[
\int_{C_2}
y e^x\,dx+x e^y\,dy
=
\boxed{
2e-2
}.
\]


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The two values are different:
\[
(e^2-1)-(2e-2)
=
(e-1)^2
>
0.
\]
Hence the integral depends on the path.


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-6){.pf-ref} give two paths with the same endpoints but different
line integrals.
Therefore the integral is not path-independent.

:::

:::

::: pf-step

This is consistent with the differential-form test.
If
\[
M(x,y)=y e^x,
\qquad
N(x,y)=x e^y,
\]
then
\[
M_y=e^x,
\qquad
N_x=e^y.
\]
These are not equal on all of
\[
\RR^2.
\]


::: pf-proof

On a simply connected domain such as
\[
\RR^2,
\]
a continuously differentiable $1$-form
\[
M\,dx+N\,dy
\]
is exact only if
\[
M_y=N_x.
\]
Here that equality fails in general, so the form is not conservative.

:::

:::

::: {.pf-step #s1-9}

For part (b), define
\[
\boxed{
F(x,y)
=
-(x^2+y^2).
}
\]
Then
\[
\nabla F(x,y)
=
(-2x,-2y)
=
-2(x,y).
\]


::: pf-proof

Differentiate:
\[
F_x=-2x,
\qquad
F_y=-2y.
\]
Thus the gradient is a negative scalar multiple of the position vector.

:::

:::

::: {.pf-step #s1-10}

For every
\[
(x,y)\ne(0,0),
\]
the vector
\[
\nabla F(x,y)
\]
points directly toward the origin.


::: pf-proof

The vector from
\[
(x,y)
\]
to the origin is
\[
-(x,y).
\]
Since
\[
\nabla F(x,y)
=
2\bigl(-(x,y)\bigr),
\]
the gradient has exactly that direction.
At the origin itself,
\[
\nabla F(0,0)=0.
\]

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} answers part (a), and steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref} answer part (b).

:::

:::

:::
