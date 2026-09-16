---
schema: qual/card@1
id: E-SS3.EX-18
kind: problem
title: "SS 3.18: The Cauchy integral formula via homotopy"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
18. Give another proof of the Cauchy integral formula

$$
f (z) = \frac {1}{2 \pi i} \int_ {C} \frac {f (\zeta)}{\zeta - z} d \zeta
$$

using homotopy of curves.

[Hint: Deform the circle C to a small circle centered at $z ,$ and note that the quotient $( f ( \zeta ) - f ( z ) ) / ( \zeta - z )$ is bounded.]
:::

::: {.solution}
Let $C$ be positively oriented and let $z$ lie in its interior. Since
\[
\frac{f(\zeta)}{\zeta-z}
=\frac{f(\zeta)-f(z)}{\zeta-z}+\frac{f(z)}{\zeta-z},
\]
set
\[
h(\zeta)=\begin{cases}
\dfrac{f(\zeta)-f(z)}{\zeta-z},&\zeta\ne z,\\[4pt]
f'(z),&\zeta=z.
\end{cases}
\]
Then $h$ is holomorphic near the region swept out by a homotopy shrinking $C$ to a sufficiently small positively oriented circle $C_r$ centered at $z$. By homotopy invariance of contour integrals of holomorphic functions,
\[
\int_C h(\zeta)\,d\zeta=\int_{C_r}h(\zeta)\,d\zeta.
\]
Letting $r\downarrow0$, the right side tends to $0$, because $h$ is bounded near $z$ and the length of $C_r$ is $2\pi r$. Hence
\[
\int_C\frac{f(\zeta)-f(z)}{\zeta-z}\,d\zeta=0.
\]
Also the winding number of $C$ about $z$ is $1$, so
\[
\int_C\frac{d\zeta}{\zeta-z}=2\pi i.
\]
Therefore
\[
\int_C\frac{f(\zeta)}{\zeta-z}\,d\zeta=2\pi i f(z),
\]
which is the Cauchy integral formula.
:::
