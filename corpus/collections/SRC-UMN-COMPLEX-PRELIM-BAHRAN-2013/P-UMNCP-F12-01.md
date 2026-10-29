---
schema: qual/card@1
id: P-UMNCP-F12-01
kind: problem
title: Möbius transformations map lines and circles to lines and circles
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Fall 2012, 1 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Show that a Möbius transformation maps a straight line or circle onto a straight line or circle.
:::

::: {.solution}

Let
$$
T(z)=\frac{az+b}{cz+d},
\qquad
ad-bc\ne0.
$$
Work on the Riemann sphere, so a straight line is regarded as a circle through $\infty$.

::: pf

::: {.pf-step #s1-1}

Every straight line or circle in $\CC$ is the zero set of an equation
$$
\boxed{
A|z|^2+Bz+\overline B\,\overline z+C=0}
$$
with
$$
A,C\in\RR,
\qquad
B\in\CC,
$$
not all coefficients zero.


::: pf-proof

A circle with center $z_0$ and radius $r>0$ has equation
$$
|z-z_0|^2=r^2.
$$
Expanding gives
$$
|z|^2
-\overline{z_0}z
-z_0\overline z
+|z_0|^2-r^2
=0,
$$
which has the stated form with $A=1$.

A straight line can be written as
$$
\operatorname{Re}(\beta z)=\lambda
$$
for some
$$
0\ne\beta\in\CC,
\qquad
\lambda\in\RR.
$$
Equivalently,
$$
\beta z+\overline\beta\,\overline z-2\lambda=0,
$$
which is the same form with $A=0$.

:::

:::

::: {.pf-step #s1-2}

Conversely, a nonempty zero set of an equation from step [](#s1-1){.pf-ref} is either a straight line or a circle.


::: pf-proof

If $A=0$, then
$$
Bz+\overline B\,\overline z+C=0.
$$
For a nonempty proper zero set one has $B\ne0$, and this is a real affine-linear equation, hence a line.

If $A\ne0$, divide by $A$ and complete the square:
$$
|z|^2
+\frac BA z
+\frac{\overline B}{A}\overline z
+\frac CA
=0.
$$
Thus
$$
\left|
z+\frac{\overline B}{A}
\right|^2
=
\frac{|B|^2}{A^2}
-\frac CA.
$$
Whenever the zero set is nonempty and not a single degenerate point, this is a circle.

:::

:::

::: {.pf-step #s1-3}

If $w=T(z)$, then
$$
z=T^{-1}(w)
=
\frac{dw-b}{-cw+a}.
$$


::: pf-proof

Starting from
$$
w(cz+d)=az+b,
$$
one obtains
$$
(cw-a)z=b-dw.
$$
Since
$$
ad-bc\ne0,
$$
the inverse Möbius transformation exists and is given by the displayed formula.

:::

:::

::: {.pf-step #s1-4}

Substituting $z=T^{-1}(w)$ into a generalized-circle equation and multiplying by
$$
|-cw+a|^2
$$
produces another equation of the form
$$
A'|w|^2+B'w+\overline{B'}\,\overline w+C'=0
$$
with
$$
A',C'\in\RR.
$$


::: pf-proof

Start from
$$
A|z|^2+Bz+\overline B\,\overline z+C=0.
$$
By step [](#s1-3){.pf-ref},
$$
z=\frac{dw-b}{-cw+a},
\qquad
\overline z
=
\frac{\overline d\,\overline w-\overline b}
{-\overline c\,\overline w+\overline a}.
$$
Multiplying by
$$
|-cw+a|^2
=
(-cw+a)(-\overline c\,\overline w+\overline a)
$$
gives
$$
\begin{aligned}
0
&=
A|dw-b|^2\\
&\quad
+B(dw-b)(-\overline c\,\overline w+\overline a)\\
&\quad
+\overline B(\overline d\,\overline w-\overline b)(-cw+a)\\
&\quad
+C|-cw+a|^2.
\end{aligned}
$$
This expression is real-valued and contains only the monomials
$$
|w|^2,
\quad
w,
\quad
\overline w,
\quad
1.
$$
Hence it has the stated form, with the coefficients of $w$ and $\overline w$ conjugate and the coefficients of $|w|^2$ and $1$ real.

:::

:::

::: {.pf-step #s1-5}

Therefore every Möbius transformation maps every straight line or circle onto a straight line or circle.


::: pf-proof

Let $C$ be the original line or circle. By step [](#s1-1){.pf-ref} it is described by a generalized-circle equation. Step [](#s1-4){.pf-ref} shows that
$$
T(C)
$$
is described by another equation of the same form. Since $T$ is bijective on the Riemann sphere, the image is nonempty and nondegenerate. By step [](#s1-2){.pf-ref} it is a straight line or circle.

:::

:::

:::

:::

::: {.remark title="Alternative proof"}
For $c\ne0$,
$$
T(z)=\frac ac+\frac{bc-ad}{c^2}\cdot\frac1{z+d/c},
$$
so every Möbius transformation is a composition of translations, nonzero complex dilations and the inversion $z\mapsto1/z$. Translations and dilations preserve lines and circles. For the inversion, substituting $z=1/w$ into $A|z|^2+Bz+\overline B\,\overline z+C=0$ and multiplying by $|w|^2$ gives $C|w|^2+\overline B w+B\overline w+A=0$, an equation of the same form with $|B|^2-AC$ unchanged.
:::
