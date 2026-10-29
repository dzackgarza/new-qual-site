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
---

::: {.problem}
Assume that $\abs b < 1$ and show that the following polynomial has exactly two roots (counting multiplicity) in $\abs{z} < 1$:
$$
f(z) \definedas z^3 + 3z^2 + bz + b^2
.$$
:::

::: {.solution}
Write $M(z)\coloneqq3z^2$.

::: pf

::: {.pf-step #bound}

On $\abs z=1$, $\abs{f(z)-M(z)}<\abs{M(z)}$.

::: pf-proof

On $\abs z=1$, $\abs{M(z)}=3$ and
$$
\abs{f(z)-M(z)}=\abs{z^3+bz+b^2}\le1+\abs b+\abs b^2<3.
$$

:::

:::

::: pf-step

$f$ has exactly $\boxed{2}$ zeros in $\abs z<1$, counted with multiplicity.

::: pf-proof

By step [](#bound){.pf-ref} and Rouché's theorem, $f$ and $M$ have the same number of zeros in $\abs z<1$, and $M$ has a double zero at $0$.

:::

:::

:::

:::
