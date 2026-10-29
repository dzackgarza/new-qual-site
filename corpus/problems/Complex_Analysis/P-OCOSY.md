---
schema: qual/card@1
id: P-OCOSY
kind: problem
title: Inverting the power series of $\cos z$ one coefficient at a time
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Trigonometry
  - Laurent Series
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source says "Find 1/cos(z) using this method", referring to the recursive inversion of a power series; the statement now names that recursion and the order z^4 the solution computes.'
---

::: {.exercise}
If $f(z)=\sum_{k\ge0}c_kz^k$ with $c_0\neq0$, then $1/f(z)=\sum_{k\ge0}b_kz^k$ near $0$, where $b_0=c_0^{-1}$ and $b_n=-c_0^{-1}\sum_{j=1}^nc_jb_{n-j}$ for $n\ge1$. Use this recursion to find the power series of $1/\cos z$ at $0$ through the term in $z^4$.
:::

::: {.solution}
Write $\cos z=\sum_kc_kz^k$, so $c_0=1$, $c_2=-\frac{1}{2!}$, $c_4=\frac{1}{4!}$, and $c_k=0$ for $k$ odd.

::: pf

::: {.pf-step #odd}
$b_k=0$ for every odd $k$.

::: pf-proof
By induction on $k$: for odd $n$, each term $c_jb_{n-j}$ has $j$ odd or $n-j$ odd, so it vanishes by $c_j=0$ or by the induction hypothesis.
:::

:::

::: pf-step
$\frac{1}{\cos z}=\boxed{1+\frac{1}{2}z^2+\frac{5}{24}z^4+\mathcal{O}(z^6)}$.

::: pf-proof
$b_0=1$. Using step [](#odd){.pf-ref}, $b_2=-c_2b_0=\frac12$ and $b_4=-(c_2b_2+c_4b_0)=\frac14-\frac1{24}=\frac{5}{24}$.
:::

:::

:::
:::
