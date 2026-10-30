---
schema: qual/card@1
id: P-CAFA25A
kind: problem
title: 'Zeros of $z^4-6z+3$ in the annulus $1<\abs z<2$'
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
How many zeros does the polynomial equation $z^4 - 6z + 3 = 0$ have in the annulus $G = \{z \in \CC : 1 < \abs{z} < 2\}$?
Please justify your answer.
:::

::: {.solution}
Let
$$
p(z)=z^4-6z+3.
$$
On $\abs{z}=1$,
$$
\abs{z^4+3}\le4<6=\abs{-6z}.
$$
By Rouché's theorem, $p$ and $-6z$ have the same number of zeros in
$\abs{z}<1$, namely one.

On $\abs{z}=2$,
$$
\abs{-6z+3}\le12+3=15<16=\abs{z^4}.
$$
Thus $p$ and $z^4$ have the same number of zeros in $\abs{z}<2$, namely four.
No zero lies on either boundary circle because the Rouché inequalities are
strict. Hence the annulus $1<\abs{z}<2$ contains
$$
\boxed{4-1=3}
$$
zeros, counted with multiplicity.
:::
