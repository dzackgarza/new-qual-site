---
schema: qual/card@1
id: P-BKF18-1A
kind: problem
title: Integral identity for $x^{-x}$
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Show that
$$
\int_0^1 x^{-x}\,dx=\sum_{n=1}^{\infty}n^{-n}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $0<x\le1$,
$$
x^{-x}=e^{-x\log x}=\sum_{n=0}^\infty\frac{(-x\log x)^n}{n!},
$$
and the integral of the sum equals the sum of the integrals.

::: pf-proof

The series is the exponential series. Each term is nonnegative, because $-x\log x\ge0$ on $(0,1]$. The monotone convergence theorem allows term-by-term integration.

:::

:::

::: {.pf-step #s2}

For each $n\ge0$,
$$
\int_0^1(-x\log x)^n\,dx=\frac{n!}{(n+1)^{n+1}}.
$$

::: pf-proof

Substitute $x=e^{-u}$, so $dx=-e^{-u}\,du$ and $-x\log x=ue^{-u}$:
$$
\int_0^1(-x\log x)^n\,dx=\int_0^\infty u^ne^{-(n+1)u}\,du.
$$
Substitute $v=(n+1)u$: the integral is $(n+1)^{-(n+1)}\int_0^\infty v^ne^{-v}\,dv=n!\,(n+1)^{-(n+1)}$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref},
$$
\int_0^1x^{-x}\,dx=\sum_{n=0}^\infty\frac{1}{(n+1)^{n+1}}=\sum_{n=1}^\infty n^{-n}.
$$

:::

:::

:::
