---
schema: qual/card@1
id: E-N5RKI
kind: problem
title: Constant boundary modulus implies constancy or an interior zero
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros
relations: []
review: draft
---

::: {.exercise}
Let $G\subset\CC$ be a bounded region, and suppose $f$ is continuous on
$\overline G$ and holomorphic on $G$. Assume that there is a constant $c\ge0$
such that
\[
|f(z)|=c
\qquad(z\in\partial G).
\]
Show that either $f$ is constant or $f$ has a zero in $G$.
:::

::: solution
If $c=0$, the maximum modulus principle gives
\[
|f(z)|\le0
\qquad(z\in G),
\]
so $f\equiv0$ and is constant.

Assume $c>0$ and suppose that $f$ has no zero in $G$. Then $1/f$ is
holomorphic on $G$ and continuous on $\overline G$. Applying the maximum
modulus principle to $f$ gives
\[
|f(z)|\le c
\qquad(z\in G),
\]
while applying it to $1/f$ gives
\[
{1\over|f(z)|}\le {1\over c},
\]
hence $|f(z)|\ge c$. Therefore $|f|\equiv c$ on $G$.

A nonconstant holomorphic function has open image, whereas the circle
$\{w:|w|=c\}$ is not open. Thus the open mapping theorem forces $f$ to be
constant. Consequently, if $f$ is not constant, it must have a zero in $G$.
:::
