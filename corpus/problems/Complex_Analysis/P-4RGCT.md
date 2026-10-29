---
schema: qual/card@1
id: P-4RGCT
kind: problem
title: Fundamental Theorem of Algebra via Rouché's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomials
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Apply Rouché's Theorem to prove the Fundamental Theorem of Algebra:

If
$$
P_n(z) = a_0 + a_1z + \cdots + a_{n-1}z^{n-1} + a_nz^n\quad  (a_n \neq 0)
$$
is a polynomial of degree $n$, then it has $n$ zeros in $\CC$.
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
