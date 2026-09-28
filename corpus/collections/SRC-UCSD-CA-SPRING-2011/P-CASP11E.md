---
schema: qual/card@1
id: P-CASP11E
kind: problem
title: "Vanishing of the contour integral of e^{iz}/log(z) over a quarter circle"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
For $R > 1$ let $C_R$ be the quarter circle parametrized by $z = Re^{i\theta}$, $0 \leq \theta \leq \pi/2$.
Prove that $$\lim_{R \to \infty} \int_{C_R} \frac{e^{iz}}{\log z}\,dz = 0,$$ where $\log z$ is the principal branch of the logarithm.

Hint: You may use the inequality $\sin\theta \geq c\theta$ for $0 \leq \theta \leq \pi/2$, with some constant $c > 0$.
Then evaluate an appropriate integral.
:::

::: {.solution}
On $C_R$, write $z=Re^{i\theta}$, $0\le\theta\le\pi/2$. Then
\[
|e^{iz}|=e^{-R\sin\theta},
\qquad
|\log z|=|\log R+i\theta|\ge\log R,
\qquad |dz|=R\,d\theta.
\]
Using $\sin\theta\ge c\theta$ on this interval,
\[
\left|\int_{C_R}\frac{e^{iz}}{\log z}\,dz\right|
\le \frac{R}{\log R}\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta
\le \frac{R}{\log R}\int_0^\infty e^{-cR\theta}\,d\theta
=\frac1{c\log R}.
\]
The last quantity tends to $0$, proving the claim.
:::
