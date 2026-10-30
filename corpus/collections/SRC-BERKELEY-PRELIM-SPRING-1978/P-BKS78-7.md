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
$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1.
$$
:::

::: {.solution}
Let
$$
E\coloneqq
\left\{
(x,y,z)\in\RR^3:
\frac{x^2}{a^2}
+\frac{y^2}{b^2}
+\frac{z^2}{c^2}
\leq1
\right\}.
$$

::: pf

::: {.pf-step #linear-change}
The linear change of variables
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

::: pf-proof
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

:::

::: {.pf-step #jacobian}
The absolute value of the Jacobian determinant of the transformation in [](#linear-change){.pf-ref} is
$$
\abs{abc}.
$$

::: pf-proof
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

:::

::: {.pf-step #unit-ball-volume}
The volume of the unit ball is
$$
\operatorname{Vol}(B)=\frac{4\pi}{3}.
$$

::: pf-proof
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

:::

::: pf-step
Therefore the enclosed volume is
$$
\boxed{
\operatorname{Vol}(E)
=
\frac{4\pi}{3}\abs{abc}
}.
$$
In the usual convention $a,b,c>0$, this is
$$
\boxed{\frac{4\pi abc}{3}}.
$$

::: pf-proof
By the change-of-variables formula, [](#linear-change){.pf-ref}, [](#jacobian){.pf-ref}, and [](#unit-ball-volume){.pf-ref},
$$
\operatorname{Vol}(E)
=
\abs{abc}\operatorname{Vol}(B)
=
\abs{abc}\frac{4\pi}{3}.
$$
:::

:::

:::

:::
