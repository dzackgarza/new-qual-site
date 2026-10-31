---
schema: qual/card@1
id: P-PRACT20-W6-03
kind: problem
title: Candidate metrics on $\RR$
classification:
  areas:
  - prelim
  topics:
  - Metric Spaces
relations: []
review: draft
---

::: {.problem}
Which of the following does not define a metric on $\RR$?

(A) $\delta(x, y) = \begin{cases} 0, & x = y, \\ 2, & x \neq y. \end{cases}$

(B) $\rho(x, y) = \min\{\abs{x - y}, 1\}$

(C) $\sigma(x, y) = \dfrac{\abs{x - y}}{3}$

(D) $\tau(x, y) = \dfrac{\abs{x - y}}{\abs{x - y} + 1}$

(E) $\omega(x, y) = (x - y)^{2}$
:::

::: {.solution}
The answer is (E).

(A) is twice the discrete metric. (B) and (D) are bounded metrics that generate the standard topology. (C) is a positive multiple of the standard metric.

(E) is not a metric because the triangle inequality fails. Let $x=0$, $y=\frac12$, $z=1$. Then

$$
1=\omega(x,z)>\omega(x,y)+\omega(y,z)=\left(\frac12\right)^2+\left(\frac12\right)^2=\frac12.
$$
:::
