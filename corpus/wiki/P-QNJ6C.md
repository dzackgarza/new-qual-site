---
schema: qual/card@1
id: P-QNJ6C
kind: problem
title: "Let $f(x, y)$ on $[-1, 1]^2$ be defined by"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $f(x, y)$ on $[-1, 1]^2$ be defined by 
$$
f(x, y) = \begin{cases}
\frac{x y}{\left(x^{2}+y^{2}\right)^{2}} & (x, y) \neq (0, 0) \\
0 & (x, y) = (0, 0)
\end{cases}
$$
Determine if $f$ is integrable.

:::{.concept}
\envlist
- Just Calculus.
- $1/r$ is not integrable on $(0, 1)$.
:::

:::{.solution}
Switching to polar coordinates and integrating over the quarter of the unit disc $D \intersect Q_1 \subseteq I^2$ in quadrant 1, we have
\[
\int_{I^2} f \, dA
&\geq \int_D f \, dA \\
&= \int_0^{\pi/2} \int_0^1 \frac{r^2 \cos(\theta)\sin(\theta)}{r^4} ~r~\dr\dtheta  \\
&= \int_0^{\pi/2} \int_0^1 \frac{\cos(\theta)\sin(\theta)}{r} \dr\dtheta  \\
&= \qty{ \int_0^1 {1\over r } \dr} \qty{ \int_0^{\pi/2} \cos(\theta)\sin(\theta) \dtheta }  \\
&= \qty{ \int_0^1 {1\over r } \dr} \qty{ \int_0^{1} u \du }  && u=\sin(\theta)\\
&= {1\over 2}\qty{ \int_0^1 {1\over r } \dr} \\
&\too \infty
.\]
:::
