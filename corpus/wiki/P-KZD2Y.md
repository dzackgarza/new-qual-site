---
schema: qual/card@1
id: P-KZD2Y
kind: problem
title: "Find the number of roots of $p(z) = z^4 - 6z + 3$ in $\\abs{z} < 1$ and"
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
  - polynomials
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Find the number of roots of $p(z) = z^4 - 6z + 3$ in $\abs{z} < 1$ and
$1 < \abs{z} < 2$ respectively.

> Note: the original problem used $4z^4-6z+3$, but I don't think it's possible to use Rouché on that at all!

:::

:::{.solution}
On $\abs{z} < 1$:

- Small: $m(z) = z^4+3$
- Big: $M(z) = -6z$

On $\abs{z} = 1$,
\[
\abs{m(z)} = \abs{z^4+3} \leq \abs{z}^4 + 3 = 4 < 6 = \abs{-6z} = \abs{M(z)}
,\]
so $Z_f = Z_M = 1$.

On $\abs{z} < 2$:

- Small: $-6z+3$
- Big: $z^4$

On $\abs{z} = 2$,
\[
\abs{m(z)} = \leq 6 + 3 = 9 < 2^4 = \abs{M(z)}
,\]
so $Z_f = Z_M = 4$.

Thus there are $4-1=3$ zeros in $1 \leq \abs{z} \leq 2$.
:::

