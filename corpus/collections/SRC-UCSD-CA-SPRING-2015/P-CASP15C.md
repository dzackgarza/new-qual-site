---
schema: qual/card@1
id: P-CASP15C
kind: problem
title: "Count roots of z^4 - 6z + 3 in an annulus"
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
How many roots does the polynomial $z^4 - 6z + 3 = 0$ have in the annulus $U = \{z \in \mathbb{C} \mid 1 < |z| < 2\}$?
:::

::: {.solution}
On $|z|=1$,
\[
|z^4+3|\le4<6=|-6z|,
\]
so by Rouché's theorem $z^4-6z+3$ has the same number of zeros in
$|z|<1$ as $-6z$, namely one.

On $|z|=2$,
\[
|-6z+3|\le15<16=|z^4|,
\]
so the polynomial has the same number of zeros in $|z|<2$ as $z^4$,
namely four.

Therefore the annulus $1<|z|<2$ contains
\[
\boxed{4-1=3}
\]
zeros, counted with multiplicity.
:::
