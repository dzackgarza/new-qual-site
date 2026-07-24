---
schema: qual/card@1
id: P-4NBXB
kind: problem
title: "Find the number of zeros in $\\abs{z} \\in (1, 2)$ of"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Find the number of zeros in $\abs{z} \in (1, 2)$ of
\[
f(z) \da z^4 + 5z + 3
.\]
Note the strict inequality.

:::

:::{.solution}
On $\abs{z} = 1$:

- Big: $M(z) = 5z$
- Small: $m(z) = z^4 + 3$
- The estimate:
\[
\abs{m(z)} \leq \abs{z}^4 + 3 = 4 < 5 = \abs{M(z)} \implies 1 = \size Z_M = \size Z_f
.\]

On $\abs{z} = 2$:

- Big: $M(z) = z^4$
- Small: $m(z) = 5z + 3$
- The estimate:
\[
\abs{m(z)} \leq 5\abs{z} + 3 = 13 < 16 = 2^4 = \abs{M(z)} \implies 4 = \size Z_M = \size Z_f
.\]

So $f$ has $4-1=3$ zeros on $\abs{z} \in (0, 2)\sm (0, 1) = [1, 2)$.
To get the strict inequality, it suffices to show $f$ has no zeros on $\abs{z} = 1$.
Estimate a lower bound:
\[
\abs{z^4 + 5z + 3} \geq \abs{\abs{5z+3} - \abs{z}^4 } = \abs{\abs{5z+3} - 1 } \geq \abs{ 2-1} > 0
.\]
The nontrivial bound at the end comes from the fact that $5z+3 = 3 + 5e^{it}$ whose modulus ranges between $3-5 = -2$ and $3+5 = 8$.
:::

