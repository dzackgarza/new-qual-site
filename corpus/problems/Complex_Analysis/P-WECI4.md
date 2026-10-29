---
schema: qual/card@1
id: P-WECI4
kind: problem
title: A monic polynomial with coefficient bounds has $d$ zeros in $\abs{z}<R$
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
Find the number of zeros in $\abs{z} < R$ of
$$
p(z) \coloneqq z^d + a_1z^{d-1} + \cdots + a_d,
$$
supposing that
$\abs{a_k}< {R^k \over d}$ for every $k$ (noting the strict inequality).

:::

::: {.hint}
Compare $p$ with $z^d$ on $\abs{z}=R$ and apply Rouché's theorem; the hypothesis on the coefficients makes the remaining terms small.
:::

::: {.solution}
Write $p = F + g$ with $F(z) = z^d$ and $g(z) = a_1 z^{d-1} + \cdots + a_d$.

::: pf

::: {.pf-step #estimate}

$\abs{g(z)} < \abs{F(z)} = R^d$ on $\abs{z} = R$.

::: pf-proof

For $\abs{z} = R$,
$$
\abs{g(z)} \leq \sum_{k=1}^{d} \abs{a_k} R^{d-k} < \sum_{k=1}^{d} \frac{R^k}{d} R^{d-k} = d\cdot\frac{R^d}{d} = R^d.
$$

:::

:::

::: pf-step

$p$ has $\boxed{d}$ zeros in $\abs{z} < R$, counted with multiplicity.

::: pf-proof

By step [](#estimate){.pf-ref} and Rouché's theorem, $p = F + g$ and $F$ have the same number of zeros in $\abs{z} < R$, and $F(z) = z^d$ has a zero of order $d$ at $0$.

:::

:::

:::

:::
