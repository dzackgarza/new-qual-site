---
schema: qual/card@1
id: P-TWH7U
kind: problem
title: Extrema of $xy$ on the ellipse $x^2+4y^2=8$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Using the method of Lagrange Multipliers, find the maximum and minimum values of $f(x,y) = xy$ on the ellipse $x^2 + 4y^2 = 8$.
:::

::: solution
Let
\[
g(x,y)=x^2+4y^2.
\]
At an extremum on $g=8$, Lagrange multipliers give
\[
(y,x)=\lambda(2x,8y),
\]
so
\[
y=2\lambda x,\qquad x=8\lambda y.
\]
Neither $x$ nor $y$ can be zero at such a point, so substitution gives
\[
1=16\lambda^2.
\]
Hence $\lambda=\pm1/4$.

If $\lambda=1/4$, then $y=x/2$. The constraint becomes
\[
x^2+4(x/2)^2=2x^2=8,
\]
so $x=\pm2$ and $y=\pm1$ with matching signs. Thus $xy=2$.

If $\lambda=-1/4$, then $y=-x/2$, giving the points $(2,-1)$ and $(-2,1)$ and hence $xy=-2$.

Therefore the maximum value is $2$ and the minimum value is $-2$.
:::
