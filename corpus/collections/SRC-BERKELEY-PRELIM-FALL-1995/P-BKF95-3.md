---
schema: qual/card@1
id: P-BKF95-3
kind: problem
title: Radius of a Taylor series for a rational function
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/Fall95_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Factored the denominator through z^12-1; its zeros are the twelfth roots
    of unity other than plus/minus 1, and the nearest poles to z=1 are
    e^{plus/minus i pi/6}.
---

::: {.problem}
Find the radius of convergence of the Taylor series about $z=1$ of
\[
f(z)=\frac1{1+z^2+z^4+z^6+z^8+z^{10}}.
\]
Express the answer using only real numbers and square roots.
:::

::: {.solution}
Let
$$
Q(z)\coloneqq
1+z^2+z^4+z^6+z^8+z^{10}.
$$

<1>1. One has
$$
(z^2-1)Q(z)=z^{12}-1.
$$

::: {.proof}
This is the finite geometric-series identity
$$
(w-1)(1+w+w^2+w^3+w^4+w^5)=w^6-1
$$
with $w=z^2$.
:::

<1>2. The zeros of $Q$ are exactly the twelfth roots of unity other than
$1$ and $-1$.

::: {.proof}
If $Q(z)=0$, step <1>1 gives
$$
z^{12}=1.
$$
Moreover,
$$
Q(1)=Q(-1)=6,
$$
so neither $1$ nor $-1$ is a zero.

Conversely, if
$$
z^{12}=1
\qquad\text{and}\qquad
z\neq\pm1,
$$
then $z^2-1\neq0$, and step <1>1 gives
$$
Q(z)=0.
$$
:::

<1>3. The poles of
$$
f(z)=\frac1{Q(z)}
$$
nearest to $z=1$ are
$$
e^{i\pi/6}
\qquad\text{and}\qquad
e^{-i\pi/6}.
$$

::: {.proof}
By step <1>2, the poles are
$$
e^{ik\pi/6},
\qquad
k=1,\ldots,5,7,\ldots,11.
$$
For any real $\theta$,
$$
\abs{1-e^{i\theta}}^2
=
2-2\cos\theta.
$$
Among the allowed nonzero angles modulo $2\pi$, the smallest absolute angle
from $0$ is $\pi/6$, attained exactly at $\theta=\pm\pi/6$. Since
$2-2\cos\theta$ increases with $\abs{\theta}$ on $[0,\pi]$, these are the
nearest poles to $1$.
:::

<1>4. Their distance from $1$ is
$$
\sqrt{2-\sqrt3}.
$$

::: {.proof}
Using
$$
\cos\frac{\pi}{6}=\frac{\sqrt3}{2},
$$
step <1>3 gives
$$
\begin{aligned}
\abs{1-e^{i\pi/6}}^2
&=
2-2\cos\frac{\pi}{6}\\
&=
2-\sqrt3.
\end{aligned}
$$
Taking the positive square root gives the stated distance.
:::

<1>5. The radius of convergence of the Taylor series of $f$ about $z=1$
is
$$
\boxed{\sqrt{2-\sqrt3}}.
$$

::: {.proof}
A Taylor series of a rational function about a point where it is analytic
has radius equal to the distance from the center to the nearest pole. Step
<1>4 computes that distance.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested radius in terms of real numbers and square
roots only.
:::
:::
