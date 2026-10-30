---
schema: qual/card@1
id: P-UGAP11F-05
kind: problem
title: Compute a line integral around the upper half-disk directly and by Green's theorem
classification:
  areas: [prelim]
  topics:
  - Line Integrals
  - Green's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $C$ be the positively oriented boundary of the upper semicircle of radius $3$, including the diameter from $(-3,0)$ to $(3,0)$. Compute
$$
\oint_C (2x+y)\,dx+y\,dy
$$
both directly and by Green's theorem.
:::

::: {.solution}

Write
$$
P(x,y)=2x+y,
\qquad
Q(x,y)=y.
$$
Let $D$ be the upper half-disk of radius $3$, so $C=\partial D$ with positive orientation.

::: pf

::: {.pf-step #s1-1}

The contribution from the diameter is $0$.


::: pf-proof

Positive orientation traverses the diameter from
$$
(-3,0)
\quad\text{to}\quad
(3,0).
$$
Parametrize it by
$$
\gamma_1(t)=(t,0),
\qquad
-3\le t\le3.
$$
Then
$$
dx=dt,
\qquad
dy=0,
$$
so
$$
\int_{\gamma_1}P\,dx+Q\,dy
=
\int_{-3}^3 2t\,dt
=0.
$$

:::

:::

::: {.pf-step #s1-2}

The contribution from the semicircular arc is
$$
\boxed{-\frac{9\pi}{2}}.
$$


::: pf-proof

Parametrize the arc by
$$
\gamma_2(t)
=
(3\cos t,3\sin t),
\qquad
0\le t\le\pi.
$$
This runs from $(3,0)$ to $(-3,0)$ and completes the positive orientation.

Along the arc,
$$
dx=-3\sin t\,dt,
\qquad
dy=3\cos t\,dt,
$$
and
$$
P=6\cos t+3\sin t,
\qquad
Q=3\sin t.
$$
Hence
$$
\begin{aligned}
P\,dx+Q\,dy
&=
(6\cos t+3\sin t)(-3\sin t)\,dt
+(3\sin t)(3\cos t)\,dt\\
&=
(-9\sin t\cos t-9\sin^2t)\,dt.
\end{aligned}
$$
Therefore
$$
\begin{aligned}
\int_{\gamma_2}P\,dx+Q\,dy
&=
-9\int_0^\pi\sin t\cos t\,dt
-9\int_0^\pi\sin^2t\,dt\\
&=
0
-9\cdot\frac\pi2\\
&=
-\frac{9\pi}{2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Direct computation gives
$$
\boxed{
\oint_C(2x+y)\,dx+y\,dy
=
-\frac{9\pi}{2}}.
$$


::: pf-proof

Add the diameter contribution from step [](#s1-1){.pf-ref} and the arc contribution from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Green's theorem gives the same value.


::: pf-proof

Green's theorem states
$$
\oint_C P\,dx+Q\,dy
=
\iint_D
\left(
\frac{\partial Q}{\partial x}
-\frac{\partial P}{\partial y}
\right)
dA.
$$
Here
$$
\frac{\partial Q}{\partial x}=0,
\qquad
\frac{\partial P}{\partial y}=1,
$$
so the integrand is $-1$. Since the area of $D$ is
$$
\frac12\pi(3)^2
=
\frac{9\pi}{2},
$$
we obtain
$$
\oint_C P\,dx+Q\,dy
=
-\operatorname{Area}(D)
=
-\frac{9\pi}{2}.
$$

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} compute the integral both directly and via Green's theorem, with the same value.

:::

:::

:::
