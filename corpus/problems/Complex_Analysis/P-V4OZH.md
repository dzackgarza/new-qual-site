---
schema: qual/card@1
id: P-V4OZH
kind: problem
title: $f(z)=b$ has $n$ solutions in the unit disk for a product of Blaschke factors
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Rouché
  - Zeros
  - Argument Principle
relations: []
review: draft
---

::: {.problem}
For $k=1,2,\cdots, n$, suppose $\abs{a_k} < 1$, and suppose $|b|<1$. Let
\[
f(z) \definedas \qty{z - a_1 \over 1 - \bar a_1 z} \qty{z-a_2 \over 1 - \bar a_2 z} \cdots \qty{z - a_n \over 1 - \bar a_n z}
.\]
Show that $f(z) = b$ has $n$ solutions in $\abs{z} < 1$.
:::

::: {.solution}
For $|z|=1$ and each $k$,
\[
|z-a_k|=|1-\bar a_k z|,
\]
so every Blaschke factor has modulus $1$ on the unit circle. Hence
\[
|f(z)|=1>|b|
\qquad(|z|=1).
\]
The poles of $f$ are at $1/\bar a_k$, all outside the closed unit disk, so
$f$ is holomorphic on a neighborhood of $\overline\DD$.

Apply Rouché's theorem on $|z|=1$ to $f$ and $f-b$. They have the same number
of zeros in $\DD$, counted with multiplicity. The zeros of $f$ in $\DD$ are
exactly $a_1,\ldots,a_n$, with repetitions counted according to multiplicity,
so there are $n$ of them. Therefore $f-b$ also has exactly $n$ zeros in
$\DD$, counted with multiplicity. Equivalently, the equation
\[
f(z)=b
\]
has $n$ solutions in the unit disk, counted with multiplicity.
:::
