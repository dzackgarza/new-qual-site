---
schema: qual/card@1
id: E-SS1.EX-25
kind: exercise
title: "The next three calculations provide some insight into Cauchy’s theorem, which we"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: exercise
25. The next three calculations provide some insight into Cauchy’s theorem, which we treat in the next chapter.

(a) Evaluate the integrals

$$
\int_ {\gamma} z ^ {n} d z
$$

for all integers $n .$ . Here $\gamma$ is any circle centered at the origin with the positive (counterclockwise) orientation.

(b) Same question as before, but with $\gamma$ any circle not containing the origin.
:::

::: {.solution}
**(a).**

<1>1. Parametrize $\gamma$ by $z = R e^{i\theta}$, $0 \le \theta \le 2\pi$, so $dz = i R e^{i\theta}\,d\theta$.
Proof: parametrization of a circle of radius $R$ centered at the origin.

<1>2. $\int_\gamma z^n\,dz = \int_0^{2\pi} (R e^{i\theta})^n \cdot i R e^{i\theta}\,d\theta = i R^{n+1} \int_0^{2\pi} e^{i(n+1)\theta}\,d\theta$.
Proof: <1>1.

<1>3. If $n \neq -1$, then $\int_0^{2\pi} e^{i(n+1)\theta}\,d\theta = \left[\frac{e^{i(n+1)\theta}}{i(n+1)}\right]_0^{2\pi} = 0$.
Proof: the antiderivative is periodic.

<1>4. If $n = -1$, then $\int_0^{2\pi} e^{i(n+1)\theta}\,d\theta = \int_0^{2\pi} 1\,d\theta = 2\pi$, so $\int_\gamma z^{-1}\,dz = i R^0 \cdot 2\pi = 2\pi i$.
Proof: <1>2 with $n = -1$.

<1>5. Hence $\int_\gamma z^n\,dz = 0$ for $n \neq -1$ and $= 2\pi i$ for $n = -1$.
Proof: <1>3 and <1>4.

**(b).**

<1>1. If $\gamma$ is a circle not containing the origin, then $z^n$ is holomorphic on a simply connected region containing $\gamma$ (for $n \ge 0$), or on the region inside $\gamma$ (for $n < 0$, since $0$ is outside $\gamma$).
Proof: the origin is not enclosed by $\gamma$.

<1>2. Hence $\int_\gamma z^n\,dz = 0$ for all integers $n$.
Proof: <1>1 and Cauchy's theorem (the integrand is holomorphic on and inside $\gamma$).

<1>3. Q.E.D.
Proof: <1>5 (a) and <1>2 (b).
:::
