---
schema: qual/card@1
id: P-DJV6N
kind: problem
title: The cubic $z^3+3z^2+bz+b^2$ has exactly two roots in the unit disk when $|b|<1$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
---

Assume that $\abs b < 1$ and show that the following polynomial has exactly two roots (counting multiplicity) in $\abs{z} < 1$:
\[
f(z) \definedas z^3 + 3z^2 + bz + b^2
.\]

:::{.solution}
:::{.concept}
Multiple versions of Rouches theorem!
:::

- Set $h(z) = 3z^2$ and $g(z) = z^3 + bz + b^2$.
- Then on $\abs{z} = 1$,
\begin{align*}
\abs{g(z)} \leq 1 + b + b^2 < 3 = 3\abs{z}^2 = \abs{3z^2} = \abs{h}
,\end{align*}
  so $g, h$ have the same number of roots in $\abs{z} \leq_? 1$.

- But $h$ evidently has two roots in this region.

:::


