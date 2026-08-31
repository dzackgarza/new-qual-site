---
schema: qual/card@1
id: P-I3UPP
kind: problem
title: The line integral $\int_\tau x\,dy+y\,dx$ along the unit-circle arc from $(1,0)$
  to $(3/5,4/5)$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $\tau$ be the arc of the unit circle in the first quadrant, from $(1,0)$ to $(3/5, 4/5)$.
Compute $$\int_\tau x\,dy + y\,dx.$$
:::

::: {.solution}
<1>1. Exact differential formulation:
<2>1. Consider the differential 1-form $\omega = y\,dx + x\,dy$.
By the product rule for differentials:
\[
\omega = d(xy).
\]
<2>2. Thus $\omega$ is an exact 1-form on $\mathbb{R}^2$ with potential function $f(x, y) = xy$.

<1>2. Application of the Fundamental Theorem of Line Integrals:
<2>1. Let $\tau$ be any piecewise smooth path starting at $A = (1, 0)$ and ending at $B = (3/5, 4/5)$.
By the Fundamental Theorem for Line Integrals:
\[
\int_\tau (x\,dy + y\,dx) = \int_\tau d(xy) = f(B) - f(A).
\]
<2>2. Evaluate the potential function at the endpoints:
- $f(A) = f(1, 0) = 1 \cdot 0 = 0$,
- $f(B) = f\left(\frac{3}{5}, \frac{4}{5}\right) = \frac{3}{5} \cdot \frac{4}{5} = \frac{12}{25}$.
<2>3. Therefore:
\[
\int_\tau (x\,dy + y\,dx) = \frac{12}{25} - 0 = \frac{12}{25}.
\]

<1>3. Alternative verification via trigonometric parametrization:
<2>1. Parametrize the arc $\tau$ by $x(t) = \cos t, y(t) = \sin t$ for $t \in [0, t_0]$, where $\cos t_0 = 3/5$ and $\sin t_0 = 4/5$.
Then $dx = -\sin t\,dt$ and $dy = \cos t\,dt$.
<2>2. The integrand becomes:
\[
x\,dy + y\,dx = (\cos^2 t - \sin^2 t)\,dt = \cos(2t)\,dt.
\]
<2>3. Integrating:
\[
\int_0^{t_0} \cos(2t)\,dt = \left[ \frac{\sin(2t)}{2} \right]_0^{t_0} = \sin(t_0)\cos(t_0) = \frac{4}{5} \cdot \frac{3}{5} = \frac{12}{25}.
\]

<1>4. Conclusion:
$\int_\tau x\,dy + y\,dx = \frac{12}{25}$. Q.E.D.
:::
