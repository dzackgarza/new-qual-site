---
schema: qual/card@1
id: P-FAGTL
kind: problem
title: Zeros of $z^6+9z^4+z^3+2z+4$ in $\abs{z}<1$ by Rouché's theorem
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

::: {.exercise}
Find the number of zeros in $\abs{z} < 1$ of
$$
p(z) \coloneqq z^6 + 9z^4 + z^3 + 2z + 4
.$$

:::

::: {.hint}
Compare $p$ with its dominant term $9z^4$ on $\abs{z}=1$ and apply Rouché's theorem.
:::

::: {.solution}
Write $F(z) \coloneqq 9z^4$.

::: pf

::: {.pf-step #bound}
On $\abs{z} = 1$, $\abs{p(z) - F(z)} < \abs{F(z)}$.

::: pf-proof
On $\abs z = 1$ we have $\abs{F(z)} = 9$ and $\abs{p(z)-F(z)} = \abs{z^6 + z^3 + 2z + 4} \leq 1+1+2+4 = 8$.
:::

:::

::: pf-step
$p$ has $\boxed{4}$ zeros in $\abs{z}<1$, counted with multiplicity.

::: pf-proof
By step [](#bound){.pf-ref} and Rouché's theorem, $p$ and $F$ have the same number of zeros in $\abs z<1$, and $F$ has a zero of order $4$ at $0$.
:::

:::

:::

:::
