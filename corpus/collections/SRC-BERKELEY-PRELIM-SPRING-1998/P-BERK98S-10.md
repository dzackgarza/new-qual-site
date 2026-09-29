---
schema: qual/card@1
id: P-BERK98S-10
kind: problem
title: Maximum-area triangle inscribed in an ellipse
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let
\[
P_i=(a\cos\theta_i,b\sin\theta_i),\qquad i=1,2,3,
\]
be three points on the ellipse
\[
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1.
\]
Find the maximal possible area of the triangle $\triangle P_1P_2P_3$, and determine all triangles for which this maximum is attained.
:::

::: {.solution}
Let
$$
Q_i=(\cos\theta_i,\sin\theta_i),
\qquad
L=
\begin{pmatrix}
a&0\\
0&b
\end{pmatrix}.
$$
Then $P_i=LQ_i$.

::: pf

::: {.pf-step #s1}

The area of $\triangle P_1P_2P_3$ is $\abs{ab}$ times the area of
$\triangle Q_1Q_2Q_3$.

::: pf-proof

Using the determinant formula for the area of a triangle,
$$
\begin{aligned}
2\operatorname{Area}(P_1P_2P_3)
&=
\abs{\det(P_2-P_1,P_3-P_1)}\\
&=
\abs{\det L}\,
\abs{\det(Q_2-Q_1,Q_3-Q_1)}\\
&=
2\abs{ab}\operatorname{Area}(Q_1Q_2Q_3).
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

If a nondegenerate triangle is inscribed in the unit circle and its
interior angles are $A,B,C$, then its area is
$$
2\sin A\sin B\sin C.
$$

::: pf-proof

The circumradius is $1$. By the extended law of sines, the side lengths
opposite $A,B,C$ are respectively
$$
2\sin A,
\qquad
2\sin B,
\qquad
2\sin C.
$$
Using the two sides adjacent to angle $C$ gives
$$
\operatorname{Area}
=
\frac12(2\sin A)(2\sin B)\sin C
=
2\sin A\sin B\sin C.
$$

:::

:::

::: {.pf-step #s3}

Every triangle inscribed in the unit circle has area at most
$$
\frac{3\sqrt3}{4},
$$
with equality exactly for equilateral triangles.

::: pf-proof

Degenerate triangles have area zero, so suppose the triangle is
nondegenerate. Then $A,B,C\in(0,\pi)$ and
$$
A+B+C=\pi.
$$
Since $\sin$ is strictly concave on $(0,\pi)$, Jensen's inequality gives
$$
\frac{\sin A+\sin B+\sin C}{3}
\leq
\sin\frac{A+B+C}{3}
=
\frac{\sqrt3}{2},
$$
with equality exactly when
$$
A=B=C=\frac\pi3.
$$
The arithmetic--geometric mean inequality then gives
$$
(\sin A\sin B\sin C)^{1/3}
\leq
\frac{\sin A+\sin B+\sin C}{3}
\leq
\frac{\sqrt3}{2}.
$$
Combining this with step [](#s2){.pf-ref},
$$
\operatorname{Area}
\leq
2\left(\frac{\sqrt3}{2}\right)^3
=
\frac{3\sqrt3}{4}.
$$
Equality in the area bound forces equality in Jensen's inequality, hence
$A=B=C=\pi/3$; conversely an equilateral triangle attains the bound.

:::

:::

::: {.pf-step #s4}

The maximal area on the ellipse is
$$
\boxed{\frac{3\sqrt3}{4}\abs{ab}}.
$$

::: pf-proof

By step [](#s1){.pf-ref}, every area on the ellipse is $\abs{ab}$ times the
corresponding area on the unit circle. Step [](#s3){.pf-ref} gives the maximum.
For the usual convention $a,b>0$ for the semiaxes, this is
$3\sqrt3\,ab/4$.

:::

:::

::: {.pf-step #s5}

Equality holds exactly for the triangles whose parameters, up to
permutation, are
$$
\boxed{
\theta_0,
\qquad
\theta_0+\frac{2\pi}{3},
\qquad
\theta_0+\frac{4\pi}{3}
\pmod{2\pi}
}
$$
for some $\theta_0\in\RR$.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s3){.pf-ref}, equality holds exactly when the three points
$Q_i$ form an equilateral triangle on the unit circle. The vertices of
such a triangle are exactly three points separated successively by central
angles $2\pi/3$. Applying $L$ gives precisely the displayed family of
maximal-area triangles on the ellipse.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give the maximal area and characterize every equality
case.

:::

:::

:::
