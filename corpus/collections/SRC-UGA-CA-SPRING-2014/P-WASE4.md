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
Apply Rouché's theorem to prove the Fundamental Theorem of Algebra: if
$$
P(z)=a_0+a_1z+\cdots+a_{n-1}z^{n-1}+a_nz^n\qquad(a_n\neq0)
$$
is a polynomial of degree $n>0$, then it has a zero in $\CC$.
:::

::: {.solution}

Zeros are counted with multiplicity.
Write $Q(z)\coloneqq P(z)-a_nz^n$ and $C\coloneqq\sum_{k=0}^{n-1}\abs{a_k}$.

::: pf

::: {.pf-step #bound}
For every $R>\max(1,C/\abs{a_n})$, $\abs{Q(z)}<\abs{a_nz^n}$ on $\abs{z}=R$.

::: pf-proof
On $\abs{z}=R\geq1$, $\abs{Q(z)}\leq\sum_{k<n}\abs{a_k}R^k\leq CR^{n-1}<\abs{a_n}R^n$.
:::

:::

::: pf-step
$P$ has exactly $n$ zeros in $\CC$, so, since $n>0$, it has a zero.

::: pf-proof
For each $R$ as in step [](#bound){.pf-ref}, Rouché's theorem shows that $P=a_nz^n+Q$ has as many zeros in $\abs{z}<R$ as $a_nz^n$, namely $n$, and $P$ has no zero on $\abs{z}=R$.
Every zero of $P$ lies in $\abs{z}<R$ for $R$ large enough, so $P$ has exactly $n$ zeros in $\CC$.
:::

:::

:::

:::
