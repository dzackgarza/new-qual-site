---
schema: qual/card@1
id: P-DJV6N
kind: problem
title: The cubic $z^3+3z^2+bz+b^2$ has exactly two roots in the unit disk when $\abs{b}<1$
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

::: {.problem}
Assume that $\abs b < 1$ and show that the following polynomial has exactly two roots (counting multiplicity) in $\abs{z} < 1$:
$$
f(z) \coloneqq z^3 + 3z^2 + bz + b^2.
$$
:::

::: {.solution}

Let $h(z)\coloneqq3z^2$ and $g(z)\coloneqq z^3+bz+b^2$, so $f=h+g$.

::: pf

::: {.pf-step #bound}
On $\abs{z}=1$, $\abs{g(z)}<\abs{h(z)}$.

::: pf-proof
$\abs{g(z)}\le1+\abs{b}+\abs{b}^2<3=\abs{h(z)}$ because $\abs{b}<1$.
:::

:::

::: pf-step
$f$ has exactly two roots in $\abs{z}<1$, counted with multiplicity.

::: pf-proof
By step [](#bound){.pf-ref} and Rouché's theorem, $f$ and $h$ have the same number of zeros in $\abs{z}<1$, and $h$ has the double zero $0$.
:::

:::

:::

:::
