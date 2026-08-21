---
schema: qual/card@1
id: P-SCDUI
kind: problem
title: $z^3+3z^2+bz+b^2$ has exactly two roots in the unit disk when $|b|<1$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Assume that $\abs b < 1$ and show that the following polynomial has exactly two roots (counting multiplicity) in $\abs{z} < 1$:
\[
f(z) \definedas z^3 + 3z^2 + bz + b^2
.\]

:::

:::{.solution}
Big: $M(z) = 3z^2$.
Small: $m(z) = z^3+bz + b^2$.
Then on $\abs{z} = 1$:
\[
\abs{m(z)} \leq \abs{z}^3 + b\abs{z} + b^2 = 1 + b + b^2 < 3 = \abs{M(z)}
,\]
and $M(z)$ has exact two roots in $\DD$.
:::

