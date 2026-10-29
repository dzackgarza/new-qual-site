---
schema: qual/card@1
id: P-WASE4
kind: problem
title: Rouché's theorem implies the Fundamental Theorem of Algebra
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomials
  - Zeros
relations: []
review: draft
---

::: {.problem}
Use Rouche's theorem to prove the Fundamental Theorem of Algebra.
:::

::: {.solution}

Zeros are counted with multiplicity.
Write $Q(z)\coloneqq P_n(z)-a_nz^n$ and $C\coloneqq\sum_{k=0}^{n-1}\abs{a_k}$.

::: pf

::: {.pf-step #bound}
For every $R>\max(1,C/\abs{a_n})$, $\abs{Q(z)}<\abs{a_nz^n}$ on $\abs{z}=R$.

::: pf-proof
On $\abs{z}=R\geq1$, $\abs{Q(z)}\leq\sum_{k<n}\abs{a_k}R^k\leq CR^{n-1}<\abs{a_n}R^n$.
:::

:::

::: pf-step
$P_n$ has exactly $n$ zeros in $\CC$.

::: pf-proof
For each $R$ as in step [](#bound){.pf-ref}, Rouché's theorem shows that $P_n=a_nz^n+Q$ has as many zeros in $\abs{z}<R$ as $a_nz^n$, namely $n$, and $P_n$ has no zero on $\abs{z}=R$.
Every zero of $P_n$ lies in $\abs{z}<R$ for $R$ large enough, so $P_n$ has exactly $n$ zeros in $\CC$.
:::

:::

:::

:::
