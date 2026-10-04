---
schema: qual/card@1
id: P-TRIV-RA36
kind: problem
title: Surface areas of the sphere and the torus
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 36, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the surface area of

(a) the two-dimensional sphere $S ^ { 2 }$ of radius R.

(b) the two-dimensional torus $T ^ { 2 }$ formed by rotation of the center of a circle of radius $R _ { 1 }$ along a circle of radius $R _ { 2 } , R _ { 2 } > R _ { 1 }$
:::

::: {.solution}
<1>1. Parametrize the sphere of radius $R$ by
$$
X(\theta,\varphi)
=
\bigl(
R\sin\theta\cos\varphi,
R\sin\theta\sin\varphi,
R\cos\theta
\bigr),
$$
with
$$
0\leq\theta\leq\pi,
\qquad
0\leq\varphi<2\pi.
$$

::: {.proof}
This is the standard spherical parametrization.
:::

<1>2. The surface-area element is
$$
\|X_\theta\times X_\varphi\|
\,d\theta\,d\varphi
=
R^2\sin\theta
\,d\theta\,d\varphi.
$$

::: {.proof}
The tangent vectors are
$$
X_\theta
=
\bigl(
R\cos\theta\cos\varphi,
R\cos\theta\sin\varphi,
-R\sin\theta
\bigr)
$$
and
$$
X_\varphi
=
\bigl(
-R\sin\theta\sin\varphi,
R\sin\theta\cos\varphi,
0
\bigr).
$$
Their cross product has norm $R^2\sin\theta$.
:::

<1>3. Hence
$$
\operatorname{Area}(S_R^2)
=
\int_0^{2\pi}\int_0^\pi
R^2\sin\theta
\,d\theta\,d\varphi
=
\boxed{4\pi R^2}.
$$

::: {.proof}
Evaluate
$$
\int_0^\pi\sin\theta\,d\theta=2
$$
and
$$
\int_0^{2\pi}d\varphi=2\pi.
$$
:::

<1>4. Part (a) follows.

::: {.proof}
This is step <1>3.
:::

<1>5. Parametrize the torus by
$$
Y(\theta,\varphi)
=
\bigl(
(R_2+R_1\cos\theta)\cos\varphi,
(R_2+R_1\cos\theta)\sin\varphi,
R_1\sin\theta
\bigr),
$$
with
$$
0\leq\theta,\varphi<2\pi.
$$

::: {.proof}
For fixed $\varphi$, the variable $\theta$ runs around the generating circle
of radius $R_1$. The variable $\varphi$ rotates its center around the circle of
radius $R_2$.
:::

<1>6. The tangent vectors are
$$
Y_\theta
=
\bigl(
-R_1\sin\theta\cos\varphi,
-R_1\sin\theta\sin\varphi,
R_1\cos\theta
\bigr)
$$
and
$$
Y_\varphi
=
\bigl(
-(R_2+R_1\cos\theta)\sin\varphi,
(R_2+R_1\cos\theta)\cos\varphi,
0
\bigr).
$$

::: {.proof}
Differentiate the parametrization from step <1>5.
:::

<1>7. Their cross product has norm
$$
\|Y_\theta\times Y_\varphi\|
=
R_1(R_2+R_1\cos\theta).
$$

::: {.proof}
The two tangent vectors are orthogonal. Their norms are
$$
\|Y_\theta\|=R_1
$$
and
$$
\|Y_\varphi\|
=
R_2+R_1\cos\theta.
$$
The latter is positive because $R_2>R_1$. Hence the norm of the cross product
is the product of these norms.
:::

<1>8. Therefore
$$
\begin{aligned}
\operatorname{Area}(T^2)
&=
\int_0^{2\pi}\int_0^{2\pi}
R_1(R_2+R_1\cos\theta)
\,d\theta\,d\varphi\\
&=
\boxed{4\pi^2R_1R_2}.
\end{aligned}
$$

::: {.proof}
The cosine term integrates to zero over a full period, so
$$
\int_0^{2\pi}
R_1(R_2+R_1\cos\theta)
\,d\theta
=
2\pi R_1R_2.
$$
Multiplying by the $2\pi$ from the $\varphi$-integration gives the result.
:::

<1>9. Part (b) follows.

::: {.proof}
This is step <1>8.
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>4 and <1>9 establish parts (a) and (b), respectively.
:::
:::
