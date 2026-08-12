---
schema: qual/card@1
id: P-YZBES
kind: problem
title: "Find the number of roots of $z^4 - 6z + 3 =0$ in $|z|<1$ and $1 < |z| < 2$ respectively. On $\\abs{z} \\leq 1$: Big: $M(z) = -6z$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Find the number of roots of $z^4 - 6z + 3 =0$ in $|z|<1$ and
$1 < |z| < 2$ respectively.
:::

:::{.solution}
On $\abs{z} \leq 1$:

- Big: $M(z) = -6z$
- Small: $m(z) = z^4 + 3$

Then on $\abs{z} = 1$,
\[
\abs{m(z)} \leq \abs{z}^4 + 3 = 4 < 6 = \abs{-6z} = \abs{M(z)}
,\]
so $1 = Z_M = Z_f$ here.

On $\abs{z} \leq 2$:

- Big: $M(z) = z^4$
- Small: $m(z) = -6z+3$.

Then on $\abs{z} = 2$,
\[
\abs{m(z)} = \abs{-6z + 3} \leq 6\abs{z} + 3 = 15 < 16 = 2^4 = \abs{z}^4 = \abs{M(z)}
,\]
so $4 = Z_M = Z_f$ here.

Thus there are $4-1 = 3$ zeros in $1 \leq \abs{z} \leq 2$.
:::

