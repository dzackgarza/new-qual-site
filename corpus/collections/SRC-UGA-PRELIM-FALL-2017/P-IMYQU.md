---
schema: qual/card@1
id: P-IMYQU
kind: problem
title: $\int_0^\infty x^n e^{-x}\,dx = n!$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Improper Integrals
  - Integration by Parts
  - Induction
relations: []
review: draft
---

::: {.problem}
Prove, for every nonnegative integer $n$, that
$$
\int_0^\infty x^ne^{-x}\,dx=n!.
$$
:::

::: {.solution}

No retained solution set covers this exercise: the card's own induction follows, with the convergence of the integral, the boundary term and the induction step separated.

::: pf

::: {.pf-step #converges}
For every $n\ge0$ the integral $\int_{0}^{\infty}x^{n}e^{-x}\,dx$ converges.

::: pf-proof
The integrand is continuous and nonnegative on $[0,\infty)$. Since $x^{n}e^{-x/2}\to0$ as $x\to\infty$, there is $M$ with $x^{n}e^{-x/2}\le M$ for all $x\ge0$, hence $x^{n}e^{-x}\le Me^{-x/2}$ there; and $\int_{0}^{\infty}Me^{-x/2}\,dx=2M<\infty$, so the integral converges by comparison.
:::

:::

::: {.pf-step #base}
$\int_{0}^{\infty}x^{0}e^{-x}\,dx=1=0!$.

::: pf-proof
$\int_{0}^{T}e^{-x}\,dx=1-e^{-T}\to1$ as $T\to\infty$.
:::

:::

::: {.pf-step #step}
If $\int_{0}^{\infty}x^{n-1}e^{-x}\,dx=(n-1)!$ with $n\ge1$, then $\int_{0}^{\infty}x^{n}e^{-x}\,dx=n!$.

::: pf-proof
Integration by parts with $u=x^{n}$, $dv=e^{-x}dx$ on $[0,T]$ gives $\int_{0}^{T}x^{n}e^{-x}\,dx=\big[-x^{n}e^{-x}\big]_{0}^{T}+n\int_{0}^{T}x^{n-1}e^{-x}\,dx$. The boundary term is $-T^{n}e^{-T}$, which tends to $0$ as $T\to\infty$ because the exponential dominates the power, and vanishes at the lower limit since $n\ge1$. So the integral equals $n\int_{0}^{\infty}x^{n-1}e^{-x}\,dx=n\,(n-1)!=n!$ by the induction hypothesis.
:::

:::

::: {.pf-qed}
By steps [](#base){.pf-ref} and [](#step){.pf-ref}, induction on $n$ gives $\int_{0}^{\infty}x^{n}e^{-x}\,dx=n!$ for every nonnegative integer $n$, the integrals existing by step [](#converges){.pf-ref}.
:::

:::

:::
