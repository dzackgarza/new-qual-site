---
schema: qual/card@1
id: P-4NBXB
kind: problem
title: Zeros of $z^4+5z+3$ in $1<|z|<2$
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
Find the number of zeros in $\abs{z} \in (1, 2)$ of
$$
f(z) \coloneqq z^4 + 5z + 3
.$$
Note the strict inequality.

:::

::: {.solution}

::: pf

::: {.pf-step #inner}
$f$ has exactly one zero in $\abs{z}<1$ and none on $\abs{z}=1$.

::: pf-proof
On $\abs{z}=1$, $\abs{z^4+3}\leq4<5=\abs{5z}$.
By Rouché's theorem, $f$ and $5z$ have the same number of zeros in $\abs{z}<1$, namely one.
On $\abs{z}=1$, $\abs{f(z)}\geq\abs{5z}-\abs{z^4+3}\geq1>0$.
:::

:::

::: {.pf-step #outer}
$f$ has exactly four zeros in $\abs{z}<2$ and none on $\abs{z}=2$.

::: pf-proof
On $\abs{z}=2$, $\abs{5z+3}\leq13<16=\abs{z^4}$.
By Rouché's theorem, $f$ and $z^4$ have the same number of zeros in $\abs{z}<2$, namely four, and $\abs{f(z)}\geq16-13>0$ on $\abs{z}=2$.
:::

:::

::: pf-step
$f$ has exactly $\boxed{3}$ zeros, counted with multiplicity, in $1<\abs{z}<2$.

::: pf-proof
By steps [](#inner){.pf-ref} and [](#outer){.pf-ref}, the zeros in $\abs{z}<2$ number four, one of them lies in $\abs{z}<1$, and none lies on $\abs{z}=1$.
:::

:::

:::

:::
