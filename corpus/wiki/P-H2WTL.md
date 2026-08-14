---
schema: qual/card@1
id: P-H2WTL
kind: problem
title: "The question provides some insight into Cauchy's theorem.\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - contour-integration
  - winding-number
  - integrals
relations: []
review: draft
---
:::{.problem title="?"}
The question provides some insight into Cauchy's theorem. Solve the
problem without using the Cauchy theorem.

1.  Evaluate the integral $\displaystyle{\int_{\gamma} z^n dz}$ for
    all integers $n$. Here $\gamma$ is any circle centered at the
    origin with the positive (counterclockwise) orientation.

2.  Same question as (a), but with $\gamma$ any circle not
    containing the origin.

3.  Show that if $|a|<r<|b|$, then
    $\displaystyle{\int_{\gamma}\frac{dz}{(z-a)(z-b)} dz=\frac{2\pi i}{a-b}}$.
    Here $\gamma$ denotes the circle centered at the origin, of
    radius $r$, with the positive orientation.
:::

:::{.solution}
\[
\int_\gamma z^n\dz = \int_0^{2\pi} R^n e^{itn} \cdot iRe^{it} \dt
= R^{n+1} \int_0^{2\pi} e^{i(t+1)n}\dt 
= { i R^{n+1} \over i(n+1) } \delta_{n+1 = 0}
.\]

About a point $a$ and $R<\abs{a}$,
\[
\int_{\abs{z-a} = R} z^n\dz 
&= \int_0^{2\pi} (a + re^{it})^n \cdot ire^{it}\dt \\
&= \int_0^{2\pi} \sum_{1\leq k\leq n} {n \choose k} a_k R^{n-k+1} e^{it(n-k)} \cdot ire^{it}\dt \\
&= i \int_0^{2\pi} \sum_{1\leq k\leq n} {n \choose k} a_k R^{n-k+1} e^{it(n-k+1)} \dt \\
&= i \sum_{1\leq k\leq n} {n \choose k} a_k R^{n-k+1} \int_0^{2\pi} e^{it(n-k+1)} \dt \\
&= i \sum_{1\leq k\leq n} {n \choose k} a_k R^{n-k+1} \cdot 0 \\
&= 0
,\]
provided $n\neq 0$, in which case $\int_\gamma \dz = 2\pi$.

For the third computation, this follows from partial fraction decomposition.
:::
