---
schema: qual/card@1
id: P-CAFA23D
kind: problem
title: '$\int_0^{2\pi} e^{e^{i\theta}}\,d\theta$ as a contour integral'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the exponential
    series at e^{i theta} with |e^{i theta}| = 1 converges uniformly by the M-test, so
    termwise integration is justified; the n = 0 term contributes 2 pi and every n >= 1
    term vanishes since (e^{2 pi i n} - 1)/(i n) = 0. The uniform convergence that the
    termwise step needs is now proved rather than asserted, and the two cases of the
    elementary integral are separated. The collection's provenance is the examination paper
    only, so no retained solution set covers the exercise and the argument is the card's
    own.
---

::: {.problem}
Evaluate $\displaystyle \int_0^{2\pi} e^{e^{i\theta}}\,d\theta$, carefully explaining your solution.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #uniform}
$\sum_{n\ge0}\frac{e^{in\theta}}{n!}$ converges uniformly in $\theta\in[0,2\pi]$, and its sum is $e^{e^{i\theta}}$.

::: pf-proof
For $\theta$ real, $e^{e^{i\theta}}=\sum_{n\ge0}\frac{(e^{i\theta})^n}{n!}$ by the exponential series at the point $e^{i\theta}$. Since $\abs{e^{i\theta}}=1$, the $n$-th summand has modulus $\frac{1}{n!}$, and $\sum_n\frac1{n!}$ converges, so the Weierstrass $M$-test gives uniform convergence on the whole interval.
:::

:::

::: {.pf-step #termwise}
$$
\int_0^{2\pi}e^{e^{i\theta}}\,d\theta=\sum_{n=0}^{\infty}\frac{1}{n!}\int_0^{2\pi}e^{in\theta}\,d\theta .
$$

::: pf-proof
Uniform convergence on a compact interval permits integrating a series term by term, the partial sums being continuous and the limit integrable; the $n=0$ summand is the constant $1$.
:::

:::

::: {.pf-step #terms}
For every integer $n\ge0$,
$$
\int_0^{2\pi}e^{in\theta}\,d\theta=\begin{cases}2\pi,&n=0,\\0,&n\ge1.\end{cases}
$$

::: pf-proof
For $n=0$ the integrand is $1$. For $n\ge1$ an antiderivative is $\frac{e^{in\theta}}{in}$, so the integral equals $\frac{e^{2\pi in}-1}{in}=\frac{1-1}{in}=0$.
:::

:::

::: {.pf-step}
$\displaystyle\int_0^{2\pi}e^{e^{i\theta}}\,d\theta=\boxed{2\pi}$.

::: pf-proof
Substituting step [](#terms){.pf-ref} into step [](#termwise){.pf-ref} leaves only the $n=0$ term of the series, namely $\frac{1}{0!}\cdot2\pi=2\pi$.
:::

:::

:::
:::
