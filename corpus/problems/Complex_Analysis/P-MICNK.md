---
schema: qual/card@1
id: P-MICNK
kind: problem
title: $az^n+z+1$ has a root in $\abs{z}\le 2$
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
Let $a\in \CC$ and $n\geq 2$.
Show that the following polynomial has at least one root in $\abs{z} \leq 2$:
$$
f(z) = az^n + z + 1.
$$
:::

::: {.solution}
::: pf

::: pf-step
If $\abs{a}<2^{-n}$, then $f$ has a root in $\abs{z}<2$.

::: pf-proof
On $\abs{z}=2$, $\abs{az^n}=\abs{a}2^n<1\le\abs{z}-1\le\abs{z+1}$. By Rouché's theorem $f$ and $z+1$ have the same number of zeros in $\abs{z}<2$, namely one.
:::

:::

::: pf-step
If $\abs{a}\ge2^{-n}$, then $f$ has a root in $\abs{z}\le2$.

::: pf-proof
Here $a\neq0$, so $f$ has degree $n$ with roots $z_1,\ldots,z_n$ counted with multiplicity. By Vieta's formulas $\abs{z_1\cdots z_n}=\abs{1/a}\le2^n$. If every root satisfied $\abs{z_k}>2$, the product would have modulus greater than $2^n$.
:::

:::

:::
:::
