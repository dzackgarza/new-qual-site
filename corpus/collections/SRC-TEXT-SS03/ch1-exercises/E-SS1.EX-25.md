---
schema: qual/card@1
id: E-SS1.EX-25
kind: problem
title: $\int_\gamma z^n\,dz$ over circles around and away from the origin
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

::: {.exercise}
25. The next three calculations provide some insight into Cauchy’s theorem, which we treat in the next chapter.

(a) Evaluate the integrals

$$
\int_ {\gamma} z ^ {n} d z
$$

for all integers $n .$ . Here $\gamma$ is any circle centered at the origin with the positive (counterclockwise) orientation.

(b) Same question as before, but with $\gamma$ any circle not containing the origin.
:::

::: {.solution}
<1>1. (a) If $\gamma$ is the positively oriented circle of radius $R$ centered at $0$, then $\int_\gamma z^n\,dz = \boxed{0}$ for $n \neq -1$ and $\int_\gamma z^{-1}\,dz=\boxed{2\pi i}$.

::: {.proof}
Parametrize $\gamma$ by $z = R e^{i\theta}$, $0 \le \theta \le 2\pi$, so $dz = i R e^{i\theta}\,d\theta$ and
$$\int_\gamma z^n\,dz = i R^{n+1} \int_0^{2\pi} e^{i(n+1)\theta}\,d\theta.$$
If $n \neq -1$, the integrand has the $2\pi$-periodic antiderivative $e^{i(n+1)\theta}/(i(n+1))$, so the integral is $0$. If $n = -1$, the integrand is $1$, and the integral is $iR^0\cdot 2\pi = 2\pi i$.
:::

<1>2. (b) If the origin lies outside the closed disc bounded by $\gamma$, then $\int_\gamma z^n\,dz = \boxed{0}$ for every integer $n$.

::: {.proof}
The closed disc bounded by $\gamma$ is a compact set not containing $0$, so it lies in a slightly larger open disc $D$ with $0\notin D$. The function $z^n$ is holomorphic on $D$ for every integer $n$, and Cauchy's theorem in the disc $D$ gives $\int_\gamma z^n\,dz=0$.
:::
:::
