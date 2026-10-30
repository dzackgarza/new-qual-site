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

::: pf

::: pf-step

Parametrize the sphere of radius $R$ by
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


::: pf-proof

This is the standard spherical parametrization.

:::

:::

::: pf-step

The surface-area element is
$$
\norm{X_\theta\times X_\varphi}
\,d\theta\,d\varphi
=
R^2\sin\theta
\,d\theta\,d\varphi.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-3}

Hence
$$
\operatorname{Area}(S_R^2)
=
\int_0^{2\pi}\int_0^\pi
R^2\sin\theta
\,d\theta\,d\varphi
=
\boxed{4\pi R^2}.
$$


::: pf-proof

Evaluate
$$
\int_0^\pi\sin\theta\,d\theta=2
$$
and
$$
\int_0^{2\pi}d\varphi=2\pi.
$$

:::

:::

::: {.pf-step #s1-4}

Part (a) follows.


::: pf-proof

This is step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Parametrize the torus by
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


::: pf-proof

For fixed $\varphi$, the variable $\theta$ runs around the generating circle
of radius $R_1$. The variable $\varphi$ rotates its center around the circle of
radius $R_2$.

:::

:::

::: pf-step

The tangent vectors are
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


::: pf-proof

Differentiate the parametrization from step [](#s1-5){.pf-ref}.

:::

:::

::: pf-step

Their cross product has norm
$$
\norm{Y_\theta\times Y_\varphi}
=
R_1(R_2+R_1\cos\theta).
$$


::: pf-proof

The two tangent vectors are orthogonal. Their norms are
$$
\norm{Y_\theta}=R_1
$$
and
$$
\norm{Y_\varphi}
=
R_2+R_1\cos\theta.
$$
The latter is positive because $R_2>R_1$. Hence the norm of the cross product
is the product of these norms.

:::

:::

::: {.pf-step #s1-8}

Therefore
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


::: pf-proof

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

:::

::: {.pf-step #s1-9}

Part (b) follows.


::: pf-proof

This is step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-9){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
