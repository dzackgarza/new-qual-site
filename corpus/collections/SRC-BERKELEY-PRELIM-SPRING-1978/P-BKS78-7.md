---
schema: qual/card@1
id: P-BKS78-7
kind: problem
title: Volume enclosed by an ellipsoid
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Find the volume enclosed by
\[
\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1.
\]
:::

::: {.solution}
Let
$$
E\coloneqq
\left\{
(x,y,z)\in\mathbb R^3:
\frac{x^2}{a^2}
+\frac{y^2}{b^2}
+\frac{z^2}{c^2}
\leq1
\right\}.
$$

<1>1. The linear change of variables
$$
x=au,
\qquad
y=bv,
\qquad
z=cw
$$
maps the unit ball
$$
B\coloneqq
\{(u,v,w):u^2+v^2+w^2\leq1\}
$$
onto $E$.

::: {.proof}
Substitution gives
$$
\frac{x^2}{a^2}
+\frac{y^2}{b^2}
+\frac{z^2}{c^2}
=
u^2+v^2+w^2.
$$
Thus the defining inequality for $E$ becomes precisely the defining inequality for $B$.
:::

<1>2. The absolute value of the Jacobian determinant of the transformation in step <1>1 is
$$
|abc|.
$$

::: {.proof}
The derivative matrix is diagonal:
$$
\begin{pmatrix}
a&0&0\\
0&b&0\\
0&0&c
\end{pmatrix},
$$
whose determinant is $abc$. Volume uses its absolute value.
:::

<1>3. The volume of the unit ball is
$$
\operatorname{Vol}(B)=\frac{4\pi}{3}.
$$

::: {.proof}
Using spherical coordinates,
$$
\begin{aligned}
\operatorname{Vol}(B)
&=
\int_0^1
\int_0^\pi
\int_0^{2\pi}
r^2\sin\phi
\,d\theta\,d\phi\,dr\\
&=
\left(\int_0^1r^2\,dr\right)
\left(\int_0^\pi\sin\phi\,d\phi\right)
\left(\int_0^{2\pi}d\theta\right)\\
&=
\frac13\cdot2\cdot2\pi
=
\frac{4\pi}{3}.
\end{aligned}
$$
:::

<1>4. Therefore the enclosed volume is
$$
\boxed{
\operatorname{Vol}(E)
=
\frac{4\pi}{3}|abc|
}.
$$
In the usual convention $a,b,c>0$, this is
$$
\boxed{\frac{4\pi abc}{3}}.
$$

::: {.proof}
By the change-of-variables formula and steps <1>1--<1>3,
$$
\operatorname{Vol}(E)
=
|abc|\operatorname{Vol}(B)
=
|abc|\frac{4\pi}{3}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested volume.
:::
:::
