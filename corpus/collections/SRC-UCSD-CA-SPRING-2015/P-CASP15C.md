---
schema: qual/card@1
id: P-CASP15C
kind: problem
title: 'Roots of $z^4-6z+3$ in an annulus'
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Rouché
  - Polynomial Roots
relations: []
review: draft
---

::: {.problem}
How many roots does the polynomial $z^4 - 6z + 3 = 0$ have in the annulus $U = \{z \in \CC \mid 1 < \abs{z} < 2\}$?
:::

::: {.solution}
On $\abs{z}=1$,
$$
\abs{z^4+3}\le4<6=\abs{-6z},
$$
so by Rouché's theorem $z^4-6z+3$ has the same number of zeros in
$\abs{z}<1$ as $-6z$, namely one.

On $\abs{z}=2$,
$$
\abs{-6z+3}\le15<16=\abs{z^4},
$$
so the polynomial has the same number of zeros in $\abs{z}<2$ as $z^4$,
namely four.

Therefore the annulus $1<\abs{z}<2$ contains
$$
\boxed{4-1=3}
$$
zeros, counted with multiplicity.
:::
