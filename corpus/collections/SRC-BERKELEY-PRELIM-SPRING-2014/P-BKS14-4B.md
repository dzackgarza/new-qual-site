---
schema: qual/card@1
id: P-BKS14-4B
kind: problem
title: Area formula for an injective holomorphic map
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the holomorphic Jacobian formula, change of variables for an injective holomorphic map, injectivity of z+z^2/2, and the polar-coordinate area integral.
---

::: {.problem}
Let \(f\) be an injective holomorphic function on the open unit disk \(U\subset\mathbb C\). Show that the area of \(f(U)\) is
\[
\int_U |f'(z)|^2\,dx\,dy.
\]
Compute the area of the image of \(U\) under
\[
f(z)=z+\frac{z^2}{2}.
\]
:::

::: {.solution}
Write
$$
f(z)=u(x,y)+iv(x,y),
\qquad
z=x+iy.
$$

<1>1. The real Jacobian determinant of $f$ is
$$
J_f(x,y)
=
\abs{f'(z)}^2.
$$

::: {.proof}
The real derivative matrix is
$$
Df
=
\begin{pmatrix}
u_x&u_y\\
v_x&v_y
\end{pmatrix}.
$$
The Cauchy--Riemann equations give
$$
v_y=u_x,
\qquad
v_x=-u_y.
$$
Therefore
$$
\begin{aligned}
J_f
&=
u_xv_y-u_yv_x\\
&=
u_x^2+u_y^2\\
&=
\abs{f'(z)}^2.
\end{aligned}
$$
:::

<1>2. An injective holomorphic function on a domain has
$$
f'(z)\neq0
$$
at every point.

::: {.proof}
This is the standard local mapping theorem for holomorphic functions:
if the first nonzero term of the Taylor expansion of
$$
f(z)-f(z_0)
$$
at $z_0$ has degree $m\geq2$, then $f$ is locally $m$-to-$1$ near
$z_0$. Local injectivity therefore forces $m=1$, equivalently
$f'(z_0)\neq0$.
:::

<1>3. The injective holomorphic map
$$
f:U\longrightarrow f(U)
$$
is a $C^1$ diffeomorphism.

::: {.proof}
By step <1>2, the real Jacobian determinant in step <1>1 is positive
everywhere. The inverse function theorem therefore gives a $C^1$ local
inverse near every point.

Because $f$ is globally injective, these local inverses agree on overlaps
and assemble to the inverse map on $f(U)$. Thus $f$ is a $C^1$
diffeomorphism onto its image.
:::

<1>4. The area of the image satisfies
$$
\boxed{
\operatorname{Area}(f(U))
=
\int_U\abs{f'(z)}^2\,dx\,dy
}.
$$

::: {.proof}
Apply the change-of-variables theorem to the diffeomorphism in step
<1>3:
$$
\operatorname{Area}(f(U))
=
\int_U\abs{J_f(x,y)}\,dx\,dy.
$$
Step <1>1 gives
$$
J_f=\abs{f'}^2\geq0,
$$
which yields the displayed formula.
:::

<1>5. The function
$$
f(z)=z+\frac{z^2}{2}
$$
is injective on $U$.

::: {.proof}
Suppose
$$
f(z_1)=f(z_2).
$$
Then
$$
\begin{aligned}
0
&=
f(z_1)-f(z_2)\\
&=
(z_1-z_2)
\left(
1+\frac{z_1+z_2}{2}
\right).
\end{aligned}
$$
If $z_1\neq z_2$, then
$$
z_1+z_2=-2.
$$
But
$$
\abs{z_1+z_2}
\leq
\abs{z_1}+\abs{z_2}
<
2
$$
for $z_1,z_2\in U$, a contradiction. Hence $z_1=z_2$.
:::

<1>6. For this function,
$$
f'(z)=1+z.
$$

::: {.proof}
Differentiate the polynomial.
:::

<1>7. One has
$$
\int_U\abs{1+z}^2\,dx\,dy
=
\frac{3\pi}{2}.
$$

::: {.proof}
Use polar coordinates
$$
z=re^{i\theta},
\qquad
0\leq r<1,
\qquad
0\leq\theta<2\pi.
$$
Then
$$
\abs{1+z}^2
=
1+2r\cos\theta+r^2.
$$
Therefore
$$
\begin{aligned}
\int_U\abs{1+z}^2\,dx\,dy
&=
\int_0^1\int_0^{2\pi}
\left(
1+2r\cos\theta+r^2
\right)
r\,d\theta\,dr\\
&=
2\pi
\int_0^1(r+r^3)\,dr\\
&=
2\pi
\left(
\frac12+\frac14
\right)\\
&=
\frac{3\pi}{2}.
\end{aligned}
$$
:::

<1>8. Hence the image of the unit disk under
$$
f(z)=z+\frac{z^2}{2}
$$
has area
$$
\boxed{\frac{3\pi}{2}}.
$$

::: {.proof}
Combine steps <1>4, <1>5, <1>6, and <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>4 proves the general area formula, and step <1>8 computes the
requested example.
:::
:::
